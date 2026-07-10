#!/usr/bin/env python3
"""Inject Schema.org JobPosting JSON-LD into job HTML files."""
import json
import re
import os
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent

# Load jobs data
with open(BASE / 'loker' / 'lowongan.json') as f:
    data = json.load(f)

jobs = data['jobs']
site = data['site']

# Build slug->job map
job_map = {job['slug']: job for job in jobs}

def extract_salary_range(salary_text):
    """Parse 'Rp X-Y Juta' or 'Rp X Juta' to min/max in IDR."""
    nums = re.findall(r'(\d+(?:[.,]\d+)?)', salary_text.replace('.', '').replace(',', ''))
    if not nums:
        return 0, 0
    vals = [int(n) for n in nums]
    if len(vals) >= 2:
        return vals[0] * 1_000_000, vals[1] * 1_000_000
    elif len(vals) == 1:
        return vals[0] * 1_000_000, vals[0] * 1_000_000
    return 0, 0

def parse_location(location):
    """Extract city and province from location string."""
    loc = location.lower()
    if 'bali' in loc or 'denpasar' in loc:
        return 'Denpasar', 'Bali'
    elif 'tangerang' in loc:
        return 'Tangerang', 'Banten'
    elif 'bandung' in loc:
        return 'Bandung', 'Jawa Barat'
    elif 'yogyakarta' in loc or 'jogja' in loc:
        return 'Yogyakarta', 'DI Yogyakarta'
    elif 'surabaya' in loc:
        return 'Surabaya', 'Jawa Timur'
    elif 'remote' in loc:
        return 'Indonesia', 'Indonesia'
    elif 'makassar' in loc:
        return 'Makassar', 'Sulawesi Selatan'
    elif 'medan' in loc:
        return 'Medan', 'Sumatera Utara'
    elif 'semarang' in loc:
        return 'Semarang', 'Jawa Tengah'
    else:
        return 'Jakarta', 'DKI Jakarta'

def employment_type_map(job_type):
    t = job_type.lower().replace(' ', '_').replace('-', '_')
    mapping = {
        'full_time': 'FULL_TIME',
        'part_time': 'PART_TIME',
        'contract': 'CONTRACTOR',
        'internship': 'INTERN',
        'freelance': 'SELF_EMPLOYED',
    }
    for k, v in mapping.items():
        if k in t:
            return v
    return 'FULL_TIME'

def inject_schema(html_path: Path, job: dict) -> bool:
    """Inject JSON-LD JobPosting schema into HTML file. Returns True if injected."""
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Check if schema already exists
    if 'application/ld+json' in html and '@type": "JobPosting' in html:
        return False  # Already has schema

    salary_min, salary_max = extract_salary_range(job.get('salary', 'Rp 0'))
    city, province = parse_location(job.get('location', 'Indonesia'))

    schema = {
        "@context": "https://schema.org/",
        "@type": "JobPosting",
        "title": job['title'],
        "description": job['description'],
        "identifier": {
            "@type": "PropertyValue",
            "name": site['title'],
            "value": job['slug']
        },
        "datePosted": job['posted'],
        "validThrough": job['expires'],
        "employmentType": employment_type_map(job.get('type', 'Full-time')),
        "hiringOrganization": {
            "@type": "Organization",
            "name": job['company'],
            "sameAs": job.get('source_url', site['url'])
        },
        "jobLocation": {
            "@type": "Place",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "",
                "addressLocality": city,
                "addressRegion": province,
                "addressCountry": "ID"
            }
        },
        "baseSalary": {
            "@type": "MonetaryAmount",
            "currency": "IDR",
            "value": {
                "@type": "QuantitativeValue",
                "minValue": salary_min,
                "maxValue": salary_max,
                "unitText": "MONTH"
            }
        },
        "qualifications": " ".join(job.get('requirements', [])),
        "responsibilities": " ".join(job.get('responsibilities', [])),
        "educationRequirements": "S1 atau setara" if any('s1' in r.lower() or 'd3' in r.lower() or 'diploma' in r.lower() or 'sarjana' in r.lower() for r in job.get('requirements', [])) else "Tidak ditentukan",
        "experienceRequirements": " ".join([r for r in job.get('requirements', []) if 'pengalaman' in r.lower() or 'tahun' in r.lower()][:2]) or "Sesuai standar industri",
        "skills": " ".join(job.get('requirements', [])[:5]),
        "benefits": " ".join(job.get('benefits', [])),
        "workHours": "FULL_TIME" if 'full' in job.get('type', '').lower() else "PART_TIME" if 'part' in job.get('type', '').lower() else "CONTRACTOR" if 'contract' in job.get('type', '').lower() else "INTERN" if 'intern' in job.get('type', '').lower() else "FULL_TIME"
    }

    script_tag = f'<script type="application/ld+json">\n{json.dumps(schema, ensure_ascii=False, indent=2)}\n</script>'

    # Inject before </head>
    if '</head>' in html:
        html = html.replace('</head>', f'  {script_tag}\n</head>')
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html)
        return True
    return False

# Process all HTML files in post directory
post_dir = BASE / 'loker' / 'post'
injected = 0
skipped = 0

for html_file in post_dir.glob('*.html'):
    slug = html_file.stem
    if slug in job_map:
        if inject_schema(html_file, job_map[slug]):
            injected += 1
            print(f"Injected: {slug}")
        else:
            skipped += 1
    else:
        print(f"Warning: No job data for {slug}")

print(f"\nDone! Injected: {injected}, Skipped (already had schema): {skipped}")