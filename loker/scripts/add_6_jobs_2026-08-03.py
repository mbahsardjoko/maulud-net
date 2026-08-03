#!/usr/bin/env python3
"""Insert 6 new real jobs (from web_search results) into lowongan.json at index 0."""
import json

DB = '/tmp/maulud-net/loker/lowongan.json'

with open(DB, 'r') as f:
    data = json.load(f)

new_jobs = [
    {
        "slug": "software-engineer-ocbc-indonesia",
        "title": "Software Engineer",
        "company": "OCBC Indonesia",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 10-18 Juta",
        "posted": "2026-08-03",
        "expires": "2026-09-02",
        "description": "OCBC Indonesia membuka kesempatan bagi Software Engineer untuk bergabung dalam pengembangan solusi perbankan digital yang modern, aman, dan andal. Anda akan terlibat dalam berbagai proyek menarik — mulai dari pengembangan fitur baru hingga optimalisasi sistem perbankan inti — serta berkolaborasi dengan tim lintas fungsi. Posisi ini cocok untuk engineer yang ingin berkembang di lingkungan perbankan yang dinamis dengan standar engineering dan keamanan tingkat tinggi.",
        "requirements": [
            "Minimal 2-4 tahun pengalaman sebagai Software Engineer",
            "Menguasai minimal satu bahasa pemrograman (Java, .NET/C#, atau Node.js)",
            "Pemahaman baik tentang REST API, database SQL, dan microservices",
            "Familiar dengan version control (Git) dan CI/CD practices",
            "Pemahaman dasar cloud platform (AWS/Azure/GCP) adalah nilai plus",
            "Pengalaman di industri perbankan/fintech adalah nilai plus",
            "Kemampuan problem solving dan komunikasi yang baik",
            "Bersedia bekerja onsite/hybrid di Jakarta"
        ],
        "responsibilities": [
            "Mengembangkan dan memelihara aplikasi perbankan digital",
            "Merancang dan mengimplementasikan API serta integrasi antar sistem",
            "Melakukan code review dan memastikan kualitas kode",
            "Berkolaborasi dengan product owner, QA, dan tim bisnis",
            "Menulis unit test dan automation test untuk fitur kritis",
            "Menganalisis dan memperbaiki isu produksi",
            "Mendokumentasikan arsitektur dan alur sistem",
            "Ikut serta dalam perencanaan teknis dan estimasi sprint"
        ],
        "benefits": [
            "Gaji kompetitif (Rp 10-18 Juta) sesuai pengalaman",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Asuransi kesehatan tambahan",
            "Bonus tahunan berbasis performa",
            "Program training dan sertifikasi",
            "Lingkungan kerja profesional dan jenjang karir jelas",
            "Fasilitas kantor modern di area CBD Jakarta"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/software-engineer-at-ocbc-indonesia-4330113976",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/software-engineer-at-ocbc-indonesia-4330113976",
        "featured": False
    },
    {
        "slug": "senior-software-engineer-backend-grab",
        "title": "Senior Software Engineer, Backend",
        "company": "Grab",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 25-45 Juta",
        "posted": "2026-08-03",
        "expires": "2026-09-02",
        "description": "Grab, superapp terkemuka di Asia Tenggara, mencari Senior Software Engineer (Backend) untuk bergabung dengan tim engineering di Indonesia. Dalam peran ini, Anda akan mendesain dan membangun backend services yang robust, scalable, observable, dan cost-efficient — terutama menggunakan Golang di atas platform berbasis Kubernetes. Anda akan berkolaborasi erat dengan tim-tim tersebar di Asia serta berkontribusi pada arsitektur sistem yang melayani jutaan pengguna setiap hari.",
        "requirements": [
            "Minimal 5-7 tahun pengalaman backend development",
            "Expert di Golang atau bahasa backend lain dengan kemauan belajar Go",
            "Pengalaman mendalam dengan Kubernetes dan container orchestration",
            "Solid di distributed systems, microservices, dan event-driven architecture",
            "Pengalaman dengan database besar (PostgreSQL, MySQL, Redis, atau Cassandra)",
            "Familiar dengan message queues (Kafka, NATS, atau RabbitMQ)",
            "Pengalaman observability: monitoring, logging, tracing",
            "Kemampuan mentoring dan technical leadership",
            "Kemampuan komunikasi lintas tim dan kolaborasi remote"
        ],
        "responsibilities": [
            "Mendesain dan mengimplementasikan backend services yang scalable dan cost-efficient",
            "Membangun fitur-fitur baru pada platform Grab dengan standar kualitas tinggi",
            "Mengoptimasi performa sistem, query database, dan penggunaan resource",
            "Berkolaborasi dengan product, data, dan platform teams di Asia",
            "Melakukan design review, code review, dan technical documentation",
            "Mentoring engineer junior dan menegakkan engineering best practices",
            "Menangani insiden produksi dan root cause analysis",
            "Berkontribusi pada roadmap teknis dan inisiatif platform"
        ],
        "benefits": [
            "Gaji sangat kompetitif (Rp 25-45 Juta) + bonus tahunan",
            "Equity/stock options Grab",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Asuransi kesehatan premium untuk keluarga",
            "Flexible hybrid work arrangement",
            "Learning budget dan akses conference",
            "MacBook Pro dan peralatan kerja modern",
            "Kesempatan berdampak langsung ke jutaan pengguna Asia Tenggara"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/senior-software-engineer-backend-at-grab-4419165405",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/senior-software-engineer-backend-at-grab-4419165405",
        "featured": True
    },
    {
        "slug": "software-engineer-csharp-fullstack-ninjaone",
        "title": "Software Engineer (C# Fullstack)",
        "company": "NinjaOne",
        "location": "Bandung, Jawa Barat, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 15-25 Juta",
        "posted": "2026-08-03",
        "expires": "2026-09-02",
        "description": "NinjaOne, perusahaan SaaS global yang berfokus pada IT management dan monitoring, membuka lowongan Software Engineer spesialis C# Fullstack untuk bekerja di Bandung. Anda akan mengembangkan fitur-fitur yang dipakai ribuan profesional IT di seluruh dunia, mencakup frontend maupun backend dengan teknologi C# dan .NET. Perusahaan menawarkan lingkungan kerja modern, fleksibilitas kerja, dan kesempatan tumbuh bersama tim engineering global.",
        "requirements": [
            "Minimal 3-5 tahun pengalaman sebagai Software Engineer",
            "Expert di C# dan .NET/.NET Core",
            "Pengalaman fullstack: frontend (React/Angular) dan backend (ASP.NET Core)",
            "Pengalaman REST API design dan integrasi sistem",
            "Pemahaman database SQL (SQL Server atau PostgreSQL)",
            "Familiar dengan testing (unit, integration) dan code quality tools",
            "Pengalaman CI/CD dan cloud (Azure/AWS) adalah nilai plus",
            "Kemampuan bahasa Inggris untuk kolaborasi tim global",
            "Bersedia bekerja dari Bandung (hybrid)"
        ],
        "responsibilities": [
            "Mengembangkan fitur fullstack pada platform NinjaOne",
            "Merancang dan membangun REST API yang scalable",
            "Melakukan code review dan menjaga kualitas kode",
            "Berkolaborasi dengan product manager dan desainer",
            "Menulis unit dan integration tests",
            "Mengoptimasi performa aplikasi dan database",
            "Berpartisipasi dalam on-call dan incident response",
            "Mendokumentasikan keputusan teknis dan arsitektur"
        ],
        "benefits": [
            "Gaji kompetitif (Rp 15-25 Juta)",
            "Flexible work arrangement (hybrid)",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Asuransi kesehatan",
            "Learning budget dan pelatihan bersertifikat",
            "Bekerja dengan produk SaaS global dan tim internasional",
            "Perangkat kerja modern (laptop + monitor)",
            "Kultur remote-friendly dan work-life balance"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/software-engineer-c%23-fullstack-bandung-indonesia-at-ninjaone-4432241561",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/software-engineer-c%23-fullstack-bandung-indonesia-at-ninjaone-4432241561",
        "featured": False
    },
    {
        "slug": "graduate-intern-software-engineer-formulatrix",
        "title": "Graduate Intern - Software Engineer (Backend)",
        "company": "Formulatrix Indonesia",
        "location": "Semarang, Jawa Tengah, Indonesia",
        "type": "Internship",
        "category": "Teknologi",
        "salary": "Rp 5-8 Juta",
        "posted": "2026-08-03",
        "expires": "2026-09-02",
        "description": "Formulatrix Indonesia menawarkan program Graduate Intern Software Engineer (Backend) di Semarang untuk lulusan baru yang ingin mendapatkan pengalaman praktis di bidang pengembangan software. Melalui program ini, peserta mendapat exposure dan kesempatan mengeksplorasi jalur karir, belajar dari engineer senior, serta terlibat langsung dalam pengembangan produk teknologi otomasi laboratorium yang digunakan di berbagai negara.",
        "requirements": [
            "Lulusan baru (fresh graduate) S1 Teknik Informatika, Ilmu Komputer, atau bidang terkait",
            "Pemahaman kuat tentang OOP, data structures, dan algorithms",
            "Familiar dengan minimal satu bahasa pemrograman (Java, C#, Python, atau Go)",
            "Pengetahuan dasar database SQL dan REST API",
            "Kemampuan bahasa Inggris teknis (membaca dan menulis)",
            "Motivasi tinggi untuk belajar dan berkembang",
            "Bersedia mengikuti program internship di Semarang"
        ],
        "responsibilities": [
            "Mengembangkan backend services di bawah bimbingan senior engineer",
            "Menulis clean code dan unit tests",
            "Mempelajari arsitektur dan codebase produk Formulatrix",
            "Berpartisipasi dalam sprint planning dan daily standup",
            "Membantu debugging dan perbaikan isu",
            "Mendokumentasikan proses dan keputusan teknis",
            "Menghadiri sesi training dan knowledge sharing",
            "Menyelesaikan project akhir yang dievaluasi tim"
        ],
        "benefits": [
            "Stipend bulanan (Rp 5-8 Juta)",
            "Mentoring 1-on-1 dari engineer berpengalaman",
            "Pengalaman bekerja dengan produk teknologi internasional",
            "Kesempatan konversi menjadi karyawan tetap",
            "Sertifikat internship",
            "Lingkungan kerja kolaboratif dan suportif",
            "Exposure ke teknologi otomasi laboratorium terkini"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/software-engineer-graduate-intern-at-formulatrix-indonesia-4373308317",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/software-engineer-graduate-intern-at-formulatrix-indonesia-4373308317",
        "featured": False
    },
    {
        "slug": "esb-academy-marketing-bootcamp-trainee",
        "title": "ESB Academy Marketing Bootcamp Trainee",
        "company": "PT Esensi Solusi Buana (ESB)",
        "location": "Jakarta, Indonesia",
        "type": "Program",
        "category": "Marketing",
        "salary": "Rp 4-7 Juta",
        "posted": "2026-08-03",
        "expires": "2026-09-02",
        "description": "PT Esensi Solusi Buana (ESB) membuka program ESB Academy Marketing Bootcamp Trainee bagi fresh graduate atau mahasiswa tingkat akhir di bidang Marketing, Desain Komunikasi Visual, atau bidang terkait. Program ini dirancang untuk mencetak talenta marketing yang siap kerja melalui pelatihan intensif dan pengalaman praktis — termasuk mengelola aset desain, menjaga timeline proyek, dan berkontribusi pada kampanye nyata perusahaan.",
        "requirements": [
            "Fresh graduate atau mahasiswa tingkat akhir di Marketing, Desain Komunikasi Visual, atau bidang terkait",
            "Memiliki passion di bidang marketing dan branding",
            "Familiar dengan tools desain (Canva, Adobe Photoshop/Illustrator) adalah nilai plus",
            "Kreatif, komunikatif, dan mampu bekerja dalam tim",
            "Mampu mengelola waktu dan menjaga deadline proyek",
            "Bersedia mengikuti program bootcamp di Jakarta"
        ],
        "responsibilities": [
            "Mengikuti pelatihan intensif marketing dan branding",
            "Membantu menyusun dan mengeksekusi kampanye marketing",
            "Mengorganisir aset desain dan menjaga timeline proyek",
            "Membuat konten marketing untuk berbagai kanal",
            "Menganalisis performa kampanye dan menyusun laporan",
            "Berkolaborasi dengan tim kreatif dan sales",
            "Presentasi hasil project kepada mentor dan manajemen"
        ],
        "benefits": [
            "Uang saku/trainee allowance (Rp 4-7 Juta)",
            "Pelatihan intensif dan mentoring dari praktisi marketing",
            "Pengalaman kerja nyata pada proyek klien",
            "Sertifikat ESB Academy",
            "Kesempatan menjadi karyawan tetap setelah program",
            "Portofolio kampanye untuk pengembangan karir",
            "Lingkungan kerja muda dan dinamis"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/esb-academy-marketing-bootcamp-trainee-at-pt-esensi-solusi-buana-esb-4328717480",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/esb-academy-marketing-bootcamp-trainee-at-pt-esensi-solusi-buana-esb-4328717480",
        "featured": False
    },
    {
        "slug": "digital-content-social-media-intern-panin-dai-ichi-life",
        "title": "Digital Content & Social Media Intern",
        "company": "Panin Dai-ichi Life",
        "location": "Jakarta, Indonesia",
        "type": "Internship",
        "category": "Konten & Kreatif",
        "salary": "Rp 3-5 Juta",
        "posted": "2026-08-03",
        "expires": "2026-09-02",
        "description": "Panin Dai-ichi Life, perusahaan asuransi jiwa patungan antara Panin Group dan Dai-ichi Life (Jepang), membuka posisi Digital Content & Social Media Intern. Intern akan terlibat dalam produksi konten digital dan pengelolaan media sosial perusahaan menggunakan tools seperti CapCut, VN, InShot, dan Canva. Posisi ini cocok untuk mahasiswa aktif atau fresh graduate yang komunikatif, teliti, proaktif, dan antusias belajar hal baru.",
        "requirements": [
            "Mahasiswa aktif (semester akhir) atau fresh graduate",
            "Komunikatif, teliti, dan proaktif",
            "Familiar dengan Microsoft Office (Word, Excel, PowerPoint)",
            "Menguasai tools editing konten seperti CapCut, VN, InShot, atau Canva",
            "Mampu bekerja dalam tim dan beradaptasi cepat",
            "Passion terhadap konten digital dan media sosial",
            "Bersedia magang di area Jakarta"
        ],
        "responsibilities": [
            "Membuat konten digital untuk media sosial perusahaan",
            "Mengedit video pendek dan materi visual",
            "Membantu menyusun kalender konten media sosial",
            "Monitoring dan merespons engagement di kanal sosial media",
            "Riset tren konten dan kompetitor",
            "Mendukung pelaksanaan campaign digital marketing",
            "Menyusun laporan performa konten secara berkala"
        ],
        "benefits": [
            "Uang saku magang (Rp 3-5 Juta)",
            "Pengalaman kerja di perusahaan asuransi ternama",
            "Mentoring dari tim digital & marketing profesional",
            "Sertifikat magang",
            "Kesempatan networking dan pengembangan karir",
            "Portofolio konten digital untuk karir ke depan",
            "Lingkungan kerja suportif dan inklusif"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/digital-content-social-media-intern-at-panin-dai-ichi-life-4373436099",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/digital-content-social-media-intern-at-panin-dai-ichi-life-4373436099",
        "featured": False
    }
]

# Duplicate check
existing_slugs = {job.get('slug') for job in data.get('jobs', [])}
existing_urls = {job.get('source_url') for job in data.get('jobs', []) if job.get('source_url')}
dupes = 0
for job in new_jobs:
    if job['slug'] in existing_slugs:
        print(f"WARNING: slug exists: {job['slug']}")
        dupes += 1
    if job['source_url'] in existing_urls:
        print(f"WARNING: source_url exists: {job['source_url']}")
        dupes += 1
if dupes:
    raise SystemExit(f"Aborting: {dupes} duplicates found")

# Insert at index 0
data['jobs'] = new_jobs + data['jobs']

with open(DB, 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Inserted {len(new_jobs)} new jobs. Total jobs now: {len(data['jobs'])}")
