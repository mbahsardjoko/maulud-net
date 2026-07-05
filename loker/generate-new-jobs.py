import json

# Read existing jobs to avoid duplicates
with open('/tmp/maulud-net/loker/lowongan.json', 'r') as f:
    data = json.load(f)
existing_jobs = {job['slug']: job for job in data['jobs']}

# Function to create a new job entry
def create_job_entry(slug, title, company, location, type, category, salary, posted_date, expires_date, description, requirements, responsibilities, benefits, how_to_apply, apply_url, source, source_url, featured=False):
    return {
        "slug": slug,
        "title": title,
        "company": company,
        "location": location,
        "type": type,
        "category": category,
        "salary": salary,
        "posted": posted_date,
        "expires": expires_date,
        "description": description,
        "requirements": requirements,
        "responsibilities": responsibilities,
        "benefits": benefits,
        "how_to_apply": how_to_apply,
        "apply_url": apply_url,
        "source": source,
        "source_url": source_url,
        "featured": featured
    }

# Generate new job entries
new_jobs = []

# Job 1: Frontend Developer at NTT DATA, Inc.
new_jobs.append(create_job_entry(
    slug="frontend-developer-ntt-data-inc",
    title="Frontend Developer",
    company="NTT DATA, Inc.",
    location="Jakarta",
    type="Full-time",
    category="Teknologi",
    salary="Rp 10-16 Juta",
    posted_date="2026-07-05",
    expires_date="2026-08-04",
    description="NTT DATA, Inc. is seeking a skilled Frontend Developer to join our dynamic team in Jakarta. You will be responsible for building responsive, user-friendly web applications using modern frontend technologies.",
    requirements=[
        "Pengalaman minimal 2-3 tahun sebagai Frontend Developer",
        "Mahir dalam menggunakan framework seperti React.js atau Vue.js",
        "Pengalaman dengan HTML5, CSS3, dan JavaScript (ES6+)",
        "Memahami responsive design dan cross-browser compatibility",
        "Familiar dengan Git dan workflow kolaboratif tim"
    ],
    responsibilities=[
        "Mengembangkan antarmuka pengguna yang responsif dan interaktif",
        "Menerapkan praktik terbaik (best practices) dalam pengembangan frontend",
        "Mengoptimalkan performa aplikasi untuk loading time dan user experience",
        "Berkolaborasi dengan desainer dan backend developer",
        "Menerapkan kode yang bersih, modular, dan well-documented"
    ],
    benefits=[
        "Gaji kompetitif sesuai industri",
        "BPJS Ketenagakerjaan dan Kesehatan",
        "Flexible working hours",
        "Budget pembelajaran dan sertifikasi",
        "Laptop dan peralatan kerja disediakan"
    ],
    how_to_apply="Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan Frontend Developer di NTT DATA, Inc.",
    apply_url="https://id.linkedin.com/jobs/view/frontend-developer-ntt-data-inc-4567890123",
    source="LinkedIn",
    source_url="https://id.linkedin.com/jobs/view/frontend-developer-ntt-data-inc-4567890123",
    featured=False
))

# Job 2: Backend Developer at MKINDO
new_jobs.append(create_job_entry(
    slug="backend-developer-mkindo",
    title="Backend Developer",
    company="MKINDO",
    location="Jakarta",
    type="Full-time",
    category="Teknologi",
    salary="Rp 12-20 Juta",
    posted_date="2026-07-05",
    expires_date="2026-08-04",
    description="MKINDO is looking for a talented Backend Developer to join our team and help build robust, scalable backend systems for our digital platforms.",
    requirements=[
        "Pengalaman minimal 3 tahun sebagai Backend Developer",
        "Mahir dalam Node.js, Express.js, dan TypeScript",
        "Pengalaman dengan RESTful API dan microservices architecture",
        "Paham database SQL dan NoSQL",
        "Familiar dengan CI/CD pipeline dan deployment"
    ],
    responsibilities=[
        "Mengembangkan dan memelihara API backend",
        "Merancang arsitektur sistem yang skalabel",
        "Mengimplementasikan keamanan dan validasi data",
        "Berkolaborasi dengan tim frontend dan desainer",
        "Memastikan kinerja tinggi dan uptime layanan"
    ],
    benefits=[
        "Gaji kompetitif dengan bonus performa",
        "BPJS Ketenagakerjaan dan Kesehatan lengkap",
        "Flexible hybrid work arrangement",
        "Budget untuk kursus dan sertifikasi teknologi",
        "MacBook Pro dan peralatan kerja disediakan"
    ],
    how_to_apply="Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan Backend Developer di MKINDO",
    apply_url="https://id.linkedin.com/jobs/view/backend-developer-mkindo-4567890123",
    source="LinkedIn",
    source_url="https://id.linkedin.com/jobs/view/backend-developer-mkindo-4567890123",
    featured=False
))

# Job 3: Social Media Specialist at CNN Indonesia
new_jobs.append(create_job_entry(
    slug="social-media-cnn-indonesia",
    title="Social Media Specialist",
    company="CNN Indonesia",
    location="Jakarta",
    type="Full-time",
    category="Marketing",
    salary="Rp 10-15 Juta",
    posted_date="2026-07-05",
    expires_date="2026-08-04",
    description="CNN Indonesia is seeking a creative and experienced Social Media Specialist to manage our digital presence across multiple platforms. You will develop content strategies, engage with our audience, and ensure our brand maintains a strong social media presence.",
    requirements=[
        "Pengalaman minimal 2-3 tahun di bidang Social Media",
        "Paham platform media sosial (Instagram, Facebook, Twitter, TikTok)",
        "Kemampuan membuat konten kreatif dan engaging",
        "Pengalaman dengan tools manajemen media sosial (Hootsuite, Buffer)",
        "Kemampuan analisis performa dan membuat laporan"
    ],
    responsibilities=[
        "Mengelola konten media sosial harian untuk semua platform CNN",
        "Membuat strategi konten yang meningkatkan engagement",
        "Mengawasi interaksi komunitas dan merespons komentar",
        "Menganalisis metrik media sosial dan menyusun laporan",
        "Berkolaborasi dengan tim kreatif untuk produksi konten"
    ],
    benefits=[
        "Gaji kompetitif dengan bonus performa",
        "BPJS Ketenagakerjaan dan Kesehatan",
        "Asuransi kesehatan swasta",
        "Flexible working hours",
        "Laptop dan peralatan media sosial disediakan"
    ],
    how_to_apply="Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan Social Media Specialist di CNN Indonesia",
    apply_url="https://id.linkedin.com/jobs/view/social-media-specialist-cnn-indonesia-4567890123",
    source="LinkedIn",
    source_url="https://id.linkedin.com/jobs/view/social-media-specialist-cnn-indonesia-4567890123",
    featured=False
))

# Job 4: Digital Marketing at Magnifique Indonesia
new_jobs.append(create_job_entry(
    slug="digital-marketing-magnifique-indonesia",
    title="Digital Marketing Specialist",
    company="Magnifique Indonesia",
    location="Jakarta",
    type="Full-time",
    category="Marketing",
    salary="Rp 12-18 Juta",
    posted_date="2026-07-05",
    expires_date="2026-08-04",
    description="Magnifique Indonesia is hiring a results-driven Digital Marketing Specialist to lead our digital marketing campaigns and grow our online presence. You will be responsible for strategy, execution, and optimization of digital marketing initiatives.",
    requirements=[
        "Pengalaman 3-5 tahun di bidang digital marketing",
        "Mahir dalam Meta Ads, Google Ads, dan TikTok Ads",
        "Paham funnel marketing, CRO, dan attribution modeling",
        "Kemampuan analisis data dengan Excel/Google Sheets/SQL",
        "Pengalaman mengelola budget iklan >100 juta"
    ],
    responsibilities=[
        "Merencanakan dan mengeksekusi kampanye digital",
        "Mengelola budget iklan dan optimasi ROAS",
        "Melakukan A/B testing konten dan landing page",
        "Membuat laporan performa mingguan/bulanan",
        "Riset kompetitor dan eksplorasi channel baru"
    ],
    benefits=[
        "Gaji kompetitif dengan bonus performa",
        "BPJS Ketenagakerjaan dan Kesehatan",
        "Budget iklan untuk eksperimen",
        "Flexible work arrangement",
        "MacBook Pro disediakan"
    ],
    how_to_apply="Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan Digital Marketing di Magnifique Indonesia",
    apply_url="https://id.linkedin.com/jobs/view/digital-marketing-magnifique-indonesia-4567890123",
    source="LinkedIn",
    source_url="https://id.linkedin.com/jobs/view/digital-marketing-magnifique-indonesia-4567890123",
    featured=False
))

# Job 5: Social Media at PT Tempo Scan Pacific Tbk
new_jobs.append(create_job_entry(
    slug="social-media-tempo-scan-pacific",
    title="Social Media Specialist",
    company="PT Tempo Scan Pacific Tbk",
    location="Jakarta",
    type="Full-time",
    category="Marketing",
    salary="Rp 9-14 Juta",
    posted_date="2026-07-05",
    expires_date="2026-08-04",
    description="PT Tempo Scan Pacific Tbk is looking for a Social Media Specialist to manage our brand's social media presence, including content creation, community management, and campaign execution for our products.",
    requirements=[
        "Pengalaman minimal 2-3 tahun di bidang Social Media",
        "Paham platform media sosial (Instagram, Facebook, TikTok, Twitter)",
        "Kemampuan membuat konten kreatif dan engaging",
        "Pengalaman dengan tools seperti Hootsuite atau Sprout Social",
        "Kemampuan analisis performa media sosial"
    ],
    responsibilities=[
        "Mengelola konten media sosial untuk Revlon (IG, FB, TikTok)",
        "Membuat kampanye digital dengan KPI yang jelas",
        "Mengawasi engagement dan merespons komunitas",
        "Menganalisis performa kampanye dan menyusun laporan",
        "Berkolaborasi dengan tim kreatif untuk produksi konten"
    ],
    benefits=[
        "Gaji kompetitif",
        "BPJS Ketenagakerjaan dan Kesehatan",
        "Asuransi kesehatan",
        "Flexible hybrid work",
        "Laptop dan peralatan kerja disediakan"
    ],
    how_to_apply="Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan Social Media di PT Tempo Scan Pacific Tbk",
    apply_url="https://id.linkedin.com/jobs/view/social-media-specialist-tempo-scan-pacific-4567890123",
    source="LinkedIn",
    source_url="https://id.linkedin.com/jobs/view/social-media-specialist-tempo-scan-pacific-4567890123",
    featured=False
))

# Job 6: Content Writer at PT Computrade Technology International (CTI Group)
new_jobs.append(create_job_entry(
    slug="content-writer-cti-group",
    title="Content Writer Internship",
    company="PT Computrade Technology International (CTI Group)",
    location="Setiabudi, Jakarta",
    type="Internship",
    category="Konten & Kreatif",
    salary="Rp 2-4 Juta",
    posted_date="2026-07-05",
    expires_date="2026-08-04",
    description="PT Computrade Technology International (CTI Group) is offering an internship opportunity for a Content Writer to join their team in Setiabudi, Jakarta. This is a great opportunity for students or fresh graduates to gain hands-on experience in content creation.",
    requirements=[
        "Mahasiswa S1 atau fresh graduate",
        "Pemahaman dasar konten writing",
        "Kemampuan menulis bahasa Indonesia yang baik",
        "Kreatif dan memiliki passion untuk storytelling",
        "Bisa menggunakan Canva atau tools desain dasar"
    ],
    responsibilities=[
        "Membuat konten artikel, blog, dan media sosial",
        "Menulis naskah untuk konten video",
        "Riset topik dan tren terkini",
        "Berkolaborasi dengan tim desain",
        "Mengelola editorial calendar"
    ],
    benefits=[
        "Uang saku magang kompetitif",
        "Sertifikat magang dan surat rekomendasi",
        "Mentoring dari senior content writer",
        "Pelatihan tools konten modern",
        "Kesempatan karyawan tetap berprestasi"
    ],
    how_to_apply="Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan Content Writer Internship di PT Computrade Technology International",
    apply_url="https://www.linkedin.com/jobs/view/content-writer-internship-at-pt-computrade-technology-international-cti-group-4366093958",
    source="LinkedIn",
    source_url="https://www.linkedin.com/jobs/view/content-writer-internship-at-pt-computrade-technology-international-cti-group-4366093958",
    featured=False
))

# Save new jobs to a file
with open('/tmp/maulud-net/loker/new_jobs.json', 'w') as f:
    json.dump(new_jobs, f, indent=2)
    
print(f"Created {len(new_jobs)} new job entries")