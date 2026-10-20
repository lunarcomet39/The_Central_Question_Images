# The Central Question Images

[![CDN](https://img.shields.io/badge/CDN-jsDelivr-orange.svg)](https://www.jsdelivr.com/)
[![Images](https://img.shields.io/badge/images-16%2C631%2B-blue.svg)]()
[![License](https://img.shields.io/badge/license-CC%20BY--SA%204.0-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-live%20production-brightgreen.svg)]()

> A dedicated, high-speed, global CDN asset repository for 16,631+ diagrams, chemical structures, circuit schematics, vector diagrams, and mathematical figures used across HSC Board & College test papers and admission questions.

Hosted on GitHub and accelerated globally across 750+ points of presence via **jsDelivr CDN**.

---

## How to Hotlink Images via jsDelivr CDN

Every image in this repository is accessible worldwide with zero egress bandwidth costs and sub-50ms latency using jsDelivr's global multi-CDN network.

### Standard URL Format

```html
https://cdn.jsdelivr.net/gh/lunarcomet39/The_Central_Question_Images@main/images/{subject}/{year}/{filename}
```

### Live Examples by Subject

- **Physics (2026 Board Test Paper)**:
  ```html
  <img src="https://cdn.jsdelivr.net/gh/lunarcomet39/The_Central_Question_Images@main/images/physics/2026/A5K5u6qQYNNKl2QYb-Ny_.png" alt="Physics Diagram" />
  ```

- **Chemistry (2025 Test Paper)**:
  ```html
  <img src="https://cdn.jsdelivr.net/gh/lunarcomet39/The_Central_Question_Images@main/images/chemistry/2025/x1aAx5lLdV_qbd0gy2Kx7.png" alt="Chemical Structure" />
  ```

- **Biology (2024 Test Paper)**:
  ```html
  <img src="https://cdn.jsdelivr.net/gh/lunarcomet39/The_Central_Question_Images@main/images/biology/2024/7nvbhGoNy7uYplRVIEah9.png" alt="Biological Specimen" />
  ```

- **Higher Math (2023 Test Paper)**:
  ```html
  <img src="https://cdn.jsdelivr.net/gh/lunarcomet39/The_Central_Question_Images@main/images/higher_math/2023/zIaLZkV61yQV4Gtye_rMv.png" alt="Math Graph" />
  ```

- **ICT (Information & Communication Technology)**:
  ```html
  <img src="https://cdn.jsdelivr.net/gh/lunarcomet39/The_Central_Question_Images@main/images/ict/2023/nQrynwoy1X.png" alt="Logic Gate Schematic" />
  ```

---

## Version Pinning & Cache Control

For immutable caching and protection against upstream branch changes, pin the version tag:

```html
<!-- Tagged Release (Recommended for production websites) -->
https://cdn.jsdelivr.net/gh/lunarcomet39/The_Central_Question_Images@v1.0.0/images/physics/2026/example.png

<!-- Main Branch (Always latest commit) -->
https://cdn.jsdelivr.net/gh/lunarcomet39/The_Central_Question_Images@main/images/physics/2026/example.png
```

### Instant Cache Invalidation (Purge API)

If an image is updated, force-purge the jsDelivr edge cache by prefixing with `purge.jsdelivr.net`:
```bash
curl https://purge.jsdelivr.net/gh/lunarcomet39/The_Central_Question_Images@main/images/physics/2026/example.png
```

---

## Directory Structure & Partitioning

To avoid GitHub web interface lag and keep repository browsing fluid, all 16,631 images are organized into 2-level directory partitions by **Subject** and **Exam Session Year**:

```
images/
├── physics/
│   ├── 2026/          # HSC 2026 Board & College physics figures
│   ├── 2025/          # HSC 2025 Board & College physics figures
│   ├── 2024/          # HSC 2024 Board & College physics figures
│   ├── ...
│   └── undated/       # Textbook & miscellaneous figures
├── chemistry/
│   ├── 2026/
│   ├── 2025/
│   └── ...
├── biology/
├── higher_math/
├── ict/
├── english/
└── bangla/
```

No single directory exceeds 1,000 files, ensuring fast loading in the GitHub web UI.

---

## Asset Breakdown

| Subject | Unique Images | Primary Content |
|---|---|---|
| **Chemistry** | 4,730 | Organic reaction mechanisms, structural formulas, titration curves |
| **Physics** | 4,703 | Circuit diagrams, ray optics, vector graphs, wave mechanics |
| **Biology** | 3,196 | Anatomical cross-sections, genetics charts, botanical taxonomy |
| **Higher Math** | 1,975 | Conic sections, 3D coordinate geometry, function plots |
| **ICT** | 1,796 | Logic gates, truth tables, flowcharts, network topology diagrams |
| **English** | 220 | Reading comprehension illustrations, table extracts |
| **Bangla** | 20 | Passage figures |
| **Total** | **16,631** | **~1.32 GB optimized Web Assets** |

---

## Manifest Mapping

The complete machine-readable mapping from original asset URLs to their canonical CDN paths is stored in [`image_manifest.json`](image_manifest.json):

```json
{
  "https://assets.chorcha.net/A5K5u6qQYNNKl2QYb-Ny_.png": {
    "clean_url": "https://assets.chorcha.net/A5K5u6qQYNNKl2QYb-Ny_.png",
    "filename": "A5K5u6qQYNNKl2QYb-Ny_.png",
    "subject": "physics",
    "year": "2026",
    "rel_path": "images/physics/2026/A5K5u6qQYNNKl2QYb-Ny_.png",
    "cdn_url": "https://cdn.jsdelivr.net/gh/lunarcomet39/The_Central_Question_Images@main/images/physics/2026/A5K5u6qQYNNKl2QYb-Ny_.png"
  }
}
```

---

## License

Assets cataloged in this repository are intended for academic and non-commercial educational purposes under the **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)** license.
