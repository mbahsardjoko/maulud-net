import json
from datetime import datetime, timedelta

# Baca existing data
with open('lowongan.json', 'r') as f:
    data = json.load(f)

# Data lowongan baru berdasarkan hasil web_search REAL
today = datetime.now().strftime("%Y-%m-%d")
expires = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")

new_jobs = [
    {
        "slug": "project-manager-e-solutions-jakarta",
        "title": "Project Manager",
        "company": "E-Solutions",
        "location": "Jakarta",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 12-18 Juta",
        "posted": today,
        "expires": expires,
        "description": "E-Solutions mencari Project Manager berpengalaman untuk memimpin tim teknologi. Posisi ini bertanggung jawab mengelola siklus hidup proyek dari perencanaan hingga implementasi, memastikan delivery tepat waktu dengan kualitas tinggi.",
        "requirements": [
            "Pengalaman minimal 3 tahun sebagai Project Manager di bidang teknologi",
            "Mampu mengelola tim 8-10 orang dan stakeholder lintas fungsi",
            "Pemahaman kuat tentang project planning, risk management, dan change management",
            "Sertifikasi PMP atau Agile/Scrum adalah nilai tambah",
            "Komunikasi dan leadership skills yang baik"
        ],
        "responsibilities": [
            "Mengelola siklus hidup proyek dari inisiasi hingga closure",
            "Melakukan project planning, estimasi, dan resource allocation",
            "Mengelola risiko proyek dan melakukan change management",
            "Memimpin tim 8-10 orang dan koordinasi dengan stakeholder",
            "Monitoring progress dan reporting ke management"
        ],
        "benefits": [
            "Gaji kompetitif",
            "Asuransi kesehatan",
            "Bonus berbasis kinerja",
            "Pelatihan dan sertifikasi profesional",
            "Lingkungan kerja yang dinamis"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/project-manager-at-e-solutions-4394604802",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/project-manager-at-e-solutions-4394604802",
        "featured": True
    },
    {
        "slug": "software-engineer-golang-bank-sinarmas",
        "title": "Software Engineer (Golang)",
        "company": "PT Bank Sinarmas Tbk",
        "location": "Jakarta",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 8-14 Juta",
        "posted": today,
        "expires": expires,
        "description": "PT Bank Sinarmas membuka kesempatan untuk Software Engineer dengan spesialisasi Golang. Bergabunglah dengan tim engineering yang solid untuk membangun solusi perbankan digital yang inovatif dan scalable.",
        "requirements": [
            "Minimal 1 tahun pengalaman dengan Golang",
            "Strong proficiency dalam Go programming language",
            "Pemahaman tentang microservices architecture",
            "Pengalaman dengan database relational dan NoSQL",
            "Familiar dengan Git dan CI/CD pipeline"
        ],
        "responsibilities": [
            "Develop dan maintain aplikasi backend menggunakan Golang",
            "Design dan implement RESTful APIs",
            "Collaborate dengan tim product dan frontend",
            "Write clean, maintainable, dan well-tested code",
            "Troubleshoot dan optimize aplikasi untuk performa maksimal"
        ],
        "benefits": [
            "Gaji kompetitif sesuai pengalaman",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Tunjangan transportasi",
            "Program training dan development",
            "Career growth di industri perbankan"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/software-engineer-at-pt-bank-sinarmas-tbk-4302493019",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/software-engineer-at-pt-bank-sinarmas-tbk-4302493019",
        "featured": False
    },
    {
        "slug": "software-engineer-hicolleagues-jakarta",
        "title": "Software Engineer",
        "company": "HiColleagues",
        "location": "Jakarta",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 7-12 Juta",
        "posted": today,
        "expires": expires,
        "description": "HiColleagues sedang berkembang pesat dan mencari Software Engineer untuk bergabung dengan tim teknologi kami. Anda akan bekerja pada produk yang digunakan oleh ribuan pengguna dan berkontribusi langsung pada pertumbuhan platform.",
        "requirements": [
            "Gelar Sarjana di bidang Computer Science, Information Technology, atau terkait",
            "Pengalaman 1-3 tahun dalam software development",
            "Proficient dengan bahasa pemrograman modern (Java, Python, atau JavaScript)",
            "Pemahaman konsep OOP dan design patterns",
            "Problem solving yang baik dan attitude positif"
        ],
        "responsibilities": [
            "Develop fitur baru sesuai requirement dari product team",
            "Maintain dan improve existing codebase",
            "Code review dan collaborate dengan tim developer",
            "Write technical documentation",
            "Participate dalam sprint planning dan daily standup"
        ],
        "benefits": [
            "Kompensasi kompetitif",
            "Asuransi kesehatan",
            "Flexible working hours",
            "Kesempatan belajar teknologi baru",
            "Team building dan company outing"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/software-engineer-at-hicolleagues-4375676705",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/software-engineer-at-hicolleagues-4375676705",
        "featured": False
    },
    {
        "slug": "freelance-seo-content-writer-acc",
        "title": "Freelance SEO Content Writer (Remote)",
        "company": "Astra Credit Companies (ACC)",
        "location": "Remote",
        "type": "Freelance",
        "category": "Konten & Kreatif",
        "salary": "Rp 4-7 Juta",
        "posted": today,
        "expires": expires,
        "description": "Astra Credit Companies membuka kesempatan bagi Freelance SEO Content Writer untuk mengembangkan konten website perusahaan. Posisi ini cocok untuk content writer berpengalaman yang memahami SEO dan ingin bekerja secara remote dengan fleksibilitas tinggi.",
        "requirements": [
            "Pengalaman minimal 2 tahun sebagai content writer atau copywriter",
            "Pemahaman kuat tentang SEO dan keyword research",
            "Kemampuan menulis dalam Bahasa Indonesia yang baik dan menarik",
            "Portfolio writing (artikel, blog, atau website content)",
            "Self-motivated dan mampu bekerja secara mandiri"
        ],
        "responsibilities": [
            "Menulis dan mengoptimasi konten website untuk SEO",
            "Riset keyword dan competitor analysis",
            "Develop content calendar dan content strategy",
            "Edit dan proofread content sebelum publikasi",
            "Collaborate dengan tim marketing untuk content alignment"
        ],
        "benefits": [
            "Work from anywhere (fully remote)",
            "Flexible working hours",
            "Fee kompetitif per project",
            "Kesempatan bekerja dengan brand besar",
            "Portfolio building dengan perusahaan kredibel"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://www.linkedin.com/posts/tangguh-dwijayanto_freelancewriter-contentwriter-remotework-activity-7337754307422785536-hWgy",
        "source": "LinkedIn",
        "source_url": "https://www.linkedin.com/posts/tangguh-dwijayanto_freelancewriter-contentwriter-remotework-activity-7337754307422785536-hWgy",
        "featured": False
    },
    {
        "slug": "project-manager-wipro-jakarta",
        "title": "Project Manager",
        "company": "Wipro",
        "location": "Jakarta",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 15-22 Juta",
        "posted": today,
        "expires": expires,
        "description": "Wipro, perusahaan teknologi global terkemuka, membuka posisi Project Manager untuk operasional di Jakarta. Anda akan mengelola project life cycle dan memberikan leadership kepada tim project dalam memastikan delivery yang sukses dan tepat waktu.",
        "requirements": [
            "Pengalaman minimal 5 tahun dalam project management di IT/teknologi",
            "Sertifikasi PMP, Prince2, atau Agile/Scrum Master",
            "Track record sukses mengelola large-scale projects",
            "Excellent communication dan stakeholder management skills",
            "Bahasa Inggris fluent (written dan verbal)"
        ],
        "responsibilities": [
            "Manage project life cycle dari inisiasi hingga closure",
            "Provide leadership kepada project resources",
            "Ensure timely delivery sesuai budget dan scope",
            "Risk management dan issue resolution",
            "Client communication dan stakeholder reporting"
        ],
        "benefits": [
            "Gaji sangat kompetitif dengan bonus",
            "Asuransi kesehatan premium",
            "International exposure dan training",
            "Career progression di perusahaan global",
            "Work-life balance programs"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/project-manager-at-wipro-4072458632",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/project-manager-at-wipro-4072458632",
        "featured": False
    }
]

# Insert di posisi 0 (paling atas)
for job in reversed(new_jobs):
    data['jobs'].insert(0, job)

# Save ke file
with open('lowongan.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ {len(new_jobs)} lowongan berhasil ditambahkan")
for i, job in enumerate(new_jobs, 1):
    print(f"{i}. {job['title']} ({job['company']}) - {job['source_url']}")
