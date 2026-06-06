# Maulud.net — Lowongan Kerja

Portal lowongan kerja Indonesia. Static site via GitHub → Netlify.

## Struktur

```
/
├── index.html          # Halaman utama daftar lowongan
├── style.css           # Styling
├── lowongan.json       # Data lowongan (update otomatis via cron)
├── post/               # Halaman detail tiap lowongan
│   └── [slug].html
├── robots.txt          # SEO
├── sitemap.xml         # SEO
├── 404.html            # Halaman tidak ditemukan
└── scripts/
    └── generate-post.py  # Generate halaman detail dari JSON
```

## Cara Nambah Lowongan Baru

1. Edit `lowongan.json` — tambah entry baru di array `jobs`
2. Jalankan: `python3 scripts/generate-post.py`
3. Commit & push ke `main`

Auto-deploy via Netlify ✅

## Credentials

- GitHub: mbahsardjoko/maulud-net
- Email: fmindrayana@gmail.com
- Git user: CR7
- Netlify: connected via GitHub
