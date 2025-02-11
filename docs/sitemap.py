import os

# GitHub Pages ka URL yahan enter karein
BASE_URL = "https://yakub-8287.github.io/sai_furniture/"

# Jis folder me .html pages hain, uska path
HTML_FOLDER = "output_html"

sitemap_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""

# Sabhi .html files ko list karna
for file in os.listdir(HTML_FOLDER):
    if file.endswith(".html"):
        page_url = f"{BASE_URL}{file}"
        sitemap_content += f"    <url>\n        <loc>{page_url}</loc>\n        <changefreq>weekly</changefreq>\n        <priority>0.8</priority>\n    </url>\n"

sitemap_content += "</urlset>"

# File save karna
with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_content)

print("✅ Sitemap.xml successfully created!")
