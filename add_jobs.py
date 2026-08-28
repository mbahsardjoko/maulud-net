#!/usr/bin/env python3
"""Add new job listings to lowongan.json"""
import json
from datetime import datetime, timedelta
from pathlib import Path

BASE = Path(__file__).resolve().parent
JSON_PATH = BASE / 'loker' / 'lowongan.json'

with open(JSON_PATH) as f:
    data = json.load(f)

today = datetime.now().strftime('%Y-%m-%d')
expires = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')

new_jobs = [
    {
        "slug": "bosshire-executive-software-engineer",
        "title": "Software Engineer",
        "company": "BOSSHIRE Executive",
        "location": "Jakarta, Indonesia (WFO)",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 12-22 Juta",
        "posted": today,
        "expires": expires,
        "description": "BOSSHIRE Executive, executive search firm terkemuka di Indonesia, membuka lowongan Software Engineer untuk bergabung dengan tim engineering klien enterprise mereka. Kandidat akan bekerja pada pengembangan aplikasi skala besar, membangun sistem backend yang scalable, dan berkolaborasi dengan cross-functional team untuk deliver solusi teknologi berkualitas tinggi. Posisi ini menawarkan peluang bekerja pada project-project menantang dari berbagai industri dengan exposure teknologi modern.",
        "requirements": [
            "Minimal 2 tahun pengalaman Software Engineering / Backend Development",
            "Mahir minimal satu bahasa: Go, Java, Python, Node.js, atau .NET",
            "Pengalaman dengan database: PostgreSQL, MySQL, MongoDB, atau Redis",
            "Paham konsep microservices, RESTful API, dan system design",
            "Familiar dengan Docker, Kubernetes, dan CI/CD pipeline",
            "Pengalaman cloud platform: AWS, GCP, atau Azure",
            "Kemampuan problem solving dan debugging yang kuat",
            "Bisa bekerja on-site di Jakarta (WFO)"
        ],
        "responsibilities": [
            "Mengembangkan dan memelihara backend services untuk aplikasi enterprise",
            "Merancang dan mengimplementasikan RESTful API dan microservices",
            "Optimasi performa database dan query untuk high-throughput systems",
            "Code review, mentoring junior engineer, dan establish engineering standards",
            "Berkolaborasi dengan Product Manager dan Designer untuk definisi fitur",
            "Troubleshooting production incidents dan root cause analysis",
            "Riset dan adopsi teknologi terbaru untuk improvement berkelanjutan"
        ],
        "benefits": [
            "Gaji kompetitif Rp 12-22 Juta + bonus performa + THR",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Asuransi kesehatan premium untuk karyawan + keluarga",
            "Laptop high-spec disediakan (MacBook Pro / ThinkPad)",
            "Budget learning: konferensi, sertifikasi, kursus (Rp 10jt/tahun)",
            "Career growth path jelas: Engineer → Senior → Lead → Architect",
            "Exposure project diverse: fintech, e-commerce, healthtech, logistics",
            "Tim engineering berkualitas, culture of ownership & excellence"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/software-engineer-at-bosshire-executive-4444353795",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/software-engineer-at-bosshire-executive-4444353795",
        "featured": True
    },
    {
        "slug": "starlight-hangars-software-engineer",
        "title": "Software Engineer",
        "company": "Starlight Hangars",
        "location": "Jakarta Raya, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 15-25 Juta",
        "posted": today,
        "expires": expires,
        "description": "Starlight Hangars, sister company of FORMULATRIX yang bergerak di industri otomatisasi laboratorium dan life sciences, mencari Software Engineer untuk mengembangkan software yang menggerakkan instrumen analitik canggih. Kandidat akan bekerja pada embedded software, firmware, dan aplikasi desktop yang interface dengan hardware precision. Posisi ini unik karena menggabungkan software engineering dengan domain sains kimia dan biologi molecular.",
        "requirements": [
            "Minimal 3 tahun pengalaman Software Engineering",
            "Mahir C++ (modern C++17/20) dan/atau Python",
            "Pengalaman embedded systems, firmware, atau real-time systems",
            "Paham hardware interfaces: UART, SPI, I2C, USB, Ethernet",
            "Familiar dengan Qt framework untuk desktop application development",
            "Pengalaman version control (Git), CI/CD, dan automated testing",
            "Background Computer Science, Electrical Engineering, atau setara",
            "Minat kuat pada domain life sciences / laboratory automation menjadi nilai plus"
        ],
        "responsibilities": [
            "Mengembangkan embedded software untuk instrumen analitik laboratory",
            "Membangun desktop application (Qt/C++) untuk instrument control & data acquisition",
            "Integrasi software dengan hardware: motor control, sensor, camera, fluidics",
            "Implementasi communication protocols antara instrument dan cloud/backend",
            "Code review, testing (unit, integration, hardware-in-the-loop)",
            "Berkolaborasi dengan mechanical, electrical, dan application scientist team",
            "Dokumentasi teknis: design spec, test plan, user manual"
        ],
        "benefits": [
            "Gaji kompetitif Rp 15-25 Juta + bonus performa + equity",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Asuransi kesehatan extensif (karyawan + pasangan + anak)",
            "Laptop high-spec + development hardware disediakan",
            "Budget learning: konferensi embedded systems, sertifikasi (Rp 15jt/tahun)",
            "Hybrid working arrangement",
            "Produk nyata: instrumen yang digunakan lab di 50+ negara",
            "Tim kecil, engineering-driven, culture of precision & innovation"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/software-engineer-at-starlight-hangars-4451976996",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/software-engineer-at-starlight-hangars-4451976996",
        "featured": False
    },
    {
        "slug": "dhl-supply-chain-ngt-mt-program-2026",
        "title": "Next Generation Talent (NGT MT Program 2026)",
        "company": "DHL Supply Chain Indonesia",
        "location": "Greater Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Administrasi",
        "salary": "Rp 10-15 Juta",
        "posted": today,
        "expires": expires,
        "description": "DHL Supply Chain Indonesia, bagian dari Deutsche Post DHL Group — perusahaan logistik terkemuka dunia, membuka program Next Generation Talent (NGT) Management Trainee 2026. Program ini dirancang untuk fresh graduate dan young professional dengan potensi tinggi untuk dikembangkan menjadi future leader di industri supply chain & logistics. Peserta akan melalui rotasi cross-functional, mentorship dari senior leader, dan project strategis dengan impact global.",
        "requirements": [
            "Fresh graduate atau maksimal 2 tahun pengalaman kerja (S1 semua jurusan)",
            "IPK minimal 3.00 dari universitas terakreditasi A",
            "Mahir Bahasa Inggris (lisan & tulis) — TOEFL/IELTS menjadi nilai plus",
            "Leadership potential: pernah memimpin organisasi, komite, atau project",
            "Analytical thinking, problem solving, dan adaptability tinggi",
            "Bersedia ditempatkan di Greater Jakarta dan melakukan travel domestik",
            "Passion pada industri logistics, supply chain, dan operations"
        ],
        "responsibilities": [
            "Mengikuti program MT 18-24 bulan dengan rotasi di 3-4 divisi (Operations, Commercial, Solutions, Project Management)",
            "Mengerjakan strategic project dengan sponsor C-level yang berimpact pada bisnis",
            "Belajar end-to-end supply chain: warehousing, transportation, freight, value-added services",
            "Berpartisipasi dalam leadership development workshop, coaching, dan mentoring session",
            "Presentasi project outcome ke senior leadership dan regional/global stakeholders",
            "Membangun network cross-functional dan cross-country dalam organisasi DHL Global"
        ],
        "benefits": [
            "Gaji kompetitif Rp 10-15 Juta + allowances + performance bonus",
            "BPJS Kesehatan dan Ketenagakerjaan sejak hari pertama",
            "Asuransi kesehatan global coverage (karyawan + keluarga)",
            "Relocation package untuk kandidat dari luar Jabodetabek",
            "Structured career path: MT → Specialist/Supervisor → Manager → Senior Leader",
            "Global exposure: assignment/secondment opportunity ke negara lain",
            "World-class learning: DHL Certified International Specialist, MBA sponsorship track",
            "Employee share purchase plan, pension fund, wellness program"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/next-generation-talent-ngt-mt-program-2026-at-dhl-supply-chain-4454019978",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/next-generation-talent-ngt-mt-program-2026-at-dhl-supply-chain-4454019978",
        "featured": False
    },
    {
        "slug": "amartek-backend-developer-golang-nodejs",
        "title": "Backend Developer (Golang/Node.js)",
        "company": "Bumi Amartha Teknologi Mandiri (Amartek)",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 12-20 Juta",
        "posted": today,
        "expires": expires,
        "description": "Bumi Amartha Teknologi Mandiri (Amartek), system integrator terkemuka yang menyediakan solusi IT infrastructure, cloud, dan cybersecurity untuk enterprise di Indonesia, mencari Backend Developer dengan keahlian Golang dan Node.js. Kandidat akan membangun dan memelihara backend services untuk platform internal dan client-facing, termasuk API gateway, microservices, dan data processing pipelines. Posisi ini menawarkan exposure pada tech stack modern dan project skala enterprise.",
        "requirements": [
            "Minimal 2 tahun pengalaman Backend Development",
            "Mahir Go (Golang): goroutines, channels, interface, generics",
            "Mahir Node.js: Express/NestJS/Fastify, async patterns, event loop",
            "Pengalaman database: PostgreSQL (advanced), Redis, MongoDB",
            "Paham microservices architecture, gRPC, RESTful API design",
            "Familiar dengan message queue: Kafka, RabbitMQ, atau NATS",
            "Container & Orchestration: Docker, Kubernetes (EKS/GKE)",
            "Pengalaman system integrator / enterprise IT menjadi nilai plus"
        ],
        "responsibilities": [
            "Mendesain dan mengembangkan backend services dengan Go dan Node.js",
            "Membangun RESTful API dan gRPC services untuk microservices architecture",
            "Optimasi performa: query tuning, caching strategy, connection pooling",
            "Implementasi event-driven architecture dengan message queue",
            "Setup observability: logging, metrics, tracing, alerting (Prometheus/Grafana)",
            "Code review, mentoring junior developer, dan establish best practices",
            "Berkolaborasi dengan DevOps, Frontend, dan Solution Architect team"
        ],
        "benefits": [
            "Gaji kompetitif Rp 12-20 Juta + bonus performa + THR",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Asuransi kesehatan premium (karyawan + pasangan + anak)",
            "Laptop MacBook Pro / ThinkPad disediakan",
            "Budget sertifikasi: AWS/GCP/Azure, CKAD, Go/Node.js certifications",
            "Hybrid working (2-3 hari WFO)",
            "Exposure project enterprise: banking, telco, government, manufacturing",
            "Tim engineering solid, culture of learning & knowledge sharing"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/backend-developer-golang-node-js-at-bumi-amartha-teknologi-mandiri-4304369493",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/backend-developer-golang-node-js-at-bumi-amartha-teknologi-mandiri-4304369493",
        "featured": False
    },
    {
        "slug": "pt-intikom-berlian-mustika-ui-ux-designer",
        "title": "UI/UX Designer",
        "company": "PT Intikom Berlian Mustika",
        "location": "DKI Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Desain",
        "salary": "Rp 10-18 Juta",
        "posted": today,
        "expires": expires,
        "description": "PT Intikom Berlian Mustika, perusahaan teknologi informasi yang fokus pada solusi banking dan financial services, mencari UI/UX Designer untuk mendesain pengalaman pengguna aplikasi mobile dan web banking. Kandidat akan bertanggung jawab penuh atas design process: user research, wireframing, prototyping, visual design, hingga usability testing. Posisi ini menawarkan tantangan mendesain untuk produk finansial yang digunakan jutaan nasabah dengan standar keamanan dan regulasi ketat.",
        "requirements": [
            "Minimal 2 tahun pengalaman UI/UX Design (banking/fintech diutamakan)",
            "Portfolio kuat: case study end-to-end dari research hingga final design",
            "Mahir Figma (advanced: auto layout, variants, design systems, prototyping)",
            "Paham user research methods: interview, usability testing, card sorting, analytics",
            "Familiar dengan design system, component library, dan handoff ke developer",
            "Paham aksesibilitas (WCAG) dan mobile platform guidelines (iOS HIG, Material Design)",
            "Kemampuan komunikasi design rationale ke stakeholder teknis & non-teknis",
            "Bersedia bekerja hybrid di Jakarta"
        ],
        "responsibilities": [
            "Melakukan user research dan competitive analysis untuk produk banking digital",
            "Mendesain user flow, wireframe, prototype (low-fi hingga high-fi) di Figma",
            "Membangun dan maintain design system untuk konsistensi multi-platform",
            "Berkolaborasi dengan Product Manager untuk definisi requirement & prioritization",
            "Handoff design ke developer: spec, asset, annotation, design token",
            "Melakukan usability testing dan iterasi berdasarkan feedback pengguna",
            "Berkontribusi pada design review, design critique session, dan design ops"
        ],
        "benefits": [
            "Gaji kompetitif Rp 10-18 Juta + bonus performa + THR",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Asuransi kesehatan extensif (karyawan + pasangan + anak)",
            "MacBook Pro + iPhone/Android untuk testing disediakan",
            "Budget learning: Figma config, UX conference, design certification (Rp 8jt/tahun)",
            "Hybrid working arrangement",
            "Produk banking skala jutaan user, impact nasional",
            "Tim design & product kolaboratif, design-driven culture"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/ui-ux-designer-at-pt-intikom-berlian-mustika-4375116314",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/ui-ux-designer-at-pt-intikom-berlian-mustika-4375116314",
        "featured": False
    },
    {
        "slug": "pt-berca-hardayaperkasa-fullstack-developer",
        "title": "Pengembang Fullstack",
        "company": "PT Berca Hardayaperkasa",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 10-18 Juta",
        "posted": today,
        "expires": expires,
        "description": "PT Berca Hardayaperkasa, perusahaan teknologi yang menyediakan solusi digital transformation untuk berbagai industri, mencari Fullstack Developer untuk membangun aplikasi web end-to-end. Kandidat akan bekerja pada frontend (React/Next.js) dan backend (ASP.NET Core / Laravel), database design, serta deployment ke cloud. Posisi ini cocok untuk developer yang suka ownership penuh pada product development lifecycle dan ingin exposure teknologi fullstack yang beragam.",
        "requirements": [
            "Minimal 1-2 tahun pengalaman Fullstack Web Development",
            "Frontend: Mahir React.js, Next.js, TypeScript, Tailwind CSS / CSS-in-JS",
            "Backend: Mahir ASP.NET Core (C#) ATAU Laravel (PHP) — minimal satu",
            "Database: PostgreSQL, MySQL, SQL Server — query optimization, migration",
            "State management: Redux Toolkit, Zustand, React Query / TanStack Query",
            "Authentication: JWT, OAuth2, OIDC, ASP.NET Core Identity",
            "Familiar dengan Docker, Git, CI/CD (GitHub Actions / GitLab CI)",
            "Paham RESTful API design, clean architecture, SOLID principles"
        ],
        "responsibilities": [
            "Mengembangkan fitur frontend (React/Next.js) dan backend (ASP.NET/Laravel) end-to-end",
            "Merancang database schema, migration, dan optimasi query",
            "Membangun reusable component library dan design system implementation",
            "Implementasi authentication, authorization, dan security best practices",
            "Setup CI/CD pipeline untuk automated build, test, dan deployment",
            "Code review, pairing session, dan knowledge sharing dengan tim",
            "Berkolaborasi dengan Designer, PM, dan QA untuk delivery berkualitas"
        ],
        "benefits": [
            "Gaji kompetitif Rp 10-18 Juta + bonus project + performance bonus",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "THR dan tunjangan hari raya lengkap",
            "Laptop disediakan (MacBook / Windows high-spec)",
            "Budget learning: kursus, sertifikasi, konferensi (Rp 8jt/tahun)",
            "Hybrid working fleksibel",
            "Exposure diverse project: enterprise apps, SaaS, e-gov, e-commerce",
            "Tim kecil, flat hierarchy, ownership tinggi, fast learning curve"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/pengembang-fullstack-at-pt-berca-hardayaperkasa-4320101070",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/pengembang-fullstack-at-pt-berca-hardayaperkasa-4320101070",
        "featured": False
    }
]

# Insert new jobs at the beginning (index 0)
data['jobs'] = new_jobs + data['jobs']

# Also update categories array - compute from jobs
categories = sorted(list(set(job['category'] for job in data['jobs'] if job.get('category'))))
data['categories'] = categories

with open(JSON_PATH, 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Added {len(new_jobs)} new jobs to lowongan.json")
print(f"Categories: {categories}")
for job in new_jobs:
    print(f"  - {job['title']} at {job['company']} ({job['slug']})")