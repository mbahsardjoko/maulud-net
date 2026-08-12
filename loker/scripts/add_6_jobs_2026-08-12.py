#!/usr/bin/env python3
"""Insert 6 new real job listings (found via web search) into lowongan.json."""
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE / 'loker' / 'lowongan.json'

POSTED = "2026-08-12"
EXPIRES = "2026-09-11"

with open(DB_PATH) as f:
    data = json.load(f)

NEW_JOBS = [
    {
        "slug": "content-writer-editor-unicef",
        "title": "International English Content Writer and Editor",
        "company": "UNICEF Indonesia",
        "location": "Jakarta, Indonesia / Remote",
        "type": "Contract",
        "category": "Konten & Kreatif",
        "salary": "Rp 15-25 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "UNICEF Indonesia mencari seorang konsultan individual untuk posisi International English Content Writer and Editor. Kamu akan bertugas menulis, mengedit, dan mengelola kualitas konten komunikasi serta advokasi publik UNICEF selama 12 bulan ke depan. Posisi ini membutuhkan kemampuan menulis bahasa Inggris yang sangat baik, keahlian editorial tingkat profesional, dan pemahaman tentang standar penulisan organisasi internasional. Pekerjaan dilakukan secara hybrid dari Jakarta dengan fleksibilitas remote yang tinggi.",
        "requirements": [
            "Minimal 3 tahun pengalaman profesional di bidang penulisan, editing, atau pengembangan konten dalam bahasa Inggris",
            "Sarjana Komunikasi, Jurnalistik, atau bidang terkait",
            "Penguasaan bahasa Inggris tingkat native atau near-native, baik lisan maupun tulisan",
            "Kemampuan editorial yang kuat: tata bahasa, struktur kalimat, dan konsistensi gaya bahasa",
            "Pemahaman tentang standar penulisan dan panduan brand UNICEF (diutamakan)",
            "Kemampuan riset dan analisis yang baik untuk menghasilkan konten akurat dan berbasis fakta",
            "Mampu bekerja secara mandiri, mengelola beberapa proyek sekaligus, dan memenuhi tenggat waktu",
            "Tersedia untuk kontrak 12 bulan dan bersedia bekerja dari Jakarta atau remote"
        ],
        "responsibilities": [
            "Menulis dan mengedit materi komunikasi, advokasi, dan hubungan masyarakat UNICEF dalam bahasa Inggris",
            "Memastikan setiap konten akurat, memukau, berpusat pada audiens, dan selaras dengan panduan penulisan UNICEF",
            "Melakukan quality assurance terhadap seluruh produk komunikasi di bagian Communications and Advocacy Section",
            "Berkolaborasi dengan tim program untuk mengumpulkan informasi akurat dari lapangan",
            "Mengelola beberapa proyek konten secara paralel dengan tenggat waktu yang ketat",
            "Mendukung pengembangan panduan penulisan dan standar konten UNICEF Indonesia"
        ],
        "benefits": [
            "Fee konsultan kompetitif untuk durasi 12 bulan",
            "Fleksibilitas kerja hybrid dan remote",
            "Pengalaman bekerja dengan organisasi internasional (PBB/UNICEF)",
            "Eksposur terhadap isu-isu pembangunan dan kemanusiaan di Indonesia",
            "Pengembangan profesional dan networking global",
            "Dampak nyata pada kehidupan jutaan anak di Indonesia"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/international-english-content-writer-and-editor-jakarta-indonesia-communication-and-advocacy-section-1-year-remote-at-unicef-4446046980",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/international-english-content-writer-and-editor-jakarta-indonesia-communication-and-advocacy-section-1-year-remote-at-unicef-4446046980",
        "featured": True
    },
    {
        "slug": "content-creator-specialist-kitabisa",
        "title": "Content Creator Specialist",
        "company": "Kitabisa",
        "location": "DKI Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Konten & Kreatif",
        "salary": "Rp 6-10 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "Kitabisa, platform donasi dan galang dana terbesar di Indonesia, membuka posisi Content Creator Specialist untuk tim kontennya. Kamu akan memegang peran penting dalam membuat konten kreatif dan menarik untuk berbagai platform media sosial seperti Instagram, TikTok, dan Facebook. Posisi ini membutuhkan kreativitas tinggi, kemampuan syuting dan editing konten, serta pemahaman tren media sosial yang selalu berkembang. Ini adalah kesempatan untuk berkontribusi pada misi sosial Kitabisa sambil mengasah skill konten kreatifmu.",
        "requirements": [
            "Minimal 2 tahun pengalaman sebagai Content Creator, Social Media Specialist, atau posisi serupa",
            "Kemampuan membuat konten kreatif untuk Instagram, TikTok, dan Facebook",
            "Terampil dalam pengambilan gambar (shooting), coverage on-site, dan dokumentasi kegiatan",
            "Paham tren media sosial, khususnya TikTok dan platform short-form video",
            "Menguasai tools editing video (Premiere Pro, CapCut, atau sejenisnya)",
            "Portfolio konten kreatif untuk media sosial (wajib dilampirkan)",
            "Komunikasi yang baik, kreatif, dan mampu bekerja dalam tim yang dinamis"
        ],
        "responsibilities": [
            "Membuat konten kreatif dan menarik untuk berbagai platform media sosial (Instagram, TikTok, Facebook)",
            "Melakukan syuting, coverage on-site, dan dokumentasi kegiatan untuk keperluan konten",
            "Mengembangkan konsep konten yang selaras dengan brand Kitabisa dan kampanye donasi",
            "Mengedit video dan grafis sesuai standar visual Kitabisa",
            "Menganalisis performa konten dan mengoptimasi strategi berdasarkan data engagement",
            "Berkolaborasi dengan tim marketing dan program untuk mendukung kampanye donasi"
        ],
        "benefits": [
            "Gaji kompetitif untuk posisi kreator konten",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Bekerja di platform sosial impact terbesar di Indonesia",
            "Lingkungan kerja yang inspiratif dan misi sosial",
            "Kesempatan mengembangkan skill konten kreatif dan media sosial",
            "Tim yang kolaboratif dan budaya kerja yang fleksibel"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/content-creator-specialist-at-kitabisa-4379080161",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/content-creator-specialist-at-kitabisa-4379080161",
        "featured": False
    },
    {
        "slug": "fullstack-developer-pt-iuris-international",
        "title": "Full Stack Developer",
        "company": "PT IURIS International Indonesia",
        "location": "Jakarta Selatan, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 8-15 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "PT IURIS International Indonesia, perusahaan yang bergerak di bidang solusi teknologi informasi, membuka posisi Full Stack Developer untuk ditempatkan di Jakarta Selatan. Kamu akan bertanggung jawab untuk mengembangkan komponen frontend dan backend aplikasi web, mulai dari merancang arsitektur hingga memastikan solusi yang dibangun sesuai kebutuhan bisnis klien. Peran ini membutuhkan kemampuan teknis yang menyeluruh dan kemampuan berkolaborasi dengan tim lintas fungsi.",
        "requirements": [
            "Minimal 3 tahun pengalaman sebagai Full Stack Developer atau peran pengembangan web terkait",
            "Mahir dalam JavaScript/TypeScript, React.js atau Vue.js untuk frontend",
            "Pengalaman dengan backend menggunakan Node.js, Python (Django/Flask), atau PHP (Laravel)",
            "Paham database relasional (PostgreSQL, MySQL) dan database NoSQL (MongoDB)",
            "Pengalaman dengan RESTful API design dan integrasi API pihak ketiga",
            "Familiar dengan version control (Git), CI/CD, dan deployment ke cloud",
            "Kemampuan bekerja dalam tim lintas fungsi dan komunikasi technical dengan stakeholder",
            "Bersedia bekerja on-site di Jakarta Selatan"
        ],
        "responsibilities": [
            "Mengembangkan komponen frontend dan backend aplikasi web sesuai kebutuhan klien",
            "Merancang arsitektur sistem yang scalable, maintainable, dan aman",
            "Berkolaborasi dengan tim untuk mengumpulkan kebutuhan, merancang solusi, dan mengimplementasikannya",
            "Menulis kode yang bersih, teruji, dan terdokumentasi dengan baik",
            "Melakukan debugging, testing, dan optimasi performa aplikasi",
            "Mendukung deployment dan pemeliharaan sistem di lingkungan production"
        ],
        "benefits": [
            "Gaji kompetitif Rp 8-15 Juta sesuai pengalaman dan skill",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Pengalaman kerja di perusahaan solusi TI internasional",
            "Pengembangan skill lintas teknologi (frontend, backend, DevOps)",
            "Lingkungan kerja yang profesional dan kolaboratif",
            "Kesempatan mengembangkan karier di bidang software development"
        ],
        "how_to_apply": "Kirim lamaran melalui Loker.id. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://www.loker.id/information-technology/programmer/full-stack-developer-pt-iuris-international-indonesia-jakarta-selatan.html",
        "source": "Loker.id",
        "source_url": "https://www.loker.id/information-technology/programmer/full-stack-developer-pt-iuris-international-indonesia-jakarta-selatan.html",
        "featured": False
    },
    {
        "slug": "data-analyst-pt-permodalan-nasional-madani",
        "title": "Data Analyst",
        "company": "PT Permodalan Nasional Madani (Persero)",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 7-12 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "PT Permodalan Nasional Madani (Persero), BUMN yang berfokus pada pembiayaan dan pemberdayaan UMKM di Indonesia, membuka posisi Data Analyst untuk mengelola dan menganalisis data bisnis. Kamu akan bertugas mengolah data dari berbagai sumber, menyusun laporan analitik, dan memberikan insight yang mendukung pengambilan keputusan strategis perusahaan. Posisi ini cocok untuk analis data yang ingin berkontribusi pada pemberdayaan ekonomi masyarakat melalui pendekatan berbasis data.",
        "requirements": [
            "Minimal 1 tahun pengalaman sebagai Data Analyst, Data Scientist, atau di bidang Business Intelligence",
            "Penguasaan Microsoft Excel dan/atau software pengelolaan data lainnya",
            "Paham SQL dan mampu bekerja dengan database relasional",
            "Familiar dengan tools visualisasi data (Tableau, Power BI, atau Google Data Studio)",
            "Kemampuan analisis kuantitatif dan kualitatif yang baik",
            "Detail-oriented dengan kemampuan menyajikan data secara jelas dan akurat",
            "Pendidikan minimal S1 di bidang Statistika, Matematika, Informatika, atau terkait",
            "Bersedia bekerja di kantor pusat Jakarta"
        ],
        "responsibilities": [
            "Mengumpulkan, membersihkan, dan mengolah data dari berbagai sistem internal dan eksternal",
            "Melakukan analisis data untuk mendukung keputusan bisnis dan strategi pembiayaan UMKM",
            "Menyusun laporan berkala dan dashboard analitik untuk manajemen",
            "Mengidentifikasi tren, pola, dan anomali dalam data yang relevan dengan operasional bisnis",
            "Mendukung tim business intelligence dalam pengembangan model dan framework analitik",
            "Berkolaborasi dengan berbagai departemen untuk memahami kebutuhan data dan solusi yang tepat"
        ],
        "benefits": [
            "Gaji kompetitif dengan tunjangan",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "THR dan bonus tahunan",
            "Bekerja di BUMN dengan misi sosial pemberdayaan UMKM",
            "Pengembangan profesional dan pelatihan berkelanjutan",
            "Lingkungan kerja yang stabil dan berorientasi pada dampak sosial"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/data-analyst-at-pt-permodalan-nasional-madani-persero-4327812646",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/data-analyst-at-pt-permodalan-nasional-madani-persero-4327812646",
        "featured": False
    },
    {
        "slug": "customer-service-representative-makmur",
        "title": "Customer Service Representative",
        "company": "Makmur.id",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Customer Service",
        "salary": "Rp 5-8 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "Makmur.id, platform keuangan digital yang menyediakan layanan investasi reksa dana dan saham, membuka posisi Customer Service Representative untuk melayani dan mendukung nasabah mereka di Jakarta. Kamu akan bertugas membantu pelanggan dengan pertanyaan terkait fitur produk, proses KYC, transaksi, dan produk-produk keuangan seperti reksa dana dan saham. Posisi ini membutuhkan kemampuan komunikasi yang baik, pemahaman dasar produk keuangan, dan kesabaran dalam melayani nasabah dari berbagai latar belakang.",
        "requirements": [
            "Minimal 1 tahun pengalaman di bidang customer service, terutama di industri fintech atau keuangan",
            "Pemahaman dasar produk keuangan: reksa dana, saham, dan proses transaksi investasi",
            "Kemampuan komunikasi yang sangat baik, sopan, dan responsif",
            "Familiar dengan sistem CRM dan tools ticketing support",
            "Mampu menjelaskan fitur produk dan proses KYC secara jelas kepada nasabah",
            "Ketelitian dan kemampuan menyelesaikan masalah dengan cepat dan akurat",
            "Bersedia bekerja di Jakarta dengan jadwal shift yang mungkin diperlukan"
        ],
        "responsibilities": [
            "Menangani pertanyaan dan keluhan nasabah via telepon, email, dan chat secara profesional",
            "Membantu nasabah dalam proses registrasi, verifikasi KYC, dan transaksi investasi",
            "Menjelaskan fitur produk, reksa dana, saham, dan instrumen keuangan lainnya kepada nasabah",
            "Mendokumentasikan seluruh interaksi pelanggan dalam sistem CRM secara akurat",
            "Meningkatkan pengalaman nasabah melalui layanan yang cepat, ramah, dan solutif",
            "Mengidentifikasi dan melaporkan masalah sistem atau produk ke tim terkait"
        ],
        "benefits": [
            "Gaji kompetitif Rp 5-8 Juta plus insentif berdasarkan performa",
            "BPJS Kesehatan dan Ketenagakerjaan",
            " THR dan tunjangan lainnya",
            "Pengalaman kerja di industri fintech yang berkembang pesat",
            "Pelatihan produk keuangan dan pengembangan karier",
            "Lingkungan kerja yang modern dan kolaboratif di Jakarta"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/customer-service-representative-at-makmur-4313729468",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/customer-service-representative-at-makmur-4313729468",
        "featured": False
    },
    {
        "slug": "frontend-developer-intern-dms-group",
        "title": "Front End Developer (Internship)",
        "company": "PT Digital Mediatek Solusindo (DMS Group)",
        "location": "DKI Jakarta, Indonesia",
        "type": "Internship",
        "category": "Teknologi",
        "salary": "Rp 2.5-4 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "PT Digital Mediatek Solusindo (DMS Group), perusahaan teknologi yang bergerak di bidang solusi digital, membuka kesempatan magang untuk posisi Front End Developer. Program magang ini dirancang untuk mahasiswa atau fresh graduate yang ingin mendalami pengembangan antarmuka web dengan bimbingan langsung dari tim engineering profesional. Kamu akan belajar membangun komponen UI, bekerja dengan tools modern, dan mendapatkan pengalaman nyata di lingkungan kerja teknologi Indonesia.",
        "requirements": [
            "Mahasiswa atau fresh graduate di bidang Informatika, Teknik Komputer, atau bidang terkait",
            "Pengalaman dasar dengan HTML, CSS, dan JavaScript",
            "Familiar dengan salah satu framework frontend (React.js, Vue.js, atau Angular) menjadi nilai tambah",
            "Antusias belajar dan mau menerima feedback dari tim senior",
            "Kemampuan berpikir logis dan problem solving dasar",
            "Komunikasi yang baik dan mampu bekerja secara tim"
        ],
        "responsibilities": [
            "Membantu pengembangan dan pemeliharaan antarmuka web menggunakan HTML, CSS, dan JavaScript",
            "Menerjemahkan desain UI/UX menjadi komponen yang responsif dan fungsional",
            "Belajar menggunakan tools pengembangan modern (Git, npm, webpack, dll)",
            "Membantu testing dan debugging fitur frontend",
            "Berkolaborasi dengan tim backend dan design untuk integrasi fitur",
            "Mendokumentasikan proses belajar dan kontribusi selama program magang"
        ],
        "benefits": [
            "Uang saku magang kompetitif Rp 2.5-4 Juta",
            "Sertifikat magang dari perusahaan teknologi",
            "Bimbingan langsung dari engineer senior",
            "Pengalaman kerja nyata di industri teknologi",
            "Peluang lanjut ke posisi full-time setelah program magang selesai",
            "Lingkungan belajar yang suportif dan kolaboratif"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/front-end-developer-at-pt-digital-mediatek-solusindo-dms-group-4440185832",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/front-end-developer-at-pt-digital-mediatek-solusindo-dms-group-4440185832",
        "featured": False
    }
]

# Insert new jobs at the beginning (index 0)
for job in reversed(NEW_JOBS):
    data['jobs'].insert(0, job)

# Update categories to include Customer Service if missing
if 'categories' in data:
    for cat in [j['category'] for j in NEW_JOBS]:
        if cat not in data['categories']:
            data['categories'].append(cat)
    data['categories'].sort()

# Write back
with open(DB_PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"OK: {len(NEW_JOBS)} lowongan ditambahkan ke lowongan.json")
for i, job in enumerate(NEW_JOBS, 1):
    print(f"  {i}. {job['title']} ({job['company']}) — {job['source_url']}")
