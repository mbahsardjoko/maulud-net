#!/usr/bin/env python3
"""Add new job postings to loker/lowongan.json (batch 2026-08-11)."""
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE / 'loker' / 'lowongan.json'

NEW_JOBS = [
    {
        "slug": "product-manager-infinid-indonesia",
        "title": "Product Manager",
        "company": "Infinid Indonesia",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 10-18 Juta",
        "posted": "2026-08-11",
        "expires": "2026-09-10",
        "description": "Infinid Indonesia, perusahaan fintech yang membantu pemilik rumah mengakses kekayaan properti mereka lewat HELOC (Home Equity Line of Credit), sedang membuka posisi Product Manager. Kamu akan bertanggung jawab mendefinisikan dan memprioritaskan fitur serta kebutuhan produk agar sesuai dengan tujuan strategis perusahaan. Peran ini cocok untuk kamu yang paham agile methodology, punya kemampuan komunikasi yang kuat, dan teliti terhadap detail.",
        "requirements": [
            "Minimal 3 tahun pengalaman sebagai Product Manager atau peran produk sejenis",
            "Paham agile methodologies (Scrum/Kanban) dan product lifecycle",
            "Kemampuan menulis PRD, user stories, dan product requirement document",
            "Strong analytical thinking dan data-driven decision making",
            "Komunikasi yang baik untuk berkolaborasi lintas tim (engineering, design, business)",
            "Pengalaman di industri fintech atau produk keuangan lebih disukai",
            "Familiar dengan tools product management seperti Jira, Notion, atau Trello",
            "Kemampuan prioritisasi roadmap dan manajemen stakeholder",
            "Bersedia bekerja onsite/hybrid di Jakarta"
        ],
        "responsibilities": [
            "Mendefinisikan dan memprioritaskan fitur serta requirements produk",
            "Menyusun dan mengelola product roadmap sesuai tujuan bisnis",
            "Melakukan riset pasar, kompetitor, dan kebutuhan pengguna",
            "Berkolaborasi dengan engineering, design, dan stakeholder untuk delivery fitur",
            "Memantau metrik produk dan menyusun insight untuk iterasi",
            "Memastikan kualitas produk sesuai kebutuhan customer dan strategi perusahaan",
            "Mengelola backlog dan prioritisasi sprint bersama tim"
        ],
        "benefits": [
            "Gaji kompetitif Rp 10-18 Juta sesuai pengalaman",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Kesempatan berkembang di perusahaan fintech yang sedang bertumbuh",
            "Lingkungan kerja kolaboratif dan dinamis",
            "Pengalaman produk fintech yang berdampak nyata",
            "Kesempatan belajar dan development skill produk"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/product-manager-at-infinid-indonesia-3968791430",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/product-manager-at-infinid-indonesia-3968791430",
        "featured": True
    },
    {
        "slug": "junior-product-manager-verihubs",
        "title": "Junior Product Manager",
        "company": "Verihubs",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 7-12 Juta",
        "posted": "2026-08-11",
        "expires": "2026-09-10",
        "description": "Verihubs, perusahaan penyedia solusi verifikasi identitas berbasis AI untuk kebutuhan KYC, membuka kesempatan bagi Junior Product Manager. Kamu akan bekerja sama dengan tim untuk mengelola project, mendukung pengembangan produk, dan menyelesaikan tantangan nyata di lapangan. Posisi ini cocok untuk kamu yang ingin membangun karier di product management dengan exposure teknologi AI dan identity verification.",
        "requirements": [
            "Minimal 1 tahun pengalaman di product management, project management, atau peran terkait",
            "Familiar dengan product development lifecycle dan tools manajemen project",
            "Kemampuan analisis dan komunikasi yang baik",
            "Detail-oriented dan mampu memprioritaskan pekerjaan",
            "Tertarik dengan teknologi AI, fintech, dan identity verification",
            "Mampu bekerja dalam tim yang dinamis dan cepat bergerak",
            "Bersedia bekerja di Jakarta"
        ],
        "responsibilities": [
            "Mengelola dan mendukung pengembangan produk end-to-end",
            "Berkolaborasi dengan engineering dan stakeholder untuk delivery fitur",
            "Mengumpulkan dan menganalisis data untuk mendukung keputusan produk",
            "Menyusun dokumentasi produk dan user stories",
            "Melakukan riset pengguna dan kompetitor secara berkala",
            "Memantau performa fitur dan menyusun rekomendasi perbaikan"
        ],
        "benefits": [
            "Gaji kompetitif Rp 7-12 Juta sesuai pengalaman",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Kesempatan belajar teknologi AI dan verifikasi identitas",
            "Lingkungan kerja startup yang dinamis dan suportif",
            "Pengembangan karier product management yang jelas",
            "Tim kolaboratif dengan mentorship dari product senior"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://www.linkedin.com/jobs/view/4021404120",
        "source": "LinkedIn",
        "source_url": "https://www.linkedin.com/jobs/view/4021404120",
        "featured": False
    },
    {
        "slug": "ui-ux-designer-kredivo-group",
        "title": "UI/UX Designer",
        "company": "Kredivo Group",
        "location": "DKI Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Desain",
        "salary": "Rp 9-16 Juta",
        "posted": "2026-08-11",
        "expires": "2026-09-10",
        "description": "Kredivo Group, salah satu platform kredit digital terkemuka di Indonesia, membuka lowongan UI/UX Designer untuk bergabung dengan tim design yang berfokus pada produk fintech. Kamu akan merancang pengalaman pengguna yang intuitif untuk aplikasi dan layanan digital yang digunakan jutaan pengguna. Posisi ini cocok untuk designer yang passionate terhadap user-centered design dan ingin berdampak besar di industri fintech.",
        "requirements": [
            "Minimal 2 tahun pengalaman sebagai UI/UX Designer atau Product Designer",
            "Portfolio yang menunjukkan kemampuan design produk web maupun mobile",
            "Mahir menggunakan Figma, Sketch, atau Adobe XD",
            "Paham user research, wireframing, prototyping, dan usability testing",
            "Memahami design system dan component-based design",
            "Familiar dengan prinsip aksesibilitas dan mobile design guidelines",
            "Kemampuan komunikasi untuk kolaborasi dengan product dan engineering",
            "Bersedia bekerja di area DKI Jakarta"
        ],
        "responsibilities": [
            "Merancang UI/UX untuk produk fintech Kredivo Group",
            "Membuat wireframes, mockups, dan interactive prototypes",
            "Melakukan user research dan usability testing untuk validasi desain",
            "Menjaga konsistensi desain melalui design system",
            "Berkolaborasi dengan tim product dan engineering untuk implementasi",
            "Iterasi desain berdasarkan feedback pengguna dan data",
            "Menyajikan design solution kepada stakeholders"
        ],
        "benefits": [
            "Gaji kompetitif Rp 9-16 Juta sesuai pengalaman",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Produk fintech dengan skala pengguna jutaan orang",
            "Tim design kolaboratif dan budaya feedback yang sehat",
            "Kesempatan belajar dan berkembang di industri fintech",
            "Fasilitas kantor modern di Jakarta"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/ui-ux-designer-at-kredivo-group-4376061119",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/ui-ux-designer-at-kredivo-group-4376061119",
        "featured": False
    },
    {
        "slug": "devops-engineer-pt-siaga-abdi-utama",
        "title": "DevOps Engineer",
        "company": "PT Siaga Abdi Utama",
        "location": "Jakarta Raya, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 10-18 Juta",
        "posted": "2026-08-11",
        "expires": "2026-09-10",
        "description": "PT Siaga Abdi Utama, perusahaan solusi Human Resource yang telah berdiri sejak 2011, sedang mencari DevOps Engineer untuk menjaga sistem enterprise berjalan lancar, aman, dan efisien. Kamu akan menangani infrastruktur, otomatisasi deployment, dan monitoring layanan di lingkungan production. Posisi ini cocok untuk profesional DevOps yang detail-oriented dan senang memecahkan masalah teknis yang kompleks.",
        "requirements": [
            "Minimal 2 tahun pengalaman sebagai DevOps Engineer, Cloud Engineer, atau SRE",
            "Paham CI/CD pipeline menggunakan Jenkins, GitLab CI, atau GitHub Actions",
            "Pengalaman dengan containerization dan orchestration (Docker, Kubernetes)",
            "Familiar dengan cloud platform (AWS, GCP, atau Azure)",
            "Paham infrastructure as code (Terraform, Ansible, atau CloudFormation)",
            "Pengalaman monitoring dan logging (Prometheus, Grafana, ELK Stack)",
            "Kemampuan scripting dengan Bash, Python, atau Go",
            "Paham konsep networking, security, dan sistem Linux",
            "Bersedia bekerja onsite/hybrid di Jakarta"
        ],
        "responsibilities": [
            "Mengelola dan mengoptimasi infrastruktur production enterprise systems",
            "Membangun dan memelihara pipeline CI/CD untuk deployment otomatis",
            "Memonitor kesehatan sistem dan menangani insiden secara proaktif",
            "Mengimplementasikan security best practices pada infrastruktur",
            "Mengotomatisasi provisioning dan konfigurasi infrastruktur",
            "Berkolaborasi dengan tim development untuk reliability dan performance",
            "Mendokumentasikan konfigurasi dan prosedur operasional",
            "Melakukan capacity planning dan cost optimization"
        ],
        "benefits": [
            "Gaji kompetitif Rp 10-18 Juta sesuai pengalaman",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Pengalaman menangani sistem enterprise skala besar",
            "Kesempatan belajar teknologi cloud dan automation terbaru",
            "Lingkungan kerja profesional dan suportif",
            "Pengembangan karier di bidang DevOps dan cloud engineering"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/devops-engineer-at-pt-siaga-abdi-utama-4382773351",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/devops-engineer-at-pt-siaga-abdi-utama-4382773351",
        "featured": False
    },
    {
        "slug": "back-end-developer-node-js-vascomm",
        "title": "Back End Developer (Node.Js)",
        "company": "Vascomm",
        "location": "Sidoarjo, Jawa Timur, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 8-15 Juta",
        "posted": "2026-08-11",
        "expires": "2026-09-10",
        "description": "Vascomm Solusi Teknologi, perusahaan teknologi yang berfokus pada solusi inovatif di bidang IT, software development, dan digital ecosystem, membuka lowongan Back End Developer (Node.Js) dengan working arrangement hybrid di Sidoarjo. Kamu akan mengembangkan dan memelihara aplikasi backend menggunakan NodeJS, serta mengimplementasikan arsitektur microservices untuk memastikan skalabilitas dan fleksibilitas sistem.",
        "requirements": [
            "Minimal 2 tahun pengalaman sebagai Back End Developer",
            "Mahir menggunakan Node.js (Express, NestJS, atau sejenisnya)",
            "Paham arsitektur microservices dan RESTful API design",
            "Pengalaman dengan database SQL dan NoSQL (PostgreSQL, MySQL, MongoDB)",
            "Familiar dengan Git dan workflow pengembangan tim",
            "Memahami konsep caching (Redis) dan message queue",
            "Paham testing backend (unit test dan integration test)",
            "Kemampuan troubleshooting dan debugging yang baik",
            "Bersedia bekerja hybrid di Sidoarjo"
        ],
        "responsibilities": [
            "Mengembangkan dan memelihara aplikasi backend menggunakan NodeJS",
            "Mengimplementasikan arsitektur microservices untuk skalabilitas sistem",
            "Merancang dan mengelola API untuk kebutuhan aplikasi",
            "Mengoptimasi performa dan keamanan backend services",
            "Melakukan code review dan menjaga kualitas codebase",
            "Berkolaborasi dengan frontend developer dan tim product",
            "Menulis dokumentasi teknis dan API documentation",
            "Menangani bug dan issue production dengan cepat"
        ],
        "benefits": [
            "Gaji kompetitif Rp 8-15 Juta sesuai pengalaman",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Working arrangement hybrid (Sidoarjo)",
            "Kesempatan mengerjakan berbagai project digital yang menantang",
            "Lingkungan kerja kolaboratif di perusahaan teknologi",
            "Pengembangan karier dan pembelajaran teknologi terbaru"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/back-end-developer-node-js-at-vascomm-4348220100",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/back-end-developer-node-js-at-vascomm-4348220100",
        "featured": False
    },
    {
        "slug": "graphic-designer-hire-digital",
        "title": "Graphic Designer",
        "company": "Hire Digital",
        "location": "Remote (Indonesia)",
        "type": "Full-time",
        "category": "Desain",
        "salary": "Rp 6-10 Juta",
        "posted": "2026-08-11",
        "expires": "2026-09-10",
        "description": "Hire Digital sedang mencari Graphic Designer untuk mendukung redesign dan peningkatan marketing serta commercial collateral. Kamu akan membuat berbagai aset visual untuk kebutuhan brand dan campaign digital. Posisi ini cocok untuk graphic designer kreatif yang bisa bekerja remote dari Indonesia dan memiliki portofolio desain yang kuat.",
        "requirements": [
            "Minimal 1-2 tahun pengalaman sebagai Graphic Designer",
            "Portfolio yang menunjukkan kemampuan desain marketing dan brand collateral",
            "Mahir menggunakan Adobe Creative Suite (Photoshop, Illustrator, InDesign) atau Figma",
            "Paham prinsip desain, tipografi, dan color theory",
            "Mampu membuat desain untuk kebutuhan digital dan print",
            "Detail-oriented dan mampu bekerja dengan deadline",
            "Kemampuan komunikasi untuk kolaborasi remote dengan tim",
            "Bersedia bekerja remote dari Indonesia"
        ],
        "responsibilities": [
            "Mendesain marketing dan commercial collateral untuk berbagai campaign",
            "Membuat aset visual untuk media sosial, website, dan materi pemasaran",
            "Melakukan redesign dan peningkatan kualitas material brand",
            "Berkolaborasi dengan tim marketing dan content untuk kebutuhan desain",
            "Menjaga konsistensi brand identity di semua aset visual",
            "Mengelola dan mengorganisir file desain dengan rapi",
            "Menyelesaikan revisi desain sesuai feedback dengan cepat"
        ],
        "benefits": [
            "Gaji kompetitif Rp 6-10 Juta sesuai pengalaman",
            "Full remote working - kerja dari mana saja di Indonesia",
            "Kesempatan mengerjakan project untuk klien global",
            "Lingkungan kerja fleksibel dan kolaboratif",
            "Pengembangan karier di bidang design dan branding",
            "Portfolio yang beragam untuk pengembangan profesional"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/graphic-designer-at-digital-4416476987",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/graphic-designer-at-digital-4416476987",
        "featured": False
    }
]

with open(DB_PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Dedup check against existing slugs
existing_slugs = {j['slug'] for j in data['jobs']}
new_jobs = [j for j in NEW_JOBS if j['slug'] not in existing_slugs]
print(f'New jobs to add: {len(new_jobs)} (skipped dups: {len(NEW_JOBS) - len(new_jobs)})')

data['jobs'] = new_jobs + data['jobs']

# Ensure categories always a non-null array
cats = sorted({j.get('category') for j in data['jobs'] if j.get('category')})
data['categories'] = cats

with open(DB_PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

print(f"OK: added {len(new_jobs)} jobs. Total jobs: {len(data['jobs'])}")
for j in new_jobs:
    print(f"- {j['title']} @ {j['company']} ({j['source_url']})")