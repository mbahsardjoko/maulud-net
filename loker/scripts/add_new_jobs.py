#!/usr/bin/env python3
"""Add new job listings from web search results and regenerate posts."""
import json
import os
from datetime import datetime, timedelta

DATA_FILE = '/tmp/maulud-net/loker/lowongan.json'

with open(DATA_FILE, 'r') as f:
    data = json.load(f)

today = datetime.now().strftime('%Y-%m-%d')
expires = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')

new_jobs = [
    {
        "slug": "business-analyst-qoala-jakarta",
        "title": "Business Analyst",
        "company": "Qoala",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 8-15 Juta",
        "posted": today,
        "expires": expires,
        "description": "Qoala, platform insurtech terkemuka di Indonesia yang menyediakan solusi asuransi digital inovatif, membuka lowongan Business Analyst di Jakarta. Posisi ini akan bertanggung jawab menganalisis data bisnis, mengidentifikasi peluang perbaikan proses, dan memberikan rekomendasi strategis untuk mendukung pertumbuhan perusahaan. Kamu akan bekerja sama dengan tim product, engineering, dan operations untuk mendorong pengambilan keputusan berbasis data di lingkungan startup yang dinamis. Cocok untuk analis yang memiliki kemampuan analitis kuat dan passion di industri teknologi finansial.",
        "requirements": [
            "Minimal S1 di bidang Business, Statistics, Computer Science, atau terkait",
            "Pengalaman 1-2 tahun sebagai Business Analyst atau peran analitis serupa",
            "Mahir dalam SQL dan pengolahan data",
            "Pengalaman dengan tools analisis (Python, Excel, atau BI tools)",
            "Kemampuan komunikasi dan presentasi insight yang baik",
            "Pemahaman tentang produk dan metrik bisnis insurtech/fintech (nilai plus)",
            "Detail-oriented dan memiliki analytical thinking yang kuat",
            "Bersedia bekerja full-time di Jakarta"
        ],
        "responsibilities": [
            "Menganalisis data bisnis untuk mengidentifikasi tren, pola, dan peluang improvement",
            "Menyusun laporan analitis dan dashboard untuk mendukung pengambilan keputusan",
            "Berkolaborasi dengan tim product, engineering, dan operations",
            "Melakukan market research dan competitor analysis",
            "Mengelola data pipeline dan memastikan data quality",
            "Menyajikan insight dan rekomendasi ke stakeholder",
            "Mendukung perencanaan strategis dan OKR tracking"
        ],
        "benefits": [
            "Gaji kompetitif sesuai pengalaman",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Asuransi kesehatan tambahan",
            "Flexible working arrangement",
            "Laptop kerja disediakan",
            "Learning & development budget",
            "Lingkungan kerja startup yang dinamis"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/business-analyst-at-qoala-4333253216",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/business-analyst-at-qoala-4333253216",
        "featured": True
    },
    {
        "slug": "sap-analyst-new-graduate-2026-abeam-consulting-jakarta",
        "title": "SAP Analyst - New Graduate 2026",
        "company": "ABeam Consulting Indonesia",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 8-14 Juta",
        "posted": today,
        "expires": expires,
        "description": "ABeam Consulting Indonesia, bagian dari jaringan konsultan manajemen global terkemuka asal Jepang yang berfokus pada transformasi bisnis dan teknologi, membuka program New Graduate 2026 untuk posisi SAP Analyst. Program ini dirancang bagi fresh graduate yang bersemangat untuk memulai karir di dunia konsultan SAP/ERP. Kamu akan mendapatkan pelatihan intensif, mentorship dari konsultan senior, dan kesempatan bekerja pada proyek-proyek transformasi digital untuk klien-klien enterprise di berbagai industri. Cocok untuk lulusan baru yang ingin membangun karir di persimpangan antara bisnis dan teknologi.",
        "requirements": [
            "Fresh graduate S1 semua jurusan (lebih diutamakan Akuntansi, Sistem Informasi, Computer Science, atau Manajemen)",
            "IPK minimal 3.00 dari universitas terkemuka",
            "Ketertarikan kuat pada SAP/ERP dan konsultan teknologi",
            "Kemampuan analitis dan problem-solving yang baik",
            "Kemampuan komunikasi dalam Bahasa Indonesia dan Inggris yang aktif",
            "Bersedia belajar dan mengikuti pelatihan intensif",
            "Bersedia ditempatkan di Jakarta"
        ],
        "responsibilities": [
            "Mengikuti program pelatihan SAP/ERP yang komprehensif",
            "Mendukung tim konsultan dalam implementasi dan kustomisasi SAP untuk klien",
            "Melakukan analisis kebutuhan bisnis klien dan menerjemahkannya ke konfigurasi SAP",
            "Membantu dokumentasi proses bisnis dan teknis",
            "Berpartisipasi dalam testing, go-live, dan post-implementation support",
            "Berkolaborasi dengan tim multidisiplin untuk deliver solusi tepat waktu",
            "Mengikuti best practices dan metodologi konsultan ABeam"
        ],
        "benefits": [
            "Gaji kompetitif untuk fresh graduate",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Asuransi kesehatan tambahan",
            "Pelatihan SAP/ERP bersertifikasi internasional",
            "Mentoring dari konsultan senior berpengalaman",
            "Jenjang karir yang jelas di perusahaan konsultan global",
            "Kesempatan kerja pada proyek enterprise skala nasional dan regional"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/sap-analyst-new-graduate-2026-at-abeam-consulting-indonesia-4408661586",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/sap-analyst-new-graduate-2026-at-abeam-consulting-indonesia-4408661586",
        "featured": False
    },
    {
        "slug": "management-trainee-finance-accounting-app-group-jakarta",
        "title": "Management Trainee Finance & Accounting",
        "company": "APP Group",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Finance",
        "salary": "Rp 10-18 Juta",
        "posted": today,
        "expires": expires,
        "description": "APP Group, salah satu perusahaan pulp dan kertas terbesar di dunia yang berkantor pusat di Indonesia, membuka program Management Trainee Finance & Accounting. Program ini dirancang untuk mengembangkan talenta muda berbakat menjadi pemimpin masa depan di divisi keuangan perusahaan. Kamu akan mendapatkan rotasi di berbagai fungsi finance & accounting, pelatihan intensif, dan exposure langsung ke operasional bisnis skala global. Cocok untuk lulusan baru atau profesional muda yang ambisius dan ingin membangun karir di perusahaan multinasional dengan reputasi internasional.",
        "requirements": [
            "Minimal S1 Akuntansi, Manajemen Keuangan, atau jurusan terkait",
            "IPK minimal 3.00 dari universitas terkemuka",
            "Maksimal 1 tahun pengalaman kerja (fresh graduate dipersilakan)",
            "Pemahaman dasar tentang prinsip akuntansi dan pelaporan keuangan",
            "Mahir dalam Microsoft Excel dan familiar dengan ERP (SAP nilai plus)",
            "Kemampuan analitis dan numerik yang kuat",
            "Kemampuan komunikasi dalam Bahasa Indonesia dan Inggris",
            "Bersedia mengikuti program rotasi dan ditempatkan di Jakarta"
        ],
        "responsibilities": [
            "Mengikuti program rotasi di berbagai divisi finance & accounting",
            "Membantu proses pencatatan transaksi, jurnal akuntansi, dan rekonsiliasi",
            "Mendukung penyusunan laporan keuangan bulanan dan tahunan",
            "Berpartisipasi dalam proses audit internal dan eksternal",
            "Membantu analisis anggaran dan forecasting",
            "Berkolaborasi dengan tim lintas fungsi untuk kebutuhan financial reporting",
            "Mengikuti pelatihan dan pengembangan yang disediakan perusahaan"
        ],
        "benefits": [
            "Gaji kompetitif + tunjangan program trainee",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Asuransi kesehatan tambahan",
            "Program pengembangan kepemimpinan dan pelatihan teknis",
            "Rotasi di berbagai fungsi keuangan",
            "Kesempatan karir di perusahaan global skala Fortune 500",
            "Fasilitas kantor yang nyaman dan lingkungan kerja profesional"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/management-trainee-finance-accounting-at-app-group-4424502327",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/management-trainee-finance-accounting-at-app-group-4424502327",
        "featured": False
    },
    {
        "slug": "graphic-designer-olrange-tambora-jakarta",
        "title": "Graphic Designer",
        "company": "OLRANGE",
        "location": "Tambora, Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Desain",
        "salary": "Rp 5-9 Juta",
        "posted": today,
        "expires": expires,
        "description": "OLRANGE, brand lokal yang bergerak di bidang fashion dan lifestyle dengan produk-produk berkualitas tinggi dan desain yang unik, membuka lowongan Graphic Designer di Tambora, Jakarta. Kamu akan menjadi bagian dari tim kreatif yang bertanggung jawab menciptakan desain visual yang menarik untuk kebutuhan branding, marketing, dan komunikasi merek OLRANGE. Posisi ini cocok untuk desainer grafis yang kreatif, memiliki portofolio kuat, dan passionate dalam dunia fashion dan lifestyle. Kamu akan bekerja dalam lingkungan yang dinamis dan penuh inspirasi.",
        "requirements": [
            "Minimal D3/S1 Desain Grafis, Seni Visual, atau jurusan terkait",
            "Pengalaman minimal 1 tahun sebagai Graphic Designer",
            "Mahir dalam Adobe Creative Suite (Photoshop, Illustrator, InDesign)",
            "Portofolio yang menunjukkan kemampuan desain branding dan visual",
            "Pemahaman tipografi, color theory, dan komposisi visual yang baik",
            "Kreatif, detail-oriented, dan mampu bekerja dalam deadline",
            "Familiar dengan tren desain fashion/lifestyle terkini",
            "Bersedia bekerja on-site di Tambora, Jakarta"
        ],
        "responsibilities": [
            "Menciptakan desain visual untuk branding dan marketing materials",
            "Mengembangkan konsep kreatif untuk campaign produk dan promosi",
            "Mendesain konten untuk social media, website, dan marketplace",
            "Membuat desain packaging, label, dan materi cetak",
            "Berkolaborasi dengan tim marketing dan product development",
            "Menjaga konsistensi brand identity di semua touchpoint",
            "Mengikuti tren desain fashion dan lifestyle terkini"
        ],
        "benefits": [
            "Gaji kompetitif sesuai pengalaman",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Lingkungan kerja kreatif dan dinamis",
            "Produk OLRANGE dengan diskon karyawan",
            "Kesempatan mengembangkan portfolio brand fashion",
            "Pelatihan dan workshop pengembangan skill"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/graphic-designer-at-olrange-4014931276",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/graphic-designer-at-olrange-4014931276",
        "featured": False
    },
    {
        "slug": "customer-service-e-commerce-facetology-jakarta",
        "title": "Customer Service E-Commerce",
        "company": "Facetology",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Customer Service",
        "salary": "Rp 5-8 Juta",
        "posted": today,
        "expires": expires,
        "description": "Facetology, brand skincare dan kecantikan lokal yang berkembang pesat di Indonesia dengan produk-produk berbasis bahan aktif berkualitas, membuka lowongan Customer Service E-Commerce di Jakarta. Posisi ini bertanggung jawab memberikan layanan pelanggan yang prima melalui platform e-commerce, menangani pertanyaan produk, proses pemesanan, dan keluhan pelanggan dengan ramah dan profesional. Cocok untuk individu yang komunikatif, memiliki semangat pelayanan tinggi, dan ingin berkarier di industri kecantikan digital yang sedang booming.",
        "requirements": [
            "Minimal D3/S1 semua jurusan",
            "Pengalaman minimal 1 tahun di Customer Service (lebih diutamakan di e-commerce/retail)",
            "Kemampuan komunikasi verbal dan tulisan yang sangat baik",
            "Familiar dengan platform e-commerce (Shopee, Tokopedia, Lazada, TikTok Shop)",
            "Ramah, sabar, dan memiliki attitude pelayanan yang baik",
            "Mampu menangani keluhan pelanggan dengan solutif",
            "Teliti dan detail-oriented dalam dokumentasi",
            "Bersedia bekerja di Jakarta (on-site)"
        ],
        "responsibilities": [
            "Menangani pertanyaan dan konsultasi pelanggan melalui chat e-commerce dan media sosial",
            "Memproses pesanan, retur, dan refund sesuai prosedur",
            "Memberikan informasi produk dan rekomendasi skincare kepada pelanggan",
            "Menyelesaikan keluhan dan komplain pelanggan dengan solusi terbaik",
            "Mencatat dan mendokumentasikan interaksi pelanggan di sistem",
            "Berkolaborasi dengan tim warehouse dan marketing untuk kelancaran operasional",
            "Membantu meningkatkan rating dan ulasan toko di platform e-commerce"
        ],
        "benefits": [
            "Gaji pokok kompetitif + bonus kinerja",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Produk Facetology gratis setiap bulan",
            "Diskon karyawan untuk semua produk",
            "Pelatihan product knowledge dan customer service",
            "Lingkungan kerja yang supportive dan kekeluargaan",
            "Jenjang karir yang jelas di brand skincare nasional"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/customer-service-e-commerce-at-facetology-4423989281",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/customer-service-e-commerce-at-facetology-4423989281",
        "featured": False
    },
    {
        "slug": "brand-marketing-intern-pepsico-jakarta",
        "title": "Brand Marketing Intern",
        "company": "PepsiCo",
        "location": "Jakarta, Indonesia",
        "type": "Internship",
        "category": "Marketing",
        "salary": "Rp 5-7 Juta",
        "posted": today,
        "expires": expires,
        "description": "PepsiCo, perusahaan makanan dan minuman terkemuka di dunia dengan portofolio brand ikonik seperti Pepsi, Lay's, Quaker, Gatorade, dan banyak lagi, membuka kesempatan magang sebagai Brand Marketing Intern di Jakarta. Program magang ini memberikan pengalaman langsung dalam mengelola brand global di pasar Indonesia, bekerja dengan tim marketing profesional, dan terlibat dalam campaign activation, analisis pasar, dan strategi branding. Cocok untuk mahasiswa akhir atau fresh graduate yang passion di bidang brand management dan marketing FMCG.",
        "requirements": [
            "Mahasiswa aktif S1 minimal semester 6 atau fresh graduate (gap year diperbolehkan)",
            "Jurusan Marketing, Manajemen Bisnis, Komunikasi, atau terkait",
            "Minat kuat pada brand management dan industri FMCG",
            "Kemampuan analitis dan riset pasar yang baik",
            "Kreatif dan up-to-date dengan tren marketing terkini",
            "Mahir dalam Microsoft Office (PowerPoint, Excel, Word)",
            "Kemampuan komunikasi dalam Bahasa Indonesia dan Inggris",
            "Bersedia magang full-time di Jakarta"
        ],
        "responsibilities": [
            "Mendukung tim brand dalam pelaksanaan campaign marketing dan activation",
            "Melakukan riset pasar, kompetitor, dan consumer insight",
            "Membantu pengembangan materi marketing dan brand communication",
            "Menganalisis performa campaign dan menyusun laporan",
            "Berkolaborasi dengan agency dan tim internal untuk eksekusi program",
            "Mengelola administrative tasks terkait brand operations",
            "Berpartisipasi dalam brainstorming dan perencanaan strategi brand"
        ],
        "benefits": [
            "Uang saku magang kompetitif",
            "Pengalaman kerja di perusahaan FMCG global terkemuka",
            "Mentoring dari brand manager berpengalaman",
            "Exposure ke brand-brand global PepsiCo",
            "Networking dengan profesional industri FMCG",
            "Sertifikat magang dan referensi karir",
            "Produk PepsiCo gratis selama magang"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://www.linkedin.com/jobs/view/4441965016/",
        "source": "LinkedIn",
        "source_url": "https://www.linkedin.com/jobs/view/4441965016/",
        "featured": False
    }
]

# Check for duplicate slugs
existing_slugs = {job.get('slug') for job in data.get('jobs', [])}
for job in new_jobs:
    if job['slug'] in existing_slugs:
        print(f"WARNING: slug {job['slug']} already exists!")

# Insert new jobs at index 0
data['jobs'] = new_jobs + data['jobs']

# Write back
with open(DATA_FILE, 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Inserted {len(new_jobs)} new jobs. Total jobs now: {len(data['jobs'])}")
