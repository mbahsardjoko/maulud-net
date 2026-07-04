#!/usr/bin/env python3
"""Insert new job entries at index 0 of lowongan.json and regenerate HTML pages."""
import json
import subprocess
import sys
from pathlib import Path

BASE = Path('/tmp/maulud-net')
JSON_PATH = BASE / 'loker' / 'lowongan.json'

# Load existing data
with open(JSON_PATH) as f:
    data = json.load(f)

existing_jobs = data['jobs']
existing_slugs = {j['slug'] for j in existing_jobs}
existing_titles_companies = {(j['title'], j['company']) for j in existing_jobs}

print(f"Existing jobs: {len(existing_jobs)}")
print(f"Existing slugs: {existing_slugs}")

new_jobs = []

# --- Job 1: Product Manager (Indonesian Market) - Transsion Indonesia ---
j1 = {
    "slug": "product-manager-indonesian-market-transsion-indonesia",
    "title": "Product Manager (Indonesian Market)",
    "company": "Transsion Indonesia",
    "location": "Jakarta Raya",
    "type": "Full-time",
    "category": "Marketing",
    "salary": "Rp 15-25 Juta",
    "posted": "2026-07-04",
    "expires": "2026-08-03",
    "description": "Transsion Indonesia, perusahaan teknologi di balik merek TECNO, Infinix, dan itel, membuka lowongan Product Manager khusus untuk pasar Indonesia. Kamu akan bertanggung jawab mengembangkan strategi produk, melakukan riset pasar, dan berkolaborasi dengan tim engineering, marketing, dan sales untuk memastikan produk sesuai dengan kebutuhan konsumen Indonesia. Posisi ini strategis dan berpengaruh langsung terhadap pertumbuhan bisnis di pasar smartphone yang kompetitif.",
    "requirements": [
        "Pengalaman minimal 3-5 tahun sebagai Product Manager di industri teknologi/consumer electronics",
        "Memahami pasar smartphone Indonesia dan tren konsumen lokal",
        "Mampu melakukan market research, competitive analysis, dan product roadmap planning",
        "Kemampuan analitis kuat dengan data-driven decision making",
        "Komunikasi ekselen dan mampu kolaborasi lintas tim (engineering, design, marketing)",
        "Pengalaman dengan tools product management seperti Jira, Notion, atau Asana",
        "S1 segala jurusan, diutamakan Manajemen, Teknik, atau Ilmu Komputer"
    ],
    "responsibilities": [
        "Menyusun strategi produk jangka pendek dan panjang untuk pasar Indonesia",
        "Melakukan riset pasar dan analisis kompetitor secara berkala",
        "Mendefinisikan product requirements dan user stories bersama tim engineering",
        "Memantau performa produk dan metrik bisnis (sales, engagement, retention)",
        "Berkolaborasi dengan tim marketing untuk go-to-market strategy",
        "Menyusun roadmap produk berdasarkan prioritas bisnis dan feedback user",
        "Melakukan A/B testing dan iterasi produk berdasarkan data"
    ],
    "benefits": [
        "Gaji kompetitif + bonus tahunan berdasarkan performa",
        "BPJS Ketenagakerjaan dan Kesehatan",
        "Asuransi kesehatan tambahan untuk keluarga",
        "Program pengembangan karir dan sertifikasi",
        "Produk smartphone gratis setiap tahun",
        "Lingkungan kerja multinasional dan dinamis",
        "Flexible hybrid working arrangement"
    ],
    "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan Product Manager Indonesian Market di Transsion Indonesia. Informasi lebih lanjut bisa dicek di link sumber.",
    "apply_url": "https://id.linkedin.com/jobs/view/product-manager-indonesian-market-at-transsion-indonesia-4431208366",
    "source": "LinkedIn",
    "source_url": "https://id.linkedin.com/jobs/view/product-manager-indonesian-market-at-transsion-indonesia-4431208366",
    "featured": True
}

# --- Job 2: Social Media Specialist - Lazada ---
j2 = {
    "slug": "social-media-specialist-lazada",
    "title": "Social Media Specialist",
    "company": "Lazada",
    "location": "Jakarta",
    "type": "Full-time",
    "category": "Marketing",
    "salary": "Rp 8-14 Juta",
    "posted": "2026-07-04",
    "expires": "2026-08-03",
    "description": "Lazada, platform e-commerce terdepan di Asia Tenggara, mencari Social Media Specialist untuk mengelola dan mengembangkan brand presence di berbagai platform media sosial. Kamu akan bertanggung jawab menciptakan strategi konten yang engaging, mengelola komunitas online, dan menganalisis performa kampanye sosial media. Posisi ini cocok untuk kreator konten yang data-savvy dan paham tren digital terkini.",
    "requirements": [
        "Pengalaman minimal 2 tahun sebagai Social Media Specialist atau peran serupa",
        "Paham platform media sosial (Instagram, TikTok, Facebook, Twitter, LinkedIn, YouTube)",
        "Kemampuan membuat konten kreatif (copywriting, visual, video pendek)",
        "Pengalaman dengan social media management tools (Hootsuite, Buffer, Sprout Social)",
        "Mampu menganalisis data media sosial dan menyusun laporan performa",
        "Kreatif, up-to-date dengan tren, dan punya storytelling skill yang kuat",
        "Diutamakan yang punya pengalaman di e-commerce atau retail"
    ],
    "responsibilities": [
        "Mengelola jadwal posting dan konten harian di semua platform media sosial Lazada",
        "Membuat konten kreatif (caption, visual, reels, stories) yang engaging",
        "Memantau dan merespon interaksi komunitas (comments, DM, mentions)",
        "Menganalisis performa konten dan menyusun laporan mingguan/bulanan",
        "Berkolaborasi dengan tim kreatif dan brand marketing untuk kampanye besar",
        "Riset tren terbaru dan mengadaptasi strategi konten secara agile"
    ],
    "benefits": [
        "Gaji kompetitif + THR + bonus tahunan",
        "BPJS Ketenagakerjaan dan Kesehatan lengkap",
        "Asuransi kesehatan swasta",
        "Flexible hybrid work (WFO/WFH)",
        "MacBook Pro dan tools kerja disediakan",
        "Akses ke platform pembelajaran online",
        "Diskon karyawan untuk belanja di Lazada"
    ],
    "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan Social Media Specialist Indonesia di Lazada. Informasi lebih lanjut bisa dicek di link sumber.",
    "apply_url": "https://id.linkedin.com/jobs/view/social-media-specialist-indonesia-at-lazada-4227273454",
    "source": "LinkedIn",
    "source_url": "https://id.linkedin.com/jobs/view/social-media-specialist-indonesia-at-lazada-4227273454",
    "featured": False
}

# --- Job 3: Copywriter & Content Creator - Kitabisa ---
j3 = {
    "slug": "copywriter-content-creator-kitabisa",
    "title": "Copywriter & Content Creator",
    "company": "Kitabisa",
    "location": "Jakarta",
    "type": "Full-time",
    "category": "Konten & Kreatif",
    "salary": "Rp 6-10 Juta",
    "posted": "2026-07-04",
    "expires": "2026-08-03",
    "description": "Kitabisa, platform crowdfunding dan filantropi terbesar di Indonesia, mencari Copywriter & Content Creator yang kreatif dan punya hati sosial. Kamu akan menulis konten yang menginspirasi donasi, membuat storytelling campaign yang menyentuh, dan menciptakan konten untuk berbagai kanal digital. Posisi ini pas banget buat kamu yang ingin karya tulisnya punya dampak sosial nyata.",
    "requirements": [
        "Pengalaman minimal 1-2 tahun sebagai copywriter/content writer/content creator",
        "Kemampuan menulis bahasa Indonesia yang baik, benar, dan engaging",
        "Paham storytelling untuk campaign sosial dan fundraising",
        "Kreatif bikin konsep konten untuk Instagram, TikTok, YouTube, dan website",
        "Bisa menggunakan Canva atau tools desain dasar untuk visual konten",
        "Portfolio tulisan/konten wajib dilampirkan",
        "Peka terhadap isu sosial dan punya empati tinggi"
    ],
    "responsibilities": [
        "Menulis copy untuk campaign fundraising, newsletter, dan landing page",
        "Membuat konsep dan script konten video untuk media sosial",
        "Menulis artikel blog dan konten website yang informatif dan inspiratif",
        "Berkolaborasi dengan tim desain dan video untuk produksi konten",
        "Mengelola editorial calendar dan memastikan konsistensi brand voice",
        "Memonitor engagement konten dan melakukan optimasi berkelanjutan"
    ],
    "benefits": [
        "Gaji pokok + tunjangan kinerja",
        "BPJS Ketenagakerjaan dan Kesehatan",
        "Lingkungan kerja yang bermakna (social impact)",
        "Jam kerja fleksibel",
        "Akses pelatihan content writing dan digital marketing",
        "Cuti tahunan dan cuti sakit",
        "Mentoring dari senior kreatif"
    ],
    "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan Copywriter & Content Creator di Kitabisa. Informasi lebih lanjut bisa dicek di link sumber.",
    "apply_url": "https://id.linkedin.com/jobs/view/copywriter-content-creator-at-kitabisa-4378028809",
    "source": "LinkedIn",
    "source_url": "https://id.linkedin.com/jobs/view/copywriter-content-creator-at-kitabisa-4378028809",
    "featured": False
}

# --- Job 4: Graphic Designer - Mekari ---
j4 = {
    "slug": "graphic-designer-mekari",
    "title": "Graphic Designer",
    "company": "Mekari",
    "location": "Jakarta",
    "type": "Full-time",
    "category": "Desain",
    "salary": "Rp 7-12 Juta",
    "posted": "2026-07-04",
    "expires": "2026-08-03",
    "description": "Mekari, perusahaan software-as-a-service (SaaS) terkemuka di Indonesia yang memiliki produk Mekari Accounting, Mekari HR, dan Mekari Jurnal, mencari Graphic Designer untuk memperkuat tim kreatif mereka. Kamu akan mendesain aset visual untuk produk digital, campaign marketing, konten sosial media, dan branding perusahaan. Posisi ini cocok buat desainer yang punya passion di tech industry dan suka kerja dengan tim dinamis.",
    "requirements": [
        "Pendidikan minimal S1 Desain Komunikasi Visual atau setara",
        "Pengalaman 1-3 tahun sebagai Graphic Designer (lebih disukai di industri tech/SaaS)",
        "Mahir Adobe Creative Suite (Photoshop, Illustrator, After Effects)",
        "Punya portfolio desain yang kuat dan variatif",
        "Paham prinsip desain (typography, color theory, layout, composition)",
        "Kreatif, detail-oriented, dan mampu bekerja dengan deadline ketat",
        "Pengetahuan dasar motion graphics dan video editing adalah nilai plus"
    ],
    "responsibilities": [
        "Membuat aset visual untuk campaign marketing digital (social media ads, email, landing page)",
        "Mendesain materi branding dan komunikasi perusahaan",
        "Berkolaborasi dengan tim marketing dan product untuk kebutuhan desain",
        "Mengembangkan dan menjaga konsistensi brand identity",
        "Membuat ilustrasi, ikon, dan elemen visual untuk product UI",
        "Stay updated dengan tren desain terkini dan tools baru"
    ],
    "benefits": [
        "Gaji kompetitif + bonus performa",
        "BPJS Ketenagakerjaan dan Kesehatan",
        "MacBook Pro dan monitor eksternal",
        "Flexible work arrangement (hybrid)",
        "Budget untuk kursus dan conference desain",
        "Lingkungan kerja startup yang dinamis dan suportif",
        "Asuransi kesehatan tambahan"
    ],
    "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan Graphic Designer di Mekari. Informasi lebih lanjut bisa dicek di link sumber.",
    "apply_url": "https://id.linkedin.com/jobs/view/graphic-designer-at-mekari-4379418363",
    "source": "LinkedIn",
    "source_url": "https://id.linkedin.com/jobs/view/graphic-designer-at-mekari-4379418363",
    "featured": False
}

# --- Job 5: DevOps Engineer - PT Siaga Abdi Utama ---
j5 = {
    "slug": "devops-engineer-pt-siaga-abdi-utama",
    "title": "DevOps Engineer",
    "company": "PT Siaga Abdi Utama",
    "location": "Jakarta",
    "type": "Full-time",
    "category": "Teknologi",
    "salary": "Rp 10-18 Juta",
    "posted": "2026-07-04",
    "expires": "2026-08-03",
    "description": "PT Siaga Abdi Utama membuka lowongan DevOps Engineer level entry/junior untuk bergabung dengan tim infrastruktur teknologi mereka. Kamu akan belajar dan berkontribusi dalam mengelola pipeline CI/CD, automasi deployment, monitoring infrastruktur, dan menjaga ketersediaan sistem produksi. Ini kesempatan bagus buat fresh graduate atau junior engineer yang ingin membangun karir di bidang DevOps dan infrastruktur cloud.",
    "requirements": [
        "Lulusan S1 Ilmu Komputer, Teknik Informatika, atau setara",
        "Pemahaman dasar Linux/Unix dan command line",
        "Paham konsep version control (Git) dan workflow kolaboratif",
        "Familiar dengan cloud platform (AWS/GCP/Azure) - minimal tahu dasar",
        "Pengalaman dengan Docker atau containerization adalah nilai plus",
        "Bersedia belajar tools CI/CD seperti Jenkins, GitLab CI, atau GitHub Actions",
        "Kemampuan problem-solving dan debugging yang baik",
        "Bisa kerja on-site di Jakarta (full-time)"
    ],
    "responsibilities": [
        "Membantu setup dan maintenance CI/CD pipeline untuk berbagai project",
        "Melakukan deployment aplikasi ke environment staging dan production",
        "Memantau infrastruktur dan sistem menggunakan monitoring tools",
        "Mengelola source code repository dan branching strategy",
        "Berkolaborasi dengan software developer untuk optimasi deployment",
        "Mendokumentasikan proses dan konfigurasi infrastruktur",
        "Belajar dan menerapkan best practices keamanan infrastruktur"
    ],
    "benefits": [
        "Gaji kompetitif sesuai standar industri",
        "BPJS Ketenagakerjaan dan Kesehatan",
        "Pelatihan dan sertifikasi DevOps/Cloud (AWS, GCP, Docker)",
        "Mentoring dari senior engineer berpengalaman",
        "Laptop dan peralatan kerja disediakan",
        "Kesempatan berkembang ke posisi Mid/Senior DevOps",
        "Lingkungan belajar yang suportif"
    ],
    "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan DevOps Engineer di PT Siaga Abdi Utama. Informasi lebih lanjut bisa dicek di link sumber.",
    "apply_url": "https://id.linkedin.com/jobs/view/devops-engineer-at-pt-siaga-abdi-utama-4361822824",
    "source": "LinkedIn",
    "source_url": "https://id.linkedin.com/jobs/view/devops-engineer-at-pt-siaga-abdi-utama-4361822824",
    "featured": False
}

# --- Job 6: HR Manager, Indonesia - Xiaomi Technology ---
j6 = {
    "slug": "hr-manager-indonesia-xiaomi",
    "title": "HR Manager, Indonesia",
    "company": "Xiaomi Technology",
    "location": "Jakarta",
    "type": "Full-time",
    "category": "Administrasi",
    "salary": "Rp 15-25 Juta",
    "posted": "2026-07-04",
    "expires": "2026-08-03",
    "description": "Xiaomi Technology, salah satu perusahaan teknologi terbesar dunia, mencari HR Manager untuk kantor perwakilan mereka di Indonesia. Kamu akan memimpin fungsi HR secara end-to-end — mulai dari rekrutmen, manajemen kinerja, pengembangan talenta, hubungan industrial, hingga compliance ketenagakerjaan. Posisi ini strategis dan akan bekerja langsung dengan senior management serta global HR team.",
    "requirements": [
        "Pengalaman minimal 5-7 tahun di bidang Human Resources, minimal 2 tahun di posisi manajerial",
        "Paham regulasi ketenagakerjaan Indonesia (UU Ketenagakerjaan, PP, BPJS)",
        "Pengalaman di perusahaan multinasional atau teknologi sangat diutamakan",
        "Kemampuan komunikasi bahasa Inggris aktif (lisan dan tulisan)",
        "Pernah handle rekrutmen massal dan talent acquisition strategy",
        "Paham HRIS dan people analytics tools",
        "Strong leadership, interpersonal, dan problem-solving skills",
        "Bersedia bekerja full-time on-site di Jakarta"
    ],
    "responsibilities": [
        "Memimpin proses rekrutmen dan talent acquisition untuk semua level posisi",
        "Mengelola performance management system (KPI, OKR, evaluasi)",
        "Merancang dan menjalankan program pengembangan karyawan",
        "Menangani hubungan industrial dan compliance ketenagakerjaan",
        "Menyusun kebijakan HR dan employee handbook yang sesuai regulasi",
        "Berkolaborasi dengan global HR team untuk inisiatif regional",
        "Mengelola payroll, benefit, dan administrasi HR secara keseluruhan",
        "Menjadi culture champion dan menjaga employee engagement"
    ],
    "benefits": [
        "Gaji kompetitif dengan benefit kelas multinasional",
        "BPJS Ketenagakerjaan dan Kesehatan",
        "Asuransi kesehatan ekstended untuk keluarga",
        "Bonus tahunan berdasarkan performa perusahaan",
        "Program pengembangan kepemimpinan dan training global",
        "Smartphone dan perangkat Xiaomi gratis",
        "Lingkungan kerja internasional dengan standar global"
    ],
    "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan HR Manager Indonesia di Xiaomi Technology. Informasi lebih lanjut bisa dicek di link sumber.",
    "apply_url": "https://id.linkedin.com/jobs/view/hr-manager-indonesia-at-xiaomi-technology-4391693776",
    "source": "LinkedIn",
    "source_url": "https://id.linkedin.com/jobs/view/hr-manager-indonesia-at-xiaomi-technology-4391693776",
    "featured": False
}

new_jobs = [j1, j2, j3, j4, j5, j6]

# Check for duplicates
print("\\nChecking duplicates...")
for j in new_jobs:
    if j['slug'] in existing_slugs:
        print(f"  DUPLICATE (slug): {j['slug']}")
        sys.exit(1)
    if (j['title'], j['company']) in existing_titles_companies:
        print(f"  DUPLICATE (title+company): {j['title']} @ {j['company']}")
        sys.exit(1)

print("  No duplicates found. All clear.")

# Insert at index 0 (newest first)
data['jobs'] = new_jobs + existing_jobs

# Update featured: set hanya 1 true (j1 as best)
# Reset all featured to false first
for j in data['jobs']:
    j['featured'] = False
# Then set featured for the first job (j1)
data['jobs'][0]['featured'] = True

# Write back
with open(JSON_PATH, 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
    f.write('\\n')

print(f"\\nInserted {len(new_jobs)} jobs. Total jobs: {len(data['jobs'])}")

# Regenerate HTML pages
print("\\nRunning generate-post.py...")
result = subprocess.run(
    [sys.executable, str(BASE / 'loker' / 'scripts' / 'generate-post.py')],
    capture_output=True, text=True, cwd=str(BASE)
)
print(result.stdout)
if result.returncode != 0:
    print(f"STDERR: {result.stderr}")
    sys.exit(1)
if result.returncode != 0:
    sys.exit(result.returncode)

print("\\nDone! Ready for git commit.")
