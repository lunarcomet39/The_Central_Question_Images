import asyncio, os, sys, json, time
import httpx
from pathlib import Path

# Force unbuffered output
sys.stdout.reconfigure(line_buffering=True)

base_dir = r"D:\Projects\EduChickenBd\The_Central_Question_Images"
manifest_path = os.path.join(base_dir, "image_manifest.json")

with open(manifest_path, "r", encoding="utf-8") as f:
    manifest = json.load(f)

items = list(manifest.values())
total = len(items)
print(f"Total images in manifest: {total:,}", flush=True)

to_download = []
for it in items:
    dest_path = os.path.join(base_dir, it["rel_path"].replace("/", os.sep))
    if not (os.path.exists(dest_path) and os.path.getsize(dest_path) > 0):
        to_download.append((it["clean_url"], dest_path))

already_done = total - len(to_download)
print(f"Already downloaded: {already_done:,}", flush=True)
print(f"Remaining to download: {len(to_download):,}", flush=True)

# Pre-create all directory trees
dirs_to_create = set(os.path.dirname(dest) for _, dest in to_download)
for d in dirs_to_create:
    os.makedirs(d, exist_ok=True)

print(f"Verified {len(dirs_to_create)} partition directories.", flush=True)

async def main():
    if not to_download:
        print("All images are already downloaded!", flush=True)
        return

    concurrency = 25
    sem = asyncio.Semaphore(concurrency)
    downloaded_cnt = 0
    failed_cnt = 0
    total_bytes = 0
    start_time = time.time()
    lock = asyncio.Lock()
    
    limits = httpx.Limits(max_connections=35, max_keepalive_connections=25)
    async with httpx.AsyncClient(timeout=30.0, limits=limits, follow_redirects=True) as client:
        async def download_one(url, dest):
            nonlocal downloaded_cnt, failed_cnt, total_bytes
            async with sem:
                for attempt in range(1, 5):
                    try:
                        resp = await client.get(url)
                        if resp.status_code == 200 and resp.content:
                            with open(dest, "wb") as f_out:
                                f_out.write(resp.content)
                            async with lock:
                                downloaded_cnt += 1
                                total_bytes += len(resp.content)
                                if downloaded_cnt % 500 == 0 or downloaded_cnt == len(to_download):
                                    elapsed = time.time() - start_time
                                    speed = downloaded_cnt / max(0.1, elapsed)
                                    mb = total_bytes / (1024 * 1024)
                                    print(f"[{downloaded_cnt:,}/{len(to_download):,}] ({mb:.1f} MB) in {elapsed:.1f}s ({speed:.1f} imgs/sec)", flush=True)
                            return True
                        elif resp.status_code == 429:
                            await asyncio.sleep(2.0 * attempt)
                        elif resp.status_code == 404:
                            async with lock:
                                failed_cnt += 1
                            return False
                    except Exception as e:
                        if attempt < 4:
                            await asyncio.sleep(1.0 * attempt)
                async with lock:
                    failed_cnt += 1
                return False

        tasks = [download_one(u, d) for u, d in to_download]
        await asyncio.gather(*tasks)

    elapsed = time.time() - start_time
    mb = total_bytes / (1024 * 1024)
    print(f"\nDownload finished! Success: {downloaded_cnt:,} ({mb:.1f} MB), 404/Failed: {failed_cnt:,} in {elapsed:.1f}s", flush=True)

if __name__ == "__main__":
    asyncio.run(main())
