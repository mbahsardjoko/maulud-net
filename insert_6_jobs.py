#!/usr/bin/env python3
import json
from datetime import datetime, timedelta

today = "2026-07-14"
expires = "2026-08-13"

with open('/tmp/maulud-net/loker/lowongan.json') as f:
    data = json.load(f)

new_jobs = [
    {
        "slug": "android-developer-mnc-group",
        "title": "Android Developer",
        "company": "MNC Group (PT MNC Asia Holding Tbk)",
        "location": "Jakarta",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 10-18 Juta",
        "posted": today,
        "expires": expires,
        "description": "MNC Group, perusahaan media dan entertainment terbesar di Indonesia yang menaungi RCTI, MNCTV, GTV, iNews, dan berbagai platform digital, sedang mencari Android Developer untuk bergabung dengan tim mobile engineering. Sebagai Android Developer di MNC Group, kamu akan bertanggung jawab merancang, mengembangkan, dan memelihara aplikasi Android yang melayani jutaan pengguna di seluruh Indonesia. Lingkungan kerja yang dinamis dan fast-paced ini cocok untuk developer yang ingin berdampak besar pada produk media digital yang digunakan masyarakat luas setiap hari. Kamu akan bekerja dengan teknologi Android modern seperti Kotlin, Jetpack Compose, dan arsitektur MVVM dalam tim yang agile dan kolaboratif.",
        "requirements": [
            "Pengalaman minimal 2-3 tahun sebagai Android Developer dengan portfolio aplikasi yang sudah rilis di Google Play Store",
            "Mahir menggunakan Kotlin dan Java untuk pengembangan Android native",
            "Paham arsitektur MVVM, Clean Architecture, dan dependency injection (Hilt/Dagger)",
            "Pengalaman dengan Android Jetpack components (Navigation, Room, WorkManager, Compose)",
            "Familiar dengan RESTful API integration menggunakan Retrofit atau Ktor Client",
            "Paham konsep Git version control dan branching strategy",
            "Pengalaman dengan CI/CD pipeline untuk Android adalah nilai tambah",
            "Kemampuan problem-solving yang baik dan komunikasi tim yang efektif"
        ],
        "responsibilities": [
            "Mengembangkan fitur-fitur baru untuk aplikasi Android MNC Group menggunakan Kotlin dan Jetpack Compose",
            "Memelihara dan meningkatkan performa aplikasi yang sudah ada dengan optimasi kode dan resource",
            "Berkolaborasi dengan tim product, UI/UX designer, dan backend engineer dalam pengembangan fitur",
            "Melakukan code review dan memastikan kualitas kode sesuai standar tim",
            "Mengimplementasikan automated testing (unit test, integration test) untuk menjaga stabilitas aplikasi",
            "Berpartisipasi dalam sprint planning, daily stand-up, dan retrospective bersama tim agile",
            "Memonitor performa aplikasi di production dan merespon isu-isu teknis yang muncul",
            "Mendokumentasikan arsitektur, API integration, dan proses teknis untuk referensi tim"
        ],
        "benefits": [
            "Gaji kompetitif Rp 10-18 Juta/bulan + bonus kinerja tahunan",
            "BPJS Ketenagakerjaan, Kesehatan, dan Asuransi Jiwa",
            "Fasilitas laptop MacBook Pro dan perangkat kerja lengkap",
            "Lingkungan kerja di gedung MNC Center, Jakarta Pusat",
            "Akses ke program pelatihan dan konferensi teknologi tahunan",
            "Tunjangan transportasi dan komunikasi",
            "Suasana kerja yang dinamis dengan exposure ke produk media skala nasional",
            "Kesempatan mengembangkan aplikasi dengan jutaan active users"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan Android Developer di MNC Group. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/android-developer-at-mnc-group-pt-mnc-asia-holding-tbk-4399160181",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/android-developer-at-mnc-group-pt-mnc-asia-holding-tbk-4399160181",
        "featured": True
    },
    {
        "slug": "social-media-specialist-tap-growth-ai",
        "title": "Social Media Specialist",
        "company": "Tap Growth AI",
        "location": "Jakarta",
        "type": "Full-time",
        "category": "Marketing",
        "salary": "Rp 6-10 Juta",
        "posted": today,
        "expires": expires,
        "description": "Tap Growth AI, perusahaan teknologi yang fokus pada AI-driven marketing solutions, sedang mencari Social Media Specialist untuk bergabung dengan tim marketing mereka di Jakarta. Posisi ini full-time dan work from office. Kamu akan menjadi ujung tombak kehadiran brand Tap Growth AI di berbagai platform media sosial — menciptakan konten yang engaging, mengelola komunitas online, dan mengukur performa campaign sosial media. Cocok untuk kamu yang kreatif, update dengan tren digital terkini, dan punya hasrat di dunia social media marketing. Kamu akan bekerja di lingkungan startup yang cepat dengan budaya data-driven dan inovasi.",
        "requirements": [
            "Pengalaman minimal 1-2 tahun sebagai Social Media Specialist, Community Manager, atau peran serupa",
            "Kemampuan membuat konten engaging untuk Instagram, LinkedIn, Twitter/X, dan TikTok",
            "Familiar dengan social media management tools seperti Hootsuite, Buffer, atau Meta Business Suite",
            "Kemampuan copywriting yang kuat dalam Bahasa Indonesia dan Inggris",
            "Paham dasar-dasar social media analytics dan bisa membaca data performa konten",
            "Kreatif, update dengan tren terbaru, dan punya ide-ide segar untuk konten viral",
            "Pengalaman dengan paid social ads (Meta Ads, LinkedIn Ads) adalah nilai plus",
            "Mampu bekerja dalam tim dan berkoordinasi dengan desainer grafis serta content creator"
        ],
        "responsibilities": [
            "Mengelola dan mengembangkan kehadiran brand Tap Growth AI di berbagai platform media sosial",
            "Membuat dan menjadwalkan konten yang relevan, engaging, dan sesuai brand voice",
            "Memonitor dan merespons komentar, pesan, dan interaksi dari audiens secara profesional",
            "Menganalisis performa konten dan menyusun laporan bulanan untuk tim manajemen",
            "Berkolaborasi dengan tim desain dan content creator untuk produksi konten visual dan video",
            "Mengikuti tren media sosial terkini dan mengadaptasikannya ke dalam strategi konten",
            "Mengelola community engagement dan membangun hubungan positif dengan followers",
            "Membantu pelaksanaan campaign sosial media berbayar dan optimasi performanya"
        ],
        "benefits": [
            "Gaji kompetitif Rp 6-10 Juta/bulan",
            "BPJS Ketenagakerjaan dan Kesehatan",
            "Lingkungan kerja startup yang dinamis dan inovatif",
            "Kesempatan belajar AI marketing tools terkini",
            "Fasilitas laptop dari perusahaan",
            "Team building dan gathering rutin",
            "Kesempatan pengembangan karir yang cepat"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan Social Media Specialist di Tap Growth AI. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/social-media-specialist-at-tap-growth-ai-4334065430",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/social-media-specialist-at-tap-growth-ai-4334065430",
        "featured": False
    },
    {
        "slug": "accounting-manager-alfred-bali",
        "title": "Accounting Manager",
        "company": "Alfred in Bali",
        "location": "Canggu, Bali",
        "type": "Full-time",
        "category": "Finance",
        "salary": "Rp 10-18 Juta",
        "posted": today,
        "expires": expires,
        "description": "Alfred in Bali, perusahaan yang bergerak di industri lifestyle dan hospitality di Canggu, Bali, sedang mencari Accounting Manager untuk memimpin seluruh fungsi akuntansi perusahaan. Posisi ini membutuhkan profesional dengan pengalaman minimal 3 tahun yang siap mengambil tanggung jawab penuh atas siklus akuntansi, pelaporan keuangan, pengelolaan tim, dan compliance perpajakan. Kamu akan bekerja di lingkungan yang dinamis dengan pemandangan pantai Bali sebagai latar belakang — menggabungkan karir profesional dengan gaya hidup pulau yang unik. Cocok untuk akuntan senior yang mencari pengalaman bekerja di perusahaan lifestyle yang sedang berkembang pesat.",
        "requirements": [
            "Pendidikan minimal S1 Akuntansi dari universitas terkemuka",
            "Pengalaman minimal 3 tahun sebagai Accounting Manager atau Finance Manager",
            "Pemahaman mendalam tentang PSAK dan standar akuntansi Indonesia",
            "Mahir dalam perpajakan Indonesia: PPh, PPN, dan pelaporan SPT",
            "Kemampuan memimpin tim dan mengelola proses month-end closing",
            "Pengalaman dengan software akuntansi (Accurate, Jurnal, atau sejenisnya)",
            "Detail-oriented, analitis, dan mampu bekerja dengan deadline ketat",
            "Domisili Bali atau bersedia pindah ke Bali"
        ],
        "responsibilities": [
            "Memimpin siklus akuntansi perusahaan termasuk accounts payable, accounts receivable, dan general ledger",
            "Menyusun laporan keuangan bulanan, kuartalan, dan tahunan sesuai standar akuntansi",
            "Mengelola compliance perpajakan dan memastikan pelaporan pajak tepat waktu",
            "Mengawasi dan mengembangkan tim accounting",
            "Melakukan rekonsiliasi bank dan memastikan akurasi pencatatan keuangan",
            "Mendukung proses audit internal dan eksternal",
            "Menyusun budget dan forecasting bersama manajemen",
            "Mengelola cash flow dan memberikan rekomendasi strategis ke direksi"
        ],
        "benefits": [
            "Gaji kompetitif Rp 10-18 Juta/bulan",
            "BPJS Ketenagakerjaan dan Kesehatan",
            "Lingkungan kerja di Canggu, Bali dengan vibe lifestyle yang unik",
            "Fleksibilitas jam kerja",
            "Kesempatan pengembangan karir di perusahaan yang berkembang",
            "Suasana kerja yang santai namun profesional"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan Accounting Manager di Alfred in Bali. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/accounting-manager-at-alfred-in-bali-4211507546",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/accounting-manager-at-alfred-in-bali-4211507546",
        "featured": False
    },
    {
        "slug": "customer-service-staff-puratos",
        "title": "Customer Service Staff",
        "company": "Puratos Indonesia",
        "location": "Jakarta",
        "type": "Full-time",
        "category": "Customer Service",
        "salary": "Rp 5-9 Juta",
        "posted": today,
        "expires": expires,
        "description": "Puratos Indonesia, anak perusahaan dari Puratos Group — perusahaan global terkemuka di bidang bahan baku bakery, pastry, dan chocolate — sedang mencari Customer Service Staff untuk bergabung dengan tim mereka di Jakarta. Sebagai perusahaan multinasional yang telah beroperasi di lebih dari 100 negara, Puratos menawarkan lingkungan kerja profesional dengan standar global. Posisi ini akan menjadi penghubung utama antara perusahaan dan pelanggan, memastikan setiap pertanyaan, pesanan, dan keluhan ditangani dengan cepat, profesional, dan penuh solusi. Kamu akan bekerja dalam tim yang supportif dengan budaya customer-centric yang kuat.",
        "requirements": [
            "Pendidikan minimal D3/S1 semua jurusan, diutamakan Manajemen atau Komunikasi",
            "Pengalaman 1-2 tahun di customer service, sales support, atau administrasi penjualan",
            "Kemampuan komunikasi lisan dan tulisan yang sangat baik dalam Bahasa Indonesia dan Inggris",
            "Detail-oriented, service-minded, dan mampu menangani tekanan dengan tenang",
            "Familiar dengan Microsoft Office (Excel, Word, Outlook) dan ERP dasar",
            "Mampu bekerja dalam tim dan prioritas tugas dengan baik",
            "Bersedia bekerja full-time di kantor Jakarta",
            "Pengalaman di industri F&B atau manufaktur adalah nilai plus"
        ],
        "responsibilities": [
            "Menangani inquiry pelanggan melalui telepon, email, dan chat dengan respon yang cepat dan profesional",
            "Memproses order pelanggan dan memastikan akurasi data pesanan di sistem",
            "Berkolaborasi dengan tim sales, logistik, dan produksi untuk memastikan kepuasan pelanggan",
            "Membantu penyelesaian komplain dan mencari solusi terbaik untuk pelanggan",
            "Menyusun laporan aktivitas customer service dan feedback pelanggan secara berkala",
            "Memelihara database pelanggan yang akurat dan up-to-date",
            "Memberikan informasi produk, harga, dan promo kepada pelanggan",
            "Mendukung tim sales dalam administrasi dokumen penjualan"
        ],
        "benefits": [
            "Gaji kompetitif Rp 5-9 Juta/bulan + tunjangan",
            "BPJS Ketenagakerjaan, Kesehatan, dan asuransi kesehatan tambahan",
            "Lingkungan kerja perusahaan multinasional dengan standar global",
            "Training produk dan pengembangan skill customer service",
            "Tunjangan transportasi dan makan siang",
            "Bonus tahunan berdasarkan kinerja",
            "Kesempatan pengembangan karir di Puratos Group"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan Customer Service Staff di Puratos Indonesia. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/customer-service-staff-at-puratos-4350140249",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/customer-service-staff-at-puratos-4350140249",
        "featured": False
    },
    {
        "slug": "graphic-designer-content-creator-intern-eurokars",
        "title": "Graphic Designer & Content Creator Intern",
        "company": "Eurokars Group Indonesia (Mazda Indonesia)",
        "location": "Jakarta",
        "type": "Internship",
        "category": "Desain",
        "salary": "Rp 3-5 Juta",
        "posted": today,
        "expires": expires,
        "description": "Eurokars Group Indonesia, distributor resmi Mazda di Indonesia, sedang membuka posisi Graphic Designer & Content Creator Intern untuk bergabung dengan tim marketing Mazda Indonesia. Program magang ini memberikan kesempatan langka untuk berkontribusi langsung pada brand otomotif premium global. Kamu akan terlibat dalam pembuatan konten visual yang memperkuat brand image Mazda di Indonesia — dari materi digital campaign, konten media sosial, hingga materi event dan showroom. Cocok untuk mahasiswa atau fresh graduate yang punya passion di dunia otomotif, desain, dan content creation. Lingkungan kerja yang dinamis dan exposure ke brand premium akan menjadi nilai besar untuk portfolio-mu.",
        "requirements": [
            "Mahasiswa aktif minimal semester 6 atau fresh graduate D3/S1 Desain, Komunikasi Visual, atau jurusan terkait",
            "Portfolio desain yang menunjukkan kreativitas dan skill teknis (wajib dilampirkan)",
            "Mahir menggunakan Adobe Photoshop, Illustrator, dan Canva",
            "Pengalaman membuat konten video pendek untuk TikTok, Instagram Reels, atau YouTube Shorts",
            "Kreatif, up-to-date dengan tren desain dan konten digital terkini",
            "Memiliki passion di dunia otomotif adalah nilai tambah yang besar",
            "Bisa bekerja dalam tim dan menerima feedback dengan positif",
            "Bersedia magang full-time di Jakarta (on-site)"
        ],
        "responsibilities": [
            "Membuat desain visual untuk konten media sosial Mazda Indonesia (Instagram, TikTok, Facebook, YouTube)",
            "Memproduksi konten video pendek yang engaging untuk campaign digital Mazda",
            "Membantu photoshoot dan video production untuk materi marketing",
            "Mendesain materi promosi seperti brosur, banner, poster, dan merchandise",
            "Berkolaborasi dengan tim marketing dan brand dalam pengembangan konten kreatif",
            "Mengedit dan memformat konten visual sesuai brand guidelines Mazda",
            "Memonitor trend desain dan konten untuk ide-ide segar",
            "Mengelola dan mengarsipkan aset desain digital"
        ],
        "benefits": [
            "Uang saku magang Rp 3-5 Juta/bulan",
            "Pengalaman langsung dengan brand otomotif global premium",
            "Portfolio profesional untuk karir desain dan kreatif",
            "Mentoring dari tim marketing dan brand profesional",
            "Lingkungan kerja yang mendukung kreativitas",
            "Kesempatan networking di industri otomotif Indonesia"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan Graphic Designer & Content Creator Intern di Eurokars Group Indonesia (Mazda Indonesia). Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/graphic-designer-content-creator-intern-at-eurokars-group-indonesia-4424177142",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/graphic-designer-content-creator-intern-at-eurokars-group-indonesia-4424177142",
        "featured": False
    },
    {
        "slug": "content-writer-intern-siloam-hospitals",
        "title": "Content Writer Intern",
        "company": "Siloam Hospitals Group",
        "location": "Jakarta",
        "type": "Internship",
        "category": "Konten & Kreatif",
        "salary": "Rp 3-5 Juta",
        "posted": today,
        "expires": expires,
        "description": "Siloam Hospitals Group, jaringan rumah sakit swasta terbesar di Indonesia dengan lebih dari 40 rumah sakit di berbagai kota, membuka kesempatan magang untuk posisi Content Writer di kantor pusat mereka. Ini adalah peluang langka untuk bergabung dengan industri kesehatan yang terus berkembang dan mendapatkan pengalaman menulis konten profesional di lingkungan perusahaan healthcare terkemuka. Sebagai Content Writer Intern, kamu akan menulis berbagai konten untuk website, media sosial, dan materi komunikasi Siloam Hospitals — mulai dari artikel edukasi kesehatan, newsletter, hingga campaign awareness. Cocok untuk mahasiswa atau fresh graduate yang tertarik di bidang komunikasi kesehatan dan ingin membangun portfolio menulis di perusahaan besar.",
        "requirements": [
            "Mahasiswa aktif minimal semester 6 atau fresh graduate S1 Komunikasi, Jurnalistik, Marketing, atau jurusan terkait",
            "Kemampuan menulis Bahasa Indonesia yang baik, rapi, dan engaging",
            "Kemampuan menulis Bahasa Inggris dasar (pasif/aktif) adalah nilai tambah",
            "Kreatif, detail-oriented, dan mampu bekerja dengan deadline",
            "Memiliki minat atau ketertarikan di dunia kesehatan adalah nilai plus besar",
            "Portfolio tulisan (artikel, blog, caption, atau karya tulis lainnya) wajib dilampirkan",
            "Bisa bekerja dalam tim dan menerima feedback/revisi dengan baik",
            "Bersedia magang full-time di Jakarta"
        ],
        "responsibilities": [
            "Menulis artikel edukasi kesehatan untuk website dan blog Siloam Hospitals",
            "Membuat caption dan konten copy untuk media sosial (Instagram, Facebook, LinkedIn, Twitter/X)",
            "Membantu pengembangan konten newsletter dan email marketing",
            "Melakukan riset topik kesehatan dari sumber terpercaya untuk bahan tulisan",
            "Berkolaborasi dengan tim marketing, brand, dan medical staff untuk memastikan akurasi konten",
            "Mengedit dan memproofread konten sebelum dipublikasikan",
            "Memonitor performa konten dan memberikan ide untuk improvement",
            "Mendukung tim komunikasi dalam project khusus dan campaign awareness"
        ],
        "benefits": [
            "Uang saku magang Rp 3-5 Juta/bulan",
            "Pengalaman di industri healthcare terbesar di Indonesia",
            "Portfolio konten profesional yang kuat untuk karir ke depan",
            "Mentoring dari tim komunikasi dan marketing yang berpengalaman",
            "Lingkungan kerja profesional di kantor pusat Siloam Hospitals",
            "Kesempatan networking dengan profesional kesehatan dan komunikasi"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan Content Writer Intern di Siloam Hospitals Group. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/content-writer-intern-at-siloam-hospitals-group-4400096390",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/content-writer-intern-at-siloam-hospitals-group-4400096390",
        "featured": False
    }
]

# Check for duplicate slugs
existing_slugs = {job['slug'] for job in data.get('jobs', [])}
for job in new_jobs:
    if job['slug'] in existing_slugs:
        print(f"WARNING: slug {job['slug']} already exists!")
    else:
        print(f"OK: {job['slug']} is new")

# Update categories field to include all unique categories from all jobs
all_categories = set()
for job in (new_jobs + data['jobs']):
    if job.get('category'):
        all_categories.add(job['category'])
data['categories'] = sorted(list(all_categories))

# Insert new jobs at index 0
data['jobs'] = new_jobs + data['jobs']

# Write back clean JSON
with open('/tmp/maulud-net/loker/lowongan.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\nInserted {len(new_jobs)} new jobs. Total jobs now: {len(data['jobs'])}")
print(f"Categories: {data['categories']}")
