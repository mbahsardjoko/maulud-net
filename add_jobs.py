#!/usr/bin/env python3
"""Insert new job listings into lowongan.json at index 0."""
import json
from datetime import datetime, timedelta

today = datetime.now().strftime("%Y-%m-%d")
expires = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")

new_jobs = [
    {
        "slug": "backend-developer-asiatek-solusi-indonesia",
        "title": "Backend Developer",
        "company": "Asiatek Solusi Indonesia",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 12-20 Juta",
        "posted": today,
        "expires": expires,
        "description": "Asiatek Solusi Indonesia, perusahaan IT consulting yang fokus pada solusi perbankan digital, membuka lowongan Backend Developer untuk bergabung dengan tim pengembangan di Jakarta. Posisi ini menuntut pengalaman dalam pengembangan sistem backend berbasis Java dan Spring Boot, serta pemahaman mendalam tentang arsitektur microservices. Kamu akan terlibat dalam pengembangan dan pemeliharaan sistem perbankan skala enterprise yang melayani ribuan transaksi setiap harinya.",
        "requirements": [
            "S1 di bidang Ilmu Komputer, Sistem Informasi, Teknik Informatika, atau bidang terkait",
            "Minimal 3 tahun pengalaman sebagai Backend Developer",
            "Pengalaman wajib di industri perbankan atau fintech",
            "Mahir menggunakan Java, Spring Boot, dan JavaScript",
            "Pengalaman dengan Microservices dan Apache Kafka",
            "Pemahaman tentang RESTful API dan integrasi sistem",
            "Kemampuan problem solving dan analisis yang baik"
        ],
        "responsibilities": [
            "Mengembangkan dan memelihara sistem backend untuk aplikasi perbankan",
            "Merancang dan mengimplementasikan API dan microservices",
            "Berkolaborasi dengan tim frontend dan QA untuk integrasi sistem",
            "Melakukan code review dan memastikan kualitas kode",
            "Mengoptimalkan performa dan keamanan sistem backend"
        ],
        "benefits": [
            "Gaji kompetitif (Rp 12-20 Juta)",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Asuransi kesehatan tambahan",
            "Lingkungan kerja yang profesional",
            "Kesempatan pengembangan karir"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/backend-developer-at-asiatek-solusi-indonesia-4446053119",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/backend-developer-at-asiatek-solusi-indonesia-4446053119",
        "featured": True
    },
    {
        "slug": "internship-graphic-designer-seabank-indonesia",
        "title": "Internship Graphic Designer",
        "company": "SeaBank Indonesia",
        "location": "Jakarta, Indonesia",
        "type": "Internship",
        "category": "Desain",
        "salary": "Rp 3-5 Juta",
        "posted": today,
        "expires": expires,
        "description": "SeaBank Indonesia, bank digital yang berkembang pesat, membuka kesempatan magang untuk posisi Graphic Designer. Program magang ini berdurasi 6 bulan dengan jadwal kerja WFO (Work From Office) di kantor Jakarta. Cocok untuk mahasiswa tingkat akhir atau fresh graduate yang ingin mendapatkan pengalaman nyata di dunia desain grafis untuk industri perbankan digital.",
        "requirements": [
            "Mahasiswa tingkat akhir (tanpa kuliah offline) atau fresh graduate dari Jurusan Desain Komunikasi Visual, Seni Rupa, atau terkait",
            "Bersedia magang 6 bulan penuh dengan jadwal WFO di Jakarta",
            "Mulai bergabung Agustus 2026",
            "Memahami design hierarchy: tipografi, grid system, color combination",
            "Menguasai Adobe Photoshop, Illustrator, dan Figma",
            "Memiliki portofolio desain yang menarik"
        ],
        "responsibilities": [
            "Membuat aset desain untuk kebutuhan marketing digital",
            "Mendesain materi promosi termasuk banner, poster, dan konten media sosial",
            "Berkolaborasi dengan tim marketing dan brand",
            "Membantu menjaga konsistensi brand identity",
            "Mengikuti brief dan merealisasikan konsep desain"
        ],
        "benefits": [
            "Uang saku magang (Rp 3-5 Juta)",
            "Pengalaman kerja di bank digital terkemuka",
            "Sertifikat magang",
            "Bimbingan dari mentor profesional",
            "Relasi industri perbankan digital"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/internship-graphic-designer-at-seabank-indonesia-4446009430",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/internship-graphic-designer-at-seabank-indonesia-4446009430",
        "featured": False
    },
    {
        "slug": "intern-brand-content-marketing-disney-plus",
        "title": "Intern, Brand & Content Marketing (Disney+)",
        "company": "The Walt Disney Company",
        "location": "Jakarta, Indonesia",
        "type": "Internship",
        "category": "Marketing",
        "salary": "Rp 5-8 Juta",
        "posted": today,
        "expires": expires,
        "description": "The Walt Disney Company membuka lowongan Intern, Brand & Content Marketing untuk platform Disney+ Hotstar di Indonesia. Posisi ini akan mendukung kampanye marketing brand dan content, membantu koordinasi aset kreatif, bekerja sama dengan agency untuk mengelola aset campaign, serta memberikan dukungan strategis seperti mengembangkan brief dan mengumpulkan insight. Cocok untuk mahasiswa atau fresh graduate yang ingin merasakan pengalaman kerja di perusahaan hiburan kelas dunia.",
        "requirements": [
            "Mahasiswa aktif atau fresh graduate dari jurusan Marketing, Komunikasi, Bisnis, atau bidang terkait",
            "Minat kuat di bidang brand marketing dan content strategy",
            "Kemampuan komunikasi dan koordinasi yang baik",
            "Menguasai Microsoft Office (PowerPoint, Excel, Word)",
            "Kreatif dan detail-oriented",
            "Bersedia bekerja WFO di Jakarta"
        ],
        "responsibilities": [
            "Mendukung pelaksanaan kampanye brand dan content marketing untuk Disney+",
            "Membantu koordinasi pembuatan aset campaign dengan agency",
            "Mengumpulkan dan menganalisis data insight untuk campaign",
            "Membantu pengembangan brief kreatif",
            "Melakukan riset kompetitor dan tren industri hiburan"
        ],
        "benefits": [
            "Pengalaman kerja di perusahaan hiburan global terkemuka",
            "Uang saku magang kompetitif",
            "Sertifikat pengalaman internasional",
            "Networking dengan profesional industri kreatif",
            "Akses ke platform Disney+"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/intern-brand-content-marketing-disney+-jul-to-dec-2026-at-the-walt-disney-company-4382407207",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/intern-brand-content-marketing-disney+-jul-to-dec-2026-at-the-walt-disney-company-4382407207",
        "featured": False
    },
    {
        "slug": "creative-design-intern-wwf-indonesia",
        "title": "Creative Design Intern",
        "company": "WWF Indonesia",
        "location": "Jakarta, Indonesia",
        "type": "Internship",
        "category": "Desain",
        "salary": "Rp 3-5 Juta",
        "posted": today,
        "expires": expires,
        "description": "WWF-Indonesia, organisasi konservasi terkemuka, mencari Creative Design Intern untuk mendukung pengembangan konten visual dan digital yang meningkatkan engagement staf serta mendukung adopsi inisiatif baru. Posisi ini berada di bawah tim People & Culture dan akan fokus pada desain komunikasi internal. Cocok untuk mahasiswa atau fresh graduate yang ingin mengembangkan portofolio di bidang desain untuk organisasi non-profit berskala internasional.",
        "requirements": [
            "Mahasiswa aktif atau fresh graduate dari jurusan Desain Komunikasi Visual, Seni Rupa, atau bidang terkait",
            "Menguasai Adobe Creative Suite (Photoshop, Illustrator, InDesign)",
            "Kemampuan desain grafis dan layout yang baik",
            "Kreatif dan memiliki perhatian terhadap detail",
            "Memahami brand guidelines dan konsistensi visual",
            "Bersedia bekerja WFO di Jakarta"
        ],
        "responsibilities": [
            "Membuat konten visual digital untuk komunikasi internal",
            "Mendesain materi presentasi dan laporan",
            "Membantu pengembangan aset visual untuk kampanye internal",
            "Berkolaborasi dengan tim People & Culture",
            "Menjaga konsistensi brand identity WWF"
        ],
        "benefits": [
            "Uang saku magang kompetitif",
            "Pengalaman kerja di organisasi konservasi global",
            "Sertifikat magang",
            "Jaringan profesional di sektor lingkungan dan konservasi",
            "Kontribusi langsung pada misi pelestarian alam"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/creative-design-intern-at-wwf-indonesia-4319680479",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/creative-design-intern-at-wwf-indonesia-4319680479",
        "featured": False
    },
    {
        "slug": "accounting-staff-valbury-asia-group",
        "title": "Accounting Staff",
        "company": "Valbury Asia Group",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Finance",
        "salary": "Rp 6-9 Juta",
        "posted": today,
        "expires": expires,
        "description": "Valbury Asia Group, perusahaan jasa keuangan terkemuka di Indonesia, membuka lowongan Accounting Staff. Posisi ini bertanggung jawab dalam mendukung tugas akuntansi sehari-hari termasuk pembukuan, persiapan laporan keuangan, dan rekonsiliasi data. Cocok untuk lulusan akuntansi yang ingin memulai karir di industri keuangan yang dinamis dan profesional.",
        "requirements": [
            "S1 Akuntansi dari universitas terkemuka",
            "Memahami prinsip akuntansi dan standar pelaporan keuangan",
            "Menguasai Microsoft Excel dan software akuntansi",
            "Teliti, rapi, dan memiliki integritas tinggi",
            "Kemampuan analisis data yang baik",
            "Fresh graduate dipersilakan melamar"
        ],
        "responsibilities": [
            "Membantu tugas akuntansi harian termasuk pembukuan",
            "Mendukung persiapan laporan keuangan bulanan",
            "Melakukan rekonsiliasi bank dan data transaksi",
            "Membantu proses closing akuntansi bulanan",
            "Mengelola dokumen dan arsip keuangan"
        ],
        "benefits": [
            "Gaji kompetitif (Rp 6-9 Juta)",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Asuransi kesehatan",
            "Pelatihan dan pengembangan karir",
            "Lingkungan kerja profesional"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/accounting-staff-at-valbury-asia-group-4446043548",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/accounting-staff-at-valbury-asia-group-4446043548",
        "featured": False
    },
    {
        "slug": "content-creator-intern-red-comm-indonesia",
        "title": "Content Creator Intern (Japan Pop Culture)",
        "company": "RED Comm Indonesia",
        "location": "Jakarta, Indonesia",
        "type": "Internship",
        "category": "Konten & Kreatif",
        "salary": "Rp 3-5 Juta",
        "posted": today,
        "expires": expires,
        "description": "RED Comm Indonesia, agensi komunikasi dan kreatif, membuka lowongan Content Creator Intern dengan fokus pada Japanese Pop Culture. Posisi ini cocok untuk mahasiswa atau fresh graduate yang kreatif, aktif di media sosial, dan memiliki passion terhadap budaya pop Jepang (anime, manga, J-music, dll). Kamu akan bertanggung jawab memproduksi konten TikTok kreatif berdurasi pendek yang engaging dan relevan dengan tren terkini.",
        "requirements": [
            "Mahasiswa aktif atau fresh graduate dari jurusan Komunikasi, Desain, atau terkait",
            "Passion terhadap Japanese pop culture (anime, manga, J-pop, dll)",
            "Kreatif dan up-to-date dengan tren TikTok",
            "Pengalaman membuat konten video pendek (TikTok/Reels/Shorts)",
            "Kemampuan editing video dasar (CapCut, Premiere Pro, atau sejenisnya)",
            "Memiliki akun media sosial aktif"
        ],
        "responsibilities": [
            "Memproduksi konten TikTok kreatif tentang Japanese pop culture",
            "Membuat video pendek 15-30 detik yang engaging",
            "Riset tren dan referensi konten yang relevan",
            "Berkolaborasi dengan tim kreatif",
            "Mengelola jadwal posting dan engagement"
        ],
        "benefits": [
            "Uang saku magang (Rp 3-5 Juta)",
            "Pengalaman di industri kreatif dan PR",
            "Kebebasan berkreasi",
            "Portofolio konten profesional",
            "Networking dengan industri kreatif Jakarta"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/content-creator-intern-japan-pop-culture-at-red-comm-indonesia-4446007731",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/content-creator-intern-japan-pop-culture-at-red-comm-indonesia-4446007731",
        "featured": False
    }
]

# Read existing data
with open('loker/lowongan.json', 'r') as f:
    data = json.load(f)

# Insert new jobs at the beginning
data['jobs'] = new_jobs + data['jobs']

# Recompute categories from unique job categories
categories = sorted(list(set(j['category'] for j in data['jobs'] if j.get('category'))))
data['categories'] = categories

# Write back
with open('loker/lowongan.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Added {len(new_jobs)} new jobs at index 0")
print(f"   Total jobs now: {len(data['jobs'])}")
print(f"   Categories: {categories}")
for j in new_jobs:
    print(f"   - {j['title']} @ {j['company']} ({j['slug']})")
