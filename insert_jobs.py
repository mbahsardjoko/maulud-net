import json
import sys

def main():
    # Read existing lowongan.json
    with open('/tmp/maulud-net/loker/lowongan.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # New job entries
    new_jobs = [
        {
            "slug": "senior-frontend-developer-indodax",
            "title": "Senior Frontend Developer",
            "company": "INDODAX - Indonesia Digital Asset Exchange",
            "location": "Jakarta Selatan, Indonesia",
            "type": "Full-time",
            "category": "Teknologi",
            "salary": "Rp 15-25 Juta",
            "posted": "2026-08-22",
            "expires": "2026-09-21",
            "description": "INDODAX (Indonesia Digital Asset Exchange) mencari Senior Frontend Developer untuk mengembangkan platform pertukaran aset digital mereka. Kandidat harus memiliki pengalaman dalam React, TypeScript, dan pengembangan antarmuka pengguna yang responsif.",
            "requirements": [
                "Minimal 4 tahun pengalaman sebagai Frontend Developer",
                "Mahir React.js, TypeScript, dan state management",
                "Pengalaman dengan testing frontend (Jest, React Testing Library)",
                "Memahami konsep UI/UX dan kolaborasi dengan desainer"
            ],
            "responsibilities": [
                "Mengembangkan dan memelihara fitur frontend platform INDODAX",
                "Kolaborasi dengan tim backend untuk integrasi API",
                "Melakukan code review dan mentoring junior developer",
                "Mengoptimasi performa aplikasi web"
            ],
            "benefits": [
                "Gaji kompetitif",
                "BPJS Kesehatan dan Ketenagakerjaan",
                "THR dan bonus tahunan",
                "Facility lunch dan transportasi"
            ],
            "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
            "apply_url": "https://id.linkedin.com/jobs/view/senior-frontend-developer-at-indodax-indonesia-digital-asset-exchange-4332240368",
            "source": "LinkedIn Indonesia",
            "source_url": "https://id.linkedin.com/jobs/view/senior-frontend-developer-at-indodax-indonesia-digital-asset-exchange-4332240368",
            "featured": False
        },
        {
            "slug": "backend-developer-makmur",
            "title": "Backend Developer",
            "company": "Makmur",
            "location": "Jakarta Raya, Indonesia",
            "type": "Full-time",
            "category": "Teknologi",
            "salary": "Rp 8-15 Juta",
            "posted": "2026-08-22",
            "expires": "2026-09-21",
            "description": "Makmur membuka posisi Backend Developer untuk mengembangkan layanan backend menggunakan Node.js, Express, dan TypeScript. Kandidat akan bekerja dalam tim teknologi untuk membangun sistem yang scalable dan reliable.",
            "requirements": [
                "Minimal 1 tahun pengalaman sebagai Backend Developer",
                "Mahir Node.js, Express, dan TypeScript",
                "Paham konsep RESTful API dan database (MySQL/MongoDB)",
                "Pengalaman dengan Git dan kolaborasi tim"
            ],
            "responsibilities": [
                "Mengembangkan dan memelihara layanan backend",
                "Mendesain dan mengimplementasikan API",
                "Kolaborasi dengan frontend team untuk integrasi",
                "Menulis dokumentasi teknis"
            ],
            "benefits": [
                "Gaji kompetitif",
                "BPJS Kesehatan dan Ketenagakerjaan",
                "THR dan bonus tahunan",
                "Fasilitas transportasi"
            ],
            "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
            "apply_url": "https://id.linkedin.com/jobs/view/backend-developer-at-makmur-4013960614",
            "source": "LinkedIn Indonesia",
            "source_url": "https://id.linkedin.com/jobs/view/backend-developer-at-makmur-4013960614",
            "featured": False
        },
        {
            "slug": "backend-developer-youtap-technology-ltd",
            "title": "Back End Developer",
            "company": "Youtap Technology Ltd",
            "location": "Jakarta, Indonesia",
            "type": "Full-time",
            "category": "Teknologi",
            "salary": "Rp 12-20 Juta",
            "posted": "2026-08-22",
            "expires": "2026-09-21",
            "description": "Youtap Technology Ltd mencari Back End Developer dengan pengalaman dalam pengembangan backend menggunakan Go dan NestJS. Kandidat akan terlibat dalam pembuatan sistem pembayaran dan layanan keuangan digital.",
            "requirements": [
                "Minimal 3 tahun pengalaman sebagai Backend Developer",
                "Mahir Go dan/atau NestJS (TypeScript)",
                "Paham konsep microservices dan API gateway",
                "Pengalaman dengan database relasional dan NoSQL",
                "Familiar dengan Docker dan Kubernetes"
            ],
            "responsibilities": [
                "Mengembangkan layanan backend berbasis Go/NestJS",
                "Mengimplementasikan dan mengelola API",
                "Kolaborasi dengan tim produk untuk fitur baru",
                "Memastikan keamanan dan performa sistem"
            ],
            "benefits": [
                "Gaji kompetitif",
                "BPJS Kesehatan dan Ketenagakerjaan",
                "THR dan bonus tahunan",
                "Asuransi kesehatan",
                "Fasilitas transportasi"
            ],
            "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
            "apply_url": "https://id.linkedin.com/jobs/view/back-end-developer-at-youtap-technology-ltd-4304604634?position=24&pageNum=0",
            "source": "LinkedIn Indonesia",
            "source_url": "https://id.linkedin.com/jobs/view/back-end-developer-at-youtap-technology-ltd-4304604634?position=24&pageNum=0",
            "featured": False
        },
        {
            "slug": "backend-developer-goodcommerce-co",
            "title": "Back End Developer",
            "company": "Goodcommerce.co",
            "location": "Jakarta Raya, Indonesia",
            "type": "Full-time",
            "category": "Teknologi",
            "salary": "Rp 10-18 Juta",
            "posted": "2026-08-22",
            "expires": "2026-09-21",
            "description": "Goodcommerce.co membuka posisi Back End Developer untuk mengembangkan platform micro-services. Kandidat akan bekerja secara remote atau dari kantor di Jakarta Raya.",
            "requirements": [
                "Minimal 2 tahun pengalaman sebagai Backend Developer",
                "Mahir dalam pembuatan micro-services",
                "Paham konsep REST dan GraphQL",
                "Pengalaman dengan Node.js atau Python",
                "Familiar dengan cloud services (AWS/GCP)"
            ],
            "responsibilities": [
                "Mengembangkan dan memelihara layanan backend",
                "Mendesain arkitektur micro-services",
                "Kolaborasi dengan tim frontend dan data",
                "Mengoptimasi performa dan skalabilitas sistem"
            ],
            "benefits": [
                "Gaji kompetitif",
                "BPJS Kesehatan dan Ketenagakerjaan",
                "THR dan bonus tahunan",
                "Asuransi kesehatan",
                "Fasilitas kerja remote"
            ],
            "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
            "apply_url": "https://id.linkedin.com/jobs/view/back-end-developer-at-goodcommerce-co-3481602853",
            "source": "LinkedIn Indonesia",
            "source_url": "https://id.linkedin.com/jobs/view/back-end-developer-at-goodcommerce-co-3481602853",
            "featured": False
        },
        {
            "slug": "content-writer-indoesports",
            "title": "Content Writer",
            "company": "INDOESPORTS",
            "location": "Jakarta Raya, Indonesia",
            "type": "Full-time",
            "category": "Konten & Kreatif",
            "salary": "Rp 6-12 Juta",
            "posted": "2026-08-22",
            "expires": "2026-09-21",
            "description": "INDOESPORTS mencari Content Writer untuk membuat konten olahraga dan berita terkait industri olahraga di Indonesia. Kandidat akan bertanggung jawab menulis artikel, news, dan konten media sosial.",
            "requirements": [
                "Minimal 2 tahun pengalaman sebagai Content Writer",
                "Mahir menulis dalam Bahasa Indonesia yang baik dan benar",
                "Paham konsep SEO dan content marketing",
                "Pengalaman dengan platform olahraga atau berita"
            ],
            "responsibilities": [
                "Menulis artikel olahraga harian",
                "Membuat konten untuk media sosial",
                "Melakukan riset topik olahraga terkini",
                "Kolaborasi dengan tim editing dan desain"
            ],
            "benefits": [
                "Gaji kompetitif",
                "BPJS Kesehatan dan Ketenagakerjaan",
                "THR dan bonus tahunan",
                "Asuransi kesehatan",
                "Fasilitas transportasi"
            ],
            "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
            "apply_url": "https://id.linkedin.com/jobs/view/content-writer-at-indoesports-2852531181?position=19&pageNum=0",
            "source": "LinkedIn Indonesia",
            "source_url": "https://id.linkedin.com/jobs/view/content-writer-at-indoesports-2852531181?position=19&pageNum=0",
            "featured": False
        },
        {
            "slug": "content-writer-tbwa-indonesia",
            "title": "Content Writer (B2B Writer)",
            "company": "TBWA Indonesia",
            "location": "Jakarta, Indonesia",
            "type": "Full-time",
            "category": "Konten & Kreatif",
            "salary": "Rp 8-15 Juta",
            "posted": "2026-08-22",
            "expires": "2026-09-21",
            "description": "TBWA Indonesia mencari B2B Writer yang能够 menulis konten bisnis dan teknis menjadi cerita yang menarik dan mudah dimengerti. Kandidat akan bekerja dengan klien dari berbagai industri untuk membuat konten marketing dan komunikasi.",
            "requirements": [
                "Minimal 3 tahun pengalaman sebagai Content Writer atau Copywriter",
                "Mahir menulis dalam Bahasa Indonesia dan Bahasa Inggris",
                "Paham konsep B2B marketing dan komunikasi teknis",
                "Pengalaman menulis untuk industri teknologi atau industri berat"
            ],
            "responsibilities": [
                "Menulis konten B2B seperti kasus studi, white paper, dan artikel teknis",
                "Membuat konten untuk kampanye marketing",
                "Melakukan wawancara dengan ahli dan sumber ahli",
                "Kolaborasi dengan tim kreatif dan account management"
            ],
            "benefits": [
                "Gaji kompetitif",
                "BPJS Kesehatan dan Ketenagakerjaan",
                "THR dan bonus tahunan",
                "Asuransi kesehatan",
                "Fasilitas transportasi"
            ],
            "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
            "apply_url": "https://id.linkedin.com/jobs/view/content-writer-at-tbwa-indonesia-—-powered-by-ai-driven-by-disruption-for-digital-growth-4325497609",
            "source": "LinkedIn Indonesia",
            "source_url": "https://id.linkedin.com/jobs/view/content-writer-at-tbwa-indonesia-—-powered-by-ai-driven-by-disruption-for-digital-growth-4325497609",
            "featured": False
        }
    ]
    
    # Insert new jobs at the beginning of the jobs array
    data['jobs'] = new_jobs + data['jobs']
    
    # Write back
    with open('/tmp/maulud-net/loker/lowongan.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Inserted {len(new_jobs)} new job(s) at the beginning of lowongan.json")

if __name__ == '__main__':
    main()