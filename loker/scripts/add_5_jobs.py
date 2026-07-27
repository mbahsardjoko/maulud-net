#!/usr/bin/env python3
"""Add 5 new job listings from web search results."""
import json
from datetime import datetime, timedelta

DATA_FILE = '/tmp/maulud-net/loker/lowongan.json'

with open(DATA_FILE, 'r') as f:
    data = json.load(f)

today = datetime.now().strftime('%Y-%m-%d')
expires = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')

# Check existing slugs to avoid duplicates
existing_slugs = {j['slug'] for j in data['jobs']}
print(f"Existing jobs: {len(data['jobs'])}")

new_jobs = [
    {
        "slug": "strategic-marketing-manager-pt-media-telekomunikasi-mandiri-jakarta",
        "title": "Strategic Marketing Manager",
        "company": "PT Media Telekomunikasi Mandiri",
        "location": "Jakarta Raya, Indonesia",
        "type": "Full-time",
        "category": "Marketing",
        "salary": "Rp 12-20 Juta",
        "posted": today,
        "expires": expires,
        "description": "PT Media Telekomunikasi Mandiri, perusahaan solusi telekomunikasi dan teknologi informasi yang terus berkembang, membuka lowongan Strategic Marketing Manager untuk memimpin strategi pemasaran di Indonesia. Posisi ini akan bertanggung jawab merancang dan mengeksekusi inisiatif marketing yang mendorong pertumbuhan bisnis lintas portofolio solusi berbasis proyek, produk principal, layanan in-house (Growth Builder), dan layanan Smart Technology berbasis AI. Cocok untuk profesional marketing yang memiliki visi strategis, pemahaman mendalam tentang marketing funnel, dan pengalaman mengelola multi-produk portofolio di industri teknologi.",
        "requirements": [
            "Minimal S1 di bidang Marketing, Business Administration, atau terkait",
            "Pengalaman 5+ tahun di bidang marketing, dengan 2+ tahun di posisi manajerial",
            "Pemahaman kuat tentang strategi marketing digital dan tradisional",
            "Pengalaman mengelola marketing campaign lintas channel (digital, event, PR)",
            "Kemampuan analitis yang kuat dalam mengukur ROI marketing",
            "Pengalaman dengan tools marketing automation dan CRM",
            "Kemampuan kepemimpinan dan manage tim yang baik",
            "Fasih berbahasa Inggris (lisan dan tulisan)",
            "Bersedia bekerja full-time di Jakarta"
        ],
        "responsibilities": [
            "Mengembangkan dan mengimplementasikan strategi marketing tahunan yang selaras dengan target bisnis",
            "Memimpin tim marketing dalam mengeksekusi campaign pemasaran multichannel",
            "Mengelola brand positioning dan messaging untuk setiap lini produk",
            "Melakukan market research dan competitor analysis untuk mengidentifikasi peluang",
            "Memonitor dan menganalisis performa marketing campaign serta menyajikan laporan ke leadership",
            "Berkolaborasi dengan tim sales, product, dan business development",
            "Mengelola anggaran marketing dan memastikan efisiensi pengeluaran",
            "Membangun hubungan dengan media, influencer, dan mitra strategis"
        ],
        "benefits": [
            "Gaji kompetitif sesuai pengalaman (Rp 12-20 Juta)",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Asuransi kesehatan tambahan untuk karyawan dan keluarga",
            "Tunjangan transportasi dan komunikasi",
            "Bonus kinerja tahunan",
            "Kesempatan pengembangan karir dan pelatihan",
            "Lingkungan kerja profesional dan dinamis"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/strategic-marketing-manager-at-pt-media-telekomunikasi-mandiri-4441718449",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/strategic-marketing-manager-at-pt-media-telekomunikasi-mandiri-4441718449",
        "featured": True
    },
    {
        "slug": "marketing-manager-indonesia-levi-strauss-co-jakarta",
        "title": "Marketing Manager Indonesia",
        "company": "Levi Strauss & Co.",
        "location": "Jakarta Raya, Indonesia",
        "type": "Full-time",
        "category": "Marketing",
        "salary": "Rp 20-35 Juta",
        "posted": today,
        "expires": expires,
        "description": "Levi Strauss & Co., perusahaan fashion denim legendaris asal Amerika yang telah beroperasi lebih dari 150 tahun, membuka lowongan Marketing Manager untuk wilayah Indonesia. Posisi ini akan memegang peran kunci dalam mengembangkan brand awareness dan visibility di Indonesia yang merupakan pasar strategis dengan tingkat kompetisi tinggi dari brand premium lifestyle hingga brand vertikal. Kamu akan bertanggung jawab membangun brand expression yang inovatif dan mengelola consumer funnel marketing dari hulu ke hilir. Posisi ini cocok untuk brand builder handal yang menguasai seni dan sains pemasaran.",
        "requirements": [
            "Minimal S1 di bidang Marketing, Business, atau terkait",
            "Pengalaman 7+ tahun di bidang brand marketing atau marketing management",
            "Pengalaman di industri fashion, retail, atau FMCG sangat diutamakan",
            "Pemahaman mendalam tentang consumer funnel marketing",
            "Kemampuan mengelola brand portfolio dan multi-channel marketing",
            "Pengalaman dengan digital marketing dan social media strategy",
            "Kemampuan analitis dan data-driven decision making",
            "Kepemimpinan tim yang kuat dan kemampuan kolaborasi lintas fungsi",
            "Fasih berbahasa Inggris",
            "Bersedia bekerja full-time di Jakarta"
        ],
        "responsibilities": [
            "Mengembangkan strategi pemasaran tahunan untuk brand Levi's di Indonesia",
            "Mengelola brand expression, visibility, dan awareness di pasar Indonesia",
            "Memimpin pengembangan campaign marketing dari konsep hingga eksekusi",
            "Mengelola anggaran marketing dan mengoptimalkan ROI campaign",
            "Berkolaborasi dengan tim global, sales, dan retail operations",
            "Melakukan analisis pasar dan competitor untuk mengidentifikasi growth opportunity",
            "Mengelola hubungan dengan agency kreatif, media, dan influencer",
            "Memantau performa brand dan menyajikan laporan ke regional leadership"
        ],
        "benefits": [
            "Gaji kompetitif dengan benefit kelas global (Rp 20-35 Juta)",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Asuransi kesehatan komprehensif",
            "Diskon karyawan untuk produk Levi's",
            "Kesempatan pengembangan karir secara global",
            "Lingkungan kerja brand fashion internasional",
            "Flexible working arrangement"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/marketing-manager-indonesia-at-levi-strauss-co-3901750596",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/marketing-manager-indonesia-at-levi-strauss-co-3901750596",
        "featured": False
    },
    {
        "slug": "software-engineer-rpa-traveloka-jakarta",
        "title": "Software Engineer - RPA",
        "company": "Traveloka",
        "location": "Jakarta Raya, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 15-25 Juta",
        "posted": today,
        "expires": expires,
        "description": "Traveloka, platform lifestyle super-app terkemuka di Asia Tenggara yang menyediakan layanan travel, akomodasi, dan gaya hidup, membuka lowongan Software Engineer khusus untuk divisi Robotic Process Automation (RPA). Kamu akan bertanggung jawab membangun kustomisasi, ekstensi, dan pengembangan solusi otomatisasi proses bisnis menggunakan teknologi RPA. Posisi ini cocok untuk software engineer yang memiliki minat di bidang automation, scripting, dan process optimization serta ingin berkontribusi pada efisiensi operasional perusahaan teknologi berskala regional.",
        "requirements": [
            "Minimal S1 di bidang Computer Science, Information Technology, atau terkait",
            "Pengalaman 2+ tahun sebagai Software Engineer atau RPA Developer",
            "Mahir dalam Python, JavaScript/TypeScript, atau bahasa scripting lainnya",
            "Pengalaman dengan platform RPA (UiPath, Automation Anywhere, Blue Prism, atau sejenis)",
            "Pemahaman tentang API integration dan RESTful services",
            "Pengalaman dengan SQL dan database management",
            "Kemampuan problem-solving dan analitis yang kuat",
            "Bersedia bekerja full-time di Jakarta"
        ],
        "responsibilities": [
            "Mengembangkan dan memelihara solusi RPA untuk otomatisasi proses bisnis",
            "Menganalisis proses manual yang berpotensi diotomatisasi",
            "Mendesain, mengembangkan, dan menguji bot RPA",
            "Melakukan monitoring dan maintenance bot yang sudah berjalan",
            "Berkolaborasi dengan tim business process dan operations",
            "Mendokumentasikan proses teknis dan user guide",
            "Melakukan troubleshooting dan debugging issues terkait RPA"
        ],
        "benefits": [
            "Gaji kompetitif sesuai pengalaman (Rp 15-25 Juta)",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Asuransi kesehatan tambahan",
            "Employee stock option program",
            "Budget pelatihan dan konferensi",
            "Lingkungan kerja startup unicorn regional",
            "Snack dan minuman gratis di kantor",
            "Flexible working arrangement"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/software-engineer-rpa-at-traveloka-4325443699",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/software-engineer-rpa-at-traveloka-4325443699",
        "featured": False
    },
    {
        "slug": "customer-service-e-commerce-luxasia-jakarta",
        "title": "Customer Service E-Commerce",
        "company": "LUXASIA",
        "location": "Jakarta Raya, Indonesia",
        "type": "Full-time",
        "category": "Customer Service",
        "salary": "Rp 6-10 Juta",
        "posted": today,
        "expires": expires,
        "description": "LUXASIA, perusahaan distribusi dan retail produk kecantikan dan gaya hidup premium terkemuka di Asia, membuka lowongan Customer Service E-Commerce untuk mendukung operasional bisnis online yang terus berkembang. Posisi ini akan menjadi ujung tombak interaksi dengan pelanggan di platform e-commerce, memastikan setiap pertanyaan dan keluhan ditangani dengan cepat, ramah, dan profesional. Cocok untuk individu yang memiliki orientasi layanan tinggi, komunikasi yang baik, dan passion di industri kecantikan.",
        "requirements": [
            "Minimal D3/S1 semua jurusan",
            "Pengalaman 1-2 tahun di bidang customer service, terutama e-commerce",
            "Kemampuan komunikasi lisan dan tulisan yang sangat baik (Bahasa Indonesia dan Inggris)",
            "Customer-oriented dengan empathy tinggi",
            "Mampu bekerja dengan target dan tekanan",
            "Familiar dengan platform e-commerce (Shopee, Tokopedia, Lazada) dan tools support",
            "Pengetahuan dasar tentang produk kecantikan (nilai plus)",
            "Bersedia bekerja shift dan full-time di Jakarta"
        ],
        "responsibilities": [
            "Menangani pertanyaan, keluhan, dan feedback pelanggan via chat, email, dan telepon",
            "Memproses order, return, refund, dan exchange sesuai prosedur",
            "Memberikan informasi produk dan rekomendasi kepada pelanggan",
            "Mendokumentasikan interaksi pelanggan di sistem CRM",
            "Berkolaborasi dengan tim warehouse, logistic, dan marketing",
            "Menyusun laporan customer service mingguan",
            "Membantu meningkatkan customer satisfaction score"
        ],
        "benefits": [
            "Gaji kompetitif (Rp 6-10 Juta)",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Asuransi kesehatan",
            "Diskon produk kecantikan premium",
            "Lingkungan kerja yang supportive",
            "Kesempatan pengembangan karir"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/customer-service-e-commerce-at-luxasia-4368953331",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/customer-service-e-commerce-at-luxasia-4368953331",
        "featured": False
    },
    {
        "slug": "content-writer-binus-group-jakarta",
        "title": "Content Writer",
        "company": "BINUS Group",
        "location": "Jakarta Raya, Indonesia",
        "type": "Full-time",
        "category": "Konten & Kreatif",
        "salary": "Rp 6-10 Juta",
        "posted": today,
        "expires": expires,
        "description": "BINUS Group, perusahaan holding terkemuka di bidang pendidikan dan teknologi yang menaungi Bina Nusantara University dan berbagai unit usaha lainnya, membuka lowongan Content Writer untuk mengembangkan konten Knowledge Base dan Service Articles. Posisi ini akan bertanggung jawab membuat user guide, instruksi langkah demi langkah, workflow, dan prosedur operasional yang jelas dan mudah dipahami. Cocok untuk penulis teknis yang detail-oriented dan memiliki kemampuan menerjemahkan informasi kompleks menjadi konten yang accessible.",
        "requirements": [
            "Minimal S1 di bidang Communication, English Literature, Education, atau terkait",
            "Pengalaman 1-3 tahun sebagai Content Writer atau Technical Writer",
            "Kemampuan menulis dalam Bahasa Indonesia dan Inggris yang baik",
            "Detail-oriented dan mampu membuat dokumentasi yang terstruktur",
            "Familiar dengan tools dokumentasi dan content management",
            "Pengalaman mengembangkan Knowledge Base content sangat diutamakan",
            "Kemampuan riset dan wawancara dengan subject matter experts",
            "Portfolio tulisan yang bisa dilampirkan"
        ],
        "responsibilities": [
            "Mengembangkan dan memelihara konten Knowledge Base dan Service Articles",
            "Menulis user guide, step-by-step instructions, dan operational procedures",
            "Melakukan riset dan wawancara dengan SME (Subject Matter Experts)",
            "Mengupdate konten existing berdasarkan feedback dan perubahan proses",
            "Memastikan konsistensi brand voice dan terminologi di semua dokumentasi",
            "Berkolaborasi dengan tim product, IT, dan customer service",
            "Menganalisis metrics konten untuk perbaikan berkelanjutan"
        ],
        "benefits": [
            "Gaji kompetitif (Rp 6-10 Juta)",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Asuransi kesehatan tambahan",
            "Akses ke fasilitas pendidikan BINUS",
            "Lingkungan kerja profesional dan inovatif",
            "Kesempatan pengembangan karir",
            "Pelatihan dan sertifikasi"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/content-writer-at-binus-group-4379403606",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/content-writer-at-binus-group-4379403606",
        "featured": False
    }
]

# Check for duplicates
added = 0
for job in new_jobs:
    if job['slug'] in existing_slugs:
        print(f"SKIP (duplicate slug): {job['slug']}")
        continue
    # Insert at index 0
    data['jobs'].insert(0, job)
    existing_slugs.add(job['slug'])
    added += 1
    print(f"ADDED: {job['title']} at {job['company']}")

# Ensure categories is computed correctly (not null)
categories = sorted(set(j['category'] for j in data['jobs'] if j.get('category')))
data['categories'] = categories

with open(DATA_FILE, 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\nDone! Added {added} new jobs. Total: {len(data['jobs'])} jobs.")
print(f"Categories: {categories}")
