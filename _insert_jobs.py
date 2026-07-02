#!/usr/bin/env python3
"""Insert 6 new job listings into lowongan.json (index 0)."""
import json
from datetime import datetime, timedelta

today = "2026-07-02"
expires = (datetime.strptime(today, "%Y-%m-%d") + timedelta(days=30)).strftime("%Y-%m-%d")

new_jobs = [
    {
        "slug": "fresh-graduate-hiring-byd-indonesia-bandung",
        "title": "2026 Indonesia Fresh Graduate Hiring - Bandung",
        "company": "BYD Indonesia",
        "location": "Bandung",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 6-10 Juta",
        "posted": today,
        "expires": expires,
        "description": "BYD Indonesia, perusahaan mobil listrik global asal China yang kini berekspansi besar-besaran di Indonesia, membuka program Campus Hiring 2026 untuk fresh graduate di Bandung. Program ini dirancang untuk lulusan baru yang siap memulai karir di industri kendaraan listrik dan energi terbarukan. Kamu akan mendapatkan kesempatan belajar dari para ahli industri sambil berkontribusi langsung dalam proyek-proyek strategis BYD di Indonesia. Posisi ini cocok banget buat kamu yang lulusan baru dan pengen langsung terjun ke dunia kerja dengan bimbingan intensif.",
        "requirements": [
            "Fresh graduate atau lulusan tahun 2026 (max 1 tahun setelah lulus)",
            "Minimal S1 dari semua jurusan (diutamakan Teknik, IT, Business)",
            "IPK minimal 3.00 dari skala 4.00",
            "Bersedia ditempatkan di Bandung",
            "Kemampuan komunikasi Bahasa Inggris aktif",
            "Passionate di bidang sustainable energy dan teknologi",
            "Bersedia mengikuti program rotasi dan pelatihan intensif"
        ],
        "responsibilities": [
            "Mengikuti program pengembangan dan pelatihan terstruktur selama periode onboarding",
            "Belajar langsung dari mentor dan senior engineer di berbagai departemen",
            "Berkontribusi dalam proyek-proyek strategis perusahaan",
            "Berpartisipasi dalam rotasi antar divisi untuk memahami bisnis secara holistic",
            "Menyelesaikan tugas dan project assignment sesuai target yang ditentukan"
        ],
        "benefits": [
            "Program pengembangan karir terstruktur selama 1-2 tahun",
            "Mentorship dari profesional berpengalaman",
            "Gaji kompetitif dengan review tahunan",
            "BPJS Ketenagakerjaan dan Kesehatan",
            "Kesempatan berkembang pesat di industri EV yang sedang booming",
            "Lingkungan kerja internasional"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan BYD Indonesia. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://www.linkedin.com/jobs/view/4400089141",
        "source": "LinkedIn",
        "source_url": "https://www.linkedin.com/jobs/view/4400089141",
        "featured": True
    },
    {
        "slug": "product-manager-adecco-jakarta",
        "title": "Product Manager",
        "company": "Adecco Indonesia",
        "location": "Jakarta",
        "type": "Full-time",
        "category": "Marketing",
        "salary": "Rp 15-25 Juta",
        "posted": today,
        "expires": expires,
        "description": "Adecco Indonesia, perusahaan penyedia solusi SDM dan rekrutmen terkemuka di Indonesia, mencari seorang Product Manager yang komersial dan hands-on. Kamu akan memimpin aktivitas manajemen produk dan trade marketing untuk brand ternama di Indonesia. Posisi ini membutuhkan seseorang yang memiliki jiwa kepemimpinan kuat dan mampu mengelola seluruh lifecycle produk, dari perencanaan strategis hingga eksekusi di lapangan. Kamu akan bekerja sama dengan tim sales, marketing, dan operasional untuk memastikan produk mencapai target pasar.",
        "requirements": [
            "Minimal 3-5 tahun pengalaman sebagai Product Manager atau Brand Manager",
            "Pengalaman di industri FMCG atau konsumen menjadi nilai tambah",
            "Kemampuan analitis yang kuat untuk membaca data pasar dan tren",
            "Pengalaman dalam trade marketing dan kerjasama dengan distributor/retailer",
            "Kemampuan komunikasi dan presentasi excellent",
            "Familiar dengan tools marketing analytics dan campaign management",
            "S1 semua jurusan (Marketing/Business lebih disukai)"
        ],
        "responsibilities": [
            "Mengembangkan strategi produk jangka pendek dan jangka panjang",
            "Melakukan riset pasar untuk mengidentifikasi peluang dan ancaman kompetitif",
            "Mengelola budget marketing dan memonitor ROI setiap campaign",
            "Berkolaborasi dengan tim sales untuk mengoptimalkan distribusi produk",
            "Memonitor performa produk dan menyusun laporan berkala",
            "Mengelola lifecycle produk dari launch hingga evaluasi"
        ],
        "benefits": [
            "Gaji kompetitif di atas rata-rata industri",
            "Bekerja dengan tim profesional di perusahaan global",
            "Kesempatan mengelola brand strategis",
            "Program pelatihan pengembangan karir",
            "BPJS Ketenagakerjaan dan Kesehatan"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan Adecco Indonesia. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://www.linkedin.com/jobs/view/4433649213",
        "source": "LinkedIn",
        "source_url": "https://www.linkedin.com/jobs/view/4433649213",
        "featured": False
    },
    {
        "slug": "graphic-designer-monee-jakarta",
        "title": "Graphic Designer",
        "company": "Monee",
        "location": "Jakarta",
        "type": "Full-time",
        "category": "Desain",
        "salary": "Rp 6-12 Juta",
        "posted": today,
        "expires": expires,
        "description": "Monee, platform teknologi finansial yang berkembang pesat di Indonesia, membuka lowongan untuk Graphic Designer kreatif. Sebagai Graphic Designer di Monee, kamu akan bertanggung jawab untuk menciptakan aset visual yang engaging di seluruh touchpoint digital — mulai dari in-app visuals, campaign marketing, hingga brand communications. Posisi ini akan sangat cocok buat kamu yang punya jiwa kreatif tinggi, eye untuk detail, dan bisa bekerja cepat tanpa mengorbankan kualitas. Kamu akan jadi bagian dari tim kreatif yang mendukung pertumbuhan brand Monee.",
        "requirements": [
            "Minimal 1-2 tahun pengalaman sebagai Graphic Designer (digital portfolio wajib)",
            "Proficiency di Adobe Creative Suite (Photoshop, Illustrator, After Effects)",
            "Pengalaman mendesain untuk platform digital (mobile app, web, social media)",
            "Pemahaman tentang brand identity dan visual consistency",
            "Kreatif, up-to-date dengan tren desain terkini",
            "Kemampuan komunikasi dan menerima feedback dengan baik",
            "Pengalaman dengan tools prototyping (Figma/Principle) nilai tambah"
        ],
        "responsibilities": [
            "Membuat desain visual untuk campaign marketing di berbagai channel",
            "Mendesain in-app visuals, ilustrasi, dan aset brand",
            "Berkolaborasi dengan tim product dan marketing untuk campaign kreatif",
            "Menjaga brand consistency di semua touchpoint",
            "Membantu pengembangan brand assets dan guidelines",
            "Berpartisipasi dalam brainstorming ide kreatif untuk campaign"
        ],
        "benefits": [
            "Lingkungan kerja startup yang dinamis dan kreatif",
            "Kesempatan untuk bereksperimen dengan desain inovatif",
            "Gaji dan benefit kompetitif",
            "BPJS Ketenagakerjaan dan Kesehatan",
            "Pengembangan portofolio dan skill desain"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan Monee. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/graphic-designer-at-monee-4382977790",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/graphic-designer-at-monee-4382977790",
        "featured": False
    },
    {
        "slug": "account-executive-cnn-indonesia-jakarta",
        "title": "Account Executive",
        "company": "CNN Indonesia",
        "location": "Jakarta",
        "type": "Full-time",
        "category": "Marketing",
        "salary": "Rp 7-14 Juta",
        "posted": today,
        "expires": expires,
        "description": "CNN Indonesia, salah satu media berita terkemuka di Indonesia, membuka lowongan untuk Account Executive yang berbakat dan energetic. Posisi ini adalah jantung dari aktivitas komersial CNN Indonesia, dimana kamu akan bertanggung jawab mengelola hubungan dengan klien, menjual solusi advertising dan sponsorship, serta memastikan pendapatan perusahaan terus bertumbuh. Cocok untuk kamu yang punya jiwa sales, networking yang luas, dan paham industri media dan periklanan di Indonesia. Kamu akan bekerja dengan brand-brand besar dan membantu mereka mencapai target marketing.",
        "requirements": [
            "Minimal S1 di bidang Marketing, Business, Management atau setara",
            "Pengalaman 1-2 tahun di Account Executive, Sales, atau Business Development",
            "Memiliki network di industri media/advertising menjadi nilai tambah",
            "Kemampuan negosiasi dan komunikasi yang sangat baik",
            "Target oriented dan mampu manage multiple clients",
            "Memahami industri media, TV, dan digital advertising",
            "Fasih Bahasa Inggris aktif"
        ],
        "responsibilities": [
            "Mengelola dan mengembangkan hubungan dengan klien existing dan potensial",
            "Menjual produk iklan dan sponsorship CNN Indonesia",
            "Membuat proposal dan presentasi untuk calon klien",
            "Berkolaborasi dengan tim internal (produksi, konten, marketing)",
            "Memonitor performa campaign klien dan memberikan laporan",
            "Mencapai target penjualan yang ditetapkan setiap periode"
        ],
        "benefits": [
            "Bekerja di salah satu media ternama di Indonesia",
            "Komisi dan bonus berdasarkan pencapaian target",
            "Eksposur ke brand-brand besar nasional dan internasional",
            "Lingkungan kerja profesional dan fast-paced",
            "BPJS Ketenagakerjaan dan Kesehatan"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan CNN Indonesia. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/account-executive-at-cnn-indonesia-4424077857",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/account-executive-at-cnn-indonesia-4424077857",
        "featured": False
    },
    {
        "slug": "junior-data-analyst-pt-sarimelati-kencana-jakarta",
        "title": "Junior Data Analyst",
        "company": "PT Sarimelati Kencana Tbk",
        "location": "Jakarta Selatan",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 6-10 Juta",
        "posted": today,
        "expires": expires,
        "description": "PT Sarimelati Kencana Tbk, perusahaan waralaba restoran Pizza Hut terbesar di Indonesia, membuka lowongan untuk Junior Data Analyst. Sebagai Junior Data Analyst, kamu akan menjadi jembatan antara data dan pengambilan keputusan bisnis. Kamu akan bertanggung jawab mengolah data dari berbagai sumber, menyediakan insight untuk tim manajemen, dan memastikan data warehouse perusahaan siap mendukung kebutuhan reporting dan analisis. Posisi ini cocok untuk fresh graduate atau junior analyst yang ingin berkembang di industri F&B dan retail dengan skala operasional nasional.",
        "requirements": [
            "Minimal S1 di bidang Statistika, Matematika, Ilmu Komputer, atau setara",
            "Pengalaman 0-1 tahun sebagai Data Analyst (fresh graduate dipersilahkan)",
            "Proficiency di SQL dan data manipulation",
            "Familiar dengan tools visualisasi data (Power BI, Tableau, atau Looker)",
            "Pemahaman dasar tentang data warehouse dan ETL process",
            "Analitis dan detail-oriented",
            "Kemampuan komunikasi data secara verbal dan tulisan"
        ],
        "responsibilities": [
            "Menarik data dari berbagai sumber ke dalam data warehouse",
            "Berkoordinasi dengan berbagai fungsi untuk kebutuhan data mereka",
            "Membuat dashboard dan laporan untuk mendukung pengambilan keputusan",
            "Melakukan data cleaning dan validasi untuk memastikan akurasi data",
            "Menganalisis data penjualan, inventori, dan operasional",
            "Menyusun rekomendasi berbasis data untuk tim bisnis"
        ],
        "benefits": [
            "Bergabung dengan perusahaan F&B terbesar di Indonesia",
            "Exposure ke data operasional skala nasional",
            "Program pelatihan dan pengembangan skill data",
            "BPJS Ketenagakerjaan dan Kesehatan",
            "Jenjang karir yang jelas di bidang data analytics"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan PT Sarimelati Kencana Tbk. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/junior-data-analyst-at-pt-sarimelati-kencana-tbk-4274081191",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/junior-data-analyst-at-pt-sarimelati-kencana-tbk-4274081191",
        "featured": False
    },
    {
        "slug": "b2b-sales-executive-kulina-jakarta",
        "title": "B2B Sales Executive",
        "company": "Kulina",
        "location": "Jakarta",
        "type": "Full-time",
        "category": "Marketing",
        "salary": "Rp 6-12 Juta",
        "posted": today,
        "expires": expires,
        "description": "Kulina, startup foodtech asal Indonesia yang fokus pada layanan katering korporat dan subscription meal plan, sedang mencari B2B Sales Executive yang energik untuk memperluas jangkauan bisnis. Kamu akan menjadi ujung tombak dalam mengakuisisi dan mengelola klien korporat untuk layanan B2B Kulina. Posisi ini cocok buat kamu yang memiliki jiwa entrepreneur, suka tantangan, dan ingin menjadi bagian dari startup yang mengubah cara orang Indonesia makan. Dengan lingkungan kerja yang fast-paced dan kolaboratif, kamu akan punya kesempatan besar untuk berkembang bersama perusahaan.",
        "requirements": [
            "Minimal 1-2 tahun pengalaman di Sales, Business Development, atau Account Management",
            "Pengalaman di B2B sales (lebih disukai F&B atau korporat)",
            "Kemampuan negosiasi dan komunikasi yang excellent",
            "Target-oriented dan self-motivated",
            "Memiliki SIM dan kendaraan pribadi untuk field visit",
            "Pengalaman menggunakan CRM tools (HubSpot, Salesforce) nilai tambah",
            "S1 semua jurusan"
        ],
        "responsibilities": [
            "Mengidentifikasi dan mengakuisisi klien korporat baru untuk B2B catering",
            "Melakukan presentasi, negosiasi, dan closing deals dengan calon klien",
            "Mengelola hubungan dengan klien existing untuk memastikan retensi",
            "Mengatur jadwal trial meeting dan product sampling",
            "Mencapai target revenue bulanan yang sudah ditentukan",
            "Berkolaborasi dengan tim operasional untuk kelancaran delivery"
        ],
        "benefits": [
            "Bergabung di startup foodtech yang sedang growing fast",
            "Kompetitif gaji pokok plus komisi sales",
            "Pengalaman bekerja di lingkungan startup yang dinamis",
            "Kesempatan pengembangan karir cepat",
            "BPJS Ketenagakerjaan dan Kesehatan"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan Kulina. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/b2b-sales-executive-at-kulina-4322762874",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/b2b-sales-executive-at-kulina-4322762874",
        "featured": False
    }
]

# Read existing data
with open('/tmp/maulud-net/loker/lowongan.json') as f:
    data = json.load(f)

# Insert new jobs at the beginning (index 0)
for job in reversed(new_jobs):
    data['jobs'].insert(0, job)

# Write back
with open('/tmp/maulud-net/loker/lowongan.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"✅ Inserted {len(new_jobs)} new jobs (at index 0, preserving existing {len(data['jobs']) - len(new_jobs)} jobs)")
print(f"Total jobs now: {len(data['jobs'])}")