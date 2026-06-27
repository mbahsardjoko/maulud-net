#!/usr/bin/env python3
import json
from datetime import datetime, timedelta

today = "2026-06-27"
expires = "2026-07-27"

new_jobs = [
    {
        "slug": "senior-frontend-engineer-olx-indonesia",
        "title": "Senior Frontend Engineer",
        "company": "OLX Indonesia",
        "location": "South Jakarta, Jakarta",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Kompetitif (standar industri tech Indonesia)",
        "posted": today,
        "expires": expires,
        "description": "OLX Indonesia, platform jual-beli terbesar di Indonesia yang merupakan bagian dari OLX Group global, sedang membuka lowongan Senior Frontend Engineer. Posisi ini bertanggung jawab merancang, membangun, dan memelihara aplikasi frontend berkualitas tinggi yang melayani jutaan pengguna di seluruh Indonesia. Kamu akan bekerja dalam tim engineering yang solid, menggunakan teknologi modern untuk menciptakan pengalaman pengguna yang cepat, responsif, dan andal. Cocok untuk engineer frontend senior yang ingin berdampak besar pada produk yang digunakan sehari-hari oleh puluhan juta orang Indonesia.",
        "requirements": [
            "Minimal 5 tahun pengalaman profesional sebagai Frontend Engineer",
            "Mahir menggunakan React.js, TypeScript, dan modern JavaScript (ES6+)",
            "Pengalaman mendalam dengan performance optimization, code splitting, dan lazy loading",
            "Pemahaman kuat tentang arsitektur frontend, state management, dan design patterns",
            "Berpengalaman dengan tools testing (Jest, React Testing Library, Cypress)",
            "Familiar dengan CI/CD pipeline dan version control (Git)",
            "Mampu melakukan code review dan mentoring engineer junior",
            "Komunikasi yang baik dan mampu berkolaborasi lintas tim dengan product manager, designer, dan backend engineer"
        ],
        "responsibilities": [
            "Merancang dan mengimplementasikan fitur frontend yang scalable dan maintainable",
            "Mengoptimalkan performa aplikasi untuk pengalaman pengguna terbaik di berbagai perangkat",
            "Berkolaborasi dengan tim produk dan desain dalam merancang solusi teknis",
            "Melakukan code review secara rutin dan menjaga standar kualitas kode",
            "Mengidentifikasi serta menyelesaikan bottleneck performa dan bug kompleks",
            "Berkontribusi dalam pengembangan design system dan komponen reusable",
            "Mentoring frontend engineer junior dalam pengembangan teknis"
        ],
        "benefits": [
            "Bekerja di platform jual-beli terbesar di Indonesia dengan dampak ke jutaan pengguna",
            "Lingkungan kerja dinamis dengan standar engineering global",
            "Kompensasi dan benefit kompetitif standar industri teknologi",
            "Akses ke teknologi modern dan stack terkini",
            "Kesempatan pengembangan karier dan pelatihan profesional",
            "Asuransi kesehatan dan tunjangan sesuai kebijakan perusahaan"
        ],
        "how_to_apply": "Kirim lamaran melalui halaman LinkedIn lowongan OLX Indonesia dengan klik tombol Lamar. Siapkan CV dan portofolio teknis yang relevan.",
        "apply_url": "https://www.linkedin.com/jobs/view/4429614855/",
        "source": "LinkedIn",
        "source_url": "https://www.linkedin.com/jobs/view/4429614855/",
        "featured": True
    },
    {
        "slug": "graphic-designer-web-dexa-group",
        "title": "Graphic Designer (Web Design)",
        "company": "Dexa Group",
        "location": "Tangerang Selatan, Banten",
        "type": "Full-time",
        "category": "Desain",
        "salary": "Kompetitif (sesuai standar industri farmasi)",
        "posted": today,
        "expires": expires,
        "description": "Dexa Group, salah satu perusahaan farmasi etikal terbesar di Indonesia yang telah berdiri sejak 1969, membuka lowongan Graphic Designer dengan fokus pada Web Design. Posisi ini akan bergabung dengan tim kreatif yang bertanggung jawab dalam menciptakan desain visual yang kuat dan relevan untuk kebutuhan digital perusahaan. Kamu akan mendesain website, landing page, aset digital marketing, dan materi brand identity yang mencerminkan kredibilitas Dexa Group sebagai pemimpin industri farmasi nasional. Cocok untuk desainer visual yang memiliki pemahaman mendalam tentang layout, tipografi, storytelling visual, dan desain responsif.",
        "requirements": [
            "Pendidikan minimal S1 Desain Komunikasi Visual (DKV), Interaction Design, atau bidang terkait",
            "Pengalaman 1-3 tahun sebagai Web Designer, Visual Designer, atau UI Designer",
            "Kemampuan menciptakan desain dengan identitas visual yang kuat sesuai brand",
            "Pemahaman kuat tentang layout, visual hierarchy, tipografi, dan storytelling visual",
            "Menguasai tools desain seperti Figma, Adobe Creative Suite (Photoshop, Illustrator, XD)",
            "Familiar dengan desain responsif dan prinsip UX dasar",
            "Portofolio yang menunjukkan karya desain web dan digital yang telah dipublikasikan"
        ],
        "responsibilities": [
            "Mendesain website dan landing page untuk berbagai kebutuhan perusahaan",
            "Membuat aset visual untuk kampanye digital marketing dan media sosial",
            "Merancang brand identity dan panduan visual untuk produk baru",
            "Berkolaborasi dengan tim marketing dan digital dalam pengembangan konten kreatif",
            "Memastikan konsistensi visual di seluruh touchpoint digital Dexa Group",
            "Mengikuti tren desain terkini dan menerapkannya sesuai kebutuhan brand"
        ],
        "benefits": [
            "Bergabung dengan perusahaan farmasi terbesar dan paling terpercaya di Indonesia",
            "Lingkungan kerja profesional dengan standar corporate yang baik",
            "Kesempatan mengembangkan portofolio di industri kesehatan dan farmasi",
            "Asuransi kesehatan dan BPJS Ketenagakerjaan",
            "Pengembangan karier di bidang desain digital dan brand identity"
        ],
        "how_to_apply": "Kirim lamaran melalui halaman LinkedIn lowongan Dexa Group. Pastikan portofolio desain web dan digital kamu sudah dilampirkan.",
        "apply_url": "https://id.linkedin.com/jobs/view/graphic-designer-at-dexa-group-4429373144",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/graphic-designer-at-dexa-group-4429373144",
        "featured": False
    },
    {
        "slug": "marketing-specialist-skintific",
        "title": "Marketing Specialist",
        "company": "SKINTIFIC",
        "location": "Jakarta",
        "type": "Full-time",
        "category": "Marketing",
        "salary": "Kompetitif (sesuai standar industri beauty)",
        "posted": today,
        "expires": expires,
        "description": "SKINTIFIC, brand skincare berbasis sains yang merevolusi industri kecantikan dengan produk-produk inovatif, sedang mencari Marketing Specialist untuk memperkuat tim pemasaran di Indonesia. Posisi ini akan bertanggung jawab dalam mengeksekusi strategi pemasaran yang berdampak, mendukung peluncuran produk baru, serta membangun kehadiran merek di platform digital. Kamu akan bekerja dalam lingkungan yang dinamis dan kreatif, berkolaborasi dengan tim brand, digital, dan sales untuk mencapai target pertumbuhan bisnis. Cocok untuk profesional marketing yang passion di industri beauty dan ingin berkembang di brand yang sedang naik daun.",
        "requirements": [
            "Minimal 2 tahun pengalaman di bidang marketing, brand management, atau peran serupa",
            "Pengalaman di industri beauty, skincare, atau FMCG menjadi nilai tambah",
            "Pemahaman tentang marketing funnel, digital advertising, dan social media strategy",
            "Kreatif, analitis, dan mampu mengelola multiple project secara simultan",
            "Kemampuan komunikasi dan presentasi yang baik",
            "Familiar dengan tools marketing analytics dan social media management",
            "Lulusan S1 Marketing, Komunikasi, atau bidang terkait"
        ],
        "responsibilities": [
            "Mengeksekusi strategi pemasaran untuk mendukung peluncuran produk dan campaign brand",
            "Mengelola konten marketing di berbagai channel digital dan offline",
            "Menganalisis performa campaign dan menyusun rekomendasi optimasi",
            "Berkolaborasi dengan tim kreatif, digital, dan sales untuk eksekusi program",
            "Melakukan riset pasar dan kompetitor untuk mengidentifikasi peluang pertumbuhan",
            "Mengelola budget marketing dan memastikan efisiensi pengeluaran",
            "Menyusun laporan berkala tentang performa marketing dan insight pasar"
        ],
        "benefits": [
            "Bekerja di brand skincare berbasis sains yang sedang berkembang pesat",
            "Lingkungan kerja kreatif, dinamis, dan fast-paced",
            "Produk skincare gratis untuk karyawan",
            "Kesempatan pengembangan karier di industri beauty yang terus tumbuh",
            "Kompensasi dan benefit kompetitif"
        ],
        "how_to_apply": "Kirim lamaran melalui halaman LinkedIn lowongan SKINTIFIC dengan klik tombol Lamar. Lampirkan CV dan portofolio campaign marketing yang pernah dikerjakan.",
        "apply_url": "https://id.linkedin.com/jobs/view/marketing-specialist-at-skintific-4429440152",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/marketing-specialist-at-skintific-4429440152",
        "featured": False
    },
    {
        "slug": "ui-ux-designer-sun-life",
        "title": "UI/UX Designer",
        "company": "Sun Life Indonesia",
        "location": "South Jakarta, Jakarta",
        "type": "Full-time",
        "category": "Desain",
        "salary": "Kompetitif (standar industri asuransi/finansial)",
        "posted": today,
        "expires": expires,
        "description": "Sun Life, perusahaan asuransi dan jasa keuangan global terkemuka yang telah beroperasi lebih dari 150 tahun, membuka lowongan UI/UX Designer untuk kantor pusatnya di Jakarta Selatan. Posisi ini akan bertanggung jawab merancang pengalaman pengguna yang intuitif dan menarik untuk produk digital Sun Life Indonesia, mulai dari website, portal nasabah, hingga aplikasi mobile. Kamu akan bekerja dalam tim yang berfokus pada pengalaman pelanggan, melakukan riset pengguna, membuat wireframe dan prototype, serta memastikan desain yang dihasilkan sesuai dengan standar brand dan kebutuhan bisnis. Cocok untuk desainer yang ingin berkontribusi pada transformasi digital industri jasa keuangan di Indonesia.",
        "requirements": [
            "Minimal 2-4 tahun pengalaman UI/UX design untuk produk digital",
            "Portofolio yang menunjukkan end-to-end design process untuk web dan mobile",
            "Mahir menggunakan Figma dan tools desain/prototyping modern",
            "Pengalaman mendesain produk enterprise, financial services, atau insurance menjadi nilai tambah",
            "Pemahaman tentang design system, accessibility, dan responsive design",
            "Kemampuan melakukan user research dan usability testing",
            "Komunikasi yang baik dalam Bahasa Indonesia dan Inggris"
        ],
        "responsibilities": [
            "Merancang antarmuka dan pengalaman pengguna untuk produk digital Sun Life",
            "Membuat wireframe, user flow, prototype, dan high-fidelity mockup",
            "Melakukan user research, usability testing, dan iterasi desain berbasis data",
            "Berkolaborasi dengan product manager, engineer, dan stakeholder bisnis",
            "Berkontribusi pada design system dan konsistensi pengalaman di seluruh produk",
            "Mendokumentasikan spesifikasi desain untuk tim engineering",
            "Mengikuti tren UI/UX terkini dan menerapkan best practice"
        ],
        "benefits": [
            "Bekerja di perusahaan asuransi dan jasa keuangan global dengan reputasi kuat",
            "Lingkungan kerja profesional dengan standar internasional",
            "Asuransi kesehatan dan benefit finansial bagi karyawan",
            "Program pengembangan profesional dan pelatihan berkelanjutan",
            "Kesempatan berkontribusi pada transformasi digital industri finansial"
        ],
        "how_to_apply": "Kirim lamaran melalui halaman LinkedIn lowongan Sun Life Indonesia. Pastikan portofolio desain UI/UX kamu sudah terpasang di profil atau dilampirkan.",
        "apply_url": "https://id.linkedin.com/jobs/view/ui-ux-designer-at-sun-life-4430894050",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/ui-ux-designer-at-sun-life-4430894050",
        "featured": False
    },
    {
        "slug": "data-engineer-bjak",
        "title": "Data Engineer",
        "company": "BJAK",
        "location": "Jakarta",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Kompetitif (sesuai standar industri fintech/insurtech)",
        "posted": today,
        "expires": expires,
        "description": "BJAK, perusahaan teknologi asuransi (insurtech) yang merevolusi industri asuransi di Indonesia melalui platform digital, sedang mencari Data Engineer untuk bergabung dengan tim data. Posisi ini akan bertanggung jawab merancang, membangun, dan memelihara infrastruktur data serta pipeline yang andal untuk mendukung kebutuhan analitik dan machine learning perusahaan. Kamu akan bekerja dengan data dalam skala besar, mengelola data warehouse, serta memastikan data berkualitas tinggi tersedia untuk tim product, business intelligence, dan data science. Cocok untuk data engineer yang ingin bekerja di lingkungan fast-paced dengan dampak langsung pada pertumbuhan bisnis.",
        "requirements": [
            "Minimal 3 tahun pengalaman sebagai Data Engineer, Backend Engineer (data-heavy), atau peran serupa",
            "Strong programming skills di Python dan/atau TypeScript",
            "SQL yang solid dan pengalaman dengan database relasional (PostgreSQL, MySQL)",
            "Pengalaman dengan tools ETL/ELT seperti Airflow, dbt, atau Luigi",
            "Familiar dengan cloud platforms (GCP, AWS, atau Azure) dan layanan data-nya",
            "Pengalaman dengan data warehousing (BigQuery, Snowflake, atau Redshift)",
            "Pemahaman tentang data modeling dan arsitektur data"
        ],
        "responsibilities": [
            "Merancang, membangun, dan memelihara pipeline data ETL/ELT dari berbagai sumber",
            "Mengelola dan mengoptimalkan data warehouse untuk kebutuhan analitik",
            "Berkolaborasi dengan tim data science dan business intelligence untuk menyediakan dataset siap pakai",
            "Menjaga kualitas dan integritas data melalui monitoring dan data validation",
            "Mengoptimasi performa query dan efisiensi penyimpanan data",
            "Mendokumentasikan arsitektur data dan pipeline untuk kebutuhan tim",
            "Mendukung pengambilan keputusan berbasis data di seluruh organisasi"
        ],
        "benefits": [
            "Bekerja di insurtech yang berkembang pesat dengan teknologi modern",
            "Lingkungan kerja fast-paced dengan banyak ruang untuk inovasi",
            "Akses ke data skala besar dan stack data modern",
            "Kompensasi dan benefit kompetitif",
            "Kesempatan pengembangan karier di bidang data engineering"
        ],
        "how_to_apply": "Kirim lamaran melalui halaman LinkedIn lowongan BJAK dengan klik tombol Lamar. Siapkan CV dan portofolio project data engineering yang relevan.",
        "apply_url": "https://www.linkedin.com/jobs/view/4412444753/",
        "source": "LinkedIn",
        "source_url": "https://www.linkedin.com/jobs/view/4412444753/",
        "featured": False
    },
    {
        "slug": "data-engineer-glints-batam",
        "title": "Data Engineer",
        "company": "Glints",
        "location": "Batam, Riau Islands",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Kompetitif (standar platform talent regional)",
        "posted": today,
        "expires": expires,
        "description": "Glints, platform talent dan career discovery terbesar di Asia Tenggara yang telah membantu jutaan profesional mengembangkan karier, membuka lowongan Data Engineer di Batam. Posisi ini akan bergabung dengan tim data untuk merancang, membangun, dan memelihara infrastruktur data serta pipeline yang menopang produk-produk Glints. Kamu akan bekerja erat dengan tim Product dan Engineering untuk memastikan data tersedia, akurat, dan siap digunakan untuk kebutuhan analytics, machine learning, dan pengambilan keputusan bisnis. Posisi ini menawarkan kesempatan untuk bekerja dengan data skala regional dan teknologi modern di lingkungan startup yang dinamis.",
        "requirements": [
            "Pengalaman sebagai Data Engineer atau peran serupa",
            "Strong SQL skills dan pengalaman dengan database relasional",
            "Pengalaman dengan bahasa pemrograman Python atau Scala",
            "Familiar dengan tools ETL/ELT seperti Airflow, Spark, atau Kafka",
            "Pengalaman dengan cloud platforms (AWS, GCP, atau Azure)",
            "Pemahaman tentang data warehousing dan data lake concepts",
            "Kemampuan problem-solving dan komunikasi yang baik"
        ],
        "responsibilities": [
            "Merancang dan membangun data pipeline untuk mengolah data dari berbagai sumber",
            "Memelihara dan mengoptimalkan infrastruktur data Glints",
            "Berkolaborasi dengan tim Product dan Engineering dalam kebutuhan data",
            "Memastikan kualitas, keandalan, dan keamanan data",
            "Mengelola data warehouse dan memastikan data siap untuk analitik",
            "Mendukung tim data science dan business intelligence dalam inisiatif data-driven",
            "Mendokumentasikan pipeline dan arsitektur data"
        ],
        "benefits": [
            "Bekerja di platform talent terbesar di Asia Tenggara",
            "Tim data yang solid dengan stack teknologi modern",
            "Lingkungan startup regional dengan exposure internasional",
            "Kompensasi dan benefit kompetitif",
            "Kesempatan pengembangan karier di perusahaan yang bertumbuh pesat"
        ],
        "how_to_apply": "Kirim lamaran melalui halaman LinkedIn lowongan Glints dengan klik tombol Lamar. Pastikan CV dan pengalaman data engineering kamu sudah terupdate.",
        "apply_url": "https://www.linkedin.com/jobs/view/4370204978/",
        "source": "LinkedIn",
        "source_url": "https://www.linkedin.com/jobs/view/4370204978/",
        "featured": False
    }
]

# Read existing data
with open('/tmp/maulud-net/loker/lowongan.json', 'r') as f:
    data = json.load(f)

# Insert new jobs at index 0
for job in reversed(new_jobs):
    data['jobs'].insert(0, job)

# Write back
with open('/tmp/maulud-net/loker/lowongan.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Successfully inserted {len(new_jobs)} new jobs at index 0")
print(f"Total jobs now: {len(data['jobs'])}")
