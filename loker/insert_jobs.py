#!/usr/bin/env python3
"""Insert new jobs at index 0 of lowongan.json jobs array."""
import json
import sys

with open('loker/lowongan.json', 'r') as f:
    data = json.load(f)

new_jobs = [
    {
        "slug": "front-end-developer-scout-inc-yogyakarta",
        "title": "Front End Developer",
        "company": "Scout.inc",
        "location": "Yogyakarta, Daerah Istimewa Yogyakarta",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Kompetitif (sesuai standar industri tech)",
        "posted": "2026-06-28",
        "expires": "2026-07-28",
        "description": "Scout.inc, perusahaan teknologi yang fokus pada pengembangan produk digital inovatif, sedang membuka lowongan untuk posisi Front End Developer yang akan ditempatkan di Yogyakarta. Posisi ini bertanggung jawab mengembangkan dan memelihara antarmuka pengguna yang responsif dan interaktif menggunakan teknologi web modern. Kamu akan bekerja dalam tim engineering yang kolaboratif untuk menciptakan pengalaman pengguna yang mulus dan engaging. Cocok untuk developer frontend yang memiliki passion di bidang UI/UX dan ingin berkembang di lingkungan perusahaan teknologi yang dinamis.",
        "requirements": [
            "Minimal 2 tahun pengalaman profesional sebagai Frontend Developer",
            "Mahir menggunakan React.js atau Vue.js beserta ekosistemnya",
            "Pemahaman kuat tentang HTML5, CSS3, dan JavaScript modern (ES6+)",
            "Pengalaman dengan responsive design dan mobile-first approach",
            "Familiar dengan version control (Git) dan tools pengembangan modern",
            "Mampu berkolaborasi dengan tim backend dan desain",
            "Pemahaman dasar tentang performa web dan accessibility",
            "Lulusan S1 Ilmu Komputer, Teknik Informatika, atau bidang terkait (diutamakan)"
        ],
        "responsibilities": [
            "Mengembangkan dan memelihara antarmuka pengguna menggunakan React.js/Vue.js",
            "Menerjemahkan desain dari Figma menjadi kode frontend yang responsif dan interaktif",
            "Berkolaborasi dengan tim backend untuk integrasi API",
            "Melakukan code review dan menjaga standar kualitas kode",
            "Mengoptimalkan performa aplikasi frontend untuk pengalaman pengguna terbaik",
            "Berpartisipasi dalam diskusi teknis dan perencanaan fitur"
        ],
        "benefits": [
            "Bekerja di perusahaan teknologi inovatif dengan tim engineering solid",
            "Lingkungan kerja yang mendukung pengembangan skill teknis",
            "Kesempatan mengerjakan proyek dengan teknologi modern",
            "Kompensasi dan benefit kompetitif standar industri tech",
            "Pengembangan karir yang jelas di bidang frontend engineering"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan Scout.inc. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/front-end-developer-yogyakarta-at-scout-inc-3493500390",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/front-end-developer-yogyakarta-at-scout-inc-3493500390",
        "featured": True
    },
    {
        "slug": "motion-graphic-designer-cnbc-indonesia",
        "title": "Motion Graphic Designer",
        "company": "CNBC Indonesia",
        "location": "Jakarta",
        "type": "Full-time",
        "category": "Desain",
        "salary": "Kompetitif (sesuai standar industri media)",
        "posted": "2026-06-28",
        "expires": "2026-07-28",
        "description": "CNBC Indonesia, salah satu portal berita bisnis dan ekonomi terkemuka di Indonesia yang merupakan bagian dari jaringan CNBC International, membuka lowongan untuk posisi Motion Graphic Designer. Posisi ini akan bergabung dengan tim kreatif yang bertanggung jawab menciptakan konten visual dinamis dan animasi berkualitas tinggi untuk kebutuhan editorial, iklan, dan kampanye digital. Kamu akan bekerja sama dengan tim redaksi dan pemasaran untuk menghasilkan motion graphic yang informatif, menarik, dan sesuai dengan standar jurnalisme visual CNBC. Cocok untuk desainer motion yang memiliki ketertarikan di dunia berita dan media.",
        "requirements": [
            "Minimal 2 tahun pengalaman sebagai Motion Graphic Designer (2D & 3D)",
            "Pendidikan minimal S1 Desain Grafis, Motion Design, Desain Komunikasi Visual, atau bidang terkait",
            "Mahir menggunakan Adobe After Effects, Premiere Pro, dan Cinema 4D atau Blender",
            "Pemahaman kuat tentang prinsip animasi, tipografi, dan komposisi visual",
            "Kreatif, detail-oriented, dan mampu bekerja dalam tenggat waktu yang ketat",
            "Portofolio yang menunjukkan karya motion graphic dan animasi",
            "Nilai tambah: pengalaman di industri media, berita, atau penyiaran"
        ],
        "responsibilities": [
            "Membuat motion graphic dan animasi untuk konten berita, video explainer, dan iklan",
            "Mendesain grafis untuk kebutuhan siaran TV, digital, dan media sosial",
            "Berkolaborasi dengan tim redaksi dan marketing dalam pengembangan konsep visual",
            "Menjaga konsistensi brand identity CNBC Indonesia di setiap konten visual",
            "Mengikuti tren desain motion terkini dan mengaplikasikannya pada karya",
            "Mengelola aset desain dan memastikan kelancaran produksi konten harian"
        ],
        "benefits": [
            "Bergabung dengan jaringan media bisnis global terkemuka",
            "Lingkungan kerja kreatif dan dinamis di industri media",
            "Kesempatan mengerjakan proyek dengan brand nasional dan internasional",
            "Pengembangan karier di bidang motion design dan visual storytelling",
            "Kompensasi dan benefit sesuai standar industri media"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan CNBC Indonesia. Lampirkan portofolio motion graphic dan animasi terbaru. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://www.linkedin.com/jobs/view/4424086584/",
        "source": "LinkedIn",
        "source_url": "https://www.linkedin.com/jobs/view/4424086584/",
        "featured": False
    },
    {
        "slug": "employer-social-media-specialist-tiket-com",
        "title": "Employer Social Media Specialist",
        "company": "tiket.com",
        "location": "Jakarta",
        "type": "Full-time",
        "category": "Marketing",
        "salary": "Kompetitif (sesuai standar industri travel tech)",
        "posted": "2026-06-28",
        "expires": "2026-07-28",
        "description": "tiket.com, platform travel dan lifestyle terkemuka di Indonesia yang merupakan bagian dari grup Global Tiket Network, membuka lowongan untuk posisi Employer Social Media Specialist. Posisi ini akan bertanggung jawab mengelola dan mengembangkan brand employer tiket.com di berbagai platform media sosial. Kamu akan menciptakan konten yang menarik untuk merekrut talenta terbaik, membangun employer branding, dan meningkatkan engagement dengan kandidat potensial. Cocok untuk kreatif konten yang paham strategi social media dan memiliki passion di bidang people & culture.",
        "requirements": [
            "Minimal 1-2 tahun pengalaman di social media management, content creation, atau employer branding",
            "Kemampuan membuat dan mendesain konten media sosial yang engaging (Canva, Adobe Suite, atau tools desain lainnya)",
            "Pemahaman tentang strategi social media, algoritma platform, dan community management",
            "Kreatif, up-to-date dengan tren media sosial terkini",
            "Kemampuan menulis copy yang menarik dalam Bahasa Indonesia dan Inggris",
            "Pengalaman dengan social media analytics tools",
            "Lulusan S1 Komunikasi, Marketing, atau bidang terkait"
        ],
        "responsibilities": [
            "Membuat dan mendesain konten social media untuk employer branding tiket.com",
            "Mengelola akun media sosial employer tiket.com di berbagai platform",
            "Membangun dan menjaga engagement dengan talent pool melalui konten kreatif",
            "Berkolaborasi dengan tim HR, recruitment, dan marketing untuk campaign branding",
            "Memantau performa konten dan menyusun laporan berkala",
            "Mengikuti tren employer branding dan social media terkini",
            "Mendukung event dan aktivitas employer branding online maupun offline"
        ],
        "benefits": [
            "Bekerja di platform travel tech terkemuka di Indonesia",
            "Lingkungan kerja yang dinamis, kreatif, dan kolaboratif",
            "Kesempatan mengembangkan karier di bidang employer branding dan social media",
            "Tim people & culture yang suportif",
            "Kompensasi dan benefit sesuai standar industri tech"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan tiket.com. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://www.linkedin.com/jobs/view/2811585937/",
        "source": "LinkedIn",
        "source_url": "https://www.linkedin.com/jobs/view/2811585937/",
        "featured": False
    },
    {
        "slug": "frontend-engineer-traveloka-jakarta",
        "title": "Frontend Engineer",
        "company": "Traveloka",
        "location": "Jakarta",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Kompetitif (sesuai standar unicorn Indonesia)",
        "posted": "2026-06-28",
        "expires": "2026-07-28",
        "description": "Traveloka, perusahaan teknologi travel terkemuka di Asia Tenggara yang telah menjadi unicorn, membuka lowongan untuk posisi Frontend Engineer yang akan ditempatkan di kantor pusat Jakarta. Posisi ini akan bergabung dengan tim engineering yang bertanggung jawab mengembangkan dan memelihara platform web Traveloka yang melayani jutaan pengguna di seluruh Asia Tenggara. Kamu akan bekerja dengan teknologi frontend modern, berkolaborasi dengan product manager dan desainer, serta berkontribusi pada pengalaman pengguna yang mulus dan cepat. Cocok untuk frontend engineer yang ingin berdampak besar pada produk yang digunakan jutaan orang setiap hari.",
        "requirements": [
            "Minimal 2-4 tahun pengalaman sebagai Frontend Engineer atau peran serupa",
            "Mahir menggunakan React.js dan TypeScript di production environment",
            "Pemahaman yang kuat tentang JavaScript modern (ES6+), HTML5, dan CSS3",
            "Pengalaman dengan state management (Redux, Zustand, atau Context API)",
            "Familiar dengan responsive design, CSS preprocessors, dan CSS-in-JS",
            "Pengalaman dengan frontend testing (Jest, React Testing Library, atau Cypress)",
            "Berpengalaman mengintegrasikan RESTful API dan GraphQL",
            "Pemahaman dasar tentang performa web (Core Web Vitals, lazy loading, code splitting)"
        ],
        "responsibilities": [
            "Mengembangkan dan memelihara fitur frontend untuk platform web Traveloka",
            "Berkolaborasi dengan product manager, desainer, dan backend engineer dalam pengembangan fitur",
            "Menulis kode yang bersih, teruji, dan mudah dipelihara",
            "Melakukan code review dan berbagi pengetahuan dengan tim",
            "Mengoptimalkan performa aplikasi untuk pengalaman pengguna terbaik",
            "Berkontribusi pada design system dan komponen reusable",
            "Mengikuti best practice frontend engineering dan teknologi terkini"
        ],
        "benefits": [
            "Bekerja di salah satu unicorn teknologi terbesar di Asia Tenggara",
            "Dampak langsung ke jutaan pengguna di berbagai negara",
            "Lingkungan kerja fast-paced dengan standar engineering global",
            "Akses ke teknologi dan stack terkini",
            "Kompensasi dan benefit kompetitif standar unicorn Indonesia",
            "Kesempatan pengembangan karier dan pembelajaran berkelanjutan"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan Traveloka. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://www.linkedin.com/jobs/view/4366403859",
        "source": "LinkedIn",
        "source_url": "https://www.linkedin.com/jobs/view/4366403859",
        "featured": True
    },
    {
        "slug": "full-stack-engineer-folkatech-jakarta",
        "title": "Full Stack Engineer",
        "company": "Folkatech",
        "location": "Jakarta (Area DKI Jakarta)",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Kompetitif (sesuai standar industri software development)",
        "posted": "2026-06-28",
        "expires": "2026-07-28",
        "description": "Folkatech, perusahaan software development yang telah dipercaya oleh berbagai bisnis di Indonesia, sedang membuka lowongan untuk posisi Full Stack Engineer. Posisi ini akan bergabung dengan tim pengembangan untuk merancang, membangun, dan memelihara aplikasi web end-to-end menggunakan berbagai teknologi modern. Kamu akan bekerja pada proyek-proyek yang beragam untuk klien dari berbagai industri, memberikan kesempatan untuk terus belajar dan mengembangkan kemampuan teknis. Cocok untuk developer yang versatile dan ingin bekerja di lingkungan yang mendukung pertumbuhan teknis.",
        "requirements": [
            "Minimal 2-3 tahun pengalaman sebagai Full Stack Developer atau Software Engineer",
            "Mahir dengan salah satu framework frontend modern (React.js, Vue.js, atau Angular)",
            "Pengalaman backend dengan Node.js, PHP (Laravel), atau Python (Django/Flask)",
            "Pemahaman tentang database relasional (MySQL, PostgreSQL) dan NoSQL",
            "Familiar dengan RESTful API design dan integrasi",
            "Pengalaman dengan Git dan workflow kolaborasi pengembangan",
            "Pemahaman dasar DevOps dan deployment (Docker, CI/CD menjadi nilai tambah)",
            "Lulusan S1 Ilmu Komputer atau bidang terkait (diutamakan)"
        ],
        "responsibilities": [
            "Mengembangkan fitur end-to-end dari frontend hingga backend",
            "Merancang dan membangun RESTful API yang scalable",
            "Berkolaborasi dengan tim desain dan product dalam perencanaan fitur",
            "Melakukan code review dan menjaga kualitas kode",
            "Melakukan troubleshooting, debugging, dan optimasi performa aplikasi",
            "Berkontribusi pada dokumentasi teknis dan best practice tim",
            "Berpartisipasi dalam proses deployment dan maintenance aplikasi"
        ],
        "benefits": [
            "Bekerja di software house dengan exposure ke berbagai industri dan proyek",
            "Lingkungan kerja yang mendukung pengembangan skill teknis",
            "Kesempatan belajar teknologi baru di setiap proyek",
            "Tim engineering yang solid dan kolaboratif",
            "Kompensasi dan benefit kompetitif standar industri software"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan Folkatech. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/full-stack-engineer-at-folkatech-3603675864",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/full-stack-engineer-at-folkatech-3603675864",
        "featured": False
    }
]

# Insert at index 0 (newest first)
data['jobs'] = new_jobs + data['jobs']

with open('loker/lowongan.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Successfully inserted {len(new_jobs)} new jobs at index 0")
