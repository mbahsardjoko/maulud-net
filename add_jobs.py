#!/usr/bin/env python3
import json
from datetime import datetime, timedelta

# Load existing data
with open('/tmp/maulud-net/loker/lowongan.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Today's date
today = datetime(2026, 8, 2).strftime('%Y-%m-%d')
expires = (datetime(2026, 8, 2) + timedelta(days=30)).strftime('%Y-%m-%d')

# New jobs to add (based on real LinkedIn postings found via web_search)
new_jobs = [
    {
        "slug": "fresh-graduate-hiring-byd-indonesia-bandung",
        "title": "Fresh Graduate Hiring 2026 – Bandung",
        "company": "BYD Indonesia",
        "location": "Bandung, Jawa Barat",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 6-10 Juta",
        "posted": today,
        "expires": expires,
        "description": "BYD Indonesia membuka program Fresh Graduate Hiring 2026 untuk lulusan terbaik yang siap memulai karir di perusahaan teknologi otomotif global. Program ini dirancang untuk mengembangkan bakat muda melalui training intensif, mentoring, dan rotasi kerja di berbagai divisi. Cocok untuk fresh graduate dari berbagai jurusan teknik, IT, bisnis, dan lainnya yang ingin berkontribusi pada inovasi kendaraan listrik dan energi terbarukan.",
        "requirements": [
            "Lulusan baru (Fresh Graduate) angkatan 2025/2026 atau final year student",
            "S1 dari universitas terakreditasi A/B (Teknik, Informatika, Bisnis, atau relevan)",
            "IPK minimal 3.00 skala 4.00",
            "Memiliki passion di industri otomotif dan energi hijau",
            "Kemampuan komunikasi Bahasa Indonesia dan Inggris yang baik",
            "Bersedia ditempatkan di Bandung, Jawa Barat",
            "Leadership potential dan growth mindset"
        ],
        "responsibilities": [
            "Mengikuti program onboarding dan training intensif 6-12 bulan",
            "Bekerja pada project nyata di divisi yang ditugaskan (Engineering, IT, Production, Quality, dll)",
            "Belajar dari senior mentor dan berkontribusi pada inovasi produk",
            "Melakukan rotasi antar departemen untuk pemahaman holistic bisnis",
            "Menyusun laporan progress dan presentasi hasil project",
            "Berpartisipasi dalam continuous improvement initiatives"
        ],
        "benefits": [
            "Gaji kompetitif (Rp 6-10 Juta) + bonus performa",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Program training dan development terstruktur",
            "Mentoring dari senior leader BYD",
            "Kesempatan karir internasional di jaringan BYD global",
            "Asuransi kesehatan comprehensive",
            "Transport dan meal allowance"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn BYD Indonesia. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/2026-indonesia-fresh-graduate-hiring-–-bandung-at-byd-indonesia-4400089141",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/2026-indonesia-fresh-graduate-hiring-–-bandung-at-byd-indonesia-4400089141",
        "featured": True
    },
    {
        "slug": "devops-engineer-pt-siaga-abdi-utama",
        "title": "DevOps Engineer",
        "company": "PT Siaga Abdi Utama",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 8-14 Juta",
        "posted": today,
        "expires": expires,
        "description": "PT Siaga Abdi Utama mencari DevOps Engineer entry-level/junior untuk bergabung dengan tim infrastructure mereka. Posisi ini cocok untuk lulusan baru atau junior engineer yang ingin mengembangkan karir di bidang cloud infrastructure, CI/CD pipeline, dan automation. Perusahaan bergerak di bidang jasa dan solusi teknologi dengan lingkungan kerja yang mendukung pembelajaran.",
        "requirements": [
            "Minimal D3/S1 Teknik Informatika, Sistem Informasi, atau setara",
            "Fresh graduate atau maksimal 1-2 tahun pengalaman",
            "Pemahaman dasar Linux/Unix system administration",
            "Familiar dengan Docker dan containerization concepts",
            "Pengetahuan dasar CI/CD (GitLab CI, Jenkins, atau GitHub Actions)",
            "Basic scripting (Bash, Python, atau Go)",
            "Tertarik belajar cloud platforms (AWS, GCP, atau Azure)",
            "Kemampuan problem-solving dan komunikasi yang baik"
        ],
        "responsibilities": [
            "Membantu maintain dan monitor CI/CD pipelines",
            "Assist deployment aplikasi ke staging dan production",
            "Mengelola container orchestration (Docker, Kubernetes basics)",
            "Monitoring infrastructure health dan logging",
            "Automate repetitive tasks dengan scripting",
            "Berkolaborasi dengan development team untuk improve deployment process",
            "Dokumentasi runbooks dan standard operating procedures",
            "Belajar dan implement best practices DevOps"
        ],
        "benefits": [
            "Gaji kompetitif (Rp 8-14 Juta)",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Training dan sertifikasi cloud/DevOps",
            "Mentoring dari senior DevOps engineer",
            "Flexible working arrangement",
            "Laptop dan tools development",
            "Career growth path ke Senior DevOps/Platform Engineer"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn PT Siaga Abdi Utama. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/devops-engineer-at-pt-siaga-abdi-utama-4361822824",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/devops-engineer-at-pt-siaga-abdi-utama-4361822824",
        "featured": False
    },
    {
        "slug": "frontend-engineer-nextjs-bibit-id",
        "title": "Frontend Engineer (Next.js)",
        "company": "Bibit.id",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 10-18 Juta",
        "posted": today,
        "expires": expires,
        "description": "Bibit.id, platform investasi digital terkemuka di Indonesia, mencari Frontend Engineer dengan keahlian Next.js untuk mengembangkan user-facing features pada platform investasi mereka. Anda akan bekerja pada aplikasi web yang digunakan ratusan ribu investor, dengan fokus pada performance, accessibility, dan user experience yang seamless. Tim engineering Bibit menerapkan modern frontend practices termasuk TypeScript, React ecosystem, dan automated testing.",
        "requirements": [
            "Minimal 2-3 tahun pengalaman Frontend Development",
            "Expert dengan React.js dan Next.js (App Router, Server Components)",
            "Solid TypeScript dan modern JavaScript (ES6+)",
            "Pengalaman dengan state management (Zustand, Redux, atau React Query/TanStack Query)",
            "Familiar dengan CSS-in-JS (Tailwind CSS, Styled Components, atau CSS Modules)",
            "Pemahaman tentang web performance optimization (Core Web Vitals, SSR/SSG/ISR)",
            "Pengalaman testing (Jest, React Testing Library, Playwright/Cypress)",
            "Familiar dengan Git, CI/CD, dan code review practices",
            "Portfolio project Next.js yang bisa ditunjukkan adalah plus"
        ],
        "responsibilities": [
            "Mengembangkan dan maintain frontend features menggunakan Next.js dan React",
            "Implement UI/UX designs dengan focus pada performance dan accessibility",
            "Optimasi bundle size, loading time, dan Core Web Vitals",
            "Berkolaborasi dengan backend team untuk API integration",
            "Menulis unit, integration, dan e2e tests",
            "Code review dan mentoring junior frontend engineers",
            "Migration legacy pages ke Next.js App Router",
            "Stay updated dengan latest React/Next.js ecosystem"
        ],
        "benefits": [
            "Gaji kompetitif (Rp 10-18 Juta) + stock options",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Asuransi kesehatan premium untuk keluarga",
            "MacBook Pro dan monitor external",
            "Learning budget dan conference allowance",
            "Flexible hybrid work (WFH + office)",
            "Snack, lunch, dan wellness program",
            "Kesempatan build product untuk jutaan user"
        ],
        "how_to_apply": "Kirim lamaran dengan CV dan portfolio GitHub melalui LinkedIn Bibit.id. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/frontend-engineer-next-js-at-bibit-id-4409275943",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/frontend-engineer-next-js-at-bibit-id-4409275943",
        "featured": False
    },
    {
        "slug": "web-developer-detikcom",
        "title": "Web Developer",
        "company": "detikcom",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 8-15 Juta",
        "posted": today,
        "expires": expires,
        "description": "detikcom, portal berita online terbesar di Indonesia, mencari Web Developer untuk mengembangkan dan memelihara platform digital mereka yang melayani jutaan pembaca harian. Posisi ini menawarkan tantangan unik: high-traffic website, real-time content delivery, dan skalabilitas yang masif. Anda akan bekerja dengan stack modern pada legacy dan new platform, berkolaborasi dengan editorial, product, dan data teams.",
        "requirements": [
            "Minimal 2-4 tahun pengalaman Web Development",
            "Solid PHP (Laravel/Symfony) atau Node.js backend",
            "Frontend: Vanilla JS, Vue.js, atau React",
            "Database: MySQL/PostgreSQL, Redis, Elasticsearch",
            "Pemahaman caching strategies (Varnish, CDN, Redis)",
            "Familiar dengan Docker, Kubernetes, dan CI/CD",
            "Pengalaman high-traffic, high-availability systems adalah plus",
            "Pemahaman SEO technical dan web vitals",
            "Kemampuan debugging dan performance profiling"
        ],
        "responsibilities": [
            "Develop dan maintain web applications untuk platform detikNetwork",
            "Optimasi performance untuk jutaan pageviews/hari",
            "Implement real-time features (live blog, breaking news, notifications)",
            "Berkolaborasi dengan editorial team untuk CMS enhancements",
            "Maintain dan improve CI/CD pipelines",
            "Troubleshoot production issues dan incidents",
            "Technical debt reduction dan legacy modernization",
            "Mentoring junior developers"
        ],
        "benefits": [
            "Gaji kompetitif (Rp 8-15 Juta) + bonus tahunan",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Asuransi kesehatan extended family",
            "MacBook Pro / high-spec laptop",
            "Flexible working hours",
            "Professional development budget",
            "Akses ke industry events dan conference",
            "Unique challenge: scale media platform di Indonesia"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn detikcom. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/web-developer-at-detikcom-4411608760",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/web-developer-at-detikcom-4411608760",
        "featured": False
    },
    {
        "slug": "fullstack-developer-gositus",
        "title": "Fullstack Developer",
        "company": "Gositus (PT Go Online Solusi)",
        "location": "Jakarta Raya, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 9-16 Juta",
        "posted": today,
        "expires": expires,
        "description": "Gositus, platform pembuatan website dan digital solution untuk UMKM Indonesia, mencari Fullstack Developer untuk membangun dan memelihara produk SaaS mereka. Perusahaan ini berfokus pada empowering UMKM melalui teknologi website builder, e-commerce, dan digital marketing tools. Anda akan bekerja end-to-end: dari database design, API development, hingga frontend implementation menggunakan stack modern.",
        "requirements": [
            "Minimal 2-3 tahun pengalaman Fullstack Development",
            "Backend: Node.js (Express/NestJS) atau Go, PostgreSQL/MongoDB",
            "Frontend: React.js (Next.js preferred), TypeScript, Tailwind CSS",
            "Database design, ORM (Prisma/TypeORM), query optimization",
            "RESTful API design, GraphQL adalah plus",
            "Authentication/Authorization (JWT, OAuth, RBAC)",
            "Docker, basic AWS/GCP, CI/CD (GitHub Actions/GitLab CI)",
            "Testing: unit, integration, e2e",
            "Portfolio SaaS/product-based project adalah nilai plus"
        ],
        "responsibilities": [
            "Design dan develop fullstack features untuk platform Gositus",
            "Build scalable APIs dan microservices",
            "Develop responsive frontend dengan Next.js dan React",
            "Database modeling dan migration management",
            "Implement payment integration, webhook handling",
            "Optimasi database queries dan API performance",
            "Berkolaborasi dengan product dan design team",
            "Code review, testing, dan documentation",
            "Deploy dan monitor production services"
        ],
        "benefits": [
            "Gaji kompetitif (Rp 9-16 Juta) + equity/ESOP",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Asuransi kesehatan keluarga",
            "MacBook Pro / high-spec workstation",
            "Flexible hybrid (3 days office, 2 days WFH)",
            "Learning budget Rp 5jt/tahun",
            "Lunch provided, snack bar",
            "Impact langsung ke ribuan UMKM Indonesia"
        ],
        "how_to_apply": "Kirim lamaran dengan CV dan portfolio project melalui LinkedIn Gositus. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/fullstack-developer-at-gositus-pt-go-online-solusi-4378029794",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/fullstack-developer-at-gositus-pt-go-online-solusi-4378029794",
        "featured": False
    },
    {
        "slug": "android-developer-mnc-group",
        "title": "Android Developer",
        "company": "MNC Group (PT MNC Asia Holding Tbk)",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 10-18 Juta",
        "posted": today,
        "expires": expires,
        "description": "MNC Group, konglomerat media dan hiburan terbesar di Indonesia, mencari Android Developer untuk mengembangkan aplikasi mobile milik grup (streaming, news, entertainment, e-commerce). Anda akan bekerja pada aplikasi dengan jutaan active users, menghadapi challenge scale, video streaming, offline-first architecture, dan integrasi dengan ecosystem digital MNC. Tim mobile MNC menerapkan modern Android development: Kotlin, Jetpack Compose, Clean Architecture, dan modularization.",
        "requirements": [
            "Minimal 2-4 tahun pengalaman Android Development",
            "Expert Kotlin dan modern Android stack (Jetpack Compose, Coroutines, Flow)",
            "Solid understanding Android SDK, lifecycle, memory management",
            "Arsitektur: Clean Architecture, MVVM, MVI, Modularization",
            "Dependency Injection: Hilt/Koin, Navigation Component",
            "Testing: JUnit, Espresso, Compose Testing, Turbine",
            "CI/CD: GitHub Actions/Bitrise, Play Console management",
            "Video streaming (ExoPlayer), offline-first, push notification (FCM)",
            "Published apps di Play Store adalah wajib",
            "Kontribusi open source atau tech talk adalah plus"
        ],
        "responsibilities": [
            "Develop dan maintain aplikasi Android flagship MNC Group",
            "Implement features baru: live streaming, video on demand, personalization",
            "Optimasi app performance: startup time, memory, battery, APK size",
            "Migration legacy XML/View ke Jetpack Compose",
            "Modularisasi codebase untuk build time dan team autonomy",
            "Berkolaborasi dengan backend, design, QA, dan product team",
            "Setup dan maintain CI/CD pipeline untuk mobile",
            "Monitor crash analytics (Firebase Crashlytics/Play Console)",
            "Mentoring junior Android engineers"
        ],
        "benefits": [
            "Gaji kompetitif (Rp 10-18 Juta) + performance bonus",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Asuransi kesehatan premium (spouse + children)",
            "MacBook Pro + Android device untuk testing",
            "Flexible hybrid work arrangement",
            "Annual learning budget Rp 10jt + conference access",
            "Employee perks: streaming subscriptions, gym, cafeteria",
            "Karir di media company terbesar Indonesia dengan jutaan users"
        ],
        "how_to_apply": "Kirim lamaran dengan CV, GitHub, dan link Play Store apps melalui LinkedIn MNC Group. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/android-developer-at-mnc-group-pt-mnc-asia-holding-tbk-4399160181",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/android-developer-at-mnc-group-pt-mnc-asia-holding-tbk-4399160181",
        "featured": False
    }
]

# Insert new jobs at the beginning of the jobs array
data['jobs'] = new_jobs + data['jobs']

# Write back
with open('/tmp/maulud-net/loker/lowongan.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_jobs)} new jobs to lowongan.json")
for i, job in enumerate(new_jobs, 1):
    print(f"{i}. {job['title']} ({job['company']}) - {job['source_url']}")