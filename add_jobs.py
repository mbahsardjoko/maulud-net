#!/usr/bin/env python3
import json
from datetime import datetime, timedelta

# Read existing JSON
with open('/tmp/maulud-net/loker/lowongan.json', 'r') as f:
    data = json.load(f)

# Today and expiry date
today = "2026-08-23"
expires = "2026-09-22"

# New jobs to add (5 jobs)
new_jobs = [
    {
        "slug": "frontend-developer-scout-inc",
        "title": "Frontend Developer",
        "company": "Scout.inc",
        "location": "Yogyakarta, Daerah Istimewa Yogyakarta, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 8-15 Juta",
        "posted": today,
        "expires": expires,
        "description": "Scout.inc membuka peluang bagi Frontend Developer untuk bergabung dengan tim kreatif mereka di Yogyakarta. Kandidat akan bertanggung jawab membangun antarmuka pengguna yang responsif dan modern untuk berbagai proyek digital klien, mulai dari website korporat hingga aplikasi web interaktif.",
        "requirements": [
            "Minimal 1 tahun pengalaman sebagai Frontend Developer",
            "Mahir HTML5, CSS3, JavaScript ES6+, dan TypeScript",
            "Pengalaman dengan React.js atau Vue.js (salah satu minimal)",
            "Paham konsep responsive design dan cross-browser compatibility",
            "Familiar dengan Git dan workflow kolaborasi tim",
            "Portofolio proyek frontend wajib dilampirkan"
        ],
        "responsibilities": [
            "Mengembangkan UI komponen yang reusable dan maintainable",
            "Menerjemahkan desain Figma/Adobe XD ke kode yang clean dan semantic",
            "Mengoptimasi performa frontend: lazy loading, code splitting, bundle size",
            "Kolaborasi dengan backend developer untuk integrasi RESTful API",
            "Melakukan code review dan menjaga standar kualitas kode",
            "Troubleshooting dan debugging cross-browser issues"
        ],
        "benefits": [
            "Gaji kompetitif Rp 8-15 Juta",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "THR dan bonus tahunan",
            "Laptop disediakan",
            "Flexible working hours",
            "Budget learning dan sertifikasi (Rp 5jt/tahun)",
            "Lokasi kerja Nyaman di Yogyakarta"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/front-end-developer-yogyakarta-at-scout-inc-3493500390",
        "source": "LinkedIn Indonesia",
        "source_url": "https://id.linkedin.com/jobs/view/front-end-developer-yogyakarta-at-scout-inc-3493500390",
        "featured": True
    },
    {
        "slug": "frontend-developer-net-idstar",
        "title": "Frontend Developer (.Net)",
        "company": "PT. IDStar Cipta Teknologi",
        "location": "Jakarta Raya, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 10-18 Juta",
        "posted": today,
        "expires": expires,
        "description": "PT. IDStar Cipta Teknologi (IDstar), perusahaan solusi teknologi terkemuka, mencari Frontend Developer dengan keahlian ekosistem .NET. Posisi ini akan mengembangkan antarmuka pengguna untuk aplikasi enterprise menggunakan Blazor, ASP.NET Core, dan teknologi frontend modern.",
        "requirements": [
            "Minimal 2 tahun pengalaman Frontend Development",
            "Mahir C#, ASP.NET Core, dan Blazor (WebAssembly/Server)",
            "Kuasai HTML5, CSS3, JavaScript ES6+, TypeScript",
            "Pengalaman dengan frontend framework: React, Angular, atau Vue.js",
            "Paham konsep RESTful API dan integrasi dengan backend .NET",
            "Familiar dengan Entity Framework Core dan SQL Server",
            "Pengalaman Azure/AWS untuk deployment (diutamakan)"
        ],
        "responsibilities": [
            "Membangun UI component library menggunakan Blazor",
            "Mengembangkan Single Page Application (SPA) dengan performa tinggi",
            "Kolaborasi tim backend untuk desain API contract",
            "Implementasi authentication/authorization (IdentityServer, JWT)",
            "Optimasi rendering: server-side vs client-side Blazor",
            "Menulis unit test dan integration test (bUnit, xUnit)",
            "CI/CD pipeline setup dengan Azure DevOps/GitHub Actions"
        ],
        "benefits": [
            "Gaji kompetitif Rp 10-18 Juta + bonus performa",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "THR dan bonus tahunan",
            "Asuransi kesehatan premium",
            "Sertifikasi Microsoft/Azure dibiayai perusahaan",
            "Hybrid working arrangement",
            "Laptop high-spec disediakan"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/frontend-developer-net-at-pt-idstar-cipta-teknologi-idstar-3691710409",
        "source": "LinkedIn Indonesia",
        "source_url": "https://id.linkedin.com/jobs/view/frontend-developer-net-at-pt-idstar-cipta-teknologi-idstar-3691710409",
        "featured": False
    },
    {
        "slug": "cloud-devops-engineer-nri-indonesia",
        "title": "Cloud DevOps Engineer",
        "company": "NRI Indonesia",
        "location": "Jakarta Raya, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 15-25 Juta",
        "posted": today,
        "expires": expires,
        "description": "NRI Indonesia (Nomura Research Institute), perusahaan konsulting TI dan sistem informasi Jepang terkemuka, mencari Cloud DevOps Engineer untuk membangun dan mengelola infrastruktur cloud modern. Kandidat akan bekerja pada proyek-proyek enterprise skala besar untuk klien korporat Indonesia dan global.",
        "requirements": [
            "Minimal 3 tahun pengalaman DevOps / Cloud Engineering",
            "Mahir AWS (EC2, ECS/EKS, RDS, Lambda, CloudFormation) atau GCP/Azure",
            "Pengalaman Kubernetes (EKS/GKE/AKS): deployment, scaling, troubleshooting",
            "Infrastructure as Code: Terraform (wajib) dan/atau Ansible",
            "CI/CD: GitHub Actions, GitLab CI, Jenkins, atau ArgoCD",
            "Containerization: Docker, Helm, container security scanning",
            "Monitoring & Observability: Prometheus, Grafana, ELK/EFK, Jaeger",
            "Scripting: Python, Bash, atau Go untuk automation"
        ],
        "responsibilities": [
            "Mendesain dan mengimplementasikan arsitektur cloud native yang scalable",
            "Membangun dan memelihara CI/CD pipeline untuk microservices",
            "Mengelola Kubernetes cluster production: upgrade, backup, disaster recovery",
            "Implementasi GitOps workflow dengan ArgoCD/Flux",
            "Setup observability stack: logging, metrics, tracing, alerting",
            "Optimasi cloud cost: right-sizing, reserved instances, spot instances",
            "Security hardening: network policies, RBAC, secrets management",
            "Kolaborasi dengan dev team untuk developer self-service platform"
        ],
        "benefits": [
            "Gaji kompetitif Rp 15-25 Juta + bonus proyek",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "THR dan bonus tahunan",
            "Budget sertifikasi AWS/GCP/Azure (Rp 15jt/tahun)",
            "Laptop high-spec (MacBook Pro / ThinkPad)",
            "Hybrid working fleksibel",
            "Exposure proyek enterprise skala global",
            "Budaya kerja profesional standar Jepang"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/cloud-devops-engineer-at-nri-indonesia-4279564538",
        "source": "LinkedIn Indonesia",
        "source_url": "https://id.linkedin.com/jobs/view/cloud-devops-engineer-at-nri-indonesia-4279564538",
        "featured": False
    },
    {
        "slug": "senior-backend-developer-go-kazokku",
        "title": "Senior Backend Developer (Go)",
        "company": "KAZOKKU",
        "location": "Jakarta Raya, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 18-30 Juta",
        "posted": today,
        "expires": expires,
        "description": "KAZOKKU, platform teknologi properti dan real estate terkemuka, mencari Senior Backend Developer yang mahir Go (Golang) untuk mengembangkan layanan backend skala tinggi. Kandidat akan membangun API, microservices, dan sistem terdistribusi yang mendukung transaksi properti digital.",
        "requirements": [
            "Minimal 4 tahun pengalaman Backend Development",
            "Mahir Go (Golang): goroutines, channels, interface, generics",
            "Pengalaman framework: Gin, Echo, atau standard library net/http",
            "Paham konsep microservices, gRPC, Protocol Buffers",
            "Database: PostgreSQL (advanced), Redis, MongoDB",
            "Message queue: RabbitMQ, Kafka, atau NATS",
            "Container & Orchestration: Docker, Kubernetes",
            "Testing: unit, integration, contract testing",
            "System design: caching strategy, rate limiting, circuit breaker"
        ],
        "responsibilities": [
            "Mendesain dan mengembangkan RESTful API dan gRPC services",
            "Membangun microservices architecture dengan Go",
            "Optimasi performa database: query tuning, indexing, connection pooling",
            "Implementasi event-driven architecture dengan message queue",
            "Setup observability: structured logging, distributed tracing, metrics",
            "Code review dan mentoring junior/mid-level developer",
            "Troubleshooting production incidents dan postmortem",
            "Riset dan adopsi teknologi Go terbaru (Go 1.22+ features)"
        ],
        "benefits": [
            "Gaji kompetitif Rp 18-30 Juta + bonus equity/ESOP",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "THR dan bonus tahunan",
            "Asuransi kesehatan premium untuk keluarga",
            "Laptop MacBook Pro M-series disediakan",
            "Budget konferensi GopherCon / Go training (Rp 10jt/tahun)",
            "Flexible remote/hybrid arrangement",
            "Produk proptech berdampak pada industri real estate Indonesia"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/senior-backend-developer-go-at-kazokku-4278014365",
        "source": "LinkedIn Indonesia",
        "source_url": "https://id.linkedin.com/jobs/view/senior-backend-developer-go-at-kazokku-4278014365",
        "featured": False
    },
    {
        "slug": "senior-appsec-engineer-phincon",
        "title": "Senior Application Security Engineer",
        "company": "PHINCON",
        "location": "Jakarta Raya, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 20-35 Juta",
        "posted": today,
        "expires": expires,
        "description": "PHINCON, perusahaan cybersecurity dan digital transformation terkemuka, mencari Senior Application Security Engineer untuk memperkuat tim AppSec mereka. Posisi ini bertanggung jawab mengamankan aplikasi enterprise mulai dari kode, pipeline, hingga runtime di lingkungan production.",
        "requirements": [
            "Minimal 4 tahun pengalaman Application Security / Secure SDLC",
            "Mahir SAST/DAST/IAST/SCA tools: SonarQube, Checkmarx, Fortify, Snyk, Semgrep",
            "Paham OWASP Top 10, ASVS, MASVS, SAMM framework",
            "Secure coding review: Java, Go, Python, Node.js, .NET",
            "Container security: image scanning, runtime protection, admission control",
            "CI/CD security: pipeline hardening, supply chain security (SLSA)",
            "Threat modeling: STRIDE, PASTA, attack tree analysis",
            "Sertifikasi relevan: OSCP, OSWE, GWAPT, atau eWPTX (diutamakan)"
        ],
        "responsibilities": [
            "Menyematkan security ke SDLC: SAST/DAST/SCA di pipeline CI/CD",
            "Melakukan secure code review dan threat modeling untuk aplikasi kritis",
            "Membangun dan mengelola AppSec program: policy, metrics, reporting",
            "Vulnerability management: triage, risk assessment, remediation tracking",
            "Security champions program: training dan mentoring dev team",
            "Incident response untuk application-layer security incidents",
            "Evaluasi dan implementasi security tools baru (WAF, RASP, API gateway)",
            "Compliance support: ISO 27001, PCI DSS, POJK keamanan siber"
        ],
        "benefits": [
            "Gaji kompetitif Rp 20-35 Juta + bonus performa",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "THR dan bonus tahunan",
            "Budget sertifikasi security (OffSec, SANS, GIAC) full covered",
            "Laptop high-spec disediakan",
            "Hybrid working fleksibel di Jakarta",
            "Exposure klien enterprise: banking, telco, e-commerce, gov",
            "Karir di perusahaan cybersecurity pure-play bereputasi"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/senior-application-security-engineer-at-phincon-4394434497",
        "source": "LinkedIn Indonesia",
        "source_url": "https://id.linkedin.com/jobs/view/senior-application-security-engineer-at-phincon-4394434497",
        "featured": False
    }
]

# Insert new jobs at the beginning of jobs array (after site config)
# Keep existing jobs, just prepend new ones
data['jobs'] = new_jobs + data['jobs']

# Write back
with open('/tmp/maulud-net/loker/lowongan.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_jobs)} new jobs to lowongan.json")
for i, job in enumerate(new_jobs, 1):
    print(f"  {i}. {job['title']} at {job['company']} - {job['source_url']}")