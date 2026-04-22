"""
Patch the pristine Claude Design HTML (fr/en/th) with:
  - Font swap: Fraunces→Instrument Serif, Manrope→Inter, JetBrains Mono→Geist Mono
  - Thai: add Noto Serif Thai + IBM Plex Sans Thai fallback chain
  - SEO tags in <head> (OG, Twitter, JSON-LD, hreflang, canonical, robots)
  - Language switcher in nav.top
  - Stack logo grid section before <footer>
Keeps ALL original animations, background mesh, orbital spin, fadeIn/slideUp.
"""
import re, json, subprocess
from pathlib import Path

ROOT = Path("/home/tarpediem/projects/alwayslink")
LANDING = ROOT / "web" / "landing"
SITE = "https://alwayslinksolutions.com"
BRAND = "Always Link Solutions"
EMAIL = "hello@alwayslinksolutions.com"

# Pull pristine copies from git (commit 14d7d76 = last good state)
ORIGINALS = {}
for lang in ["fr", "en", "th"]:
    result = subprocess.run(
        ["git", "show", f"14d7d76:web/landing/{lang}/index.html"],
        capture_output=True, text=True, cwd=ROOT, check=True,
    )
    ORIGINALS[lang] = result.stdout

# -----------------------------------------------------------------------
# Stack logos — same 36 as before (already in web/landing/assets/logos/)
# Acronis NOT included (per request)
# -----------------------------------------------------------------------
STACK = [
    ("Proxmox", "proxmox"), ("Docker", "docker"), ("Kubernetes", "kubernetes"),
    ("Linux", "linux"), ("Ubuntu", "ubuntu"),
    ("Python", "python"), ("FastAPI", "fastapi"), ("TypeScript", "typescript"),
    ("Node.js", "node"), ("Bun", "bun"), ("Rust", "rust"), ("Go", "go"),
    ("PostgreSQL", "postgresql"), ("Redis", "redis"), ("Neo4j", "neo4j"), ("ChromaDB", "chromadb"),
    ("Ollama", "ollama"), ("Claude", "claude-ai"), ("OpenAI", "openai"),
    ("HuggingFace", "huggingface"), ("LangChain", "langchain"),
    ("n8n", "n8n"), ("Odoo", "odoo"), ("Mailcow", "mailcow"),
    ("Nextcloud", "nextcloud"), ("OnlyOffice", "onlyoffice"),
    ("Cloudflare", "cloudflare"), ("Nginx", "nginx"),
    ("Tailscale", "tailscale"), ("OPNsense", "opnsense"),
    ("GitHub", "github"), ("Obsidian", "obsidian"),
    ("Home Assistant", "home-assistant"), ("Jellyfin", "jellyfin"),
    ("Terraform", "terraform"), ("Ansible", "ansible"),
]

STACK_LABELS = {
    "en": ("[04] — Stack", "Tools we build with."),
    "fr": ("[04] — Stack", "Le stack qu'on opère."),
    "th": ("[04] — สแตก", "เครื่องมือที่เราใช้สร้างงาน"),
}

SEO = {
    "en": {
        "title": "Always Link Solutions — Infrastructure, AI & Automation for SME in Southeast Asia",
        "desc": ("Bangkok-based IT consulting for SME in Thailand and Southeast Asia. "
                 "Proxmox, Docker, Odoo ERP, self-hosted AI, n8n automation. "
                 "Sober infrastructure that runs in production."),
        "keywords": "IT consulting Thailand, DevOps Bangkok, Proxmox SEA, Odoo ERP, self-hosted AI, n8n automation, RAG LLM",
        "og_locale": "en_US",
    },
    "fr": {
        "title": "Always Link Solutions — Infrastructure, IA & Automation pour PME en Asie du Sud-Est",
        "desc": ("Conseil IT basé à Bangkok pour PME en Thaïlande et Asie du Sud-Est. "
                 "Proxmox, Docker, Odoo ERP, IA auto-hébergée, automatisation n8n. "
                 "Une infrastructure sobre qui tient en production."),
        "keywords": "conseil IT Thaïlande, DevOps Bangkok, Proxmox Asie du Sud-Est, Odoo ERP PME, IA auto-hébergée, automatisation n8n, RAG LLM",
        "og_locale": "fr_FR",
    },
    "th": {
        "title": "Always Link Solutions — โครงสร้างพื้นฐาน AI และระบบอัตโนมัติสำหรับ SME ในเอเชียตะวันออกเฉียงใต้",
        "desc": ("บริษัทที่ปรึกษาด้าน IT ตั้งอยู่ที่กรุงเทพฯ ให้บริการ SME ในประเทศไทยและเอเชียตะวันออกเฉียงใต้ "
                 "Proxmox, Docker, Odoo ERP, AI โฮสต์เอง, ระบบอัตโนมัติ n8n."),
        "keywords": "ที่ปรึกษา IT กรุงเทพ, DevOps ประเทศไทย, Proxmox เอเชียตะวันออกเฉียงใต้, Odoo ERP SME, AI โฮสต์เอง",
        "og_locale": "th_TH",
    },
}

def jsonld():
    return json.dumps({
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": ["Organization", "ProfessionalService"],
                "@id": f"{SITE}/#organization",
                "name": BRAND,
                "legalName": "Always Link Solutions Co., Ltd.",
                "url": SITE,
                "logo": f"{SITE}/og-image.png",
                "email": EMAIL,
                "address": {"@type": "PostalAddress", "addressLocality": "Bangkok", "addressCountry": "TH"},
                "areaServed": [
                    {"@type": "Country", "name": "Thailand"},
                    {"@type": "Country", "name": "Vietnam"},
                    {"@type": "Country", "name": "Singapore"},
                    {"@type": "Place", "name": "Southeast Asia"},
                ],
                "serviceType": ["IT consulting", "DevOps", "Infrastructure engineering",
                                "AI automation", "Odoo ERP consulting", "Self-hosted AI & RAG"],
                "knowsAbout": ["Proxmox", "Docker", "Linux", "Odoo", "PostgreSQL",
                               "Ollama", "Claude API", "LangChain", "n8n", "RAG"],
                "sameAs": ["https://github.com/tarpediem/alwayslink"],
            },
            {
                "@type": "WebSite",
                "@id": f"{SITE}/#website",
                "url": SITE,
                "name": BRAND,
                "publisher": {"@id": f"{SITE}/#organization"},
            },
        ],
    }, ensure_ascii=False, indent=2)

# -----------------------------------------------------------------------
# Patches
# -----------------------------------------------------------------------
def patch_fonts(html, lang):
    """Swap Google Fonts link + font-family declarations."""
    # Compose new fonts link
    thai_part = ""
    if lang == "th":
        thai_part = "&family=Noto+Serif+Thai:wght@400;500;600;700&family=IBM+Plex+Sans+Thai:wght@300;400;500;600&family=IBM+Plex+Sans+Thai+Looped:wght@300;400;500;600"
    new_link = (
        '<link href="https://fonts.googleapis.com/css2?'
        'family=Instrument+Serif:ital@0;1'
        '&family=Inter:wght@300;400;500;600;700'
        '&family=Geist+Mono:wght@400;500'
        f'{thai_part}'
        '&display=swap" rel="stylesheet">'
    )
    html = re.sub(
        r'<link\s+href="https://fonts\.googleapis\.com/css2[^"]+"\s+rel="stylesheet">',
        new_link, html,
    )
    # Swap font-family strings (preserve surrounding quotes/fallbacks)
    html = html.replace("'Fraunces',serif", "'Instrument Serif', 'Noto Serif Thai', serif")
    html = html.replace("'Fraunces'", "'Instrument Serif'")
    html = html.replace("'Manrope',sans-serif", "'Inter', 'IBM Plex Sans Thai', sans-serif")
    html = html.replace("'Manrope'", "'Inter'")
    html = html.replace("'JetBrains Mono',monospace", "'Geist Mono', monospace")
    html = html.replace("'JetBrains Mono'", "'Geist Mono'")
    # Inside <text> SVG elements too:
    html = html.replace('font-family="Manrope, Helvetica, Arial, sans-serif"',
                        'font-family="Inter, Helvetica, Arial, sans-serif"')
    html = html.replace('font-family="JetBrains Mono, Menlo, monospace"',
                        'font-family="Geist Mono, Menlo, monospace"')
    return html

def patch_seo(html, lang):
    """Inject SEO tags into <head>."""
    s = SEO[lang]
    url = f"{SITE}/{lang}/"
    alternates = "\n".join(
        f'<link rel="alternate" hreflang="{c}" href="{SITE}/{c}/" />'
        for c in ["en", "fr", "th"]
    )
    alternates += f'\n<link rel="alternate" hreflang="x-default" href="{SITE}/en/" />'

    seo_block = f"""<title>{s['title']}</title>
<meta name="description" content="{s['desc']}" />
<meta name="keywords" content="{s['keywords']}" />
<meta name="author" content="{BRAND}" />
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1" />
<meta name="theme-color" content="#0A0C10" />
<meta name="color-scheme" content="dark" />

<link rel="canonical" href="{url}" />
{alternates}

<meta property="og:type" content="website" />
<meta property="og:title" content="{s['title']}" />
<meta property="og:description" content="{s['desc']}" />
<meta property="og:url" content="{url}" />
<meta property="og:site_name" content="{BRAND}" />
<meta property="og:locale" content="{s['og_locale']}" />
<meta property="og:image" content="{SITE}/og-image.png" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />

<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{s['title']}" />
<meta name="twitter:description" content="{s['desc']}" />
<meta name="twitter:image" content="{SITE}/og-image.png" />

<link rel="icon" type="image/svg+xml" href="/als-mark.svg" />

<script type="application/ld+json">
{jsonld()}
</script>
"""
    # Replace original <title>... tag and inject all SEO above
    html = re.sub(r'<title>[^<]*</title>', '', html, count=1)
    html = html.replace("</head>", seo_block + "\n</head>", 1)
    return html

def patch_lang_switcher(html, active_lang):
    """Inject language switcher + hreflang pills into the nav.top, right before the CTA."""
    pills = []
    for code in ["en", "fr", "th"]:
        cls = " active" if code == active_lang else ""
        pills.append(f'<a href="/{code}/" hreflang="{code}" class="lang-pill{cls}">{code.upper()}</a>')
    pill_html = (
        '<div class="lang-switch" role="group" aria-label="Language">'
        + "".join(pills)
        + "</div>"
    )
    # Add the matching CSS near the end of <style>
    lang_css = """
  .lang-switch{display:inline-flex;align-items:center;gap:2px;border:1px solid var(--line-2);border-radius:999px;padding:3px;margin-right:14px;font-family:'Geist Mono',monospace;font-size:11px;letter-spacing:0.1em}
  .lang-switch a.lang-pill{padding:4px 10px;color:var(--ink-mute);border-radius:999px;text-decoration:none;transition:all .25s ease;text-transform:uppercase}
  .lang-switch a.lang-pill:hover{color:var(--ink)}
  .lang-switch a.lang-pill.active{background:var(--ink);color:var(--bg)}
  @media (max-width:640px){.lang-switch{margin-right:8px}.lang-switch a.lang-pill{padding:3px 7px;font-size:10px}}
"""
    html = html.replace("/* selection */", lang_css + "\n  /* selection */", 1)
    # Insert pills BEFORE the CTA anchor inside nav.top
    html = re.sub(
        r'(<a href="#contact" class="cta">)',
        pill_html + r'\1',
        html, count=1,
    )
    return html

def patch_stack_section(html, lang):
    """Add a stack logo grid section before <footer>."""
    label, title = STACK_LABELS[lang]
    items = "\n".join(
        f'        <div class="stack-cell"><img src="/assets/logos/{slug}.svg" alt="{name}" loading="lazy" /><span>{name}</span></div>'
        for name, slug in STACK
    )
    stack_css = """
  /* ---------- STACK GRID ---------- */
  .stack{padding:110px 0;border-top:1px solid var(--line)}
  .stack .stack-grid{
    margin-top:52px;display:grid;grid-template-columns:repeat(auto-fill, minmax(120px, 1fr));
    gap:1px;background:var(--line);border:1px solid var(--line);
  }
  .stack-cell{
    background:var(--bg);padding:28px 14px;display:flex;flex-direction:column;
    align-items:center;justify-content:center;gap:14px;min-height:120px;
    transition:background .25s ease;
  }
  .stack-cell:hover{background:var(--bg-2)}
  .stack-cell img{width:34px;height:34px;opacity:0.85;transition:opacity .25s;filter:saturate(0.92)}
  .stack-cell:hover img{opacity:1;filter:none}
  .stack-cell span{font-family:'Geist Mono',monospace;font-size:10.5px;letter-spacing:0.06em;color:var(--ink-mute);text-align:center}
  @media (max-width:520px){.stack .stack-grid{grid-template-columns:repeat(3,1fr)}.stack-cell{padding:20px 6px;min-height:96px}.stack-cell img{width:26px;height:26px}}
"""
    html = html.replace("/* selection */", stack_css + "\n  /* selection */", 1)

    stack_html = f"""
  <!-- =============== STACK =============== -->
  <section class="stack" id="stack">
    <div class="section-head">
      <h2>{title}</h2>
      <span class="num">{label}</span>
    </div>
    <div class="stack-grid">
{items}
    </div>
  </section>
"""
    # Insert the stack section after the quote-block (#philosophy), before <footer>
    html = html.replace("  <!-- =============== FOOTER =============== -->", stack_html + "\n  <!-- =============== FOOTER =============== -->")
    return html

def patch_html_lang_dir(html, lang):
    # Ensure <html lang="xx"> is correct (already set in originals but safe to enforce)
    html = re.sub(r'<html\s+lang="[a-z]{2}">', f'<html lang="{lang}">', html, count=1)
    return html

def build_one(lang):
    html = ORIGINALS[lang]
    html = patch_html_lang_dir(html, lang)
    html = patch_fonts(html, lang)
    html = patch_seo(html, lang)
    html = patch_lang_switcher(html, lang)
    html = patch_stack_section(html, lang)

    # Clean up extra blank lines we might have introduced
    html = re.sub(r'\n\s*\n\s*\n+', '\n\n', html)

    out = LANDING / lang / "index.html"
    out.write_text(html)
    print(f"  ✓ {lang}/index.html  {out.stat().st_size:>7} B")

if __name__ == "__main__":
    for lang in ["fr", "en", "th"]:
        build_one(lang)
    print("Patched. Original Claude Design structure preserved.")
