#!/usr/bin/env python3
"""Generate HTML detail pages for all jobs in lowongan.json."""
import json
import os
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent

with open(BASE / 'lowongan.json') as f:
    data = json.load(f)

jobs = data['jobs']
site = data['site']

os.makedirs(BASE / 'post', exist_ok=True)

LOCATION_ICON = '\U0001f310'  # globe
COMPANY_ICON = '\U0001f3e2'
BRIEFCASE = '\U0001f4bc'
MONEY = '\U0001f4b0'
CALENDAR = '\U0001f4c5'
STAR = '\u2b50'
CHECK = '\u2714\ufe0f'
TARGET = '\U0001f3af'
GIFT = '\U0001f381'
PENCIL = '\U0001f4dd'
BACK = '\u2190'
PIN = '\U0001f4cd'
HOME = '\U0001f3e0'
LIST = '\U0001f4cb'
INFO = '\u2139\ufe0f'

for job in jobs:
    slug = job['slug']
    type_class = job['type'].lower().replace(' ', '').replace('-', '') if job.get('type') else 'fulltime'
    loc_icon = LOCATION_ICON if 'remote' in job['location'].lower() else PIN

    reqs = '\n'.join(f'      <li>{r}</li>' for r in job.get('requirements', []))
    resp = '\n'.join(f'      <li>{r}</li>' for r in job.get('responsibilities', []))
    benefits = '\n'.join(f'      <li>{b}</li>' for b in job.get('benefits', []))

    tags_html = (
        f'<span class="tag {type_class}">{job["type"]}</span>\n'
        f'            <span class="tag">{job["category"]}</span>'
    )

    # Related jobs
    related = [j for j in jobs if j['category'] == job['category'] and j['slug'] != slug][:3]
    related_html = ''
    if related:
        related_cards = ''
        for r in related:
            r_loc_icon = LOCATION_ICON if 'remote' in r['location'].lower() else PIN
            related_cards += (
                f'      <a href="/post/{r["slug"]}" style="text-decoration:none;color:inherit">\n'
                f'        <div class="job-card">\n'
                f'          <h2>{r["title"]}</h2>\n'
                f'          <div class="company">{r["company"]}</div>\n'
                f'          <div class="job-meta">\n'
                f'            <span>{r_loc_icon} {r["location"]}</span>\n'
                f'            <span>{BRIEFCASE} {r["type"]}</span>\n'
                f'            <span>{MONEY} {r["salary"]}</span>\n'
                f'          </div>\n'
                f'        </div>\n'
                f'      </a>\n'
            )
        related_html = (
            f'<section class="related">\n'
            f'  <div class="container">\n'
            f'    <h3>{PIN} Lowongan Terkait</h3>\n'
            f'    <div class="job-grid">\n'
            f'{related_cards}'
            f'    </div>\n'
            f'  </div>\n'
            f'</section>'
        )

    # Apply box
    apply_html = ''
    if job.get('how_to_apply') or job.get('apply_url'):
        apply_html = (
            f'<div class="apply-box">\n'
            f'  <h3>{PENCIL} Cara Melamar</h3>\n'
            f'  <p>{job.get("how_to_apply", "")}</p>\n'
            f'  <a href="{job["apply_url"]}" class="apply-btn" target="_blank" rel="noopener">Kirim Lamaran {BACK}</a>\n'
            f'</div>'
        )

    featured_badge = f'{STAR} ' if job.get('featured') else ''

    html = (
        '<!DOCTYPE html>\n'
        '<html lang="id">\n'
        '<head>\n'
        '  <meta charset="UTF-8">\n'
        '  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        f'  <title>{job["title"]} &mdash; {site["title"]}</title>\n'
        f'  <meta name="description" content="{job["description"][:150]}">\n'
        f'  <meta property="og:title" content="{job["title"]} &mdash; {site["title"]}">\n'
        f'  <meta property="og:description" content="{job["description"][:150]}">\n'
        '  <meta property="og:image" content="https://images.unsplash.com/photo-1486312338219-ce68d2c6f44d?w=1200&q=80">\n'
        f'  <meta property="og:url" content="{site["url"]}/post/{slug}">\n'
        '  <meta property="og:type" content="article">\n'
        f'  <meta property="og:site_name" content="{site["title"]}">\n'
        '  <meta name="twitter:card" content="summary_large_image">\n'
        f'  <meta name="twitter:title" content="{job["title"]} &mdash; {site["title"]}">\n'
        f'  <meta name="twitter:description" content="{job["description"][:150]}">\n'
        f'  <link rel="canonical" href="{site["url"]}/post/{slug}">\n'
        '  <link rel="stylesheet" href="/style.css">\n'
        '</head>\n'
        '<body>\n'
        '\n'
        '<nav>\n'
        '  <div class="container">\n'
        f'    <a href="/" class="logo">{site["title"]}</a>\n'
        '    <div class="nav-links">\n'
        f'      <a href="/">{HOME} Beranda</a>\n'
        f'      <a href="/#daftar-lowongan">{LIST} Lowongan</a>\n'
        f'      <a href="/tentang">{INFO} Tentang</a>\n'
        '    </div>\n'
        '  </div>\n'
        '</nav>\n'
        '\n'
        '<section class="article-header">\n'
        '  <div class="container">\n'
        '    <a href="/#daftar-lowongan" class="back-link">\u2190 Kembali ke daftar lowongan</a>\n'
        f'    <h1>{featured_badge}{job["title"]}</h1>\n'
        '    <div class="article-meta">\n'
        f'      <span>{COMPANY_ICON} {job["company"]}</span>\n'
        f'      <span>{loc_icon} {job["location"]}</span>\n'
        f'      <span>{BRIEFCASE} {job["type"]}</span>\n'
        f'      <span>{MONEY} {job["salary"]}</span>\n'
        f'      <span>{CALENDAR} {job["posted"]}</span>\n'
        '    </div>\n'
        '    <div class="article-tags">\n'
        f'      {tags_html}\n'
        '    </div>\n'
        '  </div>\n'
        '</section>\n'
        '\n'
        '<div class="article-content">\n'
        '  <div class="container">\n'
        f'    <p>{job["description"]}</p>\n'
        '\n'
        '    <h2>Kualifikasi</h2>\n'
        '    <ul>\n'
        f'{reqs}\n'
        '    </ul>\n'
        '\n'
        '    <h2>Tanggung Jawab</h2>\n'
        '    <ul>\n'
        f'{resp}\n'
        '    </ul>\n'
        '\n'
        '    <h2>Benefit</h2>\n'
        '    <ul>\n'
        f'{benefits}\n'
        '    </ul>\n'
        '\n'
        f'{apply_html}\n'
        '  </div>\n'
        '</div>\n'
        '\n'
        f'{related_html}\n'
        '\n'
        '<footer>\n'
        '  <div class="container">\n'
        f'    <p>\u00a9 2026 <a href="{site["url"]}">{site["title"]}</a> &mdash; Portal Lowongan Kerja Indonesia</p>\n'
        '  </div>\n'
        '</footer>\n'
        '\n'
        '</body>\n'
        '</html>\n'
    )

    with open(BASE / 'post' / f'{slug}.html', 'w') as f:
        f.write(html)
    print(f'OK: post/{slug}.html')

print(f'\nDone! Generated {len(jobs)} job pages.')
