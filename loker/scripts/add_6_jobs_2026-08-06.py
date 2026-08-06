#!/usr/bin/env python3
"""Insert 6 new real job listings (found via web search) into lowongan.json."""
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE / 'loker' / 'lowongan.json'

POSTED = "2026-08-06"
EXPIRES = "2026-09-05"

with open(DB_PATH) as f:
    data = json.load(f)

NEW_JOBS = [
    {
        "slug": "general-manager-marketing-multitrend-indo-jakarta",
        "title": "General Manager Marketing",
        "company": "MULTITREND Indo Tbk",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Marketing",
        "salary": "Rp 20-30 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "MULTITREND Indo Tbk, perusahaan perdagangan dan distribusi yang menaungi berbagai brand elektronik ternama di Indonesia, sedang membuka posisi General Manager Marketing. Kamu akan memimpin tim marketing untuk merancang, mengembangkan, dan menjalankan marketing plan tahunan yang menyeluruh serta memastikan eksekusi campaign berjalan selaras dengan target bisnis. Posisi ini cocok untuk pemimpin marketing berpengalaman yang memiliki visi strategis kuat, memahami dinamika pasar ritel, dan mampu menggerakkan tim lintas fungsi untuk mencapai pertumbuhan brand.",
        "requirements": [
            "Pengalaman minimal 8-10 tahun di bidang marketing, dengan minimal 3-4 tahun di posisi manajemen/leadership",
            "Pemahaman kuat tentang strategi marketing, brand management, dan channel distribution",
            "Pengalaman menyusun dan mengeksekusi marketing plan tahunan skala nasional",
            "Kemampuan analisis pasar, data, dan measurement ROI campaign",
            "Kepemimpinan yang kuat serta keterampilan komunikasi dan negosiasi yang baik",
            "Pengalaman di industri elektronik, FMCG, atau distributor menjadi nilai tambah"
        ],
        "responsibilities": [
            "Merancang dan mengembangkan marketing plan tahunan yang komprehensif",
            "Menyusun strategi brand awareness, sales, dan kegiatan promosi di berbagai kanal",
            "Memimpin tim marketing untuk mengeksekusi program sesuai target",
            "Menganalisis hasil campaign dan mengevaluasi efektivitas strategi",
            "Berkoordinasi lintas fungsi (sales, supply chain, finance) untuk mendukung pertumbuhan",
            "Mengelola anggaran marketing dan memastikan efisiensi spend"
        ],
        "benefits": [
            "Gaji kompetitif dengan tunjangan sesuai level manajerial",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Bonus tahunan berdasarkan performa",
            "Tunjangan hari raya (THR)",
            "Jenjang karir di perusahaan distribusi terkemuka",
            "Lingkungan kerja profesional dan dinamis"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://www.linkedin.com/jobs/view/4437725558/",
        "source": "LinkedIn",
        "source_url": "https://www.linkedin.com/jobs/view/4437725558/",
        "featured": True
    },
    {
        "slug": "marketing-manager-it-company-terralogiq",
        "title": "Marketing Manager IT Company",
        "company": "Terralogiq",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Marketing",
        "salary": "Rp 10-18 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "Terralogiq, perusahaan yang bergerak di bidang solusi teknolog dan digital marketing, sedang membuka lowongan Marketing Manager untuk pos di sektor industri IT. Kandidat ideal akan bertanggung jawab mengembangkan, mengelola, mengeksekusi, serta menganalisis strategi dan kampanye pemasaran perusahaan. Posisi ini cocok untuk marketer yang berpengalaman, memahami industri teknologi, dan mampu menggerakkan pertumbuhan brand melalui pendekatan data dan kreatif.",
        "requirements": [
            "Pengalaman minimal 4-5 tahun di bidang marketing, preferensi di industri teknologi/digital",
            "Kemampuan mengembangkan dan mengeksekusi rencana serta kampanye marketing",
            "Pemahaman digital marketing, content strategy, dan marketing analytics",
            "Kemampuan analisis data untuk mengambil keputusan",
            "Komunikasi yang baik serta kemampuan koordinasi lintas tim",
            "Pengalaman terleadership menjadi nilai tambah"
        ],
        "responsibilities": [
            "Mengembangkan dan mengeksekusi strategi serta kampanye marketing",
            "Mengelola dan menganalisis performa marketing campaign",
            "Berkoordinasi dengan tim internal untuk eksekusi aktivitas",
            "Menyusun rencana marketing jangka pendek dan panjang",
            "Memonitor anggaran marketing dan mengukur ROI",
            "Mendukung pertumbuhan brand dan customer"
        ],
        "benefits": [
            "Gaji kompetitif sesuai standar industri IT",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Kesempatan kerja di perusahaan teknologi",
            "Pengembangan karir di bidang marketing digital",
            "Lingkungan kerja kolaboratif dan mendukung pertumbuhan"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/marketing-manager-it-company-at-terralogiq-4370637478",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/marketing-manager-it-company-at-terralogiq-4370637478",
        "featured": False
    },
    {
        "slug": "software-engineer-tech-mahindra-indonesia",
        "title": "Software Engineer",
        "company": "Tech Mahindra",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 15-25 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "Tech Mahindra, perusahaan multinasional bidang IT dan konsultasi digital terkemuka asal India yang beroperasi secara global, sedang membuka lowongan Software Engineer untuk penempatan di Indonesia. Posisi ini menuntut pengalaman di bidang pengembangan perangkat lunak dengan keahlian pada teknologi otomasi dan pipeline seperti Jenkins, dan total pengalaman yang disarankan sekitar 3-12 tahun. Cocok untuk software engineer dengan latar belakang engineering yang solid, memahami siklus pengembangan, dan bisa terjun langsung pada project klien di lingkungan global.",
        "requirements": [
            "Pengalaman sebagai Software Engineer sesuai kesempatan yang dipersyaratkan (sekitar 3-12 tahun)",
            "Keahlian pada teknologi CI/CD dan otomasi seperti Jenkins",
            "Pemahaman kuat terstruktur tentang siklus pengembangan software",
            "Kemampuan problem-solving dan bekerja dalam tim",
            "Komunikasi bahasa Inggris yang baik (lisan dan tulisan)",
            "Pengalaman di project enterprise/multinasional menjadi nilai plus"
        ],
        "responsibilities": [
            "Mengembangkan dan memelihara perangkat lunak sesuai kebutuhan bisnis",
            "Mengimplementasikan dan mengelola pipeline CI/CD (Jenkins)",
            "Melakukan testing, debugging, dan menjaga kualitas kode",
            "Berkolaborasi dengan tim engineering lintas fungsi",
            "Mendokumentasikan work serta proses teknis",
            "Mendukung deployment dan maintenance sistem"
        ],
        "benefits": [
            "Gaji kompetitif sesuai pengalaman dan skala",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Pengalaman bekerja di perusahaan teknologi global",
            "Kesempatan pengembangan skill dan sertifikasi",
            "Lingkungan kerja berstandar internasional"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/software-engineer-at-tech-mahindra-3886482409",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/software-engineer-at-tech-mahindra-3886482409",
        "featured": False
    },
    {
        "slug": "social-media-strategist-detikcom-jakarta",
        "title": "Social Media Strategist",
        "company": "detikcom",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Konten & Kreatif",
        "salary": "Rp 8-15 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "detikcom, salah satu portal berita digital terbesar dan terpopuler di Indonesia, sedang membuka lowongan Social Media Strategist. Posisi ini akan memimpin perencanaan dan eksekusi strategi media sosial perusahaan, mengelola kehadiran brand di berbagai platform, dan memaksimalkan distribusi konten untuk menjangkau audiens yang luas. Cocok untuk strategist media sosial yang kreatif, mengasah pemahaman tren platform, serta mampu menyusun strategi yang mendukung pertumbuhan audiens dan engagement.",
        "requirements": [
            "Pengalaman sebagai social media specialist/strategist/media social",
            "Pemahaman mendalam tentang ekosistem berbagai platform social media",
            "Kemampuan menyusun strategi konten dan kalender editorial",
            "Data-literate dengan kemampuan analisis engagement/performance",
            "Kreativitas tinggi dan mengenal tren viral media digital",
            "Komunikasi yang baik dalam bahasa Indonesia dan Inggris"
        ],
        "responsibilities": [
            "Memimpin perencanaan dan eksekusi strategi media sosial",
            "Mengelola kalender konten dan distribusi di berbagai platform",
            "Menganalisis performa media sosial dan mengevaluasi strategi",
            "Berkolaborasi dengan editor dan tim content untuk penjangkauan",
            "Mengidentifikasi tren untuk meningkatkan engagement",
            "Menyusun laporan dan mempresentasikan hasil kepada stakeholder"
        ],
        "benefits": [
            "Gaji kompetitif sesuai pengalaman",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Pengalaman bekerja di portal media nasional terkemuka",
            "Lingkungan kerja yang kreatif dan dinamis",
            "Kesempatan membangun strategi media untuk audiens besar masyarakat Indonesia"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/social-media-strategist-at-detikcom-4307341646",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/social-media-strategist-at-detikcom-4307341646",
        "featured": False
    },
    {
        "slug": "laravel-developer-remote-hidden-gems-talent",
        "title": "Laravel Developer (Remote)",
        "company": "Hidden Gems Talent",
        "location": "Remote, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 9-16 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "Hidden Gems Talent sedang membuka lowongan Laravel Developer untuk posisi kerja remote yang bisa dikerjakan dari Indonesia. Posisi ini membutuhkan kandidat yang yakin berkomunikasi profesional dalam bahasa Inggris secara tertulis mau lisan karena tim bekerja lintas negara dengan gaya kerja remote. Kamu akan bertanggung jawab mengembangkan aplikasi web berbasis Laravel, memastikan kualitas kode, dan berkolaborasi dengan tim dari daerah zona waktu berbeda.",
        "requirements": [
            "Kemampuan komunikasi profesional dalam bahasa Inggris (tertulis dan lisan) menjadi syarat penting",
            "Pengalaman mengembangkan aplikasi web menggunakan Laravel/PHP",
            "Pemahaman basis sebagai MySQL/PostgreSQL dan konsep REST API",
            "Familiar dengan Git dan workflow pengembangan tim",
            "Disiplin dan mampu bekerja mandiri dalam lingkungan remote",
            "Pengalaman remote dan bekerja lintas zona waktu menjadi nilai tambah"
        ],
        "responsibilities": [
            "Mengembangkan dan memelihara aplikasi berbasis Laravel/PHP",
            "Membangun dan mengintegrasikan API serta fitur baru",
            "Memastikan kualitas dan keamanan kode melalui best practice",
            "Berkolaborasi dengan tim remote lintas waktu",
            "Melakukan debugging dan optimalisasi performa",
            "Menjaga dokumentasi teknis"
        ],
        "benefits": [
            "Fleksibilitas remote dan bisa bekerja dari mana saja",
            "Gaji kompetitif sesuai pengalaman",
            "Kolaborasi dengan perusahaan internasional/global",
            "Pengembangan skill di teknologi Laravel",
            "Lingkungan kerja 100% remote"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://www.linkedin.com/jobs/view/4444531696/",
        "source": "LinkedIn",
        "source_url": "https://www.linkedin.com/jobs/view/4444531696/",
        "featured": False
    },
    {
        "slug": "social-media-admin-pt-digital-indonesia-bersatu",
        "title": "Social Media Admin",
        "company": "PT Digital Indonesia Bersatu",
        "location": "DKI Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Marketing",
        "salary": "Rp 4-7 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "PT Digital Indonesia Bersatu membuka lowongan Social Media Admin untuk bergabung dalam tim pengelolaan digital di area DKI Jakarta. Posisi ini terbuka bagi kandidat lulusan SMA/SMK/S1 yang memahami tren media sosial dan mampu mengelola konten serta interaksi di berbagai platform. Cocok untuk kamu yang kreatif, aktif berselancar di media sosial, dan ingin meniti karir di bidang pengelolaan digital",
        "requirements": [
            "Lulusan SMA/SMK/S1 sederajat",
            "Paham dan aktif mengikuti tren social media terbaru",
            "Menguasai pengelolaan akun dan konten di berbagai platform",
            "Kemampuan menulis dan menyiarkan konten yang menarik",
            "Detail, kreatif dan komunikatif",
            "Bersedia bekerja dan berkembang di area DKI Jakarta"
        ],
        "responsibilities": [
            "Mengelola dan mengupdate konten akun media sosial perusahaan",
            "Membuat konten yang relevan mengikuti tren",
            "Menanggapi audiens dan mempertahankan engagement",
            "Memonitor performa posting dan menyusun laporan",
            "Berkolaborasi dengan tim kreatif/digital",
            "Memonitor dan mengoptimasi strategi konten"
        ],
        "benefits": [
            "Gaji pokok beserta tunjangan",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Lingkungan kerja yang muda dan kreatif",
            "Kesempatan berkembang di bidang digital marketing",
            "Pengalaman mengelola media sosial profesional"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/social-media-admin-at-pt-digital-indonesia-bersatu-4441232060",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/social-media-admin-at-pt-digital-indonesia-bersatu-4441232060",
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