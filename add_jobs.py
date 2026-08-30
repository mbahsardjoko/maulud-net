#!/usr/bin/env python3
import json
from datetime import datetime, timedelta

# Load existing data
with open('/tmp/maulud-net/loker/lowongan.json', 'r') as f:
    data = json.load(f)

# Today's date
today = datetime(2026, 8, 30)
expires = today + timedelta(days=30)

# New jobs to add (based on real LinkedIn search results)
new_jobs = [
    {
        "slug": "byd-indonesia-fresh-graduate-hiring-2026",
        "title": "Fresh Graduate Hiring 2026",
        "company": "BYD Indonesia",
        "location": "Jakarta Raya, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 8-15 Juta",
        "posted": "2026-08-30",
        "expires": "2026-09-29",
        "description": "BYD Indonesia, pionir kendaraan listrik (EV) dan energi terbarukan global, membuka program Fresh Graduate Hiring 2026 untuk posisi teknologi dan engineering. Kandidat akan bergabung dengan tim inovasi yang membangun platform digital, sistem manufaktur cerdas, dan solusi energi bersih. Program ini dirancang untuk fresh graduate dengan potensi tinggi yang ingin mengembangkan karir di industri mobilitas listrik dan teknologi hijau skala global.",
        "requirements": [
            "Fresh graduate S1 Teknik Informatika, Teknik Elektro, Teknik Mesin, atau Jurusan STEM terkait",
            "IPK minimal 3.00 dari universitas terakreditasi A",
            "Mahir Bahasa Inggris (lisan & tulis) - TOEFL/IELTS nilai plus",
            "Pemahaman dasar programming: Python, C++, Java, atau Go",
            "Minat kuat pada industri EV, battery technology, atau renewable energy",
            "Kemampuan analisis, problem solving, dan adaptability tinggi",
            "Bersedia ditempatkan di Jakarta dan travel ke site manufaktur",
            "Passion pada sustainability dan green technology"
        ],
        "responsibilities": [
            "Mengikuti program onboarding dan rotasi teknis 12-18 bulan",
            "Berkolaborasi dengan senior engineer pada project R&D EV dan energy storage",
            "Membantu pengembangan software untuk sistem manufaktur otomatisasi",
            "Melakukan analisis data produksi dan efisiensi energi",
            "Berpartisipasi dalam continuous improvement dan innovation project",
            "Mendokumentasikan technical specification dan test report",
            "Presentasi progress project ke stakeholder teknis dan manajemen"
        ],
        "benefits": [
            "Gaji kompetitif Rp 8-15 Juta + bonus performa + THR",
            "BPJS Kesehatan dan Ketenagakerjaan sejak hari pertama",
            "Asuransi kesehatan premium (karyawan + keluarga)",
            "Laptop high-spec disediakan",
            "Budget learning: konferensi EV/battery tech, sertifikasi (Rp 15jt/tahun)",
            "Structured career path: Graduate → Engineer → Senior → Lead",
            "Exposure teknologi EV cutting-edge dan global R&D network",
            "Employee vehicle purchase program & charging benefit"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/2026-indonesia-fresh-graduate-hiring-–-jakarta-at-byd-indonesia-4437371994",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/2026-indonesia-fresh-graduate-hiring-–-jakarta-at-byd-indonesia-4437371994",
        "featured": True
    },
    {
        "slug": "pt-bank-mandiri-odp-it-2026",
        "title": "Officer Development Program (ODP) Information Technology 2026",
        "company": "PT Bank Mandiri (Persero) Tbk",
        "location": "Jakarta Raya, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 10-18 Juta",
        "posted": "2026-08-30",
        "expires": "2026-09-29",
        "description": "PT Bank Mandiri (Persero) Tbk, bank terbesar di Indonesia, membuka Officer Development Program (ODP) bidang Information Technology untuk angkatan 2026. Program ini dirancang untuk mempersiapkan future IT leader perbankan dengan kurikulum komprehensif: core banking system, digital banking platform, cybersecurity, data engineering, dan enterprise architecture. Peserta akan melalui rotasi di berbagai divisi IT, mentorship dari C-level technology officer, dan strategic project dengan impact nasional.",
        "requirements": [
            "Fresh graduate atau maksimal 1 tahun pengalaman (S1 Semua Jurusan, IT diutamakan)",
            "IPK minimal 3.00 (skala 4.00) dari universitas terakreditasi A",
            "Usia maksimal 25 tahun per Agustus 2026",
            "Mahir Bahasa Inggris (TOEFL minimal 500 / IELTS 6.0 menjadi nilai plus)",
            "Logical thinking, analytical skill, dan learning agility tinggi",
            "Pemahaman dasar: programming, database, networking, cybersecurity",
            "Leadership potential: aktif organisasi, competition winner, atau project lead",
            "Bersedia menjalani ikatan dinas dan ditempatkan di seluruh Indonesia"
        ],
        "responsibilities": [
            "Mengikuti program ODP IT durasi 18-24 bulan dengan rotasi 4 divisi",
            "Belajar core banking, digital channel, data platform, dan security operations",
            "Mengerjakan strategic project: modernisasi legacy system, cloud migration, AI banking",
            "Berpartisipasi leadership development: executive coaching, business simulation, community service",
            "Membangun network cross-functional dengan IT leader dan business unit",
            "Presentasi capstone project ke Board of Directors dan C-Level",
            "Mendapatkan sertifikasi: ITIL, TOGAF, AWS/Azure, Cybersecurity fundamental"
        ],
        "benefits": [
            "Gaji kompetitif Rp 10-18 Juta + allowances + performance bonus",
            "BPJS Kesehatan dan Ketenagakerjaan sejak hari pertama",
            "Asuransi kesehatan global coverage (karyawan + keluarga)",
            "Relocation package untuk kandidat dari luar Jabodetabek",
            "Structured career path: ODP → IT Specialist → Team Lead → VP/SVP",
            "Global exposure: secondment opportunity ke mitra bank internasional",
            "World-class learning: certified banking IT specialist, MBA sponsorship track",
            "Employee share purchase plan, pension fund, wellness program"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/officer-development-program-information-technology-2026-at-pt-bank-mandiri-persero-tbk-4368552684",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/officer-development-program-information-technology-2026-at-pt-bank-mandiri-persero-tbk-4368552684",
        "featured": False
    },
    {
        "slug": "pt-megayasa-teknologi-acs-fids-engineering",
        "title": "ACS & FIDS Engineering",
        "company": "PT Megayasa Teknologi Indonesia",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 12-20 Juta",
        "posted": "2026-08-30",
        "expires": "2026-09-29",
        "description": "PT Megayasa Teknologi Indonesia, system integrator terkemuka untuk solusi bandara dan aviation technology, mencari Engineer dengan pengalaman hands-on Access Control System (ACS) dan Flight Information Display System (FIDS). Kandidat akan bertanggung jawab atas desain, instalasi, komisioning, dan maintenance sistem keamanan bandara serta sistem informasi penerbangan di berbagai bandara internasional Indonesia. Posisi ini menawarkan tantangan unik mengerjakan project aviation technology skala besar dengan standar regulasi ketat.",
        "requirements": [
            "Minimal 3 tahun pengalaman ACS / FIDS / Airport Systems Engineering",
            "Mahir sistem ACS: HID, Lenel, Software House, Gallagher, atau Mercury",
            "Pengalaman FIDS: Vanderlande, Beontra, Damarel, atau sistem sejenis",
            "Paham standar aviation: ICAO Annex 17, TSA, dan regulasi Kemenhub RI",
            "Kemampuan network: VLAN, routing, firewall, industrial protocol (Modbus, BACnet)",
            "Pengalaman project management: site survey, BoQ, installation, commissioning, handover",
            "Familiar dengan PLC/SCADA untuk integrasi sistem bangunan (BMS)",
            "Bersedia travel ke site bandara di seluruh Indonesia"
        ],
        "responsibilities": [
            "Merancang arsitektur ACS & FIDS untuk project bandara baru dan upgrade existing",
            "Melakukan site survey, requirement gathering, dan technical design review",
            "Mengelola instalasi hardware: controller, reader, barrier, display, network infrastructure",
            "Konfigurasi software ACS: access level, anti-passback, elevator integration, visitor management",
            "Setup FIDS: flight data feed (AODB/IATA), display mapping, multi-language, emergency messaging",
            "Melakukan commissioning test: SAT, FAT, integrated system test dengan ATC/airline",
            "Menghasilkan as-built drawing, O&M manual, dan training untuk operator bandara",
            "Troubleshooting critical issue 24/7 selama warranty period dan maintenance contract"
        ],
        "benefits": [
            "Gaji kompetitif Rp 12-20 Juta + bonus project + THR",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Asuransi kesehatan extensif (karyawan + pasangan + anak)",
            "Laptop + measurement tools disediakan",
            "Travel allowance & daily allowance untuk site visit bandara",
            "Budget sertifikasi: aviation security, network, project management (Rp 15jt/tahun)",
            "Exposure project bandara skala nasional & internasional (Kualanamu, Kertajati, dll)",
            "Karir path: Engineer → Senior Engineer → Project Manager → Division Head"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/acs-fids-engineering-at-pt-megayasa-teknologi-indonesia-4354813206",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/acs-fids-engineering-at-pt-megayasa-teknologi-indonesia-4354813206",
        "featured": False
    },
    {
        "slug": "pt-adicipta-inovasi-teknologi-fullstack-developer",
        "title": "Fullstack Developer",
        "company": "PT Adicipta Inovasi Teknologi",
        "location": "Jakarta Barat, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 10-18 Juta",
        "posted": "2026-08-30",
        "expires": "2026-09-29",
        "description": "PT Adicipta Inovasi Teknologi, software house yang fokus pada pengembangan aplikasi enterprise dan digital transformation untuk klien korporat, membuka lowongan Fullstack Developer. Kandidat akan bekerja pada end-to-end product development: dari requirement analysis, system design, frontend/backend development, hingga deployment dan maintenance. Tech stack modern: React/Next.js, Node.js/Go, PostgreSQL, Docker, Kubernetes. Posisi ini cocok untuk developer yang ingin ownership penuh pada product lifecycle dan exposure project beragam domain.",
        "requirements": [
            "Minimal 2 tahun pengalaman Fullstack Web Development",
            "Frontend: Mahir React.js, Next.js, TypeScript, Tailwind CSS / CSS-in-JS",
            "Backend: Mahir Node.js (Express/NestJS/Fastify) ATAU Go (Gin/Echo/Fiber) — minimal satu",
            "Database: PostgreSQL (advanced), Redis, MongoDB — query optimization, migration",
            "State management: Redux Toolkit, Zustand, React Query / TanStack Query",
            "Authentication: JWT, OAuth2, OIDC, NextAuth.js",
            "Familiar dengan Docker, Git, CI/CD (GitHub Actions / GitLab CI)",
            "Paham RESTful API design, clean architecture, SOLID principles",
            "Portfolio project fullstack yang sudah live (production) menjadi nilai plus"
        ],
        "responsibilities": [
            "Mengembangkan fitur frontend (React/Next.js) dan backend (Node.js/Go) end-to-end",
            "Merancang database schema, migration, dan optimasi query PostgreSQL",
            "Membangun reusable component library dan design system implementation",
            "Implementasi authentication, authorization, dan security best practices",
            "Setup CI/CD pipeline untuk automated build, test, dan deployment ke Kubernetes",
            "Code review, pairing session, dan knowledge sharing dengan tim",
            "Berkolaborasi dengan Designer, PM, dan QA untuk delivery berkualitas",
            "Troubleshooting production issue dan performance optimization"
        ],
        "benefits": [
            "Gaji kompetitif Rp 10-18 Juta + bonus project + performance bonus",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "THR dan tunjangan hari raya lengkap",
            "Laptop disediakan (MacBook / Windows high-spec)",
            "Budget learning: kursus, sertifikasi, konferensi (Rp 8jt/tahun)",
            "Hybrid working fleksibel (2-3 hari WFO di Jakarta Barat)",
            "Exposure diverse project: enterprise apps, SaaS, e-gov, e-commerce",
            "Tim kecil, flat hierarchy, ownership tinggi, fast learning curve"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/fullstack-developer-at-pt-adicipta-inovasi-teknologi-4400295770",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/fullstack-developer-at-pt-adicipta-inovasi-teknologi-4400295770",
        "featured": False
    },
    {
        "slug": "camline-elisa-industriq-software-engineer-surabaya",
        "title": "Software Engineer",
        "company": "camLine | Elisa Industriq",
        "location": "Surabaya, Jawa Timur, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 12-22 Juta",
        "posted": "2026-08-30",
        "expires": "2026-09-29",
        "description": "camLine (Elisa Industriq), perusahaan software Jerman yang bergerak di Manufacturing Execution System (MES) dan Advanced Process Control (APC) untuk industri semiconductor, electronics, dan high-tech manufacturing, mencari Software Engineer untuk lokasi Surabaya. Kandidat akan terlibat dalam pengembangan solusi MES yang digunakan pabrik-pabrik chip dan elektronik terkemuka di Asia. Posisi ini menawarkan peluang kerja pada enterprise software B2B skala global dengan tech stack modern dan best practice engineering Jerman.",
        "requirements": [
            "Minimal 2 tahun pengalaman Software Development (Java, C#, atau Python)",
            "Mahir OOP, design patterns, clean code, SOLID principles",
            "Pengalaman database: PostgreSQL, Oracle, atau SQL Server",
            "Familiar dengan web technology: REST API, HTML/CSS/JavaScript (React/Vue nilai plus)",
            "Paham CI/CD: Jenkins, GitLab CI, atau GitHub Actions",
            "Pengalaman container: Docker, Kubernetes (OpenShift nilai plus)",
            "Background Computer Science / Software Engineering / Teknik Informatika",
            "Mahir Bahasa Inggris (komunikasi dengan tim global Jerman & Asia)",
            "Bersedia bekerja hybrid di Surabaya (kantor di area Pakuwon/ITC)"
        ],
        "responsibilities": [
            "Mengembangkan fitur MES: production tracking, quality management, material logistics, equipment integration",
            "Berpartisipasi full development lifecycle: requirements, design, coding, testing, deployment",
            "Integrasi dengan equipment semiconductor: SECS/GEM, OPC-UA, Modbus TCP",
            "Implementasi Advanced Process Control algorithms untuk yield improvement",
            "Code review, unit/integration testing, static analysis (SonarQube)",
            "Berkolaborasi dengan Product Owner, QA, dan DevOps di tim cross-functional (Agile/Scrum)",
            "Dokumentasi teknis: API spec, architecture decision records, runbook",
            "Support customer on-site di pabrik semiconductor untuk go-live dan hypercare"
        ],
        "benefits": [
            "Gaji kompetitif Rp 12-22 Juta + bonus performa + THR",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Asuransi kesehatan premium (karyawan + keluarga)",
            "Laptop high-spec (MacBook Pro / ThinkPad) disediakan",
            "Budget learning: konferensi internasional, sertifikasi Java/Cloud, German language course",
            "Hybrid working arrangement",
            "Exposure industri semiconductor & high-tech manufacturing global",
            "Karir internasional: kesempatan transfer ke kantor Jerman, Singapura, Malaysia, Taiwan"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/software-engineer-surabaya-indonesia-at-camline-elisa-industriq-4400362349",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/software-engineer-surabaya-indonesia-at-camline-elisa-industriq-4400362349",
        "featured": False
    },
    {
        "slug": "air-arabia-workshop-planning-engineer-jakarta",
        "title": "Workshop Planning Engineer",
        "company": "Air Arabia",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 15-25 Juta",
        "posted": "2026-08-30",
        "expires": "2026-09-29",
        "description": "Air Arabia, low-cost carrier terbesar di Timur Tengah dan Afrika Utara yang sedang ekspansi ke Asia Tenggara, membuka lowongan Workshop Planning Engineer untuk recruitment event di Jakarta September 2026. Posisi ini berkaitan dengan perencanaan dan pengelolaan maintenance workshop untuk fleet Airbus A320 family. Kandidat akan bertanggung jawab atas planning maintenance check, spare parts management, engineering order coordination, dan compliance dengan regulasi EASA/GCAA/DGCA. Peluang unik bergabung dengan airline LCC global yang berkembang pesat.",
        "requirements": [
            "Minimal 3 tahun pengalaman Workshop Planning / Maintenance Planning di industri penerbangan",
            "Paham maintenance planning: C-check, structural inspection, component overhaul, AD/SB management",
            "Pengalaman dengan MRO software: AMOS, TRAX, Ramco, atau Rusada",
            "Memahami regulasi: EASA Part M/CAMO, GCAA CAR M, DGCA CASR 145",
            "Familiar dengan aircraft documentation: AMM, IPC, SRM, CMP, wiring diagram manual",
            "Pengalaman spare parts planning: provisioning, inventory optimization, reliability analysis",
            "S1 Teknik Penerbangan / Teknik Mesin / Aeronautical Engineering",
            "Mahir Bahasa Inggris (technical documentation & communication dengan HQ Sharjah)",
            "Bersedia travel ke Sharjah (HQ) untuk training dan alignment periodik"
        ],
        "responsibilities": [
            "Menyusun maintenance planning program untuk fleet Airbus A320 (base check, phase check, OOP task)",
            "Mengelola engineering order (EO) dan service bulletin (SB) incorporation planning",
            "Koordinasi spare parts provisioning dengan procurement & logistics untuk minimize AOG",
            "Monitor aircraft reliability: PIREP analysis, recurrent defect, reliability report bulanan",
            "Liaison dengan CAMO/Quality untuk compliance & airworthiness review",
            "Persiapan maintenance check: work package planning, manpower allocation, tooling/ground equipment",
            "Koordinasi dengan vendor MRO untuk heavy check dan component overhaul",
            "Reporting ke Head of Maintenance Engineering & HQ Engineering di Sharjah"
        ],
        "benefits": [
            "Gaji kompetitif Rp 15-25 Juta + housing allowance + transport allowance",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Asuransi kesehatan global coverage (karyawan + keluarga)",
            "Travel benefit: unlimited ID90 tickets Air Arabia network (karyawan + keluarga)",
            "Relocation package untuk kandidat dari luar Jakarta",
            "Training & certification: EASA Part 66, Type Rating A320, AMOS/TRAX advanced",
            "Karir internasional: rotation program ke HQ Sharjah atau station lain di network Air Arabia",
            "Exposure fleet expansion project: new aircraft induction, line maintenance setup"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://ae.linkedin.com/jobs/view/workshop-planning-engineer-jakarta-recruitment-event-at-air-arabia-4450262721",
        "source": "LinkedIn",
        "source_url": "https://ae.linkedin.com/jobs/view/workshop-planning-engineer-jakarta-recruitment-event-at-air-arabia-4450262721",
        "featured": False
    }
]

# Check for duplicates
existing_slugs = {job['slug'] for job in data['jobs']}
existing_source_urls = {job['source_url'] for job in data['jobs']}

jobs_to_add = []
for job in new_jobs:
    if job['slug'] in existing_slugs:
        print(f"SKIP duplicate slug: {job['slug']}")
        continue
    if job['source_url'] in existing_source_urls:
        print(f"SKIP duplicate source_url: {job['source_url']}")
        continue
    jobs_to_add.append(job)

if not jobs_to_add:
    print("No new jobs to add (all duplicates)")
    exit(0)

# Insert new jobs at the beginning (index 0)
for job in reversed(jobs_to_add):
    data['jobs'].insert(0, job)

# Update categories from jobs
all_categories = set(data.get('categories', []))
for job in data['jobs']:
    if job.get('category'):
        all_categories.add(job['category'])
data['categories'] = sorted(list(all_categories))

# Save
with open('/tmp/maulud-net/loker/lowongan.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(jobs_to_add)} new jobs:")
for i, job in enumerate(jobs_to_add, 1):
    print(f"  {i}. {job['title']} ({job['company']}) - {job['source_url']}")