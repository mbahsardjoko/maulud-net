#!/usr/bin/env python3
"""Insert 6 new real job listings (found via web search) into lowongan.json."""
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE / 'loker' / 'lowongan.json'

POSTED = "2026-08-05"
EXPIRES = "2026-09-04"

NEW_JOBS = [
    {
        "slug": "content-writer-indoesports-jakarta",
        "title": "Content Writer",
        "company": "INDOESPORTS",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Konten & Kreatif",
        "salary": "Rp 5-9 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "INDOESPORTS, media yang fokus pada industri esports dan gaming di Indonesia, sedang membuka kesempatan bagi Content Writer untuk bergabung dengan tim redaksi. Dalam peran ini, kamu akan memproduksi artikel, berita, dan konten seputar dunia esports, turnamen, serta perkembangan industri gaming Tanah Air. Posisi ini cocok untuk penulis yang punya passion kuat di dunia gaming dan esports, serta mampu menyajikan informasi dengan gaya yang menarik dan mudah dicerna pembaca.",
        "requirements": [
            "Sedang di semester akhir (semester 7) atau fresh graduate dari jurusan Komunikasi, Jurnalistik, atau bidang terkait",
            "Keterampilan menulis yang baik dalam Bahasa Indonesia",
            "Passion dan pemahaman terhadap dunia esports dan gaming",
            "Mampu menulis berita, artikel, dan konten kreatif",
            "Teliti, cepat belajar, dan mampu bekerja dalam deadline",
            "Familiar dengan SEO dasar dan best practices konten online adalah nilai plus"
        ],
        "responsibilities": [
            "Menulis artikel, berita, dan konten seputar esports dan gaming",
            "Melakukan riset topik dan mengikuti perkembangan industri esports",
            "Berkolaborasi dengan tim redaksi dan editor",
            "Mengoptimalkan konten agar menarik dan mudah dibaca",
            "Membantu mengelola kalender konten dan ide topik baru"
        ],
        "benefits": [
            "Gaji kompetitif dan kesempatan berkembang di industri esports",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Pengalaman bekerja di media esports terkemuka",
            "Akses dan coverage ke event serta turnamen esports",
            "Lingkungan kerja yang dinamis dan penuh semangat",
            "Kesempatan membangun portofolio konten gaming"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/content-writer-at-indoesports-2852531181",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/content-writer-at-indoesports-2852531181",
        "featured": False
    },
    {
        "slug": "content-writer-b2b-tbwa-indonesia-jakarta",
        "title": "Content Writer (B2B Writer)",
        "company": "TBWA\\ Indonesia",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Konten & Kreatif",
        "salary": "Rp 6-12 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "TBWA\\ Indonesia, bagian dari jaringan agensi kreatif global TBWA, sedang mencari B2B Writer berbahasa Indonesia untuk memperkuat tim konten. Kamu akan menulis konten strategis untuk klien-klien B2B, mulai dari artikel, whitepaper, case study, hingga konten digital marketing. Peran ini menggabungkan kemampuan menulis dengan pemahaman strategi bisnis, cocok untuk penulis yang mampu menerjemahkan bahasa teknis menjadi konten yang mengedukasi namun tetap engaging.",
        "requirements": [
            "Pengalaman menulis konten B2B, corporate, atau copywriting",
            "Kemampuan menulis yang sangat baik dalam Bahasa Indonesia",
            "Pemahaman tentang strategi konten dan komunikasi bisnis",
            "Mampu menghasilkan konten sesuai panduan brand dan brief",
            "Detail-oriented dan mampu bekerja dengan banyak proyek",
            "Kemampuan Bahasa Inggris untuk membaca referensi adalah nilai plus"
        ],
        "responsibilities": [
            "Menulis konten B2B untuk berbagai klien TBWA\\ Indonesia",
            "Mengembangkan ide dan konsep konten yang strategis",
            "Berkolaborasi dengan strategist, desainer, dan account team",
            "Melakukan riset topik dan industri klien",
            "Menjaga konsistensi tone of voice dan kualitas konten",
            "Menyesuaikan draft berdasarkan feedback dan revisi"
        ],
        "benefits": [
            "Gaji kompetitif sesuai pengalaman",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Pengalaman di agensi kreatif jaringan global",
            "Exposure ke klien korporasi dan brand besar",
            "Lingkungan kerja kreatif dan kolaboratif",
            "Kesempatan pengembangan profesional dan jenjang karir"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/content-writer-at-tbwa-indonesia-—-powered-by-ai-driven-by-disruption-for-digital-growth-4325497609",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/content-writer-at-tbwa-indonesia-—-powered-by-ai-driven-by-disruption-for-digital-growth-4325497609",
        "featured": False
    },
    {
        "slug": "customer-service-mandarin-second-talent-remote",
        "title": "Customer Service Operations Support (Mandarin Speaker)",
        "company": "Second Talent",
        "location": "Remote, Indonesia",
        "type": "Full-time",
        "category": "Customer Service",
        "salary": "Rp 6-11 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "Second Talent membuka lowongan Customer Service Operations Support bagi talenta Indonesia yang fasih berbahasa Mandarin untuk ditempatkan bekerja secara remote. Kamu akan menjadi penghubung utama bagi klien berbahasa Mandarin melalui telepon, email, dan chat, membantu menjawab pertanyaan seputar status pengiriman, jadwal, dan berbagai pertanyaan logistik. Posisi ini cocok untuk kamu yang komunikatif, teliti, dan nyaman bekerja jarak jauh dengan tim internasional.",
        "requirements": [
            "Fasih berbahasa Mandarin (lisan dan tulisan)",
            "Kemampuan komunikasi yang sangat baik",
            "Pengalaman di bidang customer service atau operations support adalah nilai plus",
            "Teliti dan mampu menangani banyak pertanyaan secara bersamaan",
            "Nyaman bekerja remote dan mengatur waktu sendiri",
            "Kemampuan Bahasa Indonesia dan/atau Bahasa Inggris yang baik"
        ],
        "responsibilities": [
            "Menjadi titik kontak utama bagi klien berbahasa Mandarin",
            "Menjawab pertanyaan via telepon, email, dan chat",
            "Menangani pertanyaan seputar status pengiriman, jadwal, dan logistik",
            "Mendokumentasikan interaksi dan feedback pelanggan",
            "Berkolaborasi dengan tim operasional untuk menyelesaikan masalah",
            "Menjaga tingkat kepuasan pelanggan yang tinggi"
        ],
        "benefits": [
            "Gaji kompetitif + bekerja 100% remote dari Indonesia",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Pengalaman bekerja dengan tim dan klien internasional",
            "Fleksibilitas lokasi kerja",
            "Pengembangan keterampilan bahasa dan komunikasi",
            "Kesempatan berkembang di perusahaan talent global"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/customer-service-operations-support-mandarin-speaker-remote-indonesian-talent-at-second-talent-4293711997",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/customer-service-operations-support-mandarin-speaker-remote-indonesian-talent-at-second-talent-4293711997",
        "featured": False
    },
    {
        "slug": "finance-accountant-pt-gerbang-watugunung-jakarta",
        "title": "Finance Accountant",
        "company": "PT Gerbang Watugunung Niaga",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Finance",
        "salary": "Rp 7-12 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "PT Gerbang Watugunung Niaga, perusahaan yang bergerak di bidang perdagangan dan distribusi, sedang mencari Finance Accountant untuk bergabung dengan tim keuangan di Jakarta. Kamu akan bertanggung jawab atas koordinasi dan pelaksanaan rekonsiliasi akun, pencatatan transaksi keuangan, serta penyusunan laporan agar akurat dan tepat waktu. Posisi ini cocok untuk profesional akuntansi yang detail-oriented dan memahami standar akuntansi Indonesia.",
        "requirements": [
            "Sarjana (S1) Akuntansi atau bidang terkait",
            "Pengalaman 1-3 tahun sebagai accountant atau finance staff",
            "Pemahaman kuat tentang prinsip dan standar akuntansi (SAK/PSAK)",
            "Menguasai Microsoft Excel dan software akuntansi (jurnal, accurate, dll)",
            "Kemampuan melakukan rekonsiliasi akun dan analisis data keuangan",
            "Teliti, jujur, dan mampu bekerja dalam tenggat waktu",
            "Bersedia bekerja di Jakarta"
        ],
        "responsibilities": [
            "Koordinasi dan pelaksanaan rekonsiliasi akun",
            "Mencatat dan memverifikasi transaksi keuangan harian",
            "Menyusun laporan keuangan bulanan dan tahunan",
            "Mengelola dokumen dan administrasi akuntansi",
            "Membantu proses closing dan audit internal",
            "Berkolaborasi dengan tim finance, tax, dan operasional"
        ],
        "benefits": [
            "Gaji kompetitif sesuai pengalaman",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "THR dan tunjangan lainnya",
            "Pengalaman bekerja di perusahaan perdagangan yang stabil",
            "Kesempatan pengembangan karir di bidang keuangan",
            "Lingkungan kerja profesional dan suportif"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/finance-accountant-at-pt-gerbang-watugunung-niaga-3995829455",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/finance-accountant-at-pt-gerbang-watugunung-niaga-3995829455",
        "featured": False
    },
    {
        "slug": "graphic-designer-rocketindo-jakarta",
        "title": "Graphic Designer",
        "company": "Rocketindo",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Desain",
        "salary": "Rp 7-14 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "Rocketindo, digital marketing agency yang fokus mendukung brand lokal dan internasional memasarkan produk di Indonesia, sedang mencari Graphic Designer. Kamu akan menciptakan visual design untuk berbagai kebutuhan klien — mulai dari konten media sosial, materi iklan, hingga aset brand. Posisi ini cocok untuk desainer yang kreatif, menguasai tool desain, dan mampu menerjemahkan brief menjadi visual yang menarik dan sesuai identitas brand klien.",
        "requirements": [
            "Pengalaman sebagai Graphic Designer (minimal 1 tahun, diutamakan)",
            "Menguasai Adobe Creative Suite (Photoshop, Illustrator, dll)",
            "Memahami prinsip desain, tipografi, dan komposisi",
            "Mampu bekerja dengan brief dan menjaga konsistensi brand",
            "Familiar dengan Figma adalah nilai plus",
            "Kreatif, teliti, dan mampu bekerja dalam deadline",
            "Portofolio desain yang relevan"
        ],
        "responsibilities": [
            "Membuat visual design untuk kebutuhan klien",
            "Mendesain konten media sosial, iklan, dan materi promosi",
            "Mengembangkan aset brand sesuai guidelines",
            "Berkolaborasi dengan tim kreatif, copywriter, dan account",
            "Menyesuaikan desain berdasarkan feedback dan revisi",
            "Menjaga kualitas dan konsistensi visual di semua kanal"
        ],
        "benefits": [
            "Gaji kompetitif (Rp 7-14 Juta) sesuai pengalaman",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Pengalaman bekerja dengan berbagai klien dan industri",
            "Lingkungan kerja yang kreatif dan dinamis",
            "Kesempatan mengembangkan portofolio profesional",
            "Jenjang karir di agency digital marketing"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/graphic-designer-at-rocketindo-3902659296",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/graphic-designer-at-rocketindo-3902659296",
        "featured": True
    },
    {
        "slug": "brand-marketing-specialist-erajaya-north-jakarta",
        "title": "Brand Marketing Specialist",
        "company": "Erajaya Active Lifestyle",
        "location": "North Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Marketing",
        "salary": "Rp 8-15 Juta",
        "posted": POSTED,
        "expires": EXPIRES,
        "description": "Erajaya Active Lifestyle, bagian dari grup Erajaya yang fokus pada lifestyle dan gadget, sedang membuka lowongan Brand Marketing Specialist di Jakarta Utara. Kamu akan bertanggung jawab merancang dan mengeksekusi strategi pemasaran brand, membangun brand awareness, dan mendukung pertumbuhan bisnis. Posisi ini cocok untuk profesional marketing yang kreatif, memahami perilaku pasar, dan mampu mengelola kampanye dari konsep hingga eksekusi.",
        "requirements": [
            "Pengalaman 2-4 tahun di bidang brand marketing atau marketing",
            "Pemahaman tentang brand management dan strategi pemasaran",
            "Kemampuan merancang dan mengeksekusi kampanye marketing",
            "Familiar dengan digital marketing dan social media",
            "Mampu menganalisis data dan performa kampanye",
            "Kemampuan komunikasi dan kolaborasi lintas tim yang baik",
            "Bersedia bekerja di Jakarta Utara"
        ],
        "responsibilities": [
            "Merancang dan mengeksekusi strategi pemasaran brand",
            "Mengelola kampanye brand awareness dan promosi",
            "Berkolaborasi dengan tim kreatif, media, dan sales",
            "Memonitor performa kampanye dan menganalisis hasil",
            "Melakukan riset pasar dan kompetitor",
            "Mengelola anggaran marketing dan program promosi",
            "Menjaga konsistensi brand di semua touchpoint"
        ],
        "benefits": [
            "Gaji kompetitif sesuai pengalaman",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Bonus dan tunjangan kinerja",
            "Pengalaman bekerja di perusahaan lifestyle terkemuka",
            "Kesempatan mengelola brand dengan eksposur besar",
            "Lingkungan kerja profesional dengan jenjang karir jelas"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://www.linkedin.com/jobs/view/4373331053/",
        "source": "LinkedIn",
        "source_url": "https://www.linkedin.com/jobs/view/4373331053/",
        "featured": False
    },
]

with open(DB_PATH) as f:
    data = json.load(f)

jobs = data['jobs']
existing_slugs = {j['slug'] for j in jobs}
existing_urls = {j.get('source_url') for j in jobs if j.get('source_url')}

added = []
for job in NEW_JOBS:
    if job['slug'] in existing_slugs:
        print(f"SKIP (dup slug): {job['slug']}")
        continue
    if job['source_url'] in existing_urls:
        print(f"SKIP (dup url): {job['slug']}")
        continue
    jobs.insert(0, job)
    existing_slugs.add(job['slug'])
    existing_urls.add(job['source_url'])
    added.append(job['slug'])

# Ensure categories is a proper array (never null)
cats = [j['category'] for j in jobs if j.get('category')]
data['categories'] = sorted(set(cats))

with open(DB_PATH, 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added: {len(added)} jobs")
for s in added:
    print(" -", s)