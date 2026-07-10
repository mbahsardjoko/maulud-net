#!/usr/bin/env python3
"""Insert 5 new real job listings into lowongan.json at index 0."""
import json
import datetime

today = "2026-07-10"
expires = "2026-08-10"

new_jobs = [
    {
        "slug": "indonesia-2026-voyage-program-engineering-marriott",
        "title": "Indonesia 2026 Voyage Program - Engineering",
        "company": "Marriott International",
        "location": "Jakarta",
        "type": "Full-time",
        "category": "Administrasi",
        "salary": "Rp 6-10 Juta",
        "posted": today,
        "expires": expires,
        "description": "Marriott International membuka program pengembangan kepemimpinan global Voyage 2026 untuk fresh graduate di bidang Engineering. Program full-time berbayar ini dirancang untuk lulusan universitas yang ingin memulai karir di industri perhotelan kelas dunia. Kamu akan menjalani pelatihan hands-on di hotel Marriott yang dikelola langsung, belajar dari para mentor berpengalaman, dan mengikuti kurikulum kepemimpinan terstruktur. Program ini mencakup rotasi di berbagai area engineering hotel seperti HVAC, kelistrikan, plumbing, dan perawatan gedung. Voyage adalah program bergengsi yang beroperasi di 50+ negara dan telah melahirkan banyak pemimpin di Marriott International.",
        "requirements": [
            "Fresh graduate S1 jurusan Teknik Mesin, Teknik Elektro, Teknik Industri, atau Teknik Sipil",
            "IPK minimal 3.00/4.00",
            "Memiliki passion di industri perhotelan dan hospitality",
            "Kemampuan komunikasi dan interpersonal yang baik",
            "Bahasa Inggris aktif (lisan dan tulisan)",
            "Bersedia menjalani program full-time selama 6-12 bulan di Jakarta"
        ],
        "responsibilities": [
            "Mengikuti program rotasi di berbagai divisi engineering hotel",
            "Mempelajari sistem manajemen perawatan gedung dan peralatan hotel",
            "Membantu tim engineering dalam operasional harian dan pemeliharaan preventif",
            "Berpartisipasi dalam proyek pengembangan dan renovasi properti hotel",
            "Menyusun laporan teknis dan dokumentasi perawatan",
            "Mengikuti sesi mentorship dan pengembangan kepemimpinan"
        ],
        "benefits": [
            "Gaji kompetitif + tunjangan",
            "Program pelatihan kepemimpinan global (Voyage)",
            "Mentor dari senior management hotel",
            "BPJS Ketenagakerjaan dan Kesehatan",
            "Kesempatan karir di jaringan Marriott International global",
            "Akomodasi dan meal allowance selama program"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman Indonesia 2026 Voyage Program - Engineering di Marriott International. Setelah submit online, selesaikan video interview yang akan dikirimkan tim rekrutmen. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/indonesia-2026-voyage-program-engineering-at-marriott-international-4437184038",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/indonesia-2026-voyage-program-engineering-at-marriott-international-4437184038",
        "featured": False
    },
    {
        "slug": "customer-service-pik-2-fit-hub",
        "title": "Customer Service - PIK 2",
        "company": "FIT HUB Indonesia",
        "location": "Tangerang",
        "type": "Full-time",
        "category": "Customer Service",
        "salary": "Rp 3-7 Juta",
        "posted": today,
        "expires": expires,
        "description": "FIT HUB, gym dan pusat kebugaran premium pertama di Indonesia dengan harga terjangkau, membuka lowongan Customer Service untuk lokasi PIK 2, Tangerang. Sebagai Customer Service di FIT HUB, kamu bukan hanya melayani member tapi juga menjadi cheerleader yang memotivasi mereka meraih tujuan fitnessnya. Kamu akan memberikan informasi mengenai produk dan layanan FIT HUB, menangani dan menyelesaikan pertanyaan member, serta memastikan setiap pengunjung mendapatkan pengalaman fitness yang luar biasa. Ini kesempatan bagus untuk membangun karir di industri kebugaran yang sedang booming di Indonesia.",
        "requirements": [
            "Pendidikan minimal SMA/SMK atau D3/S1 semua jurusan",
            "Pengalaman di bidang customer service atau hospitality (diutamakan)",
            "Komunikatif, ramah, dan memiliki attitude positif",
            "Menyukai interaksi dengan orang lain dan siap membantu",
            "Bersedia bekerja dengan sistem shift",
            "Berpenampilan rapi dan menarik",
            "Tinggal di area Tangerang atau sekitarnya"
        ],
        "responsibilities": [
            "Memberikan informasi mengenai produk, layanan, dan promo FIT HUB kepada member dan calon member",
            "Menangani registrasi member baru dan proses administrasi keanggotaan",
            "Menjawab pertanyaan dan menyelesaikan keluhan member dengan ramah dan profesional",
            "Memastikan area front desk dan lobby selalu rapi dan bersih",
            "Berkolaborasi dengan tim fitness dan sales untuk memberikan pengalaman terbaik bagi member",
            "Membantu operasional harian klub kebugaran"
        ],
        "benefits": [
            "Gaji pokok + insentif bulanan",
            "BPJS Ketenagakerjaan dan Kesehatan",
            "Free akses ke semua klub FIT HUB di Indonesia",
            "Pelatihan dan pengembangan karir",
            "Lingkungan kerja yang muda, energik, dan supportive",
            "Kesempatan berkembang di industri kebugaran"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman Customer Service - PIK 2 di FIT HUB Indonesia. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/customer-service-pik-2-at-fit-hub-4415106706",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/customer-service-pik-2-at-fit-hub-4415106706",
        "featured": False
    },
    {
        "slug": "human-resources-specialist-rocketindo",
        "title": "Human Resources Specialist",
        "company": "PT Rocketindo",
        "location": "Jakarta (Thamrin)",
        "type": "Full-time",
        "category": "Administrasi",
        "salary": "Rp 7-12 Juta",
        "posted": today,
        "expires": expires,
        "description": "Rocketindo, perusahaan teknologi yang membantu brand berkembang di pasar digital Indonesia, mencari Human Resources Specialist untuk bergabung di kantor pusat Thamrin, Jakarta. Kamu akan mendukung operasional people operations, memperkuat proses HR, dan membantu menciptakan tempat kerja yang terstruktur dan berkinerja tinggi. Posisi ini cocok untuk profesional HR yang ingin berkembang di lingkungan startup yang dinamis dan cepat berkembang. Kamu akan bekerja sama dengan tim manajemen untuk membangun fondasi SDM yang solid seiring pertumbuhan perusahaan.",
        "requirements": [
            "Pengalaman minimal 1-2 tahun di bidang Human Resources (generalist atau recruitment)",
            "Pemahaman tentang siklus HR: rekrutmen, onboarding, payroll, performance management",
            "Mahir menggunakan tools HR dan Microsoft Office/Google Workspace",
            "Pengetahuan tentang peraturan ketenagakerjaan Indonesia (UU Cipta Kerja)",
            "Komunikasi baik, teliti, dan mampu menjaga kerahasiaan data",
            "Berorientasi pada solusi dan mampu bekerja dalam tim",
            "Bersedia bekerja on-site di Thamrin, Jakarta"
        ],
        "responsibilities": [
            "Mengelola proses rekrutmen end-to-end: sourcing, screening, interview, offering",
            "Mengurus administrasi karyawan: kontrak, BPJS, absensi, payroll",
            "Membangun dan memelihara database karyawan serta dokumen HR",
            "Mendukung program onboarding dan offboarding karyawan",
            "Menjadi penghubung antara karyawan dan manajemen untuk isu-isu HR",
            "Membantu pengembangan kebijakan dan prosedur HR internal"
        ],
        "benefits": [
            "Gaji kompetitif Rp 7-12 juta per bulan (adjustable)",
            "BPJS Ketenagakerjaan dan Kesehatan",
            "Lingkungan kerja startup yang dinamis dan inklusif",
            "Kesempatan pengembangan karir dan pelatihan",
            "Tim yang kolaboratif dan suportif",
            "Lokasi kantor strategis di pusat Jakarta"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman Human Resources Specialist di Rocketindo. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/human-resources-specialist-at-rocketindo-4423153918",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/human-resources-specialist-at-rocketindo-4423153918",
        "featured": False
    },
    {
        "slug": "video-editor-ku-creatives-unlimited",
        "title": "Video Editor",
        "company": "Ku Creatives Unlimited",
        "location": "Jakarta",
        "type": "Full-time",
        "category": "Konten & Kreatif",
        "salary": "Rp 6-10 Juta",
        "posted": today,
        "expires": expires,
        "description": "Ku Creatives Unlimited, sebuah creative agency yang berbasis di Jakarta, mencari Video Editor berpengalaman untuk bergabung dengan tim kreatif mereka. Kamu akan bertanggung jawab mengedit footage video, membuat motion graphics untuk berbagai platform media sosial, dan menghasilkan konten video berkualitas tinggi untuk klien dari berbagai industri. Posisi ini cocok untuk video editor kreatif yang memiliki passion di dunia konten digital dan motion design. Ku Creatives Unlimited mengerjakan proyek-proyek untuk brand ternama di Indonesia dan regional.",
        "requirements": [
            "Pengalaman minimal 3 tahun sebagai Video Editor atau Motion Graphic Designer",
            "Mahir menggunakan Adobe Premiere Pro, After Effects, dan software editing lainnya",
            "Kreatif dalam storytelling visual dan pemilihan musik/efek",
            "Paham format dan tren video untuk media sosial (Instagram Reels, TikTok, YouTube Shorts)",
            "Mampu bekerja dalam tim dan memenuhi deadline",
            "Portfolio karya video wajib dilampirkan saat melamar"
        ],
        "responsibilities": [
            "Mengedit dan memproduksi konten video untuk berbagai platform",
            "Membuat motion graphics dan animasi untuk video sosial media dan iklan",
            "Melakukan color grading, audio mixing, dan efek visual",
            "Berkolaborasi dengan tim creative untuk mengembangkan konsep visual",
            "Memastikan output video sesuai dengan brand guideline klien",
            "Mengelola dan mengarsipkan file project dengan rapi"
        ],
        "benefits": [
            "Gaji kompetitif sesuai pengalaman",
            "BPJS Ketenagakerjaan dan Kesehatan",
            "Lingkungan kerja kreatif dan suportif",
            "Proyek klien brand ternama nasional & internasional",
            "Kesempatan pengembangan skill dan sertifikasi",
            "Fasilitas kantor yang nyaman di Jakarta"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman Video Editor di Ku Creatives Unlimited. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/video-editor-at-ku-creatives-unlimited-4425883490",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/video-editor-at-ku-creatives-unlimited-4425883490",
        "featured": False
    },
    {
        "slug": "ui-ux-designer-sinarmas-mining",
        "title": "UI/UX Designer (Project Based)",
        "company": "Sinarmas Mining",
        "location": "Jakarta",
        "type": "Contract",
        "category": "Desain",
        "salary": "Rp 8-15 Juta",
        "posted": today,
        "expires": expires,
        "description": "Sinarmas Mining, bagian dari Sinarmas Group yang bergerak di sektor pertambangan dan energi, mencari UI/UX Designer untuk mengerjakan proyek berbasis kontrak selama 6 bulan. Kamu akan merancang antarmuka web dan aplikasi yang responsif dan user-friendly untuk mendukung transformasi digital perusahaan pertambangan. Posisi ini menantang karena kamu akan mendesain solusi digital untuk industri yang unik, menggabungkan aspek teknis operasional tambang dengan user experience yang modern.",
        "requirements": [
            "Pengalaman minimal 2 tahun sebagai UI/UX Designer",
            "Portfolio yang menunjukkan kemampuan mendesain web dan aplikasi mobile",
            "Mahir menggunakan Figma, Adobe XD, atau Sketch",
            "Paham prinsip desain responsif dan design system",
            "Mampu melakukan user research dan usability testing",
            "Kreatif, detail-oriented, dan bisa bekerja dalam tim"
        ],
        "responsibilities": [
            "Merancang antarmuka pengguna (UI) yang responsif dan intuitif untuk web dan mobile",
            "Membuat wireframe, mockup, dan interactive prototype",
            "Melakukan user research dan usability testing untuk memvalidasi desain",
            "Berkolaborasi dengan developer dan product team untuk implementasi desain",
            "Mengembangkan dan memelihara design system perusahaan",
            "Menyajikan konsep desain kepada stakeholder internal"
        ],
        "benefits": [
            "Gaji proyek kompetitif",
            "BPJS Ketenagakerjaan dan Kesehatan",
            "Pengalaman kerja di perusahaan grup Sinarmas",
            "Portofolio proyek enterprise skala besar",
            "Lingkungan kerja profesional dan modern",
            "Jam kerja fleksibel (hybrid)"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman UI/UX Designer di Sinarmas Mining. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/ui-ux-designer-at-sinarmas-mining-4381439006",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/ui-ux-designer-at-sinarmas-mining-4381439006",
        "featured": True
    }
]

with open('loker/lowongan.json') as f:
    data = json.load(f)

# Insert at index 0
data['jobs'] = new_jobs + data['jobs']

# Recompute categories from all jobs to prevent null issue
cats = sorted(set(j['category'] for j in data['jobs'] if j.get('category')))
data['categories'] = cats

with open('loker/lowongan.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"OK: Inserted {len(new_jobs)} new jobs at top of lowongan.json")
print(f"Categories: {cats}")
for j in new_jobs:
    print(f"  - {j['slug']}")
