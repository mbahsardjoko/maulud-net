#!/usr/bin/env python3
"""Insert 6 new real job listings (2026-08-04) into loker/lowongan.json."""
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent
JSON_PATH = BASE / 'loker' / 'lowongan.json'

with open(JSON_PATH) as f:
    data = json.load(f)

POSTED = '2026-08-04'
EXPIRES = '2026-09-03'

new_jobs = [
    {
        "slug": "android-engineer-ajaib-jakarta",
        "title": "Android Engineer",
        "company": "Ajaib",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 15-25 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "Ajaib, perusahaan teknologi finansial (fintech) yang berkembang pesat di Indonesia, membuka lowongan Android Engineer untuk bergabung dengan tim mobile engineering. Anda akan terlibat dalam pengembangan aplikasi investasi yang digunakan oleh jutaan pengguna, membangun fitur baru, serta memastikan performa dan stabilitas aplikasi Android tetap prima. Posisi ini cocok untuk engineer yang punya semangat tinggi dalam membangun produk finansial yang aman, cepat, dan mudah digunakan.",
        "requirements": [
            "Minimal 2-4 tahun pengalaman sebagai Android Engineer",
            "Menguasai Kotlin dan/atau Java untuk pengembangan Android",
            "Pemahaman baik tentang Android SDK, Jetpack, dan arsitektur MVVM/Clean Architecture",
            "Pengalaman dengan REST API, offline storage, dan dependency injection",
            "Familiar dengan testing (unit test, UI test) dan CI/CD mobile",
            "Pemahaman dasar tentang keamanan aplikasi mobile adalah nilai plus",
            "Kemampuan problem solving dan kerja sama tim yang baik",
            "Bersedia bekerja onsite/hybrid di Jakarta"
        ],
        "responsibilities": [
            "Mengembangkan dan memelihara aplikasi Android Ajaib",
            "Membangun fitur baru sesuai kebutuhan produk dan bisnis",
            "Berkolaborasi dengan product manager, desainer, dan backend engineer",
            "Melakukan code review dan menjaga kualitas kode",
            "Mengoptimalkan performa aplikasi dan mengurangi crash rate",
            "Menulis unit test dan automation test",
            "Menganalisis dan memperbaiki isu yang ditemukan di produksi",
            "Mengikuti perkembangan teknologi Android terbaru dan menerapkannya"
        ],
        "benefits": [
            "Gaji kompetitif (Rp 15-25 Juta) sesuai pengalaman",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Asuransi kesehatan tambahan",
            "Bonus tahunan berbasis performa",
            "Lingkungan kerja startup yang dinamis dan suportif",
            "Kesempatan berkembang bersama salah satu fintech terbesar di Indonesia"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/android-engineer-at-ajaib-4279580817",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/android-engineer-at-ajaib-4279580817",
        "featured": False
    },
    {
        "slug": "software-engineer-fullstack-samsung-jakarta",
        "title": "Software Engineer - Fullstack",
        "company": "Samsung Southeast Asia & Oceania",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 20-35 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "Samsung Southeast Asia & Oceania membuka kesempatan bagi Software Engineer (Fullstack) untuk bergabung dengan tim teknologi di Jakarta. Anda akan terlibat dalam pengembangan solusi digital yang mendukung berbagai lini bisnis Samsung di kawasan Asia Tenggara dan Oseania. Peran ini menuntut kemampuan di sisi frontend maupun backend, dengan standar engineering tinggi serta kolaborasi lintas tim dan negara.",
        "requirements": [
            "Minimal 3-5 tahun pengalaman sebagai Fullstack Engineer",
            "Menguasai bahasa pemrograman frontend (React/Vue/Angular) dan backend (Node.js/Python/Java)",
            "Pengalaman membangun REST API dan integrasi sistem",
            "Pemahaman database SQL dan NoSQL",
            "Familiar dengan cloud platform (AWS/Azure/GCP) dan containerization",
            "Pengalaman CI/CD dan testing otomatis",
            "Kemampuan bahasa Inggris yang baik untuk kolaborasi regional",
            "Pengalaman di lingkungan enterprise/corporate adalah nilai plus"
        ],
        "responsibilities": [
            "Mengembangkan fitur fullstack pada aplikasi dan platform digital Samsung",
            "Merancang arsitektur solusi yang scalable dan maintainable",
            "Berkolaborasi dengan tim produk dan engineering di berbagai negara",
            "Melakukan code review dan menegakkan engineering best practices",
            "Mengoptimalkan performa aplikasi dan database",
            "Menulis unit test, integration test, dan dokumentasi teknis",
            "Berpartisipasi dalam perencanaan teknis dan estimasi proyek"
        ],
        "benefits": [
            "Gaji sangat kompetitif (Rp 20-35 Juta)",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Asuransi kesehatan untuk karyawan dan keluarga",
            "Bonus tahunan berbasis performa",
            "Pengalaman bekerja dengan brand teknologi global",
            "Lingkungan kerja profesional dengan jenjang karir jelas",
            "Kesempatan kolaborasi dengan tim internasional"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://www.linkedin.com/jobs/view/4432176346/",
        "source": "LinkedIn",
        "source_url": "https://www.linkedin.com/jobs/view/4432176346/",
        "featured": False
    },
    {
        "slug": "developer-ai-native-web-inquivix-remote-indonesia",
        "title": "Developer - AI-Native Web Development (Indonesia, Remote)",
        "company": "Inquivix",
        "location": "Remote, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 12-20 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "Inquivix, digital marketing agency yang berbasis di Seoul dan membantu perusahaan internasional masuk serta berkembang di pasar Korea, membuka lowongan Developer untuk pengembangan web AI-native. Posisi ini bekerja remote dari Indonesia dengan jam kerja yang menyesuaikan business hours KST. Anda akan membangun dan memelihara website klien, landing page, serta aset digital lainnya dengan memanfaatkan teknologi AI untuk meningkatkan efisiensi pengembangan.",
        "requirements": [
            "Minimal 2-4 tahun pengalaman pengembangan web (frontend/backend)",
            "Menguasai HTML, CSS, JavaScript, dan framework modern (React/Next.js)",
            "Pengalaman dengan API integration dan CMS",
            "Familiar dengan AI tools untuk workflow pengembangan (coding assistant, automation)",
            "Kemampuan bekerja remote dengan overlap jam kerja KST",
            "Kemampuan bahasa Inggris yang baik (lisan dan tulisan)",
            "Teliti, mandiri, dan punya manajemen waktu yang baik",
            "Portofolio website/landing page yang relevan"
        ],
        "responsibilities": [
            "Mengembangkan dan memelihara website serta landing page klien",
            "Menerapkan pendekatan AI-native dalam proses pengembangan",
            "Berkolaborasi dengan tim marketing dan desain di Seoul",
            "Mengoptimalkan performa website, SEO, dan user experience",
            "Melakukan debugging dan perbaikan isu secara berkala",
            "Mendokumentasikan proses pengembangan dan keputusan teknis",
            "Menjaga komunikasi rutin dengan tim lintas zona waktu"
        ],
        "benefits": [
            "Gaji kompetitif (Rp 12-20 Juta)",
            "Bekerja 100% remote dari Indonesia",
            "Pengalaman bekerja dengan tim internasional (Korea)",
            "Exposure ke teknologi AI untuk pengembangan web",
            "Fleksibilitas jam kerja dengan overlap KST",
            "Kesempatan menangani klien global"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/developer-—-ai-native-web-development-indonesia-remote-at-inquivix-4435035872",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/developer-—-ai-native-web-development-indonesia-remote-at-inquivix-4435035872",
        "featured": False
    },
    {
        "slug": "engineering-manager-pt-bank-neo-commerce-jakarta",
        "title": "Engineering Manager",
        "company": "PT Bank Neo Commerce Tbk",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 40-60 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "PT Bank Neo Commerce Tbk, bank digital yang terus berkembang di Indonesia, mencari Engineering Manager untuk memimpin pengembangan sistem dan aplikasi perbankan. Anda akan bertanggung jawab mengarahkan desain, pengembangan, dan peningkatan sistem perbankan agar selaras dengan tujuan bisnis dan operasional, serta membina tim engineer agar mampu menghadirkan solusi digital yang scalable, aman, dan berkualitas tinggi.",
        "requirements": [
            "Minimal 7-10 tahun pengalaman di bidang software engineering, dengan 3+ tahun sebagai people manager",
            "Pengalaman memimpin tim engineer dalam proyek berskala besar",
            "Pemahaman mendalam tentang software development lifecycle (system design, coding, testing, deployment)",
            "Pengalaman di industri perbankan/fintech adalah nilai plus",
            "Kemampuan arsitektur sistem, microservices, dan cloud",
            "Kemampuan komunikasi dan stakeholder management yang baik",
            "Kemampuan bahasa Inggris untuk komunikasi profesional",
            "Bersedia bekerja onsite/hybrid di Jakarta"
        ],
        "responsibilities": [
            "Memimpin desain, pengembangan, dan peningkatan sistem perbankan digital",
            "Mengelola dan membina tim engineering agar menghasilkan solusi berkualitas tinggi",
            "Mengawasi end-to-end software development lifecycle",
            "Berkolaborasi erat dengan product, business, dan operations teams",
            "Memastikan standar keamanan, skalabilitas, dan performa sistem",
            "Melakukan perencanaan kapasitas tim, rekrutmen, dan mentoring",
            "Menyusun roadmap teknis dan prioritas pengembangan",
            "Menjadi penghubung antara kebutuhan bisnis dan eksekusi teknis"
        ],
        "benefits": [
            "Gaji sangat kompetitif (Rp 40-60 Juta)",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Asuransi kesehatan premium",
            "Bonus tahunan berbasis performa",
            "Kesempatan memimpin tim di bank digital terdepan",
            "Lingkungan kerja modern dan dinamis",
            "Jenjang karir dan pengembangan kepemimpinan"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/engineering-manager-at-pt-bank-neo-commerce-tbk-4435411960",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/engineering-manager-at-pt-bank-neo-commerce-tbk-4435411960",
        "featured": True
    },
    {
        "slug": "tax-associate-pt-suzuki-indomobil-motor-jakarta",
        "title": "Tax Associate",
        "company": "PT Suzuki Indomobil Motor",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Finance",
        "salary": "Rp 8-12 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "PT Suzuki Indomobil Motor, perusahaan otomotif terkemuka di Indonesia, membuka lowongan Tax Associate untuk bergabung dengan tim finance & tax. Anda akan terlibat dalam pengelolaan kewajiban perpajakan perusahaan, termasuk compliance, pelaporan, dan perencanaan pajak. Posisi ini cocok untuk lulusan Akuntansi atau Perpajakan yang ingin membangun karir di bidang perpajakan korporasi dengan standar profesional tinggi.",
        "requirements": [
            "Sarjana (S1) Akuntansi atau Perpajakan dengan IPK minimal 3.00 dari universitas terkemuka",
            "Pengalaman 1-3 tahun di bidang perpajakan (fresh graduate dengan magang relevan juga dipertimbangkan)",
            "Memiliki pengetahuan tentang Transfer Pricing (TP)",
            "Memahami peraturan perpajakan Indonesia (PPh, PPN, dan ketentuan terkait)",
            "Familiar dengan e-SPT/e-Faktur dan aplikasi perpajakan",
            "Teliti, analitis, dan mampu bekerja dalam tenggat waktu",
            "Kemampuan komunikasi yang baik dan siap bekerja sama dengan tim",
            "Bersedia bekerja di Jakarta"
        ],
        "responsibilities": [
            "Menyiapkan dan menyampaikan pelaporan pajak bulanan dan tahunan",
            "Mengelola dokumen dan administrasi perpajakan perusahaan",
            "Membantu proses compliance dan pemeriksaan pajak",
            "Melakukan analisis perpajakan terkait transaksi dan proyek bisnis",
            "Berkolaborasi dengan tim finance, accounting, dan konsultan pajak",
            "Mengikuti perkembangan regulasi perpajakan terbaru",
            "Mendukung perencanaan pajak (tax planning) perusahaan"
        ],
        "benefits": [
            "Gaji kompetitif (Rp 8-12 Juta)",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Asuransi kesehatan tambahan",
            "THR dan bonus tahunan",
            "Pengalaman bekerja di perusahaan otomotif ternama",
            "Kesempatan pengembangan karir di bidang perpajakan",
            "Lingkungan kerja profesional dan suportif"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/tax-associate-at-pt-suzuki-indomobil-motor-4191534371",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/tax-associate-at-pt-suzuki-indomobil-motor-4191534371",
        "featured": False
    },
    {
        "slug": "ui-ux-designer-contract-pt-maybank-sekuritas-indonesia",
        "title": "UI/UX Designer (Contract)",
        "company": "PT Maybank Sekuritas Indonesia",
        "location": "Jakarta, Indonesia",
        "type": "Contract",
        "category": "Desain",
        "salary": "Rp 10-18 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "PT Maybank Sekuritas Indonesia, anak perusahaan Maybank Group yang bergerak di bidang sekuritas, membuka lowongan UI/UX Designer (Contract) untuk memperkuat tim produk digital. Anda akan merancang pengalaman pengguna untuk platform investasi dan layanan sekuritas yang modern, intuitif, dan sesuai kebutuhan nasabah. Posisi ini cocok untuk desainer dengan pengalaman 1-3 tahun yang ingin berkembang di industri keuangan.",
        "requirements": [
            "Pengalaman 1-3 tahun sebagai UI/UX Designer atau Product Designer",
            "Memahami tren, prinsip, dan best practices UI/UX",
            "Menguasai tools desain seperti Figma, Sketch, atau Adobe XD",
            "Kemampuan membuat wireframe, prototype, dan design system",
            "Pemahaman dasar usability testing dan riset pengguna",
            "Kemampuan komunikasi dan kolaborasi lintas tim yang baik",
            "Portofolio desain produk digital yang relevan",
            "Pengalaman di industri finansial/fintech adalah nilai plus"
        ],
        "responsibilities": [
            "Merancang user interface dan user experience untuk produk digital",
            "Membuat wireframe, mockup, dan interactive prototype",
            "Berkolaborasi dengan product manager dan software engineer",
            "Melakukan riset pengguna dan usability testing",
            "Menjaga konsistensi design system dan brand guidelines",
            "Menganalisis feedback pengguna dan melakukan iterasi desain",
            "Mendokumentasikan keputusan desain dan handoff ke tim engineering"
        ],
        "benefits": [
            "Gaji kompetitif (Rp 10-18 Juta)",
            "Pengalaman bekerja di perusahaan sekuritas ternama (Maybank Group)",
            "Kesempatan mengerjakan produk finansial berdampak besar",
            "Lingkungan kerja profesional",
            "Kolaborasi dengan tim produk dan teknologi yang solid",
            "Fleksibilitas kerja (hybrid)"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/ui-ux-designer-contract-at-pt-maybank-sekuritas-indonesia-4390798191",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/ui-ux-designer-contract-at-pt-maybank-sekuritas-indonesia-4390798191",
        "featured": False
    }
]

# Dedup check: reject if slug already exists
existing_slugs = {j['slug'] for j in data['jobs']}
for nj in new_jobs:
    if nj['slug'] in existing_slugs:
        raise SystemExit(f"DUPLICATE slug: {nj['slug']}")
    existing_slugs.add(nj['slug'])

# Insert at index 0
data['jobs'] = new_jobs + data['jobs']

# Recompute categories (never null — frontend bug prevention)
cats = sorted({j['category'] for j in data['jobs'] if j.get('category')})
data['categories'] = cats

with open(JSON_PATH, 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"OK: inserted {len(new_jobs)} jobs. Total now: {len(data['jobs'])}")
print("Categories:", cats)
