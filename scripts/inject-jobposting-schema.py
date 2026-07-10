#!/usr/bin/env python3
"""Inject Schema.org JobPosting JSON-LD into job HTML files."""
import json
import re
import os
import sys
from pathlib import Path
from datetime import datetime

BASE = Path(__file__).resolve().parent.parent

# Load jobs data
with open(BASE / 'loker' / 'lowongan.json') as f:
    data = json.load(f)

jobs = data['jobs']
site = data['site']

def inject_schema(html_path: Path, job: dict) -> bool:
    """Inject JSON-LD JobPosting schema into HTML file."""
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Check if schema already exists
    if 'application/ld+json' in html and '@type": "JobPosting' in html:
        return False  # Already has schema

    # Parse salary to min/max
    salary_text = job.get('salary', 'Rp 0')
    salary_min = 0
    salary_max = 0
    # Extract numbers from "Rp X-Y Juta" or "Rp X Juta"
    import re
    nums = re.findall(r'(\d+(?:[.,]\d+)?)', salary_text.replace('.', '').replace(',', ''))
    if nums:
        vals = [int(n) for n in nums]
        if len(vals) >= 2:
            salary_min = vals[0] * 1_000_000
            salary_max = vals[1] * 1_000_000
        elif len(vals) == 1:
            salary_min = salary_max = vals[0] * 1_000_000

    # Parse location
    location = job.get('location', 'Indonesia')
    # Extract city/province
    address_locality = 'Jakarta'
    address_region = 'DKI Jakarta'
    if 'bali' in location.lower() or 'denpasar' in location.lower():
        address_locality = 'Denpasar'
        address_region = 'Bali'
    elif 'tangerang' in location.lower():
        address_locality = 'Tangerang'
        address_region = 'Banten'
    elif 'bandung' in location.lower():
        address_locality = 'Bandung'
        address_region = 'Jawa Barat'
    elif 'yogyakarta' in location.lower() or 'jogja' in location.lower():
        address_locality = 'Yogyakarta'
        address_region = 'DI Yogyakarta'
    elif 'surabaya' in location.lower():
        address_locality = 'Surabaya'
        address_region = 'Jawa Timur'
    elif 'remote' in location.lower():
        address_locality = 'Indonesia'
        address_region = 'Indonesia'
    else:
        # Default to Jakarta
        address_locality = 'Jakarta'
        address_region = 'DKI Jakarta'

    # Build schema
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
        "employmentType": job['type'].upper().replace('-', '_').replace(' ', '_'),
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
                "addressLocality": address_locality,
                "addressRegion": address_region,
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

def main():
    post_dir = BASE / 'loker' / 'post'
    if not post_dir.exists():
        print("Post directory not found")
        return

    # Build slug->job map
    job_map = {job['slug']: job for job in jobs}

    # Process all HTML files
    injected = 0
    skipped = 0
    for html_file in post_dir.glob('*.html'):
        slug = html_file.stem
        if slug in job_map:
            if inject_schema(html_file, job_map[slug]):
                injected += 1
                print(f"Injected: {slug}.html")
            else:
                skipped += 1
        else:
            print(f"No job data for: {slug}")

    print(f"\nDone! Injected: {injected}, Skipped (already has schema): {skipped}")

if __name__ == '__main__':
    main()