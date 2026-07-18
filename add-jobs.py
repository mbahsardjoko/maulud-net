#!/usr/bin/env python3
"""Add 6 new job listings to lowongan.json (at index 0)."""
import json
from datetime import date, timedelta

today = date.today()
expires = today + timedelta(days=30)
today_str = today.isoformat()
expires_str = expires.isoformat()

NEW_JOBS = [
    {
        "slug": "graphic-designer-pop-mart-jakarta",
        "title": "Graphic Designer",
        "company": "POP MART",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Desain",
        "salary": "Rp 6-10 Juta",
        "posted": today_str,
        "expires": expires_str,
        "description": "POP MART, perusahaan mainan dan koleksi asal Tiongkok yang telah mendunia, mencari Graphic Designer kreatif dan detail-oriented untuk bergabung dengan tim di Jakarta. Kamu akan bertanggung jawab menciptakan visual yang memukau untuk brand POP MART, mulai dari konten media sosial, materi promosi, hingga desain in-store. Posisi ini cocok untuk desainer yang memiliki passion pada seni, budaya pop, dan mainan koleksi, serta ingin bekerja di lingkungan brand global yang dinamis.",
        "requirements": [
            "Pengalaman minimal 1-2 tahun sebagai Graphic Designer",
            "Mahir Adobe Creative Suite (Photoshop, Illustrator, After Effects)",
            "Mahir Figma untuk desain digital dan prototyping",
            "Portofolio yang kuat menunjukkan kemampuan desain visual dan kreativitas",
            "Pemahaman yang baik tentang tipografi, teori warna, dan komposisi",
            "Kreatif, up-to-date dengan tren desain dan pop culture",
            "Mampu bekerja dalam tim dan memenuhi deadline",
            "Bahasa Inggris aktif adalah nilai plus"
        ],
        "responsibilities": [
            "Mendesain konten visual untuk media sosial, website, dan campaign marketing",
            "Membuat materi promosi: poster, banner, brosur, dan merchandise",
            "Mengembangkan visual untuk in-store display dan event POP MART",
            "Berkolaborasi dengan tim marketing dan creative untuk konsep visual",
            "Menjaga konsistensi brand identity di semua platform",
            "Mengikuti tren desain dan pop culture untuk konten yang relevan"
        ],
        "benefits": [
            "Gaji kompetitif dengan review tahunan",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Lingkungan kerja kreatif dan internasional",
            "Produk POP MART gratis dan diskon karyawan",
            "Kesempatan mengikuti event dan pameran",
            "Asuransi kesehatan tambahan"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/graphic-designer-at-pop-mart-4087384383",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/graphic-designer-at-pop-mart-4087384383",
        "featured": True
    },
    {
        "slug": "marketing-associate-program-apple-indonesia",
        "title": "Marketing Associate Program, Indonesia",
        "company": "Apple",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Marketing",
        "salary": "Rp 15-25 Juta",
        "posted": today_str,
        "expires": expires_str,
        "description": "Apple International Marketing team mencari kandidat terbaik untuk bergabung dalam Marketing Associate Program di Indonesia selama 18 bulan. Program ini dirancang untuk mengembangkan early career talent melalui rotasi di berbagai fungsi marketing, exposure ke produk-produk Apple, dan mentorship dari para pemimpin industri. Kamu akan berkontribusi pada strategi marketing Apple di Indonesia dan Asia Tenggara, serta belajar dari para ahli di bidang brand management, digital marketing, dan retail marketing.",
        "requirements": [
            "Fresh graduate atau maksimal 2 tahun pengalaman di bidang marketing",
            "Gelar S1 dari jurusan Marketing, Komunikasi, Bisnis, atau bidang terkait",
            "IPK minimal 3.20 dari 4.00",
            "Passion yang kuat terhadap produk dan brand Apple",
            "Kemampuan analitis dan data-driven mindset",
            "Kreatif dan memiliki storytelling skills yang baik",
            "Bahasa Inggris aktif (lisan dan tulisan)",
            "Bersedia bekerja full-time di Jakarta untuk program 18 bulan"
        ],
        "responsibilities": [
            "Mendukung tim marketing dalam perencanaan dan eksekusi kampanye",
            "Menganalisis data pasar dan konsumen untuk menginformasikan strategi",
            "Berkolaborasi dengan tim kreatif, digital, dan retail marketing",
            "Mengelola proyek marketing dari konsep hingga eksekusi",
            "Menyusun laporan performa kampanye dan insight untuk stakeholders",
            "Berpartisipasi dalam global marketing initiatives"
        ],
        "benefits": [
            "Gaji kompetitif standar perusahaan multinasional",
            "Program pelatihan dan pengembangan intensif selama 18 bulan",
            "Mentorship dari Apple leaders",
            "Asuransi kesehatan premium dan BPJS",
            "Produk Apple dan akses ke employee discount",
            "Kesempatan karir jangka panjang di Apple",
            "Lingkungan kerja inklusif dan inovatif"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://www.linkedin.com/jobs/view/4365813339",
        "source": "LinkedIn",
        "source_url": "https://www.linkedin.com/jobs/view/4365813339",
        "featured": False
    },
    {
        "slug": "graduate-analyst-ai-deloitte-jakarta",
        "title": "T&T Graduate Analyst – Artificial Intelligence",
        "company": "Deloitte",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 8-15 Juta",
        "posted": today_str,
        "expires": expires_str,
        "description": "Deloitte Indonesia membuka kesempatan bagi fresh graduate untuk bergabung dalam Technology & Transformation (T&T) practice sebagai Graduate Analyst di bidang Artificial Intelligence. Kamu akan bekerja pada proyek-proyek AI transformatif untuk klien di berbagai industri — membantu mereka merancang, mengembangkan, dan mengimplementasikan solusi AI yang mendorong pertumbuhan bisnis. Posisi ini ideal untuk lulusan yang passionat tentang AI dan ingin membuat dampak nyata melalui konsultan teknologi.",
        "requirements": [
            "Fresh graduate S1 dari jurusan Teknik Informatika, Ilmu Komputer, Sistem Informasi, Matematika, Statistika, atau terkait",
            "IPK minimal 3.00 dari 4.00",
            "Pemahaman dasar tentang machine learning, AI, dan data analytics",
            "Pengalaman dengan Python, SQL, dan libraries data science (Pandas, NumPy, Scikit-learn)",
            "Kemampuan analitis dan problem-solving yang kuat",
            "Komunikasi yang baik dalam Bahasa Indonesia dan Inggris",
            "Bersedia bekerja di Jakarta dengan kemungkinan perjalanan dinas ke klien"
        ],
        "responsibilities": [
            "Membantu tim dalam mengembangkan solusi AI untuk klien di berbagai industri",
            "Melakukan analisis data, data preprocessing, dan feature engineering",
            "Mengembangkan dan mengimplementasikan model machine learning",
            "Membantu dalam penyusunan presentasi dan laporan untuk klien",
            "Berpartisipasi dalam workshop dan diskusi dengan klien",
            "Melakukan riset teknologi AI terbaru dan best practice industri"
        ],
        "benefits": [
            "Gaji kompetitif dengan bonus tahunan",
            "Program pelatihan dan sertifikasi AI/data science",
            "Mentorship dari senior consultants dan partners",
            "BPJS Kesehatan, Ketenagakerjaan, dan asuransi swasta",
            "Exposure ke klien dan proyek multinasional",
            "Program pengembangan karir terstruktur",
            "Lingkungan kerja global dengan standar profesional tinggi"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://www.linkedin.com/jobs/view/4432218294",
        "source": "LinkedIn",
        "source_url": "https://www.linkedin.com/jobs/view/4432218294",
        "featured": False
    },
    {
        "slug": "customer-service-engineer-siemens-healthineers-jakarta",
        "title": "Customer Service Engineer (Field Service) – Jakarta",
        "company": "Siemens Healthineers",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Customer Service",
        "salary": "Rp 10-18 Juta",
        "posted": today_str,
        "expires": expires_str,
        "description": "Siemens Healthineers, perusahaan teknologi medis global terkemuka, mencari Customer Service Engineer (Field Service) untuk bergabung dengan tim Indonesia di Jakarta. Kamu akan bertanggung jawab melakukan instalasi, perawatan, perbaikan, dan update produk-produk kesehatan Siemens di fasilitas kesehatan seluruh Indonesia. Posisi ini cocok untuk engineer yang memiliki technical aptitude kuat dan ingin berkontribusi pada peningkatan kualitas layanan kesehatan di Indonesia dengan standar global.",
        "requirements": [
            "Gelar S1/D4 di bidang Teknik Elektro, Teknik Biomedis, Teknik Mesin, atau terkait",
            "Pengalaman minimal 2-3 tahun di field service atau maintenance engineering",
            "Pengalaman di bidang alat kesehatan sangat diutamakan",
            "Kemampuan troubleshooting teknis yang kuat dan analitis",
            "Bersedia melakukan perjalanan dinas ke berbagai kota di Indonesia",
            "Kemampuan komunikasi yang baik dengan customer",
            "Bahasa Inggris aktif (lisan dan tulisan)",
            "Memiliki SIM A dan kendaraan sendiri"
        ],
        "responsibilities": [
            "Melakukan instalasi, commissioning, dan kalibrasi peralatan medis Siemens",
            "Melakukan preventive maintenance dan perbaikan sesuai standar Siemens",
            "Mendiagnosis dan menyelesaikan masalah teknis di lokasi customer",
            "Memberikan pelatihan dasar kepada pengguna alat medis",
            "Mendokumentasikan setiap service visit dan report secara lengkap",
            "Menjaga hubungan baik dengan customer dan memahami kebutuhan mereka"
        ],
        "benefits": [
            "Gaji kompetitif dengan tunjangan lapangan",
            "Kendaraan dinas atau allowance transportasi",
            "BPJS Kesehatan, Ketenagakerjaan, dan asuransi kesehatan premium",
            "Pelatihan teknis produk Siemens Healthineers di dalam dan luar negeri",
            "Tunjangan hari raya dan bonus tahunan",
            "Asuransi perjalanan dinas",
            "Program pengembangan karir di perusahaan med-tech global"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://www.linkedin.com/jobs/view/customer-service-engineer-field-service-jakarta-at-siemens-healthineers-4029009969",
        "source": "LinkedIn",
        "source_url": "https://www.linkedin.com/jobs/view/customer-service-engineer-field-service-jakarta-at-siemens-healthineers-4029009969",
        "featured": False
    },
    {
        "slug": "content-creator-social-media-gently-jakarta",
        "title": "Content Creator & Social Media Specialist",
        "company": "Gently",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Konten & Kreatif",
        "salary": "Rp 5-9 Juta",
        "posted": today_str,
        "expires": expires_str,
        "description": "Gently, brand babycare dan lifestyle yang berkembang pesat di Indonesia, mencari Content Creator & Social Media Specialist untuk bergabung dengan tim kreatif mereka. Kamu akan bertanggung jawab menciptakan konten engaging untuk Instagram, TikTok, dan platform sosial lainnya, serta mengelola strategi sosial media untuk meningkatkan brand awareness dan engagement. Posisi ini cocok untuk kreator konten yang memiliki pemahaman mendalam tentang tren media sosial dan perilaku konsumen digital.",
        "requirements": [
            "Pengalaman minimal 2 tahun sebagai Content Creator, Social Media Specialist, atau peran serupa",
            "Pengalaman di industri babycare, beauty, parenting, atau lifestyle sangat diutamakan",
            "Mahir dalam berbagai format konten dan platform (Instagram, TikTok, Threads, Reels)",
            "Kemampuan copywriting dan storytelling yang kuat",
            "Terampil menggunakan alat editing video dan foto (CapCut, Premiere Pro, Canva)",
            "Pemahaman tentang social media analytics dan tren konten",
            "Kreatif, proaktif, dan mampu bekerja dalam target",
            "Portofolio konten yang kuat (wajib)"
        ],
        "responsibilities": [
            "Menciptakan dan memproduksi konten kreatif untuk Instagram, TikTok, dan platform sosial lainnya",
            "Mengembangkan strategi konten yang selaras dengan brand identity Gently",
            "Mengelola jadwal posting, community engagement, dan interaksi dengan followers",
            "Memonitor tren media sosial dan mengadaptasinya untuk konten brand",
            "Berkolaborasi dengan influencer, KOL, dan brand partners",
            "Menganalisis performa konten dan memberikan rekomendasi improvement",
            "Membuat laporan bulanan social media metrics dan insight"
        ],
        "benefits": [
            "Gaji kompetitif + performance bonus",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Lingkungan kerja kreatif dan dinamis",
            "Produk Gently gratis untuk karyawan",
            "Fleksibilitas kerja (hybrid)",
            "Kesempatan berkembang di brand lifestyle yang sedang naik daun",
            "Akses ke tools dan platform content creation premium"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/content-creator-social-media-specialist-at-gently-4306422002",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/content-creator-social-media-specialist-at-gently-4306422002",
        "featured": False
    },
    {
        "slug": "junior-software-engineer-backend-tiketcom-jakarta",
        "title": "Junior Software Engineer, Backend",
        "company": "Tiket.com (PT. Global Tiket Network)",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 8-14 Juta",
        "posted": today_str,
        "expires": expires_str,
        "description": "Tiket.com, platform travel dan lifestyle terkemuka di Indonesia, membuka lowongan Junior Software Engineer, Backend untuk bergabung dengan tim engineering mereka di Jakarta. Kamu akan merancang dan mengembangkan backend services yang scalable, resilient, dan high-performance untuk melayani jutaan pengguna Tiket.com. Posisi ini cocok untuk fresh graduate atau junior engineer yang ingin belajar dari para senior engineer dan berkontribusi pada produk travel terbesar di Indonesia.",
        "requirements": [
            "Fresh graduate S1 Ilmu Komputer, Teknik Informatika, atau bidang terkait",
            "Pemahaman kuat tentang algoritma, struktur data, dan pemrograman berorientasi objek",
            "Pengalaman dengan salah satu bahasa pemrograman: Go, Java, Python, atau Node.js",
            "Pemahaman dasar tentang database relasional (MySQL/PostgreSQL) dan NoSQL",
            "Familiar dengan RESTful API dan microservices architecture",
            "Pemahaman tentang version control (Git)",
            "Kemampuan problem-solving dan learning agility yang tinggi",
            "Bersedia bekerja di Jakarta (hybrid)"
        ],
        "responsibilities": [
            "Mengembangkan dan memelihara backend services untuk platform Tiket.com",
            "Menulis kode yang bersih, terstruktur, dan ter-test dengan baik",
            "Berkolaborasi dengan tim frontend, product, dan QA dalam pengembangan fitur",
            "Mengoptimalkan performa API dan database query",
            "Berpartisipasi dalam code review dan diskusi teknis tim",
            "Belajar dan menerapkan best practice dalam software engineering"
        ],
        "benefits": [
            "Gaji kompetitif untuk fresh graduate",
            "BPJS Kesehatan, Ketenagakerjaan, dan asuransi swasta",
            "Program mentorship dari senior engineers",
            "Lingkungan kerja startup unicorn dengan tech stack modern",
            "MacBook dan peralatan kerja lengkap",
            "Makan siang dan snack di kantor",
            "Tiket pesawat dan hotel diskon untuk karyawan",
            "Kesempatan belajar dan berkembang di perusahaan travel terkemuka"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/junior-software-engineer-backend-at-tiket-com-4404279817",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/junior-software-engineer-backend-at-tiket-com-4404279817",
        "featured": False
    }
]

# Read existing JSON
with open('/tmp/maulud-net/loker/lowongan.json') as f:
    data = json.load(f)

existing_slugs = {j['slug'] for j in data['jobs']}
existing_companies = {j['company'] for j in data['jobs']}

# Verify no duplicates
for j in NEW_JOBS:
    assert j['slug'] not in existing_slugs, f"DUPLICATE SLUG: {j['slug']}"
    print(f"  ✓ {j['title']} @ {j['company']} ({j['slug']})")

# Insert new jobs at index 0 (beginning of array)
data['jobs'] = NEW_JOBS + data['jobs']

# Write back
with open('/tmp/maulud-net/loker/lowongan.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
    f.write('\n')

print(f"\n✅ Added {len(NEW_JOBS)} new jobs at the beginning.")
print(f"Total jobs now: {len(data['jobs'])}")
