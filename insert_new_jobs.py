#!/usr/bin/env python3
"""Insert new jobs at index 0 of lowongan.json jobs array."""
import json
from datetime import datetime, timedelta

with open('loker/lowongan.json', 'r') as f:
    data = json.load(f)

today = datetime(2026, 7, 6)
posted = today.strftime("%Y-%m-%d")
expires = (today + timedelta(days=30)).strftime("%Y-%m-%d")

new_jobs = [
    {
        "slug": "back-end-engineer-lingotalk",
        "title": "Back-end Engineer",
        "company": "LingoTalk",
        "location": "Jakarta",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 12-22 Juta",
        "posted": posted,
        "expires": expires,
        "description": "LingoTalk, platform pembelajaran bahasa terkemuka di Asia Tenggara, sedang mencari Back-end Engineer berbakat untuk bergabung dengan tim engineering mereka di Jakarta. Kamu akan bertanggung jawab merancang, membangun, dan memelihara layanan back-end yang scalable menggunakan teknologi modern. Posisi ini cocok untuk engineer yang suka tantangan arsitektur sistem dan ingin berdampak pada produk yang digunakan ribuan pelajar bahasa.",
        "requirements": [
            "Pengalaman minimal 2+ tahun dalam pengembangan back-end atau full-stack",
            "Berbasis di Jakarta, lancar berbahasa Inggris dan Bahasa Indonesia",
            "Nyaman bekerja langsung dengan leadership di lingkungan fast-paced",
            "Mahir dalam bahasa pemrograman seperti Go, Python, atau Node.js",
            "Pengalaman dengan database relasional (PostgreSQL/MySQL) dan NoSQL",
            "Paham desain RESTful API dan arsitektur microservices",
            "Familiar dengan Git dan workflow kolaboratif tim"
        ],
        "responsibilities": [
            "Mengembangkan dan memelihara layanan back-end untuk platform LingoTalk",
            "Merancang arsitektur sistem yang scalable dan maintainable",
            "Berkolaborasi dengan tim frontend, mobile, dan product dalam pengembangan fitur",
            "Mengimplementasikan best practices keamanan dan validasi data",
            "Memastikan kinerja tinggi dan uptime layanan",
            "Berpartisipasi dalam code review dan diskusi teknis"
        ],
        "benefits": [
            "Gaji kompetitif sesuai industri edtech",
            "BPJS Ketenagakerjaan dan Kesehatan",
            "Flexible working hours",
            "Budget pembelajaran dan sertifikasi teknologi",
            "Laptop dan peralatan kerja disediakan",
            "Lingkungan kerja yang mendukung pertumbuhan bahasa dan teknologi"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan Back-end Engineer di LingoTalk. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/back-end-engineer-at-lingotalk-4354850416",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/back-end-engineer-at-lingotalk-4354850416",
        "featured": True
    },
    {
        "slug": "ml-engineer-pt-astra-international-tbk",
        "title": "ML Engineer",
        "company": "PT Astra International Tbk",
        "location": "Jakarta",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 15-25 Juta",
        "posted": posted,
        "expires": expires,
        "description": "PT Astra International Tbk, salah satu konglomerat terbesar di Indonesia, membuka lowongan ML Engineer untuk bergabung dengan tim data science dan AI mereka di Jakarta. Posisi ini strategis dalam mengembangkan solusi machine learning yang mendukung berbagai bisnis unit Astra, dari otomotif, keuangan, hingga properti. Kamu akan bekerja pada proyek-proyek nyata dengan dampak bisnis yang signifikan di skala nasional.",
        "requirements": [
            "Pengalaman minimal 3 tahun sebagai ML Engineer atau Data Scientist",
            "Mahir dalam Python dan framework ML (TensorFlow, PyTorch, scikit-learn)",
            "Pengalaman dengan MLOps, model deployment, dan CI/CD untuk ML",
            "Paham konsep deep learning, NLP, computer vision, atau time series",
            "Pengalaman dengan cloud platform (AWS/GCP/Azure) dan containerization",
            "Kemampuan komunikasi baik untuk kolaborasi lintas tim bisnis dan teknis",
            "Lulusan S1/S2 Ilmu Komputer, Statistik, Matematika, atau bidang terkait"
        ],
        "responsibilities": [
            "Merancang, mengembangkan, dan mendeploy model machine learning ke production",
            "Membangun pipeline data dan MLOps yang robust dan scalable",
            "Berkolaborasi dengan stakeholder bisnis untuk mengidentifikasi use case ML",
            "Mengoptimalkan performa model dan monitoring di production",
            "Melakukan riset dan eksperimen teknik ML terbaru untuk problem solving",
            "Mendokumentasikan proses development dan best practices ML"
        ],
        "benefits": [
            "Gaji kompetitif dengan bonus performa",
            "BPJS Ketenagakerjaan dan Kesehatan lengkap",
            "Asuransi kesehatan tambahan",
            "International working environment di konglomerat terkemuka",
            "Kesempatan belajar dan pelatihan AI/ML",
            "Flexible hybrid working arrangement",
            "MacBook Pro dan peralatan kerja disediakan"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan ML Engineer di PT Astra International Tbk. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/ml-engineer-at-pt-astra-international-tbk-4069505789",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/ml-engineer-at-pt-astra-international-tbk-4069505789",
        "featured": False
    },
    {
        "slug": "product-manager-pintarnya",
        "title": "Product Manager",
        "company": "Pintarnya",
        "location": "Jakarta Raya",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 18-30 Juta",
        "posted": posted,
        "expires": expires,
        "description": "Pintarnya, platform edukasi teknologi yang berkembang pesat, mencari Product Manager yang exceptional untuk mengambil kepemilikan visi, strategi, dan eksekusi produk mereka di Jakarta. Sebagai PM, kamu akan menjadi jembatan antara kebutuhan user, kendala teknis, tujuan bisnis, dan dinamika pasar. Posisi ini menawarkan otonomi tinggi dan dampak langsung pada produk yang digunakan ribuan pelajar.",
        "requirements": [
            "Pengalaman 3-5 tahun sebagai Product Manager di produk tech/konsumer",
            "Track record mengelola siklus hidup produk dari ide sampe launch",
            "Kemampuan analisis data dan pengambilan keputusan berbasis data",
            "Paham metodologi agile, user research, dan product discovery",
            "Kemampuan komunikasi dan stakeholder management yang kuat",
            "Background teknis (CS/Engineering) menjadi nilai plus",
            "Passion di industri edtech dan pembelajaran digital"
        ],
        "responsibilities": [
            "Merencanakan dan mengeksekusi strategi produk sesuai visi perusahaan",
            "Mengelola product backlog, prioritisasi fitur, dan roadmap",
            "Berkolaborasi dengan tim engineering, design, data, dan marketing",
            "Melakukan user research, analisis metrik, dan kompetitor research",
            "Mendefinisikan KPI produk dan memantau performa secara berkala",
            "Memfasilitasi sprint planning, review, dan retrospective"
        ],
        "benefits": [
            "Gaji kompetitif dengan bonus performa",
            "BPJS Ketenagakerjaan dan Kesehatan",
            "Budget iklan untuk eksperimen growth",
            "Flexible work arrangement",
            "MacBook Pro disediakan",
            "Akses gratis ke platform Pintarnya",
            "Budget untuk pengembangan diri dan kursus"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan Product Manager di Pintarnya. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/product-manager-at-pintarnya-4406922507",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/product-manager-at-pintarnya-4406922507",
        "featured": False
    },
    {
        "slug": "infrastructure-engineer-duitku",
        "title": "Infrastructure Engineer",
        "company": "Duitku",
        "location": "Area DKI Jakarta",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 15-25 Juta",
        "posted": posted,
        "expires": expires,
        "description": "Duitku, payment gateway terkemuka di Indonesia, mencari Infrastructure Engineer untuk mengelola dan mengoptimalkan infrastruktur cloud mereka yang melayani jutaan transaksi. Posisi ini fokus pada reliability, scalability, dan security dari sistem pembayaran yang kritis. Kamu akan bekerja dengan tim engineering berbakat di lingkungan fintech yang fast-paced dan high-availability.",
        "requirements": [
            "Pengalaman minimal 2+ tahun sebagai Infrastructure/DevOps/SRE Engineer",
            "Mahir dengan cloud platform (AWS/GCP/Azure) dan Infrastructure as Code (Terraform)",
            "Pengalaman dengan Kubernetes, Docker, dan container orchestration",
            "Paham CI/CD pipeline, monitoring (Prometheus/Grafana), dan logging",
            "Pengalaman dengan database, caching, dan message queue systems",
            "Familiar dengan security best practices dan compliance (PCI-DSS nilai plus)",
            "Kemampuan troubleshooting sistem distributed yang kompleks"
        ],
        "responsibilities": [
            "Mengelola dan mengoptimalkan infrastruktur cloud Duitku",
            "Membangun dan memelihara CI/CD pipeline untuk deployment otomatis",
            "Mengimplementasikan monitoring, alerting, dan incident response",
            "Merancang arsitektur sistem yang high-availability dan scalable",
            "Berkolaborasi dengan tim backend untuk optimasi performa infrastruktur",
            "Memastikan compliance dan keamanan infrastruktur pembayaran"
        ],
        "benefits": [
            "Gaji kompetitif dengan bonus performa",
            "BPJS Ketenagakerjaan dan Kesehatan lengkap",
            "Asuransi kesehatan swasta",
            "Flexible hybrid work arrangement",
            "Budget untuk kursus dan sertifikasi cloud/DevOps",
            "MacBook Pro dan peralatan kerja disediakan",
            "Akses ke teknologi fintech terkini"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan Infrastructure Engineer di Duitku. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/infrastructure-engineer-at-duitku-4339027236",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/infrastructure-engineer-at-duitku-4339027236",
        "featured": False
    },
    {
        "slug": "sales-manager-ming-yang-smart-energy",
        "title": "Indonesia Sales Manager",
        "company": "Ming Yang Smart Energy",
        "location": "Jakarta Raya",
        "type": "Full-time",
        "category": "Marketing",
        "salary": "Rp 20-35 Juta",
        "posted": posted,
        "expires": expires,
        "description": "Ming Yang Smart Energy, perusahaan energi terbarukan global yang berfokus pada turbin angin dan sistem tenaga surya, mencari Indonesia Sales Manager untuk memimpin ekspansi pasar mereka di Indonesia. Posisi ini berbasis di Jakarta Raya dan bertanggung jawab mengembangkan strategi penjualan, membangun relasi dengan klien kunci (EPC, developer, utility), dan mengeksekusi deal untuk proyek pembangkit listrik terbarukan skala besar.",
        "requirements": [
            "Pengalaman minimal 5+ tahun sales di industri energi terbarukan/renewable energy",
            "Network kuat di industri listrik Indonesia (PLN, IPP, EPC, developer)",
            "Track record menangani proyek besar (utility-scale wind/solar)",
            "Paham regulasi energi Indonesia (RUPTL, EBT, izin proyek)",
            "Kemampuan negosiasi dan closing deal kompleks",
            "Bahasa Inggris aktif (lisan dan tulisan) - wajib",
            "Bersedia travel dalam dan luar kota untuk meeting klien"
        ],
        "responsibilities": [
            "Mengembangkan dan mengeksekusi strategi sales untuk pasar Indonesia",
            "Membangun dan memelihara relasi dengan key decision makers",
            "Mengidentifikasi peluang proyek baru dan mengelola pipeline sales",
            "Memimpin proses tender, proposal, dan negosiasi kontrak",
            "Berkolaborasi dengan tim teknis global untuk solution selling",
            "Melaporkan forecast sales dan aktivitas ke regional HQ"
        ],
        "benefits": [
            "Gaji kompetitif + komisi penjualan yang menarik",
            "BPJS Ketenagakerjaan dan Kesehatan",
            "Asuransi kesehatan swasta",
            "Company car dan allowance transportasi",
            "International working environment di perusahaan global",
            "Kesempatan training dan sertifikasi industri energi",
            "Flexible working arrangement"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan Indonesia Sales Manager di Ming Yang Smart Energy. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/indonesia-sales-manager-at-ming-yang-smart-energy-4317765282",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/indonesia-sales-manager-at-ming-yang-smart-energy-4317765282",
        "featured": False
    }
]

# Insert at index 0 (newest first)
data['jobs'] = new_jobs + data['jobs']

with open('loker/lowongan.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Successfully inserted {len(new_jobs)} new jobs at index 0")
for job in new_jobs:
    print(f"  - {job['title']} at {job['company']} ({job['source_url']})")