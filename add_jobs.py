import json
from datetime import date, timedelta

# Load existing data
with open('/tmp/maulud-net/loker/lowongan.json', 'r') as f:
    data = json.load(f)

today = date(2026, 8, 26)
expires = today + timedelta(days=30)

new_jobs = [
    {
        "slug": "blue-bird-group-backend-developer",
        "title": "Back End Developer",
        "company": "Blue Bird Group",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 12-20 Juta",
        "posted": today.isoformat(),
        "expires": expires.isoformat(),
        "description": "Blue Bird Group, grup transportasi terkemuka di Indonesia yang terus berinovasi di bidang teknologi, mencari Back End Developer untuk mengembangkan dan memelihara sistem backend yang mendukung operasi transportasi skala nasional. Kandidat akan bekerja pada arsitektur microservices, membangun API yang scalable, dan mengintegrasikan dengan berbagai layanan internal serta eksternal. Posisi ini menawarkan tantangan membangun teknologi yang berdampak langsung pada jutaan pengguna harian.",
        "requirements": [
            "Minimal 2 tahun pengalaman Backend Development",
            "Mahir Go (Golang) atau Java Spring Boot / Node.js",
            "Pengalaman dengan database: PostgreSQL, MySQL, Redis",
            "Paham microservices architecture, RESTful API, gRPC",
            "Familiar dengan message queue: Kafka, RabbitMQ",
            "Pengalaman Docker, Kubernetes, dan CI/CD pipeline",
            "Paham observability: logging, monitoring, distributed tracing",
            "Bisa bekerja hybrid di Jakarta"
        ],
        "responsibilities": [
            "Mengembangkan dan memelihara backend services untuk platform transportasi Blue Bird",
            "Merancang dan mengimplementasikan RESTful API dan gRPC services",
            "Membangun microservices architecture yang scalable dan resilient",
            "Integrasi dengan payment gateway, mapping service, dan third-party API",
            "Optimasi performa database dan query untuk transaksi volume tinggi",
            "Setup observability stack: logging, metrics, tracing, alerting",
            "Code review, mentoring junior engineer, dan troubleshooting production",
            "Berkolaborasi dengan product, frontend, dan DevOps team"
        ],
        "benefits": [
            "Gaji kompetitif Rp 12-20 Juta + bonus performa",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Asuransi kesehatan premium untuk karyawan + keluarga",
            "Laptop high-spec disediakan (MacBook Pro / ThinkPad)",
            "Budget learning: konferensi, sertifikasi, kursus (Rp 10jt/tahun)",
            "Hybrid working fleksibel (3 hari WFO)",
            "Produk transportasi berdampak jutaan pengguna Indonesia",
            "Tim engineering berkualitas, culture of ownership & innovation"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/back-end-developer-at-blue-bird-group-4365234393",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/back-end-developer-at-blue-bird-group-4365234393",
        "featured": True
    },
    {
        "slug": "ajari-ai-product-manager",
        "title": "Product Manager (IT)",
        "company": "AJARI.AI",
        "location": "Jakarta Metropolitan Area, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 15-25 Juta",
        "posted": today.isoformat(),
        "expires": expires.isoformat(),
        "description": "AJARI.AI, startup AI-native yang fokus pada pengembangan solusi kecerdasan buatan untuk enterprise, mencari Product Manager untuk memimpin pengembangan produk AI B2B. Kandidat akan berkolaborasi dengan tim cross-fungsi (engineering, data science, design, business) untuk mengkonsep, memvalidasi, dan meluncurkan produk-produk AI yang memecahkan masalah bisnis nyata klien. Posisi ini ideal untuk PM yang ingin membangun produk AI dari nol dengan ownership penuh.",
        "requirements": [
            "Minimal 3 tahun pengalaman Product Management (SaaS/AI/ML diutamakan)",
            "Background teknis: Computer Science, Engineering, atau setara",
            "Pengalaman end-to-end product lifecycle: discovery, validation, build, launch",
            "Paham konsep ML/AI: supervised/unsupervised learning, NLP, LLM, RAG",
            "Kuat analisis data: SQL, Python/R, Mixpanel/Amplitude untuk product analytics",
            "Familiar dengan Agile/Scrum, Jira, Confluence, Figma",
            "Kemampuan komunikasi stakeholder: engineering, data science, design, business, leadership",
            "Bersedia bekerja hybrid di Jakarta"
        ],
        "responsibilities": [
            "Mendefinisikan product vision, strategy, dan roadmap untuk produk AI enterprise",
            "Melakukan user research, competitor analysis, dan market sizing",
            "Berkolaborasi dengan Data Science/ML Engineering untuk definisi requirement model",
            "Mengelola product backlog dan prioritisasi berbasis impact vs effort (RICE, MoSCoW)",
            "Bekerja sama dengan UX Designer untuk wireframe, user flow, dan prototype",
            "Koordinasi dengan Engineering untuk sprint planning dan delivery berkualitas",
            "Menganalisis metric produk post-launch: adoption, retention, engagement, ROI",
            "Presentasi progress dan rekomendasi ke leadership untuk go/no-go decision"
        ],
        "benefits": [
            "Gaji kompetitif Rp 15-25 Juta + equity (ESOP) signifikan",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Asuransi kesehatan premium untuk karyawan + keluarga",
            "Laptop MacBook Pro disediakan",
            "Budget AI/ML learning unlimited: konferensi internasional, sertifikasi, GPU cloud",
            "Hybrid working fleksibel, autonomy tinggi",
            "Ownership penuh pada produk AI dari ide hingga launch",
            "Tim kecil, move fast, culture of experimentation & research"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/product-manager-at-ajari-ai-4331983451",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/product-manager-at-ajari-ai-4331983451",
        "featured": False
    },
    {
        "slug": "indodax-devops-engineer",
        "title": "DevOps Engineer",
        "company": "INDODAX (Indonesia Digital Asset Exchange)",
        "location": "Jakarta Raya, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 15-25 Juta",
        "posted": today.isoformat(),
        "expires": expires.isoformat(),
        "description": "INDODAX, platform pertukaran aset digital terbesar di Indonesia dengan jutaan pengguna terdaftar, mencari DevOps Engineer untuk membangun dan memelihara infrastruktur cloud-native yang secure, scalable, dan high-availability. Kandidat akan bekerja pada sistem transaksi kripto volume tinggi, mengelola Kubernetes cluster, CI/CD pipeline, dan observability stack. Posisi ini menawarkan tantangan unik di intersection fintech, blockchain, dan cloud engineering.",
        "requirements": [
            "Minimal 3 tahun pengalaman DevOps / Site Reliability Engineering",
            "Mahir Kubernetes (EKS/GKE/AKS), Docker, Helm, Kustomize",
            "Pengalaman cloud platform: AWS (diutamakan), GCP, atau Azure",
            "Mahir Infrastructure as Code: Terraform, Crossplane, atau Pulumi",
            "Pengalaman CI/CD: GitHub Actions, GitLab CI, ArgoCD, atau Tekton",
            "Paham observability: Prometheus, Grafana, Loki, Tempo, OpenTelemetry",
            "Familiar dengan service mesh: Istio, Linkerd, atau Consul",
            "Pengalaman database: PostgreSQL, Redis, Cassandra, atau ScyllaDB",
            "Bisa bekerja hybrid di Jakarta"
        ],
        "responsibilities": [
            "Mendesain, membangun, dan memelihara Kubernetes clusters production-grade",
            "Mengelola CI/CD pipeline untuk microservices (build, test, deploy, rollback)",
            "Implementasi Infrastructure as Code untuk semua resource cloud",
            "Setup dan maintenance observability stack: metrics, logs, traces, alerting",
            "Optimasi biaya cloud (FinOps) dan capacity planning",
            "Implementasi security best practices: network policies, secrets management, RBAC",
            "Incident response, root cause analysis, dan postmortem",
            "Berkolaborasi dengan engineering team untuk platform enablement"
        ],
        "benefits": [
            "Gaji kompetitif Rp 15-25 Juta + bonus performa + token allocation",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Asuransi kesehatan extensif (karyawan + pasangan + anak)",
            "Laptop MacBook Pro M-series disediakan",
            "Budget learning unlimited: konferensi, sertifikasi (CKA, CKAD, AWS certs), buku",
            "Hybrid working fleksibel (2 hari WFO)",
            "Exposure sistem kripto/fintech skala jutaan user, high-throughput",
            "Tim engineering-driven, culture of automation & reliability"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/devops-engineer-at-indodax-indonesia-digital-asset-exchange-4435447029",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/devops-engineer-at-indodax-indonesia-digital-asset-exchange-4435447029",
        "featured": False
    },
    {
        "slug": "glints-ui-ux-designer",
        "title": "UI/UX Designer (Product Design ‒ Web & Mobile)",
        "company": "Glints",
        "location": "Jakarta Raya, Indonesia",
        "type": "Full-time",
        "category": "Desain",
        "salary": "Rp 10-18 Juta",
        "posted": today.isoformat(),
        "expires": expires.isoformat(),
        "description": "Glints, platform karir dan HR technology terkemuka di Asia Tenggara, mencari UI/UX Designer untuk membantu membentuk pengalaman pengguna platform berbasis subscription food-tech mereka. Kandidat akan berkolaborasi erat dengan founder dan tim development untuk mengubah operasi real-world yang kompleks menjadi produk digital yang intuitive dan delightful. Posisi ini menawarkan ownership penuh pada product design dari research hingga handoff.",
        "requirements": [
            "Minimal 2 tahun pengalaman UI/UX Design / Product Design",
            "Portfolio kuat menampilkan case study end-to-end (research → wireframe → prototype → handoff)",
            "Mahir Figma (auto layout, components, prototyping, design systems)",
            "Paham user research methods: interview, usability testing, card sorting, analytics",
            "Familiar dengan design tokens, component libraries, dan design handoff (Zeplin/Figma dev mode)",
            "Pemahaman dasar frontend: HTML, CSS, React Native/Flutter constraints",
            "Kemampuan komunikasi desain ke stakeholder non-teknis (product, engineering, leadership)",
            "Bersedia bekerja hybrid di Jakarta"
        ],
        "responsibilities": [
            "Melakukan user research: interview, survey, usability testing untuk identifikasi pain point",
            "Membuat user flow, wireframe, high-fidelity prototype untuk fitur baru",
            "Mendesain dan maintain design system/component library yang konsisten",
            "Berkolaborasi dengan Product Manager untuk definisi requirement dan success metric",
            "Bekerja sama dengan Engineer untuk design handoff, QA visual, dan implementasi",
            "Menjalankan design review dan mengiterasi berdasarkan feedback user & stakeholder",
            "Menganalisis metric UX: task success rate, time-to-complete, NPS, drop-off points",
            "Mendokumentasikan design decision, rationale, dan accessibility guidelines"
        ],
        "benefits": [
            "Gaji kompetitif Rp 10-18 Juta + bonus performa + equity (ESOP)",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Asuransi kesehatan premium untuk karyawan + keluarga",
            "Laptop MacBook Pro disediakan",
            "Budget design learning: konferensi (Figma Config, UX conferences), kursus, buku (Rp 10jt/tahun)",
            "Hybrid working fleksibel (3 hari WFO)",
            "Produk HR/karir berdampak jutaan talenta di Asia Tenggara",
            "Tim design & product collaborative, culture of craft & user-centricity"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/ui-ux-designer-at-glints-4319890660",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/ui-ux-designer-at-glints-4319890660",
        "featured": False
    },
    {
        "slug": "tbwa-indonesia-content-writer",
        "title": "Content Writer (B2B Writer - Bahasa Indonesia)",
        "company": "TBWA Indonesia",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Konten & Kreatif",
        "salary": "Rp 8-14 Juta",
        "posted": today.isoformat(),
        "expires": expires.isoformat(),
        "description": "TBWA Indonesia, agency kreatif global yang dikenal dengan metodologi Disruption® dan kini dipadu dengan AI untuk digital growth, mencari Content Writer untuk menulis konten B2B berbahasa Indonesia. Kandidat akan menciptakan thought leadership article, case study, white paper, dan konten strategis untuk klien-klien enterprise dari berbagai industri. Posisi ini menawarkan peluang menulis untuk brand-brand top tier dengan dukungan tools AI cutting-edge.",
        "requirements": [
            "Minimal 2 tahun pengalaman Content Writing / Copywriting (B2B, agency, atau in-house)",
            "Portfolio writing kuat: article, case study, white paper, blog post berbahasa Indonesia",
            "Paham content strategy: topic cluster, SEO basics, content funnel, thought leadership",
            "Kemampuan riset topik teknis/bisnis dan menerjemahkannya jadi tulisan accessible",
            "Familiar dengan AI writing tools: ChatGPT, Claude, Jasper, atau sejenisnya",
            "Mahir Bahasa Indonesia baku dan kreatif, Bahasa Inggris passive (baca referensi global)",
            "Deadline-driven, detail-oriented, bisa handle multiple project paralel",
            "Bersedia bekerja hybrid di Jakarta"
        ],
        "responsibilities": [
            "Menulis thought leadership article, case study, white paper untuk klien B2B enterprise",
            "Melakukan riset industri, competitor, dan audience untuk content planning",
            "Berkolaborasi dengan Strategist dan Account Manager untuk content brief & messaging",
            "Mengoptimasi konten untuk SEO: keyword research, on-page, content structure",
            "Menggunakan AI tools untuk riset, outline, drafting, dan editing (human-in-the-loop)",
            "Editing dan proofreading konten tim lain untuk konsistensi tone of voice",
            "Menganalisis performa konten: traffic, engagement, lead generation, conversion",
            "Presentasi ide konten dan rekomendasi ke klien/internal stakeholder"
        ],
        "benefits": [
            "Gaji kompetitif Rp 8-14 Juta + bonus performa + THR",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Asuransi kesehatan extensif (karyawan + pasangan + anak)",
            "Laptop disediakan",
            "Budget learning: writing workshop, AI tools training, konferensi kreatif (Rp 8jt/tahun)",
            "Hybrid working arrangement",
            "Exposure brand-brand top tier Indonesia & global, portfolio prestisius",
            "Akses tools AI premium (ChatGPT Enterprise, Claude, Midjourney, dll)",
            "Budaya kreatif: disruption sessions, hackathon, creative showcase"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/content-writer-at-tbwa-indonesia-—-powered-by-ai-driven-by-disruption-for-digital-growth-4325497609",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/content-writer-at-tbwa-indonesia-—-powered-by-ai-driven-by-disruption-for-digital-growth-4325497609",
        "featured": False
    },
    {
        "slug": "lemonilo-digital-marketing-specialist",
        "title": "Digital Marketing Specialist",
        "company": "Lemonilo",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Marketing",
        "salary": "Rp 10-18 Juta",
        "posted": today.isoformat(),
        "expires": expires.isoformat(),
        "description": "Lemonilo, brand makanan sehat dan gaya hidup terkemuka di Indonesia yang dikenal dengan mi instan berbasis sayur, mencari Digital Marketing Specialist untuk mengembangkan strategi digital marketing komprehensif yang selaras dengan tujuan bisnis. Kandidat akan mengelola budget, mengalokasikan resource efektif, dan mengeksekusi kampanye di berbagai channel digital. Posisi ini cocok untuk marketing professional yang ingin berkarya di brand FMCG growth-stage dengan community loyal.",
        "requirements": [
            "Minimal 3 tahun pengalaman Digital Marketing (FMCG/e-commerce diutamakan)",
            "Mahir performance marketing: Meta Ads, Google Ads, TikTok Ads, programmatic",
            "Pengalaman marketing analytics: GA4, Mixpanel, AppsFlyer, attribution modeling",
            "Paham growth marketing: A/B testing, CRO, funnel optimization, LTV/CAC",
            "Kemampuan manajemen budget & alokasi resource across channel",
            "Familiar dengan creative strategy: brief creative, creative testing, DCO",
            "Mahir Bahasa Indonesia dan Inggris (lisan & tulis)",
            "Bersedia bekerja hybrid di Jakarta"
        ],
        "responsibilities": [
            "Mengembangkan strategi digital marketing komprehensif (brand + performance)",
            "Mengelola end-to-end campaign: planning, execution, optimization, reporting",
            "Mengelola budget marketing bulanan/kuartalan dan alokasi across channel",
            "Melakukan A/B testing berkelanjutan: creative, audience, bidding, landing page",
            "Berkolaborasi dengan Creative team untuk brief dan produksi asset iklan",
            "Menganalisis metric: ROAS, CAC, LTV, conversion rate, retention cohort",
            "Koordinasi dengan agency/partner eksternal untuk eksekusi kampanye skala besar",
            "Melaporkan performance ke leadership dengan insight actionable"
        ],
        "benefits": [
            "Gaji kompetitif Rp 10-18 Juta + bonus performa + THR",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Asuransi kesehatan premium untuk karyawan + keluarga",
            "Laptop disediakan",
            "Budget learning: sertifikasi Meta/Google/TikTok Ads, konferensi marketing (Rp 12jt/tahun)",
            "Hybrid working fleksibel",
            "Produk FMCG sehat berdampak jutaan konsumen Indonesia",
            "Free product Lemonilo unlimited, snack sehat di kantor",
            "Tim marketing data-driven, culture of experimentation & growth"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://www.linkedin.com/jobs/view/3963908490",
        "source": "LinkedIn",
        "source_url": "https://www.linkedin.com/jobs/view/3963908490",
        "featured": False
    }
]

# Check for duplicates
existing_slugs = {job['slug'] for job in data['jobs']}
new_jobs_filtered = [job for job in new_jobs if job['slug'] not in existing_slugs]

print(f"Existing jobs: {len(data['jobs'])}")
print(f"New jobs to add: {len(new_jobs_filtered)}")
for job in new_jobs_filtered:
    print(f"  - {job['slug']}: {job['title']} at {job['company']}")

# Insert new jobs at the beginning (index 0)
data['jobs'] = new_jobs_filtered + data['jobs']

# Write back
with open('/tmp/maulud-net/loker/lowongan.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\nTotal jobs after update: {len(data['jobs'])}")
print("Done!")