#!/usr/bin/env python3
import json

# Read the raw file with line-number prefixes
with open('/tmp/maulud-net/loker/lowongan.json', 'r') as f:
    raw = f.read()

# Strip the line-number prefixes like "1|", "2|", etc.
lines = raw.split('\n')
clean_lines = []
for line in lines:
    # Skip the trailing summary line if present
    if line.startswith('!!!End Patch'):
        continue
    # Remove leading "N|" prefix from read_file output
    if '|' in line:
        # Only strip if it starts with digits then pipe
        idx = line.find('|')
        prefix = line[:idx]
        if prefix.isdigit():
            line = line[idx+1:]
    clean_lines.append(line)

json_text = '\n'.join(clean_lines)

# Parse JSON
data = json.loads(json_text)

# New job entries to insert at index 0
new_jobs = [
    {
        "slug": "content-writer-cfactory-co",
        "title": "Content Writer",
        "company": "CFACTORY.CO",
        "location": "Jakarta Selatan",
        "type": "Full-time",
        "category": "Konten & Kreatif",
        "salary": "Rp 8-15 Juta",
        "posted": "2026-07-07",
        "expires": "2026-08-06",
        "description": "Menulis copy yang engaging dan sesuai dengan strategi brand. Content Writer akan bertanggung jawab mengembangkan konten untuk platform digital kami.",
        "requirements": [
            "Pengalaman 1-3 tahun di bidang content writing",
            "Kemampuan menulis dengan gaya berbeda sesuai channel",
            "Bisa menggunakan Canva atau tools desain dasar",
            "Punya portfolio tulisan yang bisa dilampirkan"
        ],
        "responsibilities": [
            "Membuat konten artikel untuk website dan blog",
            "Membuat caption untuk media sosial",
            "Menulis naskah video pendek",
            "Melakukan riset keyword untuk SEO",
            "Berkolaborasi dengan tim desain"
        ],
        "benefits": [
            "Gaji kompetitif",
            "BPJS Ketenagakerjaan",
            "Lingkungan kerja kreatif"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan Content Writer di CFACTORY.CO",
        "apply_url": "https://id.linkedin.com/jobs/view/content-writer-at-cfactory-co-4415112601",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/content-writer-at-cfactory-co-4415112601",
        "featured": False
    },
    {
        "slug": "customer-experience-bibit-id-contract",
        "title": "Customer Experience (Contract - Q1 2026)",
        "company": "Bibit.id",
        "location": "Jakarta",
        "type": "Contract",
        "category": "Customer Service",
        "salary": "Rp 7-12 Juta",
        "posted": "2026-07-07",
        "expires": "2026-08-06",
        "description": "Role Contract - Q1 2026. We are seeking a passionate Customer Experience professional with excellent communication skills",
        "requirements": [
            "Pengalaman di pelayanan pelanggan atau customer support",
            "Komunikasi ekselen bahasa Indonesia dan Inggris",
            "Empati tinggi dan kemampuan memecahkan masalah",
            "Struktur data kepuasan pelanggan"
        ],
        "responsibilities": [
            "Menangani inquiry dan complaint pelanggan",
            "Menganalisis feedback untuk perbaikan layanan",
            "Pelaporan kepuasan pelanggan kepada tim manajemen"
        ],
        "benefits": [
            "BPJS Ketenagakerjaan",
            "Asuransi kesehatan",
            "Flexible work arrangement"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman Customer Experience di Bibit.id",
        "apply_url": "https://id.linkedin.com/jobs/view/customer-experience-contract-bibit-id-4431075143",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/customer-experience-contract-bibit-id-4431075143",
        "featured": False
    },
    {
        "slug": "marriott-indonesia-voyage-program-sales-marketing-2026",
        "title": "Indonesia Voyage Program - Sales & Marketing",
        "company": "Marriott International",
        "location": "One Pacific Place 10th Floor Suite 10-12 (M1), Jakarta",
        "type": "Program",
        "category": "Marketing",
        "salary": "Rp 12-20 Juta",
        "posted": "2026-07-07",
        "expires": "2026-08-06",
        "description": "The Voyage Program is a full-time, paid development program. When you join Voyage, you gain access to Marriott's senior leaders and coaches and have many opportunities to grow in your career.",
        "requirements": [
            "Pendidikan S1 dari universitas terakreditasi",
            "Minat pada bidang hospitality atau retail",
            "Kemampuan kerja dalam tim",
            "Mentalitas belajar tinggi",
            "Bahasa Inggris lisan dan tulisan aktif"
        ],
        "responsibilities": [
            "Mengikuti program pelatihan intensif selama 12-18 bulan",
            "Bekerja di salah satu hotel Marriott di Indonesia",
            "Mengakses senior leaders melalui mentorship",
            "Mengembangkan jaringan profesional"
        ],
        "benefits": [
            "Gaji kompetitif + bonus",
            "BPJS lengkap",
            "Asuransi kesehatan",
            "Program pengembangan karier",
            "Produk hotel gratis selama pelatihan"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman Indonesia Voyage Program Sales & Marketing di Marriott International",
        "apply_url": "https://id.linkedin.com/jobs/view/indonesia-2026-voyage-program-sales-marketing-at-marriott-international-4437165794",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/indonesia-2026-voyage-program-sales-marketing-at-marriott-international-4437165794",
        "featured": True
    },
    {
        "slug": "product-marketing-intern-modena-indonesia",
        "title": "Product Marketing Intern",
        "company": "Modena Indonesia",
        "location": "Jakarta Selatan",
        "type": "Internship",
        "category": "Marketing",
        "salary": "Rp 3-5 Juta",
        "posted": "2026-07-07",
        "expires": "2026-08-06",
        "description": "Lamar lowongan kerja Product Marketing Intern di MODENA. Posisi Internship, min. sedang kuliah (final year), on-site di Jakarta Selatan",
        "requirements": [
            "S1 sedang berjalan atau baru lulus",
            "Minat pada pemasaran produk",
            "Kreativitas dan kemampuan analisis",
            "Bisa bekerja dalam tim",
            "Menguasai Microsoft Office"
        ],
        "responsibilities": [
            "Membantu persiapan dan pelaksanaan aktivitas Go-To-Market (GTM)",
            "Menyusun strategi pemasaran baru",
            "Menganalisis performa kampanye",
            "Berkolaborasi dengan tim product dan desain"
        ],
        "benefits": [
            "Pengalaman kerja di perusahaan internasional",
            "Mentoring dari senior marketer",
            "Referensi future career",
            "Mentor dan pencerahan",
            "Kerja stipend"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman Product Marketing Intern di Modena",
        "apply_url": "https://id.linkedin.com/jobs/view/product-marketing-intern-at-modena-inc-4435056099",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/product-marketing-intern-at-modena-inc-4435056099",
        "featured": False
    }
]

# Check for duplicate slugs
existing_slugs = {job.get('slug') for job in data.get('jobs', [])}
for job in new_jobs:
    if job['slug'] in existing_slugs:
        print(f"WARNING: slug {job['slug']} already exists!")

# Insert new jobs at index 0
data['jobs'] = new_jobs + data['jobs']

# Write back WITHOUT line-number prefixes (clean JSON)
with open('/tmp/maulud-net/loker/lowongan.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Inserted {len(new_jobs)} new jobs. Total jobs now: {len(data['jobs'])}")
