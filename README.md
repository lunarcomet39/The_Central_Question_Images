# The Central Question Images

[![CDN](https://img.shields.io/badge/CDN-Cloudflare%20%7C%20Statically-orange.svg)](https://statically.io/)
[![GitHub](https://img.shields.io/badge/raw-GitHub%20Fastly-blue.svg)](https://raw.githubusercontent.com/)
[![Images](https://img.shields.io/badge/images-16%2C631%2B-blue.svg)]()
[![License](https://img.shields.io/badge/license-CC%20BY--SA%204.0-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-live%20production-brightgreen.svg)]()

> A dedicated, high-speed, global CDN asset repository for 16,631+ diagrams, chemical structures, circuit schematics, vector diagrams, and mathematical figures used across HSC Board & College test papers and admission questions.

Hosted publicly on GitHub and accelerated worldwide via **Cloudflare Edge CDN (Statically)** and **GitHub / Fastly Raw CDN**.

---

## Public Repository URL

- **GitHub Repository**: `https://github.com/lunarcomet39/The_Central_Question_Images`
- **Visibility**: Public (free global edge delivery)

---

## How to Hotlink Images on Your Website

Every image is immediately accessible via two high-speed CDN options with zero egress fees and sub-50ms latency:

### Option 1: Statically Multi-CDN (Cloudflare Accelerated — Recommended)

Accelerated by Cloudflare edge caches globally. Supports automatic WebP conversion and caching with no repository size constraints:

```html
<!-- Format -->
https://cdn.statically.io/gh/lunarcomet39/The_Central_Question_Images/main/images/{subject}/{year}/{filename}

<!-- Live Example: Physics Circuit Diagram (2025 Test Paper) -->
<img src="https://cdn.statically.io/gh/lunarcomet39/The_Central_Question_Images/main/images/physics/2025/x1aAx5lLdV_qbd0gy2Kx7.png" alt="Circuit Schematic" />

<!-- Live Example: Biology Botanical Specimen (2024 Test Paper) -->
<img src="https://cdn.statically.io/gh/lunarcomet39/The_Central_Question_Images/main/images/physics/2024/7nvbhGoNy7uYplRVIEah9.png" alt="Botanical Specimen" />

<!-- Live Example: Bangla Passage Diagram (2026 Test Paper) -->
<img src="https://cdn.statically.io/gh/lunarcomet39/The_Central_Question_Images/main/images/bangla/2026/5gBAVNubCU49lISbBSji6.png" alt="Bangla Diagram" />
```

### Option 2: Native GitHub Raw CDN (Fastly Edge)

Directly served by GitHub's Fastly CDN edge nodes:

```html
<!-- Format -->
https://raw.githubusercontent.com/lunarcomet39/The_Central_Question_Images/main/images/{subject}/{year}/{filename}

<!-- Live Example -->
<img src="https://raw.githubusercontent.com/lunarcomet39/The_Central_Question_Images/main/images/physics/2025/x1aAx5lLdV_qbd0gy2Kx7.png" alt="Question Diagram" />
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
| **Total** | **16,631** | **~1.32 GB Web Assets** |

---

## Dedicated Database Copy with CDN URLs

A ready-to-use transformed database has been generated:
- File: `The_Central_Question_Database/questions_cdn.db`
- Every `question_html`, `option_a/b/c/d`, `solution_html`, and `image_urls` column has been automatically replaced to use the CDN URL:
  `https://cdn.statically.io/gh/lunarcomet39/The_Central_Question_Images/main/images/...`
- Total questions transformed: **10,851 questions with images**.

---

## Manifest Mapping

The complete machine-readable mapping from asset URLs to their canonical CDN paths is stored in [`image_manifest.json`](image_manifest.json):

```json
{
  "https://assets.example.com/A5K5u6qQYNNKl2QYb-Ny_.png": {
    "clean_url": "https://assets.example.com/A5K5u6qQYNNKl2QYb-Ny_.png",
    "filename": "A5K5u6qQYNNKl2QYb-Ny_.png",
    "subject": "physics",
    "year": "undated",
    "rel_path": "images/physics/undated/A5K5u6qQYNNKl2QYb-Ny_.png",
    "cdn_url": "https://cdn.statically.io/gh/lunarcomet39/The_Central_Question_Images/main/images/physics/undated/A5K5u6qQYNNKl2QYb-Ny_.png"
  }
}
```

---

## License

Assets cataloged in this repository are intended for academic and non-commercial educational purposes under the **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)** license.
