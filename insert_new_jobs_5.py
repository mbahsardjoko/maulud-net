#!/usr/bin/env python3
"""Insert 5 new real job listings into lowongan.json at index 0."""
import json
import os
from pathlib import Path

BASE = Path(__file__).resolve().parent

with open(BASE / 'loker' / 'lowongan.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

today = "2026-07-15"
expires = "2026-08-14"

new_jobs = [
    {
        "slug": "communications-manager-meta-indonesia",
        "title": "Communications Manager, Indonesia",
        "company": "Meta",
        "location": "Jakarta",
        "type": "Full-time",
        "category": "Marketing",
        "salary": "Rp 20-35 Juta",
        "posted": today,
        "expires": expires,
        "description": "Meta is looking for a Communications Manager to lead communications efforts in Indonesia. This full-time, Indonesia-based role is key to shaping Meta's public narrative and advancing company objectives in the country. The ideal candidate will have a deep understanding of the Indonesian media landscape—both traditional and digital—and broad experience across consumer, policy, B2B, and product communications. You will work closely with cross-functional teams to drive storytelling, manage reputational issues, and strengthen Meta's relationships with journalists, creators, and community partners across Indonesia.",
        "requirements": [
            "Pengalaman minimal 8-10 tahun di bidang communications, public relations, atau corporate communications",
            "Pemahaman mendalam tentang lanskap media tradisional dan digital Indonesia",
            "Pengalaman handling isu reputasi dan crisis communications",
            "Kemampuan storytelling dan narrative building yang kuat",
            "Bahasa Inggris dan Indonesia aktif (lisan & tulisan) — native-level proficiency",
            "Jaringan luas dengan media nasional, kreator konten, dan komunitas digital",
            "Pengalaman di perusahaan teknologi global atau konsultan PR ternama adalah nilai plus",
            "Kemampuan berpikir strategis dan bekerja dalam lingkungan fast-paced"
        ],
        "responsibilities": [
            "Memimpin strategi komunikasi Meta untuk pasar Indonesia, mencakup consumer, policy, product, dan B2B",
            "Membangun dan memelihara hubungan dengan jurnalis, kreator konten, dan opinion leaders",
            "Mengelola narasi publik Meta di Indonesia melalui press releases, media briefing, dan thought leadership",
            "Berkolaborasi dengan tim global dan regional untuk menyelaraskan komunikasi lintas pasar",
            "Menangani isu reputasi dan memberikan rekomendasi strategis ke leadership tim",
            "Memonitor dan menganalisis media coverage serta sentimen publik terhadap Meta",
            "Mengembangkan materi komunikasi termasuk press release, Q&A, talking points, dan presentasi eksekutif",
            "Mendukung kampanye dampak sosial dan inisiatif community engagement Meta"
        ],
        "benefits": [
            "Gaji kompetitif Rp 20-35 Juta/bulan + bonus tahunan dan equity (RSU)",
            "BPJS Ketenagakerjaan, Kesehatan, dan asuransi kesehatan global",
            "Program kesehatan mental dan well-being (Spring Health, EAP)",
            "Fleksibilitas hybrid work dengan budget WFH setup",
            "MacBook Pro, monitor, dan perangkat kerja lengkap",
            "Budget pembelajaran tidak terbatas (konferensi, sertifikasi, kursus)",
            "Akses ke jaringan global Meta dan program pengembangan kepemimpinan",
            "Makan siang & snack gratis di kantor, transport allowance"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan Communications Manager, Indonesia di Meta. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/communications-manager-indonesia-at-meta-4312440576",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/communications-manager-indonesia-at-meta-4312440576",
        "featured": False
    },
    {
        "slug": "compliance-officer-xtransfer-indonesia",
        "title": "Compliance Officer",
        "company": "XTransfer",
        "location": "Jakarta",
        "type": "Full-time",
        "category": "Finance",
        "salary": "Rp 12-20 Juta",
        "posted": today,
        "expires": expires,
        "description": "XTransfer, platform pembayaran lintas negara untuk bisnis global yang berbasis di China dan beroperasi di Asia Tenggara, sedang mencari Compliance Officer untuk kantor Jakarta. Posisi ini akan bertanggung jawab memimpin proses perolehan dan pemeliharaan lisensi pembayaran di Indonesia, bertindak sebagai liaison officer dengan regulator (BI, OJK), auditor, dan otoritas terkait. Kamu akan memastikan seluruh prosedur dan proses kepatuhan memenuhi standar regulasi perbankan dan fintech Indonesia. Ini adalah peluang langka untuk bergabung dengan perusahaan fintech global yang berkembang pesat di pasar Indonesia.",
        "requirements": [
            "Pengalaman minimal 5 tahun di bidang compliance, AML, atau regulatory affairs di industri fintech/perbankan",
            "Pemahaman mendalam tentang regulasi pembayaran dan perbankan Indonesia (BI, OJK, PPATK)",
            "Pengalaman mengurus dan memelihara lisensi pembayaran/dompet digital di Indonesia",
            "Kemampuan komunikasi lisan dan tulisan yang baik dalam Bahasa Indonesia dan Inggris",
            "Pernah bekerja sebagai liaison officer dengan regulator dan auditor eksternal",
            "Detail-oriented, analitis, dan mampu bekerja dalam lingkungan regulasi yang ketat",
            "Pengalaman di perusahaan fintech multinasional adalah nilai tambah besar",
            "Domisili Jakarta atau sekitarnya"
        ],
        "responsibilities": [
            "Memimpin proses perolehan dan pemeliharaan lisensi pembayaran di Indonesia (BI, OJK)",
            "Bertindak sebagai liaison officer dengan regulator, auditor, dan otoritas terkait",
            "Mengawasi dan memastikan kepatuhan terhadap regulasi anti pencucian uang (AML/CFT)",
            "Menyusun dan mengimplementasikan kebijakan serta prosedur kepatuhan internal",
            "Melakukan audit internal dan menyiapkan laporan regulasi berkala",
            "Memonitor perubahan regulasi dan memberikan rekomendasi adaptasi kebijakan",
            "Berkolaborasi dengan tim legal dan risiko untuk mitigasi kepatuhan",
            "Memberikan pelatihan kepatuhan kepada karyawan di seluruh departemen"
        ],
        "benefits": [
            "Gaji kompetitif Rp 12-20 Juta/bulan + bonus tahunan",
            "BPJS Ketenagakerjaan, Kesehatan, dan asuransi kesehatan tambahan",
            "Lingkungan kerja fintech global dengan exposure internasional",
            "Fleksibilitas hybrid work",
            "Laptop MacBook Pro dan perangkat kerja",
            "Budget pelatihan dan sertifikasi kepatuhan (CAMS, ICA, dll)",
            "Kesempatan karir lintas negara di jaringan XTransfer global",
            "Makan siang dan transport allowance"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan Compliance Officer di XTransfer. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://www.linkedin.com/jobs/view/4412671193/",
        "source": "LinkedIn",
        "source_url": "https://www.linkedin.com/jobs/view/4412671193/",
        "featured": False
    },
    {
        "slug": "data-analyst-intern-pt-smart-tbk",
        "title": "Data Analyst Intern (Traceability & NDPE Verification)",
        "company": "PT SMART Tbk",
        "location": "Jakarta",
        "type": "Internship",
        "category": "Teknologi",
        "salary": "Rp 3-5 Juta",
        "posted": "2026-07-14",
        "expires": "2026-08-13",
        "description": "PT SMART Tbk (Sinar Mas Agribusiness and Food), perusahaan agribisnis dan makanan terkemuka di Indonesia yang merupakan bagian dari Sinar Mas Group, membuka posisi Data Analyst Intern untuk program Traceability dan NDPE (No Deforestation, No Peat, No Exploitation) Verification. Kamu akan bekerja dengan tim sustainability dan data untuk memproses, membersihkan, dan memvalidasi data rantai pasok kelapa sawit. Internship full-time selama 6 bulan ini cocok untuk mahasiswa akhir atau fresh graduate yang tertarik pada data analysis, sustainability, dan industri agribisnis skala global.",
        "requirements": [
            "Mahasiswa aktif semester 6-8 atau fresh graduate S1 di bidang Statistika, Matematika, Ilmu Komputer, Sistem Informasi, atau Teknik Industri",
            "Pengalaman dengan data cleaning, validasi, QC, dan data migration (sangat diutamakan)",
            "Mahir menggunakan Microsoft Excel (Pivot Tables, VLOOKUP, formulas, data cleaning)",
            "Kemampuan analitis yang kuat, detail-oriented, dan nyaman bekerja dengan dataset besar",
            "Tertarik pada topik sustainability, lingkungan, dan rantai pasok berkelanjutan",
            "Bersedia full-time on-site internship selama 6 bulan di Jakarta",
            "Kemampuan Bahasa Inggris pasif (membaca dokumen teknis)",
            "Pengalaman dengan Python atau SQL adalah nilai tambah"
        ],
        "responsibilities": [
            "Melakukan data cleaning, validasi, dan quality control pada dataset rantai pasok kelapa sawit",
            "Membantu migrasi data dari sistem lama ke platform baru untuk traceability",
            "Menganalisis data supplier dan perkebunan untuk verifikasi NDPE compliance",
            "Membuat laporan dan dashboard visualisasi menggunakan Excel dan Google Sheets",
            "Berkolaborasi dengan tim sustainability, supply chain, dan IT dalam pengelolaan data",
            "Menyusun dokumentasi proses dan prosedur data management",
            "Mendukung tim dalam audit dan verifikasi data untuk sertifikasi keberlanjutan",
            "Mengidentifikasi anomali data dan memberikan rekomendasi perbaikan"
        ],
        "benefits": [
            "Uang saku magang Rp 3-5 Juta/bulan",
            "Pengalaman langsung di perusahaan agribisnis Fortune 500",
            "Mentoring dari senior data analyst dan tim sustainability",
            "Eksposur ke proyek sustainability berskala global",
            "Sertifikat magang dan surat rekomendasi",
            "Fasilitas kantin, transport shuttle, dan gym",
            "Kesempatan karir tetap untuk performa terbaik",
            "Lingkungan kerja profesional di Sinar Mas Group"
        ],
        "how_to_apply": "Kirim lamaran melalui halaman karir PT SMART Tbk. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://himatika.fmipa.ugm.ac.id/2026/07/14/data-analyst-intern-traceability-ndpe-verification-pt-smart-tbk/",
        "source": "UGM Career Center",
        "source_url": "https://himatika.fmipa.ugm.ac.id/2026/07/14/data-analyst-intern-traceability-ndpe-verification-pt-smart-tbk/",
        "featured": False
    },
    {
        "slug": "head-of-it-operation-development-mnc-group",
        "title": "Head of IT Operation & Development",
        "company": "PT MNC Finance (MNC Group)",
        "location": "Jakarta",
        "type": "Full-time",
        "category": "Teknologi",
        "salary": "Rp 20-30 Juta",
        "posted": "2026-07-07",
        "expires": "2026-08-06",
        "description": "PT MNC Finance, perusahaan multifinance yang tergabung dalam MNC Group (salah satu konglomerat terbesar di Indonesia), membuka kesempatan bagi profesional IT berpengalaman untuk bergabung sebagai Head of IT Operation & Development. Posisi ini bertanggung jawab memimpin fungsi IT Operations dan IT Development guna memastikan seluruh sistem, aplikasi, dan infrastruktur perusahaan berjalan secara optimal, aman, serta mendukung transformasi digital perusahaan yang sedang berlangsung. Kamu akan memimpin tim IT yang solid dan berkolaborasi dengan jajaran direksi untuk mendorong inovasi teknologi di industri multifinance.",
        "requirements": [
            "Pengalaman minimal 8 tahun di IT dengan minimal 3 tahun di level manajerial/head of department",
            "Pengalaman leading IT operations dan software development secara bersamaan",
            "Pemahaman mendalam tentang infrastruktur IT, cloud (AWS/GCP/Azure), dan keamanan siber",
            "Pengalaman di industri multifinance, perbankan, atau financial services sangat diutamakan",
            "Kemampuan mengelola budget IT dan vendor management",
            "Paham framework IT governance (COBIT, ITIL) dan regulasi OJK terkait IT",
            "Kemampuan kepemimpinan, komunikasi, dan stakeholder management yang sangat baik",
            "Domisili Jakarta dan bersedia work from office"
        ],
        "responsibilities": [
            "Memimpin tim IT Operations (infrastruktur, jaringan, keamanan) dan IT Development (software, aplikasi, mobile)",
            "Memastikan ketersediaan, performa, dan keamanan seluruh sistem IT perusahaan 24/7",
            "Menyusun dan mengeksekusi roadmap transformasi digital perusahaan",
            "Mengelola anggaran IT tahunan dan melakukan optimalisasi biaya",
            "Menjalin hubungan dengan vendor teknologi dan konsultan IT",
            "Memastikan compliance dengan regulasi OJK, GDPR, dan standar keamanan data",
            "Mengembangkan talenta IT internal melalui pelatihan dan mentorship",
            "Melaporkan performa IT dan inisiatif digital ke direksi secara berkala"
        ],
        "benefits": [
            "Gaji kompetitif Rp 20-30 Juta/bulan + bonus tahunan berbasis performa",
            "BPJS Ketenagakerjaan, Kesehatan, dan asuransi kesehatan keluarga",
            "Program pensiun dan asuransi jiwa",
            "Tunjangan transportasi eksekutif (mobil perusahaan + supir)",
            "MacBook Pro, monitor, dan perangkat IT premium",
            "Budget pengembangan profesional (sertifikasi, konferensi, MBA eksekutif)",
            "Akses ke jaringan MNC Group (media, entertainment, properti, keuangan)",
            "Program kesehatan dan wellness keluarga"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan Head of IT Operation & Development di MNC Group. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://id.linkedin.com/jobs/view/head-of-it-development-and-operation-at-mnc-group-pt-mnc-asia-holding-tbk-4439129309",
        "source": "LinkedIn",
        "source_url": "https://id.linkedin.com/jobs/view/head-of-it-development-and-operation-at-mnc-group-pt-mnc-asia-holding-tbk-4439129309",
        "featured": True
    },
    {
        "slug": "hr-dept-head-mnc-group",
        "title": "HR Dept Head",
        "company": "PT MNC Asia Holding Tbk (MNC Group)",
        "location": "Jakarta",
        "type": "Full-time",
        "category": "Administrasi",
        "salary": "Rp 15-25 Juta",
        "posted": "2026-07-07",
        "expires": "2026-08-06",
        "description": "PT MNC Asia Holding Tbk (MNC Group), perusahaan investasi terkemuka di Indonesia yang bergerak di bidang Media & Entertainment, Financial Services, dan Properti, membuka lowongan untuk posisi HR Dept Head. Posisi ini akan memimpin fungsi Human Resources di holding company dan anak perusahaan, mencakup strategi SDM, rekrutmen, pengembangan talenta, manajemen kinerja, kompensasi & benefit, hingga hubungan industrial. Kamu akan menjadi mitra strategis bagi direksi dalam mengelola sumber daya manusia di salah satu grup bisnis terbesar di Indonesia dengan lebih dari 10.000 karyawan di berbagai sektor.",
        "requirements": [
            "Pengalaman minimal 7-10 tahun di bidang Human Resources, dengan minimal 3 tahun di level manajerial/dept head",
            "Pengalaman di holding company atau grup perusahaan multi-sektor sangat diutamakan",
            "Pemahaman mendalam tentang seluruh siklus HR: rekrutmen, pengembangan, compben, IR, legal ketenagakerjaan",
            "Pengetahuan tentang regulasi ketenagakerjaan Indonesia (UU Cipta Kerja, PP, Kepmenaker)",
            "Kemampuan strategic workforce planning dan organizational development",
            "Pengalaman digitalisasi HR (HRIS, People Analytics, HR Automation)",
            "Kemampuan komunikasi dan negosiasi dengan serikat pekerja/buruh adalah nilai plus",
            "Kepemimpinan visioner dan kemampuan stakeholder management lintas sektor bisnis"
        ],
        "responsibilities": [
            "Memimpin strategi SDM holding company dan anak perusahaan MNC Group",
            "Mengelola proses rekrutmen massal dan executive search untuk berbagai posisi strategis",
            "Mengembangkan program pengembangan talenta, suksesi, dan leadership pipeline",
            "Menyusun dan mengelola sistem kompensasi & benefit yang kompetitif di tiap sektor bisnis",
            "Memastikan kepatuhan terhadap regulasi ketenagakerjaan dan hubungan industrial",
            "Mengimplementasikan HR digital transformation: HRIS, people analytics, dan employee self-service",
            "Menjadi mitra strategis bagi direksi dalam pengambilan keputusan terkait SDM",
            "Mengelola employee engagement, budaya perusahaan, dan program kesejahteraan karyawan"
        ],
        "benefits": [
            "Gaji kompetitif Rp 15-25 Juta/bulan + bonus tahunan",
            "BPJS Ketenagakerjaan, Kesehatan, dan asuransi kesehatan keluarga",
            "Program pensiun dan asuransi jiwa",
            "Tunjangan transportasi dan komunikasi",
            "Budget pengembangan profesional (sertifikasi HR, konferensi, pelatihan)",
            "Akses ke ekosistem MNC Group (media, entertainment, properti)",
            "Fasilitas kesehatan dan wellness (gym, medical check-up tahunan)",
            "Kesempatan karir di salah satu grup bisnis terbesar Indonesia"
        ],
        "how_to_apply": "Kirim lamaran melalui LinkedIn dengan klik tombol Lamar di halaman lowongan HR Dept Head di MNC Group. Informasi lebih lanjut bisa dicek di link sumber.",
        "apply_url": "https://www.linkedin.com/jobs/view/4421767179/",
        "source": "LinkedIn",
        "source_url": "https://www.linkedin.com/jobs/view/4421767179/",
        "featured": False
    }
]

# Insert at index 0
for i, job in enumerate(new_jobs):
    data['jobs'].insert(0, job)
    print(f"Inserted: {job['slug']} (index {i})")

with open(BASE / 'loker' / 'lowongan.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\nDone! Added {len(new_jobs)} jobs to lowongan.json")
print(f"Total jobs: {len(data['jobs'])}")
