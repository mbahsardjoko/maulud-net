#!/usr/bin/env python3
"""Insert 6 new real job listings (found via web search) into lowongan.json."""
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE / 'loker' / 'lowongan.json'

POSTED = "2026-08-07"
EXPIRES = "2026-09-06"

with open(DB_PATH) as f:
    data = json.load(f)

NEW_JOBS = [
    {
        "slug": "data-analyst-mcn-warna-emas-indonesia",
        "title": "Data Analyst (MCN) - New 2026",
        "company": "Warna Emas Indonesia",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 6-9 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "Warna Emas Indonesia, perusahaan yang bergerak di bidang manajemen konten kreator dan pemberi jasa digital, membuka posisi Data Analyst (MCN). Kamu akan bertugas memastikan data dari berbagai platform digital dikelola dengan rapi, dianalisis, dan diubah menjadi insight yang berguna bagi tim konten dan bisnis. Peran ini sangat cocok untuk analis data yang teliti, nyaman bekerja dengan data dari platform seperti TikTok dan Shopee, serta ingin berkontribusi pada industri kreator digital yang terus tumbuh.",
        "requirements": [
            "Pengalaman 1-3 tahun sebagai Data Analyst atau posisi serupa (fresh graduate berpengalaman diutamakan)",
            "Kemampuan mengolah dan membersihkan data dari berbagai sumber (TikTok, Shopee, dashboard internal)",
            "Menguasai Excel/Google Sheets lanjutan serta SQL; familiar dengan tools visualisasi data menjadi nilai tambah",
            "Ketelitian tinggi dalam menangani data dan perhatian terhadap detil",
            "Mampu menyusun laporan dan menyajikan insight secara jelas kepada tim non-teknis",
            "Komunikasi baik dan mampu bekerja dalam tim maupun secara mandiri"
        ],
        "responsibilities": [
            "Mengumpulkan, membersihkan, dan mengintegrasikan data dari TikTok, Shopee, serta dashboard internal",
            "Menganalisis data transaksi dan aktivitas user untuk menemukan tren dan pola",
            "Menyusun insight yang actionable untuk tim kreator dan bisnis",
            "Membuat laporan berkala dan visualisasi data untuk mendukung pengambilan keputusan",
            "Menjaga kualitas dan akurasi data agar siap dipakai lintas tim"
        ],
        "benefits": [
            "Gaji kompetitif dengan tunjangan",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Pengalaman kerja di industri kreator digital (MCN) yang berkembang",
            "Lingkungan tim yang muda, dinamis, dan kolaboratif",
            "Kesempatan mengembangkan skill analisis data dan business intelligence"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/data-analyst-mcn-at-warna-emas-indonesia-4361976619",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/data-analyst-mcn-at-warna-emas-indonesia-4361976619",
        "featured": True
    },
    {
        "slug": "full-stack-engineer-glints-jakarta",
        "title": "Full Stack Engineer",
        "company": "Glints",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 12-20 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "Glints, platform teknologi yang menghubungkan talenta dengan peluang karier di Asia Tenggara, sedang mencari Full Stack Engineer untuk di tempatkan di Jakarta. Kamu akan berperan dalam membangun dan mengembangkan fitur platform yang dipakai ribuan pengguna, mulai dari sisi frontend hingga backend. Peran ini pas untuk engineers yang menyukai tantangan, punya fondasi teknis yang kuat, dan ingin berdampak pada produk yang mendekatkan talenta dengan perusahaan terbaik.",
        "requirements": [
            "Pengalaman 2-5 tahun sebagai full stack / backend / frontend engineer",
            "Menguasai bahasa pemrograman modern (Javascript/Typescript, dan salah satu backend seperti Node.js, Golang, atau Python)",
            "Pengalaman menggunakan framework frontend seperti React.js dan memahami API design",
            "Pemahaman database relasional (SQL), caching, dan konsep arsitektur web",
            "Familiar dengan cloud services, containerization, dan tooling CI/CD menjadi nilai tambah",
            "Kemampuan problem solving yang kuat dan komunikasi tim yang baik"
        ],
        "responsibilities": [
            "Membangun, mengembangkan, dan merawat fitur platform baik di sisi frontend maupun backend",
            "Berkolaborasi dengan tim product dan design untuk menerjemahkan kebutuhan user menjadi solusi teknis",
            "Menulis code yang bersih, teruji, dan mudah dimengerti",
            "Melakukan code review dan menjaga kualitas teknis codebase",
            "Mengoptimalkan performa aplikasi serta memastikan kestabilan system"
        ],
        "benefits": [
            "Gaji kompetitif sesuai pengalaman",
            "Asuransi kesehatan dan tunjangan industri",
            "Lingkungan kerja startup teknologi yang inovatif",
            "Kesempatan belajar dan berkembang bersama talenta terbaik",
            "Fasilitas dan tools kerja yang menunjang produktivitas"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/full-stack-engineer-at-glints-3429234720",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/full-stack-engineer-at-glints-3429234720",
        "featured": False
    },
    {
        "slug": "content-writer-shoutvox-jakarta",
        "title": "Content Writer",
        "company": "ShoutVox",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Konten & Kreatif",
        "salary": "Rp 4-7 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "ShoutVox, agensi digital yang berfokus pada produksi konten dan public digital, sedang membukan posisi Content Writer untuk ditempatkan di Jakarta. Kamu akan menulis berbagai materi konten menarik, informatif, dan sesuai dengan tujuan klien, kemudian berkoordinasi dengan tim kreatif dalam proses produksinya. Peran ini cocok untuk penulis yang pandai merangkai narasi, peka terhadap tren, serta mampu mengikuti brief dan tenggat dengan baik.",
        "requirements": [
            "Pengalaman menulis konten (artikel, blog, media sosial, atau copywriting)",
            "Kemampuan komunikasi tertulis yang sangat baik dalam Bahasa Indonesia dan Inggris menjadi nilai tambah",
            "Mengerti dasar SEO penelitian kata kunci untuk konten yang mudah ditemukan online",
            "Kemampuan bekerja mandiri dan remote serta menjaga tenggat dan manajemen waktu",
            "Kreatif, teliti, dan adaptif terhadap berbagai gaya dan brand voice"
        ],
        "responsibilities": [
            "Menulis dan mengembangkan konten berkualitas untuk berbagai keperluan dan kanal",
            "Riset topik dan kata kunci untuk mendukung konten yang maksimal",
            "Menyesuaikan gaya tulisan dengan brand voice dan kebutuhan klien",
            "Berkolaborasi dengan tim kreatif dan editor dalam menyelesaikan materi konten",
            "Melakukan editing dan penyempurnaan draf sesuai feedback"
        ],
        "benefits": [
            "Gaji pokok beserta tunjangan",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Lingkungan kerja kreatif dan fleksibel",
            "Kesempatan berkembang di dunia digital content dan media",
            "Pengalaman mengerjakan konten untuk berbagai brand"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/content-writer-at-shoutvox-3726903511",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/content-writer-at-shoutvox-3726903511",
        "featured": False
    },
    {
        "slug": "junior-frontend-developer-ibunda-bandung",
        "title": "Junior Frontend Developer",
        "company": "Ibunda",
        "location": "Bandung, Jawa Barat",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 4-7 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "Ibunda, tim pengembang digital berbasis di Bandung, Jawa Barat, membuka kesempatan bagi junior untuk bergabung sebagai Frontend Developer. Kamu akan bekerja membangun dan mengembangkan antarmuka website agar mudah dipakai dan eye-catching. Posisi ini sangat pas untuk lulusan baru atau developer muda yang punya fondasi pemrogramman kuat, semangat belajar tinggi, dan ingin terus mengasah kemampuan dalam tim pengembangan yang supportive.",
        "requirements": [
            "Fresh graduate atau pengalaman junior di bidang frontend development",
            "Menguasai HTML, CSS, dan Javascript serta salah satu framework modern (React/Vue)",
            "Bisa menerjemahan desain menjadi tampilan web yang respons jika dan interaktif",
            "Memahami basic GIT dan pengembangan kolaboratif",
            "Semangat belajar, teliti, dan mampu bekerja dalam tim"
        ],
        "responsibilities": [
            "Membangun dan merawat komponen antarmuka halaman website",
            "Menampilkan data dan logika frontend sesuai kebutuhan produk",
            "Berkolaborasi dengan UI/UX dan backend untuk integrasi",
            "Mengikuti standar kode dan menjaga kualitas tampilan di berbagai perangkat",
            "Belajar dan menerapkan best practice pengembangan frontend"
        ],
        "benefits": [
            "Gaji kompetitif untuk level junior",
            "Environment belajar dan mentoring dari senior",
            "Kesempatan berkembang menjadi engineer penuh",
            "Lingkungan kerja kolaboratif dan informal",
            "Fleksibilitas kerja sesuai kebutuhan tim"
        ],
        "how_to_apply": "Kirim lamaran melalui Jora. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.jora.com/lowongan-Frontend-Developer-di-Indonesia",
        "source": "Jora",
        "source_url": "https://id.jora.com/lowongan-Frontend-Developer-di-Indonesia",
        "featured": False
    },
    {
        "slug": "content-writer-remote-gajihub-kledo",
        "title": "Content Writer (Remote)",
        "company": "PT GaJiHub (Kledo)",
        "location": "Remote, Indonesia",
        "type": "Full-time",
        "category": "Konten & Kreatif",
        "salary": "Rp 4-6 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "Kledo, platform akuntansi berbasis cloud yang membantu ribuan bisnis di Indonesia mengelola keuangan, inventori, hingga operasional dengan mudah, sedang mencari Content Writer yang professional bekerja remote. Kamu akan menyusun konten informatif seputar akuntansi, keuangan, dan solusi Kledo untuk membantu pelanggan dan calon pelanggan memahami produk. Peran ini terbuka luas tanpa minimal pendidikan tinggi tertentu dan sangat cocok untuk penulis yang rapi serta memahami topik bisnis dan keuangan.",
        "requirements": [
            "Bisa menulis konten yang jelas, informatif, dan mudah dipahami untuk topik keuangan/akuntansi",
            "Terbuka untuk berbagai jenjang pendidikan dengan kemampuan menulis yang baik",
            "Memahami dasar SEO dan ketertarikan pada produk SaaS",
            "Bisa bekerja remote dan mengelola tenggat secara mandiri",
            "Teliti dan disiplin dalam mengikuti pedoman editorial"
        ],
        "responsibilities": [
            "Menulis artikel dan materi konten tentang topik keuangan, akuntansi, dan produk Kledo",
            "Riset topik dan keyword untuk konten yang informatif dan bermanfaat",
            "Menyusun konten sesuai house style agar konsisten dan menarik",
            "Melakukan pengembangan produk dan penyempurnaan draf",
            "Berkolaborasi dengan tim digital dan marketing dalam rencana konten"
        ],
        "benefits": [
            "Bekerja 100% remote dengan honor/gaji yang kompetitif",
            "Fleksibilitas waktu kerja",
            "Pengalaman industri SaaS (software akuntansi) yang berkembang",
            "Kesempatan belajar mendalam topik keuangan dan konten digital",
            "Lingkungan kerja yang mendukung pertumbuhan individu"
        ],
        "how_to_apply": "Kirim lamaran melalui Glints. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://glints.com/id/opportunities/jobs/content-writer-remote/e8f7466d-0541-4cc4-92fb-fab111d7712c",
        "source": "Glints",
        "source_url": "https://glints.com/id/opportunities/jobs/content-writer-remote/e8f7466d-0541-4cc4-92fb-fab111d7712c",
        "featured": False
    },
    {
        "slug": "graphic-designer-pt-star-technology-digital",
        "title": "Graphic Designer",
        "company": "PT Star Technology Digital",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Desain",
        "salary": "Rp 6-9 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "PT Star Technology Digital, perusahaan aktif di bidang teknologi dan solusi digital, saat ini membuka lowongan Graphic Designer dengan ketempatkan di Jakarta. Posisi ini terbuka untuk kandidat dan level entry sampai dengan pengalaman hingga 2 tahun yang memiliki ketajaman estetika visual yang tinggi. Kamu akan bertugas menerjemahkan brief menjadi karya visual yang menarik untuk berbagai media sehingga konsisten dengan identitas brand.",
        "requirements": [
            "Pengalaman 1-3 tahun atau entry-level hingga 2 tahun di bidang Graphic Design",
            "Ketajaman tinggi terhadap detail dan estetika desain",
            "Menguasai tools desain seperti Adobe Photoshop, Illustrator, dan atau Figma",
            "Mampu menerjemahkan brief menjadi output visual",
            "Bisa bekerja dengan beragam media dan mampu bekerja dalam tim"
        ],
        "responsibilities": [
            "Membuat desain visual untuk keperluan digital, marketing, dan media sosial",
            "Menerjemahkan kebutuhan brand ke dalam karya visual yang menarik",
            "Menjaga konsistensi dan kesatuan elemen visual sesuai brand",
            "Berkolaborasi dengan tim kreatif dan marketing dalam kebutuhan desain",
            "Melakukan revisi dan finalisasi desain sesuai feedback"
        ],
        "benefits": [
            "Gaji yang selaras dengan pengalaman dan posisi",
            "Lingkungan kerja kreatif yang inovatif",
            "Pengalaman mengerjakan beragam projek digital",
            "Kesempatan mengasah skill dan berkembang",
            "Tunjangan dan kesejahteraan sesuai kebijakan perusahaan"
        ],
        "how_to_apply": "Kirim lamaran melalui Glints. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://glints.com/id/opportunities/jobs/graphic-design/8d9e4fab-4a90-40a2-9b52-381502334f96",
        "source": "Glints",
        "source_url": "https://glints.com/id/opportunities/jobs/graphic-design/8d9e4fab-4a90-40a2-9b52-381502334f96",
        "featured": False
    },
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