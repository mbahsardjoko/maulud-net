import json
from datetime import date

# Read the original file
with open('loker/lowongan.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# New jobs to add (from web search results - real LinkedIn URLs)
new_jobs = [
    {
        "slug": "software-engineer-intern-oppo-indonesia",
        "title": "Software Engineer Intern",
        "company": "OPPO Indonesia Manufacturing",
        "location": "Tangerang, Banten",
        "type": "Internship",
        "category": "Teknologi",
        "salary": "Rp 4-7 Juta",
        "posted": "2026-07-09",
        "expires": "2026-10-09",
        "description": "OPPO Indonesia Manufacturing membuka lowongan Software Engineer Intern untuk program magang 6 bulan (April - Oktober 2026). Lokasi di Kawasan Industri Bayur, Tangerang. Kamu akan belajar langsung dari engineer senior dalam mengembangkan sistem manufaktur dan aplikasi internal untuk operasional pabrik smartphone terdepan. Program ini cocok untuk mahasiswa semester akhir atau fresh graduate yang ingin hands-on experience di industri manufaktur teknologi global.",
        "requirements": [
            "Mahasiswa S1 Ilmu Komputer / Teknik Informatika / Teknik Elektro semester 6-8 atau fresh graduate max 1 tahun",
            "Pemahaman dasar pemrograman: Python, Java, C++, atau Go",
            "Paham konsep OOP, struktur data, dan algoritma dasar",
            "Familiar dengan Git, Linux command line, dan database SQL",
            "Bersedia full-time on-site di Tangerang selama 6 bulan",
            "Komunikasi baik dan antusias belajar teknologi manufaktur (IoT, Automation, MES)"
        ],
        "responsibilities": [
            "Membantu pengembangan dan maintenance aplikasi internal manufaktur (MES, WMS, QMS)",
            "Berkolaborasi dengan tim IT & OT untuk integrasi sistem produksi",
            "Membangun dashboard monitoring untuk production line menggunakan Python/Go",
            "Mengotomatisasi tugas repetitif dengan script dan tooling internal",
            "Melakukan testing, debugging, dan dokumentasi teknis",
            "Belajar best practices software engineering di skala enterprise manufacturing"
        ],
        "benefits": [
            "Uang saku magang kompetitif + transport + makan",
            "Mentoring langsung dari Senior Software Engineer OPPO Global",
            "Exposure ke teknologi manufaktur canggih (Smart Factory, IoT, AI Visual Inspection)",
            "Sertifikat magang dan surat rekomendasi",
            "Kesempatan karyawan tetap (PMT) untuk performa terbaik",
            "Fasilitas kantin, gym, dan shuttle bus karyawan"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan Software Engineer Intern di OPPO Indonesia Manufacturing. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/software-engineer-intern-at-oppo-indonesia-manufacturing-4403337642",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/software-engineer-intern-at-oppo-indonesia-manufacturing-4403337642",
        "featured": True
    },
    {
        "slug": "data-analytics-ai-analyst-new-graduate-abeam-consulting",
        "title": "Data Analytics & AI Analyst - New Graduate 2026",
        "company": "ABeam Consulting Indonesia",
        "location": "Jakarta",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 12-20 Juta",
        "posted": "2026-07-09",
        "expires": "2026-08-08",
        "description": "ABeam Consulting Indonesia membuka program New Graduate Hiring 2026 untuk posisi Data Analytics & AI Analyst. Program ini dirancang untuk lulusan baru berperforma tinggi yang ingin memulai karir di konsultasi manajemen dan transformasi digital. Kamu akan bekerja pada proyek-proyek nyata: mengembangkan model prediktif, menganalisis big data, dan memberikan insight strategis untuk klien enterprise di berbagai industri (keuangan, manufaktur, retail, telekomunikasi). Pelatihan intensif dan mentorship dari consultant senior disediakan.",
        "requirements": [
            "Fresh graduate S1/S2 (lulus 2025-2026) jurusan Statistika, Matematika, Ilmu Komputer, Data Science, atau terkait",
            "IPK minimal 3.25/4.00",
            "Kuantitatif kuat: statistik, machine learning, optimisasi, time series",
            "Mahir Python (pandas, scikit-learn, TensorFlow/PyTorch) dan SQL",
            "Pengalaman project/portfolio data science/ML (github/kaggle/academic) wajib dilampirkan",
            "Bahasa Inggris aktif (lisan & tulisan) - wajib untuk engagement global",
            "Logical thinking, problem solving, dan kemampuan presentasi ke klien"
        ],
        "responsibilities": [
            "Mengembangkan model machine learning untuk kasus bisnis klien (churn prediction, demand forecasting, fraud detection, dll)",
            "Melakukan exploratory data analysis pada dataset enterprise skala besar",
            "Membangun dashboard dan visualisasi insight untuk C-level klien (Tableau/Power BI)",
            "Berkolaborasi dengan consultant senior untuk define problem statement & solution design",
            "Mendokumentasikan methodology, assumption, dan limitation model",
            "Mengikuti program training terstruktur: consulting skill, domain knowledge, tech stack"
        ],
        "benefits": [
            "Gaji kompetitif + sign-on bonus + performance bonus",
            "BPJS Ketenagakerjaan & Kesehatan lengkap",
            "Asuransi kesehatan global (cover keluarga)",
            "Program pelatihan terstruktur 6 bulan (ABeam Academy)",
            "Mentor dedicated senior consultant",
            "Exposure proyek cross-industry & cross-border (APAC)",
            "Jalur karir jelas: Analyst → Senior Analyst → Consultant → Manager"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan Data Analytics & AI Analyst New Graduate 2026 di ABeam Consulting Indonesia. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/data-analytics-ai-analyst-new-graduate-2026-at-abeam-consulting-indonesia-4408658575",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/data-analytics-ai-analyst-new-graduate-2026-at-abeam-consulting-indonesia-4408658575",
        "featured": False
    },
    {
        "slug": "digital-advertising-specialist-vritimes-indonesia",
        "title": "Digital Advertising Specialist",
        "company": "VRITIMES Indonesia",
        "location": "Jakarta",
        "type": "Full-time",
        "category": "Marketing",
        "salary": "Rp 8-15 Juta",
        "posted": "2026-07-09",
        "expires": "2026-08-08",
        "description": "VRITIMES Indonesia, platform distribusi press release dan media monitoring terkemuka di Asia, mencari Digital Advertising Specialist untuk mengelola dan mengoptimalkan kampanye iklan digital across-platform. Kamu akan menjalankan iklan di Google Ads, Meta (Facebook/Instagram), TikTok Ads, X (Twitter), dan YouTube untuk mendorong akuisisi user B2B (PR professionals, marketer, corporate comms) serta brand awareness. Posisi ini hands-on, data-driven, dan cocok untuk digital marketer yang suka eksperimen creative, audience, dan bidding strategy.",
        "requirements": [
            "Pengalaman minimal 2 tahun hands-on digital advertising (agency atau in-house)",
            "Mahir Google Ads (Search, Display, YouTube, Performance Max) dan Meta Ads Manager",
            "Pengalaman TikTok Ads, X Ads, atau LinkedIn Ads adalah nilai plus",
            "Paham funnel marketing B2B: lead gen, nurturing, conversion tracking",
            "Kuantitatif: bisa analisis data dengan Excel/Google Sheets, Data Studio/Looker Studio",
            "Kemampuan copywriting iklan singkat yang converting (ID & EN)",
            "Portfolio kampanye dengan metric terukur (CPA, ROAS, CTR, CPL) wajib dilampirkan"
        ],
        "responsibilities": [
            "Merencanakan, mengeksekusi, dan memonitor kampanye paid media harian di multi-platform",
            "Mengelola budget iklan bulanan >Rp 500 juta dengan target ROAS efisien",
            "Melakukan A/B testing creative, audience, landing page, dan bidding strategy",
            "Membangun dan memaintain conversion tracking (GA4, GTM, CAPI, Enhanced Conversions)",
            "Menyusun laporan performa mingguan/bulanan untuk management dengan actionable insight",
            "Berkolaborasi dengan tim Creative & Content untuk produksi asset iklan",
            "Riset kompetitor & eksplorasi channel/format iklan baru (misal: Reddit Ads, Quora Ads)"
        ],
        "benefits": [
            "Gaji kompetitif + bonus performa bulanan berbasis ROAS/CPA target",
            "BPJS Ketenagakerjaan dan Kesehatan",
            "Budget iklan untuk eksperimen & pembelajaran (learning budget)",
            "Flexible work arrangement (hybrid)",
            "MacBook Pro dan tools kerja disediakan",
            "Akses ke industri PRTech & MarTech Asia yang growing fast",
            "Tim marketing yang collaborative dan data-driven"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan Digital Advertising Specialist di VRITIMES Indonesia. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/digital-advertising-specialist-at-vritimes-indonesia-4403335920",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/digital-advertising-specialist-at-vritimes-indonesia-4403335920",
        "featured": False
    },
    {
        "slug": "ui-ux-designer-remote-indonesia-hyge",
        "title": "UI/UX Designer (Remote - Indonesia)",
        "company": "Hyge Pte. Ltd.",
        "location": "Remote (Indonesia)",
        "type": "Full-time",
        "category": "Desain",
        "salary": "Rp 12-22 Juta",
        "posted": "2026-07-09",
        "expires": "2026-08-08",
        "description": "Hyge, digital agency berbasis Singapura yang fokus pada UI/UX, engineering, dan project management untuk klien di Asia Tenggara, mencari UI/UX Designer fully remote berbasis Indonesia. Kamu akan merancang website dan aplikasi yang intuitif dan indah untuk klien beragam: startup teknologi, e-commerce, fintech, hingga brand lifestyle. Posisi ini cocok untuk desainer yang ingin kerja remote dengan standar global, kolaborasi cross-timezone (CET collaboration), dan project variety yang tinggi.",
        "requirements": [
            "Pengalaman minimal 2 tahun UI/UX Designer (agency atau in-house tech)",
            "Portfolio kuat menunjukkan end-to-end process: research → wireframe → prototype → handoff",
            "Mahir Figma (advanced: auto-layout, variants, design tokens, design systems)",
            "Paham user research methods: usability testing, interviews, heuristic evaluation",
            "Pengalaman design untuk responsive web & mobile app (iOS/Android guidelines)",
            "Bisa kolaborasi efektif dengan developer (design handoff, spec, QA via Figma DevMode/Zeplin)",
            "Bahasa Inggris aktif (lisan & tulisan) - wajib untuk meeting dengan klien/stakeholder global",
            "Timezone flexible: available untuk overlap CET (sore/jam kerja malam Indonesia)"
        ],
        "responsibilities": [
            "Merancang UI/UX untuk website, web app, dan mobile app klien internasional",
            "Melakukan user research & usability testing dengan user nyata",
            "Membuat wireframe, high-fidelity mockup, interactive prototype di Figma",
            "Mengembangkan & maintain design system: components, tokens, patterns, documentation",
            "Berkolaborasi dengan PM & Engineer untuk discovery, definition, validasi solusi desain",
            "Design QA saat development: review implementasi, feedback ke engineer",
            "Presentasi desain ke klien non-teknis dengan narasi yang jelas & persuasif"
        ],
        "benefits": [
            "Gaji kompetitif (USD/IDR) + bonus performa",
            "Fully remote - kerja dari mana saja di Indonesia",
            "MacBook Pro M-series + monitor 4K + budget setup WFH",
            "Budget learning tidak terbatas: kursus, sertifikasi (NN/g, Interaction Design Foundation), konferensi",
            "Asuransi kesehatan premium",
            "Tim multinasional, kolaboratif, low-ego",
            "Project variety tinggi: fintech, SaaS, e-commerce, healthtech, lifestyle"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan UI/UX Designer Remote Indonesia di Hyge. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/ui-ux-designer-remote-%E2%80%93-indonesia-at-hyge-4262869476",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/ui-ux-designer-remote-%E2%80%93-indonesia-at-hyge-4262869476",
        "featured": False
    },
    {
        "slug": "back-end-software-developer-timkado-indonesia",
        "title": "Back End Software Developer",
        "company": "PT Timkado Sejahtera Indonesia",
        "location": "Jakarta",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 15-25 Juta",
        "posted": "2026-07-09",
        "expires": "2026-08-08",
        "description": "Timkado, travel technology company yang mengoperasikan jaringan WhatsApp Business private terbesar di Indonesia (kirim jutaan notifikasi bulanan untuk traveler internasional), mencari Back End Software Developer. Kamu akan membangun dan memelihara sistem backend skala besar: WhatsApp automation, AI-powered chatbot, notification engine, dan integration dengan 500+ travel consultant partners di Indonesia, Malaysia, dan Filipina. Tech stack: Go, Python, PostgreSQL, Redis, Kafka, Kubernetes, AWS. Cocok untuk engineer yang suka tantangan high-throughput, real-time messaging, dan distributed systems.",
        "requirements": [
            "Pengalaman minimal 3 tahun Backend Developer / Software Engineer",
            "Mahir Go (primary) dan/atau Python untuk backend development",
            "Pengalaman production dengan PostgreSQL, Redis, dan message queue (Kafka/RabbitMQ)",
            "Paham microservices architecture, RESTful API, gRPC, dan API design",
            "Pengalaman dengan Docker, Kubernetes (EKS/GKE), dan CI/CD (GitLab CI/GitHub Actions)",
            "Strong understanding: concurrency, caching strategy, database indexing, observability (Prometheus/Grafana)",
            "Pengalaman WhatsApp Business API / Twilio / messaging platform adalah nilai plus besar",
            "Bisa komunikasi teknis efektif dalam Bahasa Inggris & Indonesia"
        ],
        "responsibilities": [
            "Mengembangkan & memelihara layanan backend core: notification engine, chatbot AI, partner API",
            "Merancang arsitektur sistem untuk handle high concurrency (jutaan message/hari) dengan low latency",
            "Membangun & mengoptimalkan database schema, query, dan indexing strategy",
            "Implementasi observability: metrics, logs, traces, alerting untuk production reliability",
            "Berkolaborasi dengan Frontend, Mobile, DevOps, dan Product untuk delivery fitur end-to-end",
            "Code review, writing unit/integration test, drive engineering best practices",
            "Troubleshooting production incidents, root cause analysis, dan postmortem"
        ],
        "benefits": [
            "Gaji kompetitif + bonus performa + ESOP (stock options)",
            "BPJS Ketenagakerjaan dan Kesehatan lengkap",
            "Asuransi kesehatan tambahan untuk keluarga",
            "Flexible hybrid work arrangement (WFO/WFH)",
            "MacBook Pro M-series + monitor eksternal + budget WFH setup",
            "Budget pembelajaran & sertifikasi (AWS, GCP, CNCF, dll.)",
            "Tim engineering senior, kolaboratif, engineering-culture kuat (RFC, tech sharing, hackathon)",
            "Produk travel tech dengan user base nyata & impact bisnis terbukti"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan Back End Software Developer di PT Timkado Sejahtera Indonesia. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/back-end-software-developer-at-pt-timkado-sejahtera-indonesia-4319355381",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/back-end-software-developer-at-pt-timkado-sejahtera-indonesia-4319355381",
        "featured": False
    }
]

# Check for duplicates by slug
existing_slugs = {job['slug'] for job in data['jobs']}
new_jobs_filtered = [job for job in new_jobs if job['slug'] not in existing_slugs]

print(f"Existing jobs: {len(data['jobs'])}")
print(f"New jobs to add: {len(new_jobs_filtered)}")
for job in new_jobs_filtered:
    print(f"  - {job['title']} ({job['company']}) - {job['source_url']}")

# Prepend new jobs to the jobs array
data['jobs'] = new_jobs_filtered + data['jobs']

# Write back
with open('loker/lowongan.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\nDone! Total jobs now: {len(data['jobs'])}")
