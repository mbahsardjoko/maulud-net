import json
from datetime import datetime, timedelta

# Read existing data
with open('loker/lowongan.json', 'r') as f:
    data = json.load(f)

today = datetime(2026, 8, 23)
posted_date = today.strftime('%Y-%m-%d')
expires_date = (today + timedelta(days=30)).strftime('%Y-%m-%d')

new_jobs = [
    {
        "slug": "kredivo-group-data-scientist-ai-llm",
        "title": "Data Scientist (AI/LLM Applications)",
        "company": "Kredivo Group",
        "location": "Jakarta Raya, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 15-25 Juta",
        "posted": posted_date,
        "expires": expires_date,
        "description": "Kredivo Group, perusahaan fintech terkemuka di Asia Tenggara dengan produk unggulan Kredivo dan Kredit Pintar, mencari Data Scientist yang spesialis di AI dan Large Language Model (LLM) untuk mengembangkan sistem cerdas yang memberdayakan jutaan pengguna. Kandidat akan bekerja pada aplikasi AI modern: RAG (Retrieval-Augmented Generation), fine-tuning LLM, vector database, dan sistem rekomendasi skala produksi untuk layanan keuangan digital.",
        "requirements": [
            "Minimal 3 tahun pengalaman Data Science / ML Engineering applied",
            "Mahir Python: scikit-learn, PyTorch/TensorFlow, Hugging Face Transformers",
            "Pengalaman langsung dengan LLM: fine-tuning, RAG, prompt engineering, evaluation",
            "Paham vector database: Pinecone, Weaviate, Milvus, atau Qdrant",
            "Pengalaman MLOps: MLflow, Kubeflow, Docker, Kubernetes untuk deployment model",
            "Familiar dengan cloud ML: Vertex AI, SageMaker, atau Azure ML",
            "Kemampuan komunikasi teknis untuk presentasi ke stakeholder non-teknis",
            "Bisa bekerja hybrid di Jakarta"
        ],
        "responsibilities": [
            "Merancang, melatih, dan mengevaluasi model LLM untuk berbagai use case fintech",
            "Membangun dan memelihara RAG pipeline: data ingestion, embedding, retrieval, generation",
            "Mengimplementasikan MLOps best practices: versioning, monitoring, retraining automation",
            "Berkolaborasi dengan Data Engineer untuk data quality dan feature store",
            "Mengoptimasi model untuk production: quantization, distillation, compilation",
            "Riset dan eksperimen dengan teknik AI terbaru (multimodal, agentic AI, dll)",
            "Mendokumentasikan eksperimen, architecture decision, dan runbook",
            "Mentoring junior ML engineer dan code review"
        ],
        "benefits": [
            "Gaji kompetitif Rp 15-25 Juta + bonus project + performance bonus",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "THR dan bonus tahunan",
            "Laptop high-spec (MacBook Pro / Windows high-end + GPU cloud access)",
            "Budget learning: konferensi AI/ML (NeurIPS, ICML, lokal), sertifikasi cloud ML",
            "Hybrid working fleksibel",
            "Eksposur project AI/ML beragam industri: fintech, e-commerce, healthtech",
            "Tim ML & Data yang collaborative, culture of experimentation",
            "Akses GPU cluster untuk training model skala besar"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/data-scientist-ai-llm-applications-at-kredivo-group-4400721729",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/data-scientist-ai-llm-applications-at-kredivo-group-4400721729",
        "featured": True
    },
    {
        "slug": "pt-siaga-abdi-utama-devops-engineer",
        "title": "DevOps Engineer (Entry-Level/Junior)",
        "company": "PT Siaga Abdi Utama",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 7-12 Juta",
        "posted": posted_date,
        "expires": expires_date,
        "description": "PT Siaga Abdi Utama membuka peluang bagi DevOps Engineer entry-level/junior untuk bergabung dengan tim infrastruktur mereka di Jakarta. Posisi ini cocok untuk fresh graduate atau junior engineer yang ingin belajar dan berkembang di dunia DevOps, cloud infrastructure, dan automation. Kandidat akan dibimbing untuk membangun dan memelihara CI/CD pipeline, mengelola containerization, dan mendukung keandalan sistem production.",
        "requirements": [
            "Fresh graduate S1 Ilmu Komputer/Teknik Informatika atau pengalaman minimal 1 tahun DevOps",
            "Paham dasar Linux/Unix, networking, dan scripting (Bash/Python)",
            "Kenal Docker dan konsep containerization",
            "Paham dasar CI/CD: GitHub Actions, GitLab CI, atau Jenkins",
            "Familiar dengan cloud platform: AWS, GCP, atau Azure (minimal salah satu)",
            "Memahami Infrastructure as Code: Terraform atau Ansible (basic)",
            "Antusias belajar Kubernetes, monitoring (Prometheus/Grafana), dan logging",
            "Bersedia bekerja onsite/hybrid di Jakarta"
        ],
        "responsibilities": [
            "Membantu membangun dan memelihara CI/CD pipeline untuk deployment otomatis",
            "Mengelola Docker images dan container registry",
            "Mendukung provisioning infrastructure menggunakan Terraform/Ansible",
            "Monitoring sistem production: metrics, logs, alerting",
            "Membantu troubleshooting deployment dan infrastructure issues",
            "Belajar dan menerapkan Kubernetes untuk orchestration",
            "Mendokumentasikan runbook, SOP, dan architecture decision",
            "Berkolaborasi dengan tim development untuk developer experience"
        ],
        "benefits": [
            "Gaji kompetitif Rp 7-12 Juta + bonus performa",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "THR dan tunjangan hari raya",
            "Mentorship terstruktur dari senior DevOps engineer",
            "Budget sertifikasi cloud (AWS/GCP/Azure), CKAD, CKA",
            "Hybrid working fleksibel",
            "Laptop disediakan",
            "Culture belajar dan eksperimen teknologi baru"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/devops-engineer-at-pt-siaga-abdi-utama-4361822824",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/devops-engineer-at-pt-siaga-abdi-utama-4361822824",
        "featured": False
    },
    {
        "slug": "krom-product-manager",
        "title": "Product Manager",
        "company": "Krom",
        "location": "Jakarta Raya, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 18-28 Juta",
        "posted": posted_date,
        "expires": expires_date,
        "description": "Krom, perusahaan teknologi yang berkembang pesat, mencari Product Manager untuk memimpin pengembangan produk digital inovatif. Kandidat akan bekerja kolaboratif dengan tim engineering, analyst, design, dan business untuk mendefinisikan roadmap, mengelola lifecycle produk end-to-end, dan memastikan delivery fitur yang berdampak. Posisi ini menawarkan otonomi tinggi dalam membentuk strategi produk teknologi.",
        "requirements": [
            "Minimal 3 tahun pengalaman sebagai Product Manager di industri teknologi",
            "Pengalaman mengelola produk end-to-end: discovery, planning, delivery, iteration",
            "Kemampuan analisis data dan pasar yang kuat (SQL, Excel, Tableau/Looker/Amplitude)",
            "Paham SDLC, agile methodology, dan product workflow",
            "Kemampuan komunikasi dan stakeholder management yang excellent",
            "Pengalaman dengan produk SaaS, marketplace, atau fintech menjadi nilai plus",
            "Familiar dengan tools: JIRA, Figma, Mixpanel/Amplitude, Git",
            "Kemampuan prioritisasi berbasis impact vs effort dengan framework terstruktur"
        ],
        "responsibilities": [
            "Mendefinisikan dan mengelola product roadmap sesuai strategi bisnis",
            "Melakukan riset pasar, kompetitor, dan user research untuk identifikasi opportunity",
            "Membuat PRD (Product Requirement Document) yang detail dan actionable",
            "Berkolaborasi dengan engineering, design, dan QA untuk delivery fitur tepat waktu",
            "Menganalisis metrics produk (adoption, retention, conversion, revenue) untuk keputusan data-driven",
            "Mengelola backlog prioritas dan sprint planning bersama tim engineering",
            "Bekerja sama dengan tim marketing dan partnerships untuk go-to-market strategy",
            "Mengkomunikasikan product update ke leadership dan stakeholder cross-fungsi"
        ],
        "benefits": [
            "Gaji kompetitif Rp 18-28 Juta + bonus performa + stock option",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "THR dan tunjangan hari raya lengkap",
            "Asuransi kesehatan premium untuk karyawan dan keluarga",
            "Laptop dan perangkat kerja disediakan (MacBook Pro)",
            "Budget learning: konferensi produk, kursus, sertifikasi",
            "Hybrid working fleksibel di Jakarta",
            "Otonomi tinggi dalam memimpin produk teknologi skala cepat",
            "Tim cross-functional yang collaborative dan high-autonomy"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/product-manager-at-krom-4310845616",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/product-manager-at-krom-4310845616",
        "featured": False
    },
    {
        "slug": "archipelago-international-ui-ux-designer",
        "title": "UI/UX Designer",
        "company": "Archipelago International",
        "location": "Jakarta Raya, Indonesia",
        "type": "Full-time",
        "category": "Desain",
        "salary": "Rp 10-18 Juta",
        "posted": posted_date,
        "expires": expires_date,
        "description": "Archipelago International, manajemen hotel dan hospitalitas terbesar di Asia Tenggara, mencari UI/UX Designer untuk merancang pengalaman digital yang seamless bagi jutaan tamu dan mitra. Kandidat akan merancang interface untuk platform booking, mobile apps, loyalty program, dan internal tools yang digunakan di ribuan properti hotel di seluruh Asia. Posisi ini menawarkan tantangan desain skala enterprise di industri hospitalitas.",
        "requirements": [
            "Minimal 3 tahun pengalaman sebagai UI/UX Designer atau Product Designer",
            "Portfolio kuat menunjukkan end-to-end product design process untuk web & mobile",
            "Mahir Figma: auto-layout, variants, design tokens, prototyping advanced",
            "Paham user research, usability testing, dan design thinking methodology",
            "Kemampuan menciptakan wireframe, mockup, dan interactive prototype high-fidelity",
            "Paham accessibility standards (WCAG) dan inclusive design",
            "Pengalaman bekerja dengan design system dan component library",
            "Komunikasi visual yang kuat untuk presentasi ke stakeholder",
            "Bersedia bekerja hybrid di Jakarta"
        ],
        "responsibilities": [
            "Merancang UI/UX untuk mobile apps, web booking, dan partner dashboard",
            "Membuat wireframes, user flows, dan high-fidelity mockup untuk fitur baru",
            "Melakukan user research dan usability testing dengan end-user (tamu hotel, mitra)",
            "Membangun dan memelihara design system yang konsisten untuk semua produk digital",
            "Berkolaborasi dengan product manager dan engineering untuk definisi requirement",
            "Menghandoff desain ke engineering dengan spesifikasi yang jelas dan detail",
            "Mengoptimasi UX berdasarkan data analytics dan user feedback",
            "Menciptakan prototype interaktif untuk stakeholder review",
            "Menjaga konsistensi visual dan interaction pattern di seluruh platform"
        ],
        "benefits": [
            "Gaji kompetitif Rp 10-18 Juta sesuai pengalaman",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "THR dan bonus tahunan",
            "Laptop MacBook Pro disediakan",
            "Budget learning: design tools license, kursus, conference",
            "Hybrid working (2-3 hari WFO di Jakarta)",
            "Exposure produk hospitalitas skala jutaan pengguna di SEA",
            "Tim design yang collaborative dan culture of feedback",
            "Fasilitas kantor modern dan work-life balance",
            "Diskon stay di hotel Archipelago Group"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/ui-ux-designer-at-archipelago-international-4347477256",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/ui-ux-designer-at-archipelago-international-4347477256",
        "featured": False
    },
    {
        "slug": "sensor-tower-account-executive",
        "title": "Account Executive",
        "company": "Sensor Tower",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Marketing",
        "salary": "Rp 15-25 Juta",
        "posted": posted_date,
        "expires": expires_date,
        "description": "Sensor Tower, platform intelligence pasar aplikasi mobile terkemuka global, mencari Account Executive untuk mengembangkan bisnis di pasar Indonesia dan Asia Tenggara. Kandidat akan bertanggung jawab end-to-end sales cycle: prospeksi enterprise clients (mobile app developers, game studios, brand, investor), presentasi produk, negosiasi kontrak, hingga closing deal. Posisi ini cocok untuk sales hunter yang familiar dengan industri mobile app, data analytics, dan SaaS B2B.",
        "requirements": [
            "Minimal 3 tahun pengalaman Sales B2B / Account Executive (preferensi: SaaS, Mobile Tech, Data Analytics)",
            "Track record pencapaian sales target (minimal 80% quota attainment)",
            "Kemampuan prospeksi: cold call, email outreach, LinkedIn networking, industry event",
            "Mahir presentasi produk dan demo kepada decision maker (C-level, VP Product, Head of Growth)",
            "Kemampuan negosiasi kontrak, pricing, dan SLA dengan procurement/legal",
            "Familiar dengan CRM: Salesforce, HubSpot, Pipedrive, atau sejenisnya",
            "Paham industri mobile app: app store optimization, user acquisition, monetization",
            "Komunikasi Bahasa Inggris lancar (written/verbal) untuk kolaborasi global team",
            "Domisili Jakarta atau bersedia relocate"
        ],
        "responsibilities": [
            "Mencari dan mengkualifikasi lead enterprise: app developer, game studio, brand, investor",
            "Melakukan presentasi produk & demo platform Sensor Tower kepada stakeholder",
            "Mengelola sales pipeline end-to-end di CRM: prospeksi → proposal → negosiasi → closing",
            "Mencapai target bulanan/tahunan: revenue, new logo, upsell/cross-sell",
            "Berkolaborasi dengan Marketing untuk lead generation dan campaign support",
            "Mengkoordinasi dengan Customer Success untuk onboarding klien baru yang smooth",
            "Melakukan competitor research dan memberikan feedback ke Product team",
            "Membuat laporan aktivitas sales mingguan/bulanan dan forecasting",
            "Menjaga hubungan jangka panjang dengan key account untuk retention & expansion"
        ],
        "benefits": [
            "Gaji pokok Rp 15-25 Juta + komisi uncapped (potensi total Rp 30-50 Juta/bulan)",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "THR dan bonus tahunan",
            "Insentif quarterly achiever: trip, gadget, bonus khusus",
            "Laptop dan smartphone disediakan",
            "Budget transport & meal allowance harian",
            "Training sales methodology: MEDDIC, Challenger Sale, SPIN Selling",
            "Karier path ke Senior Account Executive → Sales Manager → Head of Sales APAC",
            "Produk data intelligence global yang digunakan top tech companies dunia",
            "Tim sales global yang energetic, collaborative, dan high-performance culture"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/account-executive-at-sensor-tower-4455402652",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/account-executive-at-sensor-tower-4455402652",
        "featured": False
    }
]

# Insert new jobs at the beginning (index 0)
for job in reversed(new_jobs):
    data['jobs'].insert(0, job)

# Update categories array - compute from jobs
categories = sorted(list(set(job['category'] for job in data['jobs'] if job.get('category'))))
data['categories'] = categories

# Write back
with open('loker/lowongan.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_jobs)} new jobs")
print(f"Total jobs now: {len(data['jobs'])}")
print(f"Categories: {categories}")
for job in new_jobs:
    print(f"  - {job['title']} ({job['company']}) - {job['source_url']}")