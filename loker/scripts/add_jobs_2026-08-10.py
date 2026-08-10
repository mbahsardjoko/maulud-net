#!/usr/bin/env python3
"""
Script to add 5 new job postings - 2026-08-10
Data sourced from LinkedIn web search results
"""

import json
from datetime import datetime, timedelta

# Load existing data
with open('/tmp/maulud-net/loker/lowongan.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Current date
posted_date = "2026-08-10"
expires_date = "2026-09-10"

# New job postings from LinkedIn search results
new_jobs = [
    {
        "slug": "backend-developer-sari-tirta-group",
        "title": "Backend Developer",
        "company": "Sari Tirta Group",
        "location": "Jakarta Raya, Indonesia",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 12-20 Juta",
        "posted": posted_date,
        "expires": expires_date,
        "description": "Sari Tirta Group mencari Backend Developer berpengalaman untuk memelihara, meningkatkan, dan memodernisasi sistem backend yang sudah ada. Kamu akan bekerja dengan teknologi modern seperti Golang, Java, dan JavaScript untuk membangun layanan backend yang scalable dan reliable. Posisi ini cocok untuk developer yang suka tantangan teknis dan ingin berkembang di perusahaan yang dinamis.",
        "requirements": [
            "Minimal 2-3 tahun pengalaman backend development",
            "Mahir dalam Golang, Java, atau JavaScript/Node.js",
            "Pengalaman maintaining dan modernizing existing systems",
            "Paham microservices architecture dan RESTful API",
            "Familiar dengan database SQL dan NoSQL (PostgreSQL, MongoDB, Redis)",
            "Pengalaman dengan Docker dan container orchestration",
            "Memahami CI/CD pipeline dan version control (Git)",
            "Problem solving yang baik dan kemampuan bekerja dalam tim",
            "Bersedia bekerja di Jakarta"
        ],
        "responsibilities": [
            "Memelihara dan mengoptimasi backend systems yang sudah ada",
            "Memodernisasi codebase legacy dengan best practices terbaru",
            "Mengembangkan RESTful API dan microservices",
            "Melakukan performance tuning dan optimization database",
            "Implementasi security measures dan data protection",
            "Code review dan mentoring junior developers",
            "Troubleshooting production issues dan bug fixing",
            "Dokumentasi teknis dan API documentation"
        ],
        "benefits": [
            "Gaji kompetitif Rp 12-20 Juta sesuai pengalaman",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "THR dan bonus tahunan",
            "Kesempatan upgrade skill dengan teknologi modern",
            "Lingkungan kerja yang supportive dan kolaboratif",
            "Work-life balance dengan flexible working hours"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/backend-developer-at-sari-tirta-group-4319892764",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/backend-developer-at-sari-tirta-group-4319892764",
        "featured": True
    },
    {
        "slug": "ui-ux-designer-glints",
        "title": "UI/UX Designer (Product Design)",
        "company": "Glints",
        "location": "Indonesia (Remote)",
        "type": "Full-time",
        "category": "Desain",
        "salary": "Rp 8-15 Juta",
        "posted": posted_date,
        "expires": expires_date,
        "description": "Glints mencari UI/UX Designer untuk membantu membentuk pengalaman platform food-tech berbasis subscription. Kamu akan berkolaborasi langsung dengan founder dan tim development untuk mentransformasi operasi real-world yang kompleks menjadi interface yang intuitif dan user-friendly. Posisi ini ideal untuk designer yang passionate tentang product design dan senang bekerja di startup environment.",
        "requirements": [
            "Minimal 2 tahun pengalaman sebagai UI/UX Designer atau Product Designer",
            "Portfolio yang kuat menunjukkan product design untuk web & mobile",
            "Mahir menggunakan Figma, Sketch, atau Adobe XD",
            "Paham user research, wireframing, dan prototyping",
            "Memahami design systems dan component-based design",
            "Familiar dengan usability testing dan user feedback iteration",
            "Kemampuan komunikasi yang baik untuk berkolaborasi dengan tim teknis",
            "Understanding tentang development constraints (HTML/CSS basics)",
            "Bisa bekerja remote dengan komunikasi yang efektif"
        ],
        "responsibilities": [
            "Merancang UI/UX untuk platform subscription-based food-tech",
            "Membuat wireframes, mockups, dan interactive prototypes",
            "Melakukan user research dan usability testing",
            "Berkolaborasi dengan founder dan developers untuk implementasi",
            "Membangun dan maintain design system untuk konsistensi",
            "Iterate designs berdasarkan user feedback dan data analytics",
            "Membuat design documentation dan style guides",
            "Present design decisions dan rationale ke stakeholders"
        ],
        "benefits": [
            "Gaji kompetitif Rp 8-15 Juta",
            "Full remote working - kerja dari mana saja",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Kesempatan shape product dari early stage",
            "Kerja langsung dengan founder dan decision makers",
            "Flexible working hours",
            "Budget untuk learning & development"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/ui-ux-designer-at-glints-4319890660",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/ui-ux-designer-at-glints-4319890660",
        "featured": False
    },
    {
        "slug": "digital-marketing-specialist-indodana",
        "title": "Digital Marketing Specialist",
        "company": "Indodana",
        "location": "Jakarta, Indonesia",
        "type": "Full-time",
        "category": "Marketing",
        "salary": "Rp 7-13 Juta",
        "posted": posted_date,
        "expires": expires_date,
        "description": "Indodana sedang mencari Digital Marketing Specialist untuk mengelola dan mengoptimasi kampanye digital marketing di berbagai platform. Kamu akan bertanggung jawab untuk meningkatkan brand awareness, engagement, dan conversion melalui strategi digital yang data-driven. Posisi ini cocok untuk marketer yang kreatif, analytical, dan selalu update dengan tren digital marketing terbaru.",
        "requirements": [
            "Minimal 2 tahun pengalaman di digital marketing",
            "Pengalaman mengelola kampanye di Google Ads, Facebook Ads, Instagram, TikTok",
            "Paham SEO, SEM, dan social media marketing strategies",
            "Kemampuan analisis data menggunakan Google Analytics, Facebook Insights",
            "Mahir copywriting untuk ads dan social media content",
            "Familiar dengan marketing automation tools",
            "Creative thinking dan problem solving",
            "Bisa bekerja dengan target dan deadline yang ketat",
            "Domisili Jakarta atau sekitarnya"
        ],
        "responsibilities": [
            "Merencanakan dan execute digital marketing campaigns di berbagai platform",
            "Mengelola budget iklan dan optimize ROI kampanye",
            "Membuat content strategy untuk social media dan paid ads",
            "Analisis performa kampanye dan buat actionable insights",
            "A/B testing untuk optimize conversion rate",
            "Koordinasi dengan creative team untuk assets kampanye",
            "Monitor kompetitor dan market trends",
            "Report hasil kampanye ke management secara berkala"
        ],
        "benefits": [
            "Gaji kompetitif Rp 7-13 Juta + bonus performa",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "THR dan annual bonus",
            "Kesempatan berkembang di perusahaan fintech terkemuka",
            "Budget untuk training dan certification",
            "Lingkungan kerja yang dinamis dan innovative",
            "Flexible working arrangement"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/digital-marketing-specialist-at-indodana-4433095288",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/digital-marketing-specialist-at-indodana-4433095288",
        "featured": False
    },
    {
        "slug": "content-writer-lengua",
        "title": "Content Writer",
        "company": "Lèngua",
        "location": "Jakarta Raya, Indonesia",
        "type": "Full-time",
        "category": "Konten & Kreatif",
        "salary": "Rp 5-9 Juta",
        "posted": posted_date,
        "expires": expires_date,
        "description": "Lèngua mencari Content Writer yang kreatif dan up-to-date dengan tren digital. Kamu akan bertanggung jawab membuat konten yang engaging untuk berbagai platform digital, mulai dari social media hingga blog dan website. Posisi ini perfect untuk writer yang paham pop culture, social media trends, dan bisa menghadirkan konten yang relevan dan menarik untuk audience Indonesia.",
        "requirements": [
            "Minimal 1-2 tahun pengalaman sebagai Content Writer atau Copywriter",
            "Portfolio tulisan yang menunjukkan versatility dan kreativitas",
            "Mahir Bahasa Indonesia dan English (writing proficiency)",
            "Paham grammar principles dan SEO writing",
            "Update dengan pop-culture dan digital content trends di Indonesia & global",
            "Familiar dengan social media trends dan cara transform jadi konten",
            "Kemampuan research dan fact-checking yang baik",
            "Bisa bekerja dengan deadline yang tight",
            "Domisili Jakarta atau bersedia commute"
        ],
        "responsibilities": [
            "Menulis konten untuk social media, blog, website, dan campaign",
            "Riset topik dan trending topics untuk content ideas",
            "Collaborate dengan creative team untuk content strategy",
            "Edit dan proofread konten sebelum publish",
            "Optimize konten untuk SEO dan engagement",
            "Monitor performa konten dan adjust strategy",
            "Maintain brand voice dan tone consistency",
            "Brainstorm creative content ideas dalam team meetings"
        ],
        "benefits": [
            "Gaji Rp 5-9 Juta sesuai pengalaman",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "Kesempatan develop portfolio dengan diverse projects",
            "Lingkungan kerja yang creative dan fun",
            "Flexible working hours",
            "Learning opportunities tentang content marketing",
            "Team outing dan company events"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/content-writer-at-lèngua-3830317284",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/content-writer-at-lèngua-3830317284",
        "featured": False
    },
    {
        "slug": "ui-ux-designer-pt-intikom-berlian-mustika",
        "title": "UI/UX Designer",
        "company": "PT. Intikom Berlian Mustika",
        "location": "Jakarta Raya, Indonesia",
        "type": "Full-time",
        "category": "Desain",
        "salary": "Rp 7-12 Juta",
        "posted": posted_date,
        "expires": expires_date,
        "description": "PT. Intikom Berlian Mustika membuka lowongan untuk UI/UX Designer dengan pengalaman 2-4 tahun. Kamu akan bertanggung jawab merancang user interface dan user experience untuk berbagai project digital. Posisi ini cocok untuk designer yang punya portfolio kuat dan ingin berkembang di perusahaan teknologi yang established dengan berbagai project menarik.",
        "requirements": [
            "Pengalaman 2-4 tahun sebagai UI/UX Designer atau UI Designer",
            "Portfolio yang kuat menunjukkan design projects",
            "Mahir Figma, Adobe XD, Sketch, atau tools sejenis",
            "Paham design principles, typography, dan color theory",
            "Pengalaman dengan user research dan usability testing",
            "Familiar dengan design systems dan component libraries",
            "Kemampuan membuat wireframes, mockups, dan prototypes",
            "Understanding basic HTML/CSS lebih disukai",
            "Bisa bekerja di Jakarta"
        ],
        "responsibilities": [
            "Merancang UI/UX untuk web dan mobile applications",
            "Membuat wireframes, user flows, dan interactive prototypes",
            "Conduct user research dan competitor analysis",
            "Collaborate dengan product managers dan developers",
            "Maintain dan develop design system",
            "Ensure consistency dalam visual design across products",
            "Present design concepts ke stakeholders",
            "Iterate designs berdasarkan feedback dan testing results"
        ],
        "benefits": [
            "Gaji Rp 7-12 Juta sesuai pengalaman",
            "BPJS Kesehatan dan Ketenagakerjaan",
            "THR dan bonus tahunan",
            "Kesempatan handle diverse projects",
            "Lingkungan kerja profesional",
            "Career development opportunities",
            "Modern office facilities"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/ui-ux-designer-at-pt-intikom-berlian-mustika-4375116314",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/ui-ux-designer-at-pt-intikom-berlian-mustika-4375116314",
        "featured": False
    }
]

# Insert new jobs at the beginning
data['jobs'] = new_jobs + data['jobs']

# Update categories list
all_categories = list(set([job['category'] for job in data['jobs']]))
all_categories.sort()
data['categories'] = all_categories

# Write back to file
with open('/tmp/maulud-net/loker/lowongan.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Successfully added {len(new_jobs)} new job postings")
print(f"📊 Total jobs: {len(data['jobs'])}")
print(f"📂 Categories: {', '.join(data['categories'])}")
print("\nNew jobs added:")
for i, job in enumerate(new_jobs, 1):
    print(f"{i}. {job['title']} - {job['company']}")
