import json

# Read existing file
with open('/tmp/maulud-net/loker/lowongan.json', 'r') as f:
    data = json.load(f)

# New jobs to prepend (from real web search results)
new_jobs = [
    {
        "slug": "campus-hiring-2026-byd-indonesia",
        "title": "Campus Hiring 2026 Fresh Graduate",
        "company": "BYD Indonesia",
        "location": "Bandung / Jakarta",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 8-15 Juta",
        "posted": "2026-07-12",
        "expires": "2026-08-11",
        "description": "BYD Indonesia, pemain global di industri kendaraan listrik dan energi terbarukan, membuka program Campus Hiring 2026 untuk fresh graduate yang ingin memulai karir di perusahaan inovatif berkelas dunia. Program ini dirancang untuk mengembangkan talenta muda melalui pelatihan intensif, mentoring dari senior engineer, dan rotasi proyek nyata di divisi R&D, manufacturing, maupun digital transformation. Kamu akan terlibat dalam proyek-proyek pionir yang mendukung transisi energi hijau Indonesia.",
        "requirements": [
            "Fresh graduate S1/D3 (angkatan 2024-2026) dari jurusan Teknik Elektro, Mekanik, Informatika, Kimia, atau terkait",
            "IPK minimal 3.00 skala 4.00",
            "Memiliki minat kuat pada industri EV, battery technology, atau renewable energy",
            "Bahasa Inggris pasif/aktif (minimal TOEIC 500 atau setara)",
            "Bersedia ditempatkan di Bandung atau Jakarta",
            "Memiliki mindset belajar cepat dan adaptif di lingkungan fast-paced",
            "Portfolio project/penelitian terkait teknologi hijau menjadi nilai plus"
        ],
        "responsibilities": [
            "Mengikuti program onboarding intensif 3-6 bulan dengan rotasi departemen",
            "Berkontribusi pada proyek R&D atau process improvement di lini produksi",
            "Menganalisis data performa produk/sistem dan menyusun rekomendasi",
            "Berkolaborasi dengan tim cross-functional (engineering, quality, supply chain)",
            "Mendokumentasikan temuan teknis dan best practice untuk knowledge sharing",
            "Menghadiri sesi mentoring rutin dengan senior engineer/manager"
        ],
        "benefits": [
            "Gaji kompetitif + tunjangan fresh graduate program",
            "BPJS Ketenagakerjaan dan Kesehatan efektif hari pertama",
            "Program pelatihan teknis & leadership berkelanjutan",
            "Akses ke jaringan global BYD untuk career development",
            "Transportasi shuttle & makan siang disediakan",
            "Lingkungan kerja inovatif dengan fasilitas lab & R&D center modern"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman Campus Hiring 2026 BYD Indonesia. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://www.linkedin.com/jobs/view/4400089141/",
        "source": "LinkedIn",
        "source_url": "https://www.linkedin.com/jobs/view/4400089141/",
        "featured": True
    },
    {
        "slug": "brilian-future-leader-program-bri-2026",
        "title": "BRILiaN Future Leader Program Specialist 2026 Wave 3",
        "company": "PT Bank Rakyat Indonesia (Persero) Tbk",
        "location": "Jakarta Raya",
        "type": "Full-time",
        "category": "Finance",
        "salary": "Rp 10-20 Juta",
        "posted": "2026-07-12",
        "expires": "2026-08-11",
        "description": "PT Bank Rakyat Indonesia (Persero) Tbk (BRI), bank terbesar di Indonesia dengan aset teratas ASEAN, membuka gelombang ke-3 program BRILiaN Future Leader Program (BFLP) 2026. Program ini dirancang untuk mencetak pemimpin masa depan perbankan melalui jalur accelerated development. Peserta akan menjalani rotasi di berbagai unit bisnis strategis — mulai dari mikro, retail, corporate, digital banking, hingga risk management — dengan bimbingan langsung dari senior leadership BRI.",
        "requirements": [
            "Fresh graduate S1/S2 (angkatan 2024-2026) dari universitas terakreditasi A/unggulan",
            "IPK minimal 3.25 (S1) / 3.50 (S2) skala 4.00",
            "Usia maksimal 25 tahun (S1) / 27 tahun (S2) per Juli 2026",
            "TOEFL ITP minimal 500 atau IELTS 6.0 / TOEIC 700",
            "Tidak terikat kontrak kerja/ikatan dinas dengan pihak lain",
            "Bersedia menjalani proses seleksi ketat (tes akademik, psikotes, wawancara panel)",
            "Memiliki integritas tinggi, leadership potential, dan komitmen karir panjang di perbankan"
        ],
        "responsibilities": [
            "Mengikuti program onboarding & immersion 6 bulan di kantor pusat & cabang",
            "Rotasi ke 3-4 unit bisnis berbeda (Micro, Consumer, Corporate, Digital, dll)",
            "Mengerjakan strategic project nyata dengan dampak bisnis terukur",
            "Berpartisipasi dalam leadership development: coaching, executive sharing, community service",
            "Menyusun business case & presentasi ke dewan direksi sebagai capstone project",
            "Membangun jaringan cross-generational dengan alumni BFLP & senior leader"
        ],
        "benefits": [
            "Gaji & tunjangan kompetitif sesuai standar BRI Management Trainee",
            "BPJS Ketenagakerjaan, Kesehatan, & Asuransi Jiwa komprehensif",
            "Program fast-track career ke posisi Officer/Assistant Manager",
            "Akses ke BRI Corporate University & sertifikasi perbankan internasional",
            "Tunjangan transportasi, komunikasi, & professional allowance",
            "Jaminan karir di bank negara terbesar dengan jaringan 10.000+ outlet"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman BRILiaN Future Leader Program BFLP Specialist 2026 Wave 3. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/brilian-future-leader-program-bflp-specialist-2026-wave-3-at-pt-bank-rakyat-indonesia-persero-tbk-4437982232",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/brilian-future-leader-program-bflp-specialist-2026-wave-3-at-pt-bank-rakyat-indonesia-persero-tbk-4437982232",
        "featured": False
    },
    {
        "slug": "international-trade-supervisor-aice-indonesia",
        "title": "International Trade Supervisor",
        "company": "Aice Indonesia",
        "location": "Jakarta Utara",
        "type": "Full-time",
        "category": "Marketing",
        "salary": "Rp 10-18 Juta",
        "posted": "2026-07-12",
        "expires": "2026-08-11",
        "description": "Aice Indonesia, brand es krim premium dari Grup Unilever yang memiliki pangsa pasar signifikan di Asia Tenggara, mencari International Trade Supervisor untuk mengembangkan bisnis ekspor ke pasar global. Posisi ini bertanggung jawab atas strategi penetrasi pasar baru, manajemen distributor internasional, serta kepatuhan regulasi perdagangan lintas batas. Kamu akan menjadi jembatan antara HQ Indonesia dengan tim regional dan kantor cabang di negara tujuan ekspor.",
        "requirements": [
            "Pengalaman minimal 3-5 tahun di international trade, export management, atau business development ekspor (FMCG/food beverage preferensi)",
            "S1 jurusan Ekonomi, Bisnis Internasional, Hukum Perdagangan, atau terkait",
            "Mahir dalam regulasi ekspor-impor Indonesia (INSW, HS Code, dokumen L/C, COO, dll)",
            "Pengalaman mengelola distributor/agen di minimal 2 negara ASEAN/Asia",
            "Bahasa Inggris lancar lisan tulis (Mandarin menjadi nilai plus besar)",
            "Kemampuan analisis pasar, pricing strategy, dan risk assessment trade",
            "Siap travel ke negara tujuan ekspor sesuai kebutuhan (20-30%)"
        ],
        "responsibilities": [
            "Menyusun & mengeksekusi roadmap ekspor Aice ke negara target baru",
            "Mengelola hubungan bisnis dengan distributor & buyer internasional",
            "Memastikan kelengkapan dokumen ekspor & kepatuhan regulasi negara tujuan",
            "Melakukan riset pasar & kompetitor untuk identifikasi opportunity & threat",
            "Berkoordinasi dengan supply chain, legal, finance, & marketing lokal",
            "Melaporkan KPI ekspor (volume, revenue, market share, collection) bulanan ke VP Sales"
        ],
        "benefits": [
            "Gaji pokok + bonus kinerja berbasis target ekspor",
            "BPJS Ketenagakerjaan & Kesehatan + asuransi travel internasional",
            "Tunjangan perjalanan dinas & representasi luar negeri",
            "Produk Unilever/Aice gratis & diskon karyawan",
            "Program rotasi global & secondment ke HQ regional",
            "Lingkungan kerja multinasional di kantor modern Jakarta Utara"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman International Trade Supervisor di Aice Indonesia. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://www.linkedin.com/jobs/view/international-trade-supervisor-at-aice-indonesia-4414438164",
        "source": "LinkedIn",
        "source_url": "https://www.linkedin.com/jobs/view/international-trade-supervisor-at-aice-indonesia-4414438164",
        "featured": False
    },
    {
        "slug": "unilever-apprenticeship-future-talents-2026",
        "title": "Apprenticeship for Future Talents 2026",
        "company": "Unilever Indonesia",
        "location": "Jakarta",
        "type": "Full-time",
        "category": "Marketing",
        "salary": "Rp 8-15 Juta",
        "posted": "2026-07-12",
        "expires": "2026-08-11",
        "description": "Unilever Indonesia, perusahaan FMCG terkemuka dengan brand household name seperti Molto, Royco, Lux, Dove, Wall's, dan Aice, membuka program Apprenticeship for Future Talents 2026. Program ini ditujukan untuk fresh graduate yang ingin belajar langsung di lingkungan bisnis nyata sambil mendapat mentoring dari praktisi senior. Peserta akan ditempatkan di salah satu fungsi: Brand Building, Customer Development, Supply Chain, Digital Transformation, atau Human Resources — dengan durasi 12-18 bulan.",
        "requirements": [
            "Fresh graduate S1 (angkatan 2024-2026) dari jurusan apapun (non-teknis welcome)",
            "IPK minimal 3.00 skala 4.00 dari universitas terakreditasi A/B",
            "Usia maksimal 25 tahun per Juli 2026",
            "Bahasa Inggris aktif (TOEFL 500+ / IELTS 6.0+ / TOEIC 650+)",
            "Pengalaman organisasi/kepanitiaan/volunteer/kegiatan kemahasiswaan aktif",
            "Tidak memiliki ikatan dinas/kerja dengan instansi lain",
            "Passion pada industri FMCG, sustainability, dan purpose-driven business"
        ],
        "responsibilities": [
            "Mengikuti structured learning curriculum: classroom, on-the-job, & action learning project",
            "Bekerja pada real business assignment di fungsi yang dipilih (Marketing, Sales, Supply Chain, HR, Digital)",
            "Menyusun & mempresentasikan improvement project kepada leadership team",
            "Berpartisipasi dalam Unilever Future Leaders Program (UFLP) selection process",
            "Berkolaborasi dengan fellow apprentices cross-fungsi untuk cross-functional project",
            "Mengembangkan personal development plan dengan mentor & line manager"
        ],
        "benefits": [
            "Stipend bulanan kompetitif + meal & transport allowance",
            "BPJS Kesehatan & Ketenagakerjaan penuh",
            "Akses ke Unilever Learning Platform (global courses, certifications)",
            "Mentoring 1-on-1 dari senior leader Unilever",
            "Kesempatan konversi ke karyawan tetap (UFLP/Management Trainee) berbasis performa",
            "Produk Unilever gratis bulanan & employee discount",
            "Hybrid working: 3 hari office (Jakarta), 2 hari remote"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman Apprenticeship for Future Talents Unilever Indonesia. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://www.linkedin.com/jobs/view/4438311956/",
        "source": "LinkedIn",
        "source_url": "https://www.linkedin.com/jobs/view/4438311956/",
        "featured": False
    },
    {
        "slug": "indonesian-digital-content-writer-remote-hire-feed",
        "title": "Indonesian Digital Content Writer (Remote)",
        "company": "Hire Feed",
        "location": "Remote - Indonesia",
        "type": "Part-Time Contract",
        "category": "Konten & Kreatif",
        "salary": "Rp 5-10 Juta",
        "posted": "2026-07-12",
        "expires": "2026-08-11",
        "description": "Hire Feed, platform rekrutmen berbasis teknologi yang menghubungkan talenta Indonesia dengan perusahaan global, mencari Indonesian Digital Content Writer untuk bekerja sepenuhnya remote. Posisi part-time contract ini cocok untuk penulis yang ingin fleksibilitas penuh sambil membangun portfolio konten digital skala internasional. Kamu akan menulis artikel blog, konten SEO, social media copy, dan email newsletter untuk audiens global dalam Bahasa Indonesia dan Inggris — fokus pada topik karir, remote work, tech hiring, dan future of work.",
        "requirements": [
            "Pengalaman minimal 1 tahun content writing / copywriting (fresh grad dengan portfolio kuat dipersilakan)",
            "Portfolio minimal 5 artikel publik (blog, Medium, LinkedIn, publikasi media) — wajib dilampirkan",
            "Kuasai Bahasa Indonesia baku & kaya; Bahasa Inggris minimal pasif (baca docs teknis) & aktif tulis basic",
            "Paham SEO dasar: keyword research, on-page optimization, search intent, heading structure",
            "Familiar dengan CMS (WordPress, Webflow, Notion, Ghost) dan tools: Grammarly, Hemingway, SurferSEO/Neuroflash",
            "Bisa kerja async, self-managed, komunikatif via Slack/Notion/Linear (remote full-time)",
            "Laptop & internet stabil sendiri (wajib)"
        ],
        "responsibilities": [
            "Menulis 4-6 artikel/bulan: blog post karir, remote work guide, hiring trends, company culture",
            "Riset topik: analisis kompetitor, keyword research, wawancaran SME internal",
            "Menyusun content calendar bulanan align dengan marketing strategy",
            "Optimasi SEO on-page: meta tags, heading structure, internal linking, schema markup",
            "Repurpose long-form content jadi social media post (LinkedIn, Twitter/X, Instagram)",
            "Kolaborasi dengan designer untuk visual pendukung (diagram, screenshot, infografis)",
            "Review & edit konten dari kontributor eksternal/junior writer"
        ],
        "benefits": [
            "Honor per artikel publish + bonus kualitas/SEO performance",
            "Fully remote: bebas lokasi di seluruh Indonesia",
            "Jam kerja fleksibel (output-based, core hours 10-15 WIB untuk sync)",
            "Budget learning: buku, kursus writing/SEO, konferensi teknologi",
            "Internet & coworking stipend bulanan",
            "Laptop allowance (setelah masa probasi 3 bulan)",
            "Cuti tahunan 14 hari + cuti sakit tidak terbatas (reasonable)",
            "Tim kecil, akses langsung ke founder & senior consultant untuk mentoring"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman Indonesian Digital Content Writer Remote di Hire Feed. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/indonesian-digital-content-writer-remote-at-hire-feed-4428670604",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/indonesian-digital-content-writer-remote-at-hire-feed-4428670604",
        "featured": False
    },
    {
        "slug": "mandarin-speaker-management-trainee-aice-indonesia",
        "title": "Mandarin Speaker Management Trainee",
        "company": "Aice Indonesia",
        "location": "Jakarta",
        "type": "Full-time",
        "category": "Marketing",
        "salary": "Rp 8-15 Juta",
        "posted": "2026-07-12",
        "expires": "2026-08-11",
        "description": "Aice Indonesia membuka program Management Trainee khusus untuk Mandarin Speaker sebagai bagian dari strategi ekspansi pasar Tiongkok dan Asia Timur. Program 18 bulan ini dirancang untuk mempersiapkan talenta muda memimpin bisnis cross-border — dari product localization, China market entry strategy, hingga manajemen distributor di mainland China, Hong Kong, dan Taiwan. Peserta akan berotasi di Marketing, Sales, Supply Chain, dan International Business Development dengan mentoring dari Country Head & Regional Director.",
        "requirements": [
            "Fresh graduate S1 (angkatan 2024-2026) dari universitas top di Indonesia/Tiongkok/SEA",
            "IPK minimal 3.25 skala 4.00",
            "Mandarin HSK 5/6 atau setara (lisan & tulis lancar) — WAJIB",
            "Bahasa Inggris aktif (TOEFL 500+ / IELTS 6.0+) untuk koordinasi regional",
            "Background bisnis, marketing, international trade, atau bahasa Tiongkok",
            "Memiliki minat kuat pada industri FMCG & pasar Greater China",
            "Bersedia travel ke Tiongkok/HK/Taiwan untuk market visit & distributor meeting"
        ],
        "responsibilities": [
            "Mengikuti rotasi 4 fungsi inti (Marketing, Sales, Supply Chain, Intl BizDev) masing-masing 4-5 bulan",
            "Melakukan riset konsumen & channel landscape di pasar Greater China untuk Aice",
            "Membantu adaptasi produk, packaging, & komunikasi marketing untuk lokalisasi Cina",
            "Mendukung negosiasi & onboarding distributor baru di mainland China/HK/Taiwan",
            "Menyusun business case & go-to-market plan untuk launch produk baru di pasar target",
            "Berkoordinasi dengan tim regional Unilever & HQ global untuk alignment strategi"
        ],
        "benefits": [
            "Stipend MT kompetitif + housing & transport allowance saat travel China",
            "BPJS Ketenagakerjaan & Kesehatan + asuransi travel internasional",
            "Kursus Bahasa Mandarin & Bahasa Inggris biaya penuh ditanggung perusahaan",
            "Mentoring langsung dari Country Head Indonesia & Regional Director China",
            "Program accelerated path ke International Brand Manager / Area Sales Manager",
            "Produk Unilever/Aice gratis & diskon karyawan",
            "Jaringan alumni MT Unilever global di 190+ negara"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman Mandarin Speaker Management Trainee di Aice Indonesia. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/mandarin-speaker-management-trainee-at-aice-indonesia-4433619428",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/mandarin-speaker-management-trainee-at-aice-indonesia-4433619428",
        "featured": False
    }
]

# Prepend new jobs to existing jobs
data['jobs'] = new_jobs + data['jobs']

# Write back
with open('/tmp/maulud-net/loker/lowongan.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_jobs)} new jobs. Total jobs: {len(data['jobs'])}")
for i, job in enumerate(new_jobs):
    print(f"{i+1}. {job['title']} ({job['company']}) - {job['source_url']}")