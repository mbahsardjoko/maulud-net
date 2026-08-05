#!/usr/bin/env python3
"""Insert 6 new real job listings (found via web search) into lowongan.json."""
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE / 'loker' / 'lowongan.json'

POSTED = "2026-08-05"
EXPIRES = "2026-09-04"

with open(DB_PATH) as f:
    data = json.load(f)

NEW_JOBS = [
    {
        "slug": "backend-engineer-paragoncorp-jakarta",
        "title": "Backend Engineer (Express.js & PostgreSQL)",
        "company": "ParagonCorp",
        "location": "Jakarta Selatan, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 12-20 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "ParagonCorp (PT Paragon Technology and Innovation), perusahaan FMCG terkemuka Indonesia yang menaungi brand kecantikan seperti Wardah dan Emina, sedang membuka lowongan Backend Engineer di Jakarta Selatan. Posisi ini bertanggung jawab mengembangkan, menguji, dan memelihara backend services menggunakan Express.js dan PostgreSQL, termasuk merancang RESTful API yang andal dan menjaga kualitas kode. Cocok untuk developer backend yang memahami arsitektur layanan, senang berkolaborasi lintas tim, dan ingin berkontribusi pada produk digital yang digunakan jutaan pengguna di Indonesia.",
        "requirements": [
            "Lulusan S1 Teknik Informatika, Ilmu Komputer, atau bidang terkait",
            "Pengalaman 2-5 tahun sebagai Backend Engineer atau Software Engineer",
            "Mahir menggunakan JavaScript/Node.js terutama Express.js",
            "Pengalaman dengan PostgreSQL dan desain database relasional",
            "Pemahaman kuat tentang desain dan implementasi RESTful API",
            "Familiar dengan Git, CI/CD, dan best practice pengembangan",
            "Kemampuan bekerja kolaboratif dengan tim product, frontend, dan DevOps"
        ],
        "responsibilities": [
            "Mengembangkan, menguji, dan memelihara backend services menggunakan Express.js dan PostgreSQL",
            "Merancang dan mengimplementasikan RESTful API yang scalable dan aman",
            "Memastikan kualitas dan reliabilitas kode melalui code review dan testing",
            "Berkolaborasi lintas tim dalam pengembangan fitur produk",
            "Mengoptimalkan performa database dan query untuk skala besar",
            "Menjaga dokumentasi teknis tetap akurat dan terkini"
        ],
        "benefits": [
            "Gaji kompetitif sesuai pengalaman dan standar industri",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Lingkungan kerja perusahaan FMCG terkemuka dengan jenjang karir jelas",
            "Kesempatan berkontribusi pada produk digital berskala besar",
            "Kultur belajar dan pengembangan skill teknis berkelanjutan",
            "Fasilitas dan tunjangan sesuai kebijakan perusahaan"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/backend-engineer-at-paragoncorp-4332545633",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/backend-engineer-at-paragoncorp-4332545633",
        "featured": True
    },
    {
        "slug": "software-engineer-tagflow-ai-jakarta",
        "title": "Software Engineer",
        "company": "Tagflow AI",
        "location": "Jakarta Raya, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Kompetitif (sesuai standar startup AI)",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "Tagflow AI, startup yang membangun platform AI fine-tuning dan retrieval untuk aplikasi AI nyata, sedang membuka lowongan Software Engineer di Jakarta. Kamu akan membangun backbone platform AI tersebut, merancang sistem yang scalable secara end-to-end, serta berkontribusi lintas area backend, frontend, dan DevOps. Posisi ini cocok untuk software engineer yang haus tantangan teknis, menyukai sistem terdistribusi, dan ingin terlibat langsung dalam pengembangan produk AI dari nol hingga produksi.",
        "requirements": [
            "Pengalaman sebagai Software Engineer atau Full-stack Developer",
            "Pemahaman kuat tentang desain sistem dan arsitektur scalable",
            "Pengalaman dengan backend (Node.js, Python, atau Go) dan membangun API",
            "Familiar dengan frontend modern dan praktik DevOps dasar",
            "Pemahaman dasar tentang AI/ML, fine-tuning, dan retrieval adalah nilai plus",
            "Kemampuan memecahkan masalah kompleks secara mandiri dan kolaboratif",
            "Bersedia bekerja di Jakarta Raya"
        ],
        "responsibilities": [
            "Merancang dan membangun sistem scalable secara end-to-end",
            "Mengembangkan fitur lintas area backend, frontend, dan DevOps",
            "Mendukung pengembangan dan deployment aplikasi AI nyata",
            "Berpartisipasi dalam perancangan arsitektur dan review kode",
            "Mengoptimalkan performa dan keandalan platform",
            "Berkolaborasi dengan tim product dan engineering"
        ],
        "benefits": [
            "Pengalaman langsung membangun produk AI modern",
            "Lingkungan kerja startup yang dinamis dan fleksibel",
            "Kesempatan belajar teknologi AI terkini",
            "Kompensasi kompetitif sesuai standar industri",
            "Peran dengan dampak besar dan ruang untuk berkembang"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/software-engineer-at-tagflow-ai-4294597575",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/software-engineer-at-tagflow-ai-4294597575",
        "featured": False
    },
    {
        "slug": "data-analyst-lamudi-indonesia-jakarta",
        "title": "Data Analyst",
        "company": "Lamudi Indonesia",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 10-18 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "Lamudi.co.id, platform properti online terpercaya di Indonesia, sedang membuka lowongan Data Analyst melalui Kalibrr. Posisi ini akan bekerja erat dengan tim Marketing untuk mengidentifikasi masalah dan peluang bisnis, mengembangkan serta memelihara laporan terkait Marketing dan Sales, dan menghasilkan actionable insights untuk mendukung penyusunan strategi baru. Cocok untuk analis data yang detail-oriented, mampu mengkomunikasikan temuan ke berbagai stakeholder, dan ingin berkontribusi pada pertumbuhan bisnis properti digital.",
        "requirements": [
            "Pengalaman sebagai Data Analyst atau peran analisis data serupa",
            "Kemampuan mengolah dan menganalisis data (Excel, SQL, dan tools analisis)",
            "Pemahaman tentang metrik Marketing dan Sales",
            "Kemampuan menyusun laporan dan visualisasi data yang jelas",
            "Keterampilan komunikasi untuk memimpin diskusi dengan stakeholder",
            "Pemahaman bahasa Inggris (lisan dan tulisan) menjadi nilai plus",
            "Lulusan S1 Statistika, Matematika, Ekonomi, atau bidang terkait"
        ],
        "responsibilities": [
            "Bekerja erat dengan tim Marketing untuk memecahkan masalah bisnis",
            "Mengembangkan dan memelihara laporan terkait Marketing dan Sales",
            "Menghasilkan actionable insights untuk mendukung strategi baru",
            "Memimpin diskusi dan mengkomunikasikan temuan ke stakeholder",
            "Memonitor performa dan tren data secara berkala",
            "Mendukung pengambilan keputusan berbasis data lintas tim"
        ],
        "benefits": [
            "Gaji kompetitif (Rp 10-18 Juta) sesuai pengalaman",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Pengalaman di platform properti digital terkemuka",
            "Kesempatan berkontribusi langsung pada strategi bisnis",
            "Lingkungan kerja yang mendukung pengembangan skill analitik"
        ],
        "how_to_apply": "Kirim lamaran melalui Kalibrr. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://www.kalibrr.com/id-ID/c/lamudi-indonesia/jobs/246087/data-analyst",
        "source": "Kalibrr",
        "source_url": "https://www.kalibrr.com/id-ID/c/lamudi-indonesia/jobs/246087/data-analyst",
        "featured": False
    },
    {
        "slug": "accounting-analyst-facetology-jakarta",
        "title": "Accounting Analyst",
        "company": "Facetology",
        "location": "Jakarta Raya, Indonesia",
        "type": "Full-time",
        "category": "Finance",
        "salary": "Rp 8-14 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "Facetology, brand skincare lokal yang berkembang pesat di Indonesia, sedang membuka lowongan Accounting Analyst di Jakarta. Posisi ini bertanggung jawab menangani akuntansi umum perusahaan, termasuk akuntansi inventori, COGS, dan perpajakan dasar. Cocok untuk profesional akuntansi dengan pengalaman 2-5 tahun, terutama yang pernah berkecimpung di industri FMCG, retail, atau beauty. Kamu akan bekerja dalam tim keuangan yang dinamis dan berkontribusi pada akurasi laporan keuangan brand kecantikan yang sedang naik daun.",
        "requirements": [
            "Lulusan S1 Akuntansi atau Finance",
            "Pengalaman 2-5 tahun di bidang akuntansi (pengalaman FMCG/retail/beauty adalah nilai plus)",
            "Pemahaman kuat tentang akuntansi inventori, COGS, dan perpajakan dasar",
            "Menguasai Microsoft Excel dan software akuntansi",
            "Teliti, jujur, dan detail-oriented",
            "Kemampuan bekerja dalam tenggat waktu dan kolaborasi tim"
        ],
        "responsibilities": [
            "Mengelola dan mencatat transaksi akuntansi harian",
            "Menyusun dan memverifikasi laporan keuangan terkait inventori dan COGS",
            "Menangani aspek perpajakan dasar perusahaan",
            "Melakukan rekonsiliasi akun dan analisis data keuangan",
            "Mendukung proses closing dan pelaporan bulanan",
            "Berkolaborasi dengan tim keuangan dan operasional"
        ],
        "benefits": [
            "Gaji kompetitif sesuai pengalaman",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Produk Facetology gratis setiap bulan",
            "Pengalaman di industri beauty/FMCG yang berkembang",
            "Lingkungan kerja muda dan dinamis",
            "Kesempatan pengembangan karir di bidang finance"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/accounting-analyst-at-facetology-4371787490",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/accounting-analyst-at-facetology-4371787490",
        "featured": False
    },
    {
        "slug": "senior-accounting-tax-specialist-mandarin-tec-do-jakarta",
        "title": "Senior Accounting & Tax Specialist (Mandarin)",
        "company": "Tec-Do",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Finance",
        "salary": "Rp 12-20 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "Tec-Do membuka lowongan Senior Accounting & Tax Specialist untuk penempatan on-site di Jakarta. Posisi full-time ini menuntut kemampuan berbahasa Mandarin karena akan menangani akuntansi dan perpajakan dengan stakeholder berbahasa Mandarin. Cocok untuk profesional akuntansi senior dengan latar belakang S1 Akuntansi atau Finance, sertifikasi profesional (CPA/CMA) menjadi nilai tambah. Kamu akan bertanggung jawab atas kelancaran akuntansi dan kepatuhan pajak perusahaan serta berkoordinasi dengan tim terkait.",
        "requirements": [
            "Lulusan S1 Akuntansi, Finance, atau bidang terkait",
            "Fasih berbahasa Mandarin (lisan dan tulisan)",
            "Pengalaman sebagai senior accountant atau tax specialist",
            "Sertifikasi profesional (CPA, CMA) menjadi nilai tambah",
            "Pemahaman kuat tentang akuntansi dan perpajakan Indonesia",
            "Menguasai software akuntansi dan perpajakan",
            "Teliti, detail-oriented, dan mampu bekerja on-site di Jakarta"
        ],
        "responsibilities": [
            "Mengelola proses akuntansi dan pelaporan keuangan perusahaan",
            "Menangani kepatuhan dan pelaporan pajak",
            "Berkoordinasi dengan stakeholder berbahasa Mandarin",
            "Menyusun laporan keuangan dan rekonsiliasi akun",
            "Mendukung proses audit internal dan eksternal",
            "Memberikan rekomendasi terkait efisiensi pajak dan akuntansi"
        ],
        "benefits": [
            "Gaji kompetitif sesuai pengalaman dan keahlian bahasa",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Pengalaman menangani akuntansi internasional",
            "Kesempatan pengembangan karir di bidang finance & tax",
            "Lingkungan kerja profesional dan multikultural"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/senior-accounting-tax-specialist-mandarin-at-tec-do-4271538013",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/senior-accounting-tax-specialist-mandarin-at-tec-do-4271538013",
        "featured": False
    },
    {
        "slug": "customer-service-mandarin-speaker-bank-neo-commerce-jakarta-utara",
        "title": "Customer Service (Mandarin Speaker)",
        "company": "PT Bank Neo Commerce Tbk",
        "location": "Jakarta Utara, Indonesia",
        "type": "Full-time",
        "category": "Customer Service",
        "salary": "Rp 7-12 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "PT Bank Neo Commerce Tbk, bank digital terkemuka di Indonesia, sedang membuka lowongan Customer Service (Mandarin Speaker) di Jakarta Utara. Posisi ini bertanggung jawab memberikan layanan pelanggan kelas satu bagi nasabah berbahasa Mandarin melalui berbagai channel, menangani pertanyaan, keluhan, dan kebutuhan nasabah dengan ramah serta profesional. Cocok untuk individu yang fasih berbahasa Mandarin, komunikatif, sabar, dan ingin berkarier di industri perbankan digital yang berkembang pesat di Indonesia.",
        "requirements": [
            "Fasih berbahasa Mandarin (lisan dan tulisan)",
            "Kemampuan komunikasi yang baik dan empati tinggi",
            "Pengalaman customer service adalah nilai tambah",
            "Ramah, sabar, dan mampu menangani keluhan pelanggan",
            "Familiar dengan layanan perbankan adalah nilai plus",
            "Bersedia ditempatkan di Jakarta Utara"
        ],
        "responsibilities": [
            "Memberikan layanan pelanggan bagi nasabah berbahasa Mandarin",
            "Menangani pertanyaan, keluhan, dan kebutuhan nasabah",
            "Memberikan informasi produk dan layanan perbankan",
            "Menjaga kepuasan dan loyalitas nasabah",
            "Mencatat dan menindaklanjuti permintaan pelanggan",
            "Berkolaborasi dengan tim terkait untuk resolusi masalah"
        ],
        "benefits": [
            "Gaji kompetitif sesuai pengalaman",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Pengalaman di industri perbankan digital",
            "Bekerja di perusahaan bank digital terkemuka",
            "Kesempatan pengembangan karir dan pelatihan",
            "Cuti dan tunjangan sesuai kebijakan perusahaan"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/customer-service-mandarin-speaker-at-pt-bank-neo-commerce-tbk-4311837697",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/customer-service-mandarin-speaker-at-pt-bank-neo-commerce-tbk-4311837697",
        "featured": False
    }
]

# Safety check: refuse if any slug already exists
existing = {j.get('slug') for j in data.get('jobs', [])}
dupes = [j['slug'] for j in NEW_JOBS if j['slug'] in existing]
if dupes:
    raise SystemExit(f"Duplicate slug detected, aborting: {dupes}")

# Insert at index 0 (newest first)
data['jobs'] = NEW_JOBS + data.get('jobs', [])

# Ensure categories always non-null array
cats = sorted({j.get('category') for j in data['jobs'] if j.get('category')})
data['categories'] = cats

with open(DB_PATH, 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"OK: inserted {len(NEW_JOBS)} jobs. Total now {len(data['jobs'])}")