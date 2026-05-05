"""
ALS landing — generator from a single dark-glass brand-kit template.
Replaces _patch.py (which patched a third-party "Claude Design" original).

Output:
  - en/index.html, fr/index.html, th/index.html
  - sitemap.xml (rewritten to match)

Brand kit reference: ~/.claude/skills/power-design/brands/als/brand-style.md
Palette: dark glass — bg #0A0C10, accent cyan #7EE8FA, accent-blue #3A6FF8, warm #E8C9A0.
Fonts: Inter (Latin), IBM Plex Sans Thai (Thai), IBM Plex Mono (code + eyebrow).
"""
from pathlib import Path
from datetime import date
import re

ROOT = Path(__file__).parent
SITE = "https://alwayslinksolutions.com"
BRAND = "Always Link Solutions"
EMAIL = "hello@alwayslinksolutions.com"
TODAY = date.today().isoformat()

# Full ALS logo SVG (white, transparent bg) — inlined so internal fonts inherit
LOGO_SVG = (ROOT / "assets" / "als-logo-full.svg").read_text(encoding="utf-8")

# ----------------------------------------------------------------------------
# Stack (same 36 logos as before, files already in assets/logos/)
# ----------------------------------------------------------------------------
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

# ----------------------------------------------------------------------------
# Localized copy (preserves original handwritten content from each language)
# ----------------------------------------------------------------------------
COPY = {
    "en": {
        "title": "Always Link Solutions — Infrastructure, AI & Automation for SME in Southeast Asia",
        "meta_desc": "Bangkok-based IT consulting for SME in Thailand and Southeast Asia. Proxmox, Docker, Odoo ERP, self-hosted AI, n8n automation. Sober infrastructure that runs in production.",
        "og_locale": "en_US",
        "nav_services": "Services",
        "nav_stack": "Stack",
        "nav_philosophy": "Philosophy",
        "nav_contact": "Contact",
        "hero_eyebrow": "&gt; SINCE 2026 // BANGKOK",
        "hero_h1_html": "Link it. Automate it.<br><span class='accent'>Own it.</span>",
        "hero_lead": "From Bangkok, we design and operate lean, resilient technical stacks: Proxmox, Docker, Linux, Odoo, self-hosted RAG and LLM pipelines, n8n workflows. Systems that hold up in production — not just in slides.",
        "hero_cta_primary": "Start a project",
        "hero_cta_secondary": "See services",
        "hero_chip_uptime": "99.95% uptime",
        "hero_chip_proxmox": "Proxmox · LXC · Docker",
        "hero_chip_open": "Open-source first",
        "term_title": "$ als status — production",
        "services_eyebrow": "&gt; SERVICES // 02",
        "services_h2_html": "Three disciplines.<br><span class='accent'>One engineering logic.</span>",
        "services_lead": "We don't sell features. We design systems your team can run, monitor, and repair without us.",
        "services": [
            {"idx": "01 / Infra", "h3_html": "Infrastructure <span class='warm'>&amp;</span> DevOps", "h3_plain": "Infrastructure & DevOps",
             "p": "Proxmox virtualization, Docker containers, Linux networking and storage. We design self-hosted platforms that are stable, monitored, and repairable by your team — not by us.",
             "tags": ["Proxmox", "Docker", "LXC", "Linux", "Nginx"]},
            {"idx": "02 / AI", "h3_html": "AI <span class='warm'>&amp;</span> Automation", "h3_plain": "AI & Automation",
             "p": "Self-hosted RAG pipelines, on-prem LLM deployment, n8n workflows built around your data. The value isn't in the model — it's in the integration.",
             "tags": ["RAG", "LLM", "n8n", "Ollama", "pgvector"]},
            {"idx": "03 / Biz", "h3_html": "Business <span class='warm'>Systems</span>", "h3_plain": "Business Systems",
             "p": "Odoo ERP, Linux desktop migrations, open-source collaboration tools. Business stacks that cover the full operational cycle without indefinite software rent.",
             "tags": ["Odoo", "OnlyOffice", "Mailcow", "Ubuntu", "RustDesk"]},
        ],
        "service_more": "Discuss a project →",
        "live_eyebrow": "&gt; PRODUCTION // LIVE",
        "live_h3": "What's running right now.",
        "live_lead": "A sample of what holds — across our homelab and our clients' infra.",
        "phil_eyebrow": "&gt; PHILOSOPHY // 03",
        "phil_quote_html": "Good infrastructure is invisible. <span class='warm-em'>It holds.</span> It doesn't page you on Friday night, doesn't ask for attention on Monday morning. Our whole craft is built around that discretion.",
        "phil_sig": "Olivier Magnier · Founder",
        "phil_h2": "Production first, slides last.",
        "stack_eyebrow": "&gt; STACK // 04",
        "stack_h2": "What we build with.",
        "stack_lead": "Open-source first, vendor-lock last. Every tool below runs in our own homelab and at every client site we operate.",
        "cta_eyebrow": "&gt; READY?",
        "cta_h2_html": "Bring us a problem.<br><span class='accent'>We'll send back a system.</span>",
        "cta_button": "Talk to us →",
        "footer_tagline": "Self-hosted business systems for SME in Southeast Asia.",
        "footer_company": "Company",
        "footer_legal": "Legal",
        "footer_reg": "Reg. 0105569079253 · Bangkok, Thailand",
        "footer_built_html": f"Built in Bangkok · last updated {TODAY}",
    },
    "fr": {
        "title": "Always Link Solutions — Infrastructure, IA & Automation pour PME en Asie du Sud-Est",
        "meta_desc": "Conseil IT basé à Bangkok pour PME en Thaïlande et Asie du Sud-Est. Proxmox, Docker, Odoo ERP, IA auto-hébergée, automatisation n8n. Une infrastructure sobre qui tient en production.",
        "og_locale": "fr_FR",
        "nav_services": "Services",
        "nav_stack": "Stack",
        "nav_philosophy": "Philosophie",
        "nav_contact": "Contact",
        "hero_eyebrow": "&gt; DEPUIS 2026 // BANGKOK",
        "hero_h1_html": "Link it. Automate it.<br><span class='accent'>Own it.</span>",
        "hero_lead": "Depuis Bangkok, on conçoit et opère des stacks techniques sobres et tenues : Proxmox, Docker, Linux, Odoo, pipelines RAG et LLM auto-hébergés, workflows n8n. Des solutions qui tiennent en production, pas des slides.",
        "hero_cta_primary": "Démarrer un projet",
        "hero_cta_secondary": "Voir les services",
        "hero_chip_uptime": "99.95 % uptime",
        "hero_chip_proxmox": "Proxmox · LXC · Docker",
        "hero_chip_open": "Open-source d'abord",
        "term_title": "$ als status — production",
        "services_eyebrow": "&gt; SERVICES // 02",
        "services_h2_html": "Trois disciplines.<br><span class='accent'>Une seule logique d'ingénierie.</span>",
        "services_lead": "On ne vend pas des fonctionnalités. On conçoit des systèmes que votre équipe peut opérer, monitorer et réparer sans nous.",
        "services": [
            {"idx": "01 / Infra", "h3_html": "Infrastructure <span class='warm'>&amp;</span> DevOps", "h3_plain": "Infrastructure & DevOps",
             "p": "Virtualisation Proxmox, conteneurisation Docker, réseau et stockage Linux. On conçoit des plateformes auto-hébergées stables, monitorées, et réparables par votre équipe — pas par nous.",
             "tags": ["Proxmox", "Docker", "LXC", "Linux", "Nginx"]},
            {"idx": "02 / AI", "h3_html": "IA <span class='warm'>&amp;</span> Automation", "h3_plain": "IA & Automation",
             "p": "Pipelines RAG auto-hébergés, déploiement de LLM en interne, workflows n8n orchestrés autour de vos données. La valeur n'est pas dans le modèle — elle est dans l'intégration.",
             "tags": ["RAG", "LLM", "n8n", "Ollama", "pgvector"]},
            {"idx": "03 / Biz", "h3_html": "Business <span class='warm'>Systems</span>", "h3_plain": "Business Systems",
             "p": "ERP Odoo, migrations Linux poste de travail, outils collaboratifs open-source. Des stacks métier qui couvrent le cycle commercial complet sans loyer logiciel indéfini.",
             "tags": ["Odoo", "OnlyOffice", "Mailcow", "Ubuntu", "RustDesk"]},
        ],
        "service_more": "Discuter du projet →",
        "live_eyebrow": "&gt; PRODUCTION // LIVE",
        "live_h3": "Ce qui tourne, là, maintenant.",
        "live_lead": "Un échantillon de ce qui tient — entre notre homelab et l'infra de nos clients.",
        "phil_eyebrow": "&gt; PHILOSOPHIE // 03",
        "phil_quote_html": "Une infrastructure bien pensée ne se voit pas. <span class='warm-em'>Elle tient.</span> Elle ne produit pas d'incident le vendredi soir, ne se rappelle à personne le lundi matin. Tout notre métier est construit autour de cette discrétion.",
        "phil_sig": "Olivier Magnier · Fondateur",
        "phil_h2": "La production avant les slides.",
        "stack_eyebrow": "&gt; STACK // 04",
        "stack_h2": "Le stack qu'on opère.",
        "stack_lead": "Open-source d'abord, vendor-lock jamais. Chaque outil ci-dessous tourne dans notre propre infra et chez chacun de nos clients.",
        "cta_eyebrow": "&gt; PRÊT ?",
        "cta_h2_html": "Apportez-nous un problème.<br><span class='accent'>On vous renvoie un système.</span>",
        "cta_button": "Parlons-en →",
        "footer_tagline": "Systèmes business auto-hébergés pour PME en Asie du Sud-Est.",
        "footer_company": "Entreprise",
        "footer_legal": "Légal",
        "footer_reg": "Reg. 0105569079253 · Bangkok, Thaïlande",
        "footer_built_html": f"Conçu à Bangkok · mis à jour {TODAY}",
    },
    "th": {
        "title": "Always Link Solutions — โครงสร้างพื้นฐาน AI และระบบอัตโนมัติสำหรับ SME ในเอเชียตะวันออกเฉียงใต้",
        "meta_desc": "บริษัทที่ปรึกษาด้าน IT ตั้งอยู่ที่กรุงเทพฯ ให้บริการ SME ในประเทศไทยและเอเชียตะวันออกเฉียงใต้ Proxmox, Docker, Odoo ERP, AI โฮสต์เอง, ระบบอัตโนมัติ n8n.",
        "og_locale": "th_TH",
        "nav_services": "บริการ",
        "nav_stack": "สแตก",
        "nav_philosophy": "ปรัชญา",
        "nav_contact": "ติดต่อ",
        "hero_eyebrow": "&gt; ตั้งแต่ 2026 // กรุงเทพฯ",
        "hero_h1_html": "Link it. Automate it.<br><span class='accent'>Own it.</span>",
        "hero_lead": "จากกรุงเทพฯ เราออกแบบและดูแลสแตกเทคนิคที่เรียบง่ายและมั่นคง: Proxmox, Docker, Linux, Odoo, ไปป์ไลน์ RAG และ LLM ที่โฮสต์เอง, เวิร์กโฟลว์ n8n ระบบที่ทำงานได้จริงในโปรดักชัน — ไม่ใช่แค่บนสไลด์",
        "hero_cta_primary": "เริ่มต้นโปรเจกต์",
        "hero_cta_secondary": "ดูบริการทั้งหมด",
        "hero_chip_uptime": "99.95% uptime",
        "hero_chip_proxmox": "Proxmox · LXC · Docker",
        "hero_chip_open": "โอเพนซอร์สก่อน",
        "term_title": "$ als status — production",
        "services_eyebrow": "&gt; บริการ // 02",
        "services_h2_html": "สามสาขาวิชา<br><span class='accent'>ภายใต้ตรรกะวิศวกรรมเดียวกัน</span>",
        "services_lead": "เราไม่ได้ขายฟีเจอร์ เราออกแบบระบบที่ทีมของคุณสามารถดูแล มอนิเตอร์ และซ่อมเองได้โดยไม่ต้องพึ่งเรา",
        "services": [
            {"idx": "01 / Infra", "h3_html": "โครงสร้างพื้นฐาน <span class='warm'>&amp;</span> DevOps", "h3_plain": "โครงสร้างพื้นฐาน & DevOps",
             "p": "เวอร์ชวลไลเซชัน Proxmox, คอนเทนเนอร์ Docker, เครือข่ายและสตอเรจ Linux เราออกแบบแพลตฟอร์มที่โฮสต์เองได้อย่างเสถียร มีการมอนิเตอร์ และทีมงานของคุณสามารถซ่อมบำรุงเองได้ — ไม่ต้องพึ่งเราตลอดเวลา",
             "tags": ["Proxmox", "Docker", "LXC", "Linux", "Nginx"]},
            {"idx": "02 / AI", "h3_html": "AI <span class='warm'>&amp;</span> ระบบอัตโนมัติ", "h3_plain": "AI & ระบบอัตโนมัติ",
             "p": "ไปป์ไลน์ RAG ที่โฮสต์เอง, การใช้งาน LLM ภายในองค์กร, เวิร์กโฟลว์ n8n ที่ออกแบบรอบข้อมูลของคุณ คุณค่าไม่ได้อยู่ที่ตัวโมเดล — แต่อยู่ที่การผสานรวมต่างหาก",
             "tags": ["RAG", "LLM", "n8n", "Ollama", "pgvector"]},
            {"idx": "03 / Biz", "h3_html": "ระบบ<span class='warm'>ธุรกิจ</span>", "h3_plain": "ระบบธุรกิจ",
             "p": "ERP Odoo, การย้ายเครื่องไคลเอนต์ไปสู่ Linux, เครื่องมือทำงานร่วมกันแบบโอเพนซอร์ส สแตกธุรกิจที่ครอบคลุมวงจรการทำงานทั้งหมดโดยไม่ต้องจ่ายค่าไลเซนส์ไม่สิ้นสุด",
             "tags": ["Odoo", "OnlyOffice", "Mailcow", "Ubuntu", "RustDesk"]},
        ],
        "service_more": "พูดคุยเกี่ยวกับโปรเจกต์ →",
        "live_eyebrow": "&gt; PRODUCTION // LIVE",
        "live_h3": "สิ่งที่กำลังทำงานอยู่ตอนนี้",
        "live_lead": "ตัวอย่างของระบบที่ทำงานอยู่ — ทั้งในโฮมแล็บของเราและในระบบของลูกค้า",
        "phil_eyebrow": "&gt; ปรัชญา // 03",
        "phil_quote_html": "โครงสร้างพื้นฐานที่ดีจะมองไม่เห็น <span class='warm-em'>มันแค่ทำงาน</span> ไม่แจ้งเตือนคุณคืนวันศุกร์ ไม่เรียกร้องความสนใจเช้าวันจันทร์ งานทั้งหมดของเราสร้างขึ้นรอบความเงียบเชิงวิศวกรรมนี้",
        "phil_sig": "Olivier Magnier · ผู้ก่อตั้ง",
        "phil_h2": "โปรดักชันก่อน สไลด์ทีหลัง",
        "stack_eyebrow": "&gt; สแตก // 04",
        "stack_h2": "เครื่องมือที่เราใช้สร้างงาน",
        "stack_lead": "โอเพนซอร์สมาก่อน ไม่ผูกกับ vendor ทุกเครื่องมือด้านล่างทำงานในโครงสร้างของเราเองและที่ลูกค้าทุกราย",
        "cta_eyebrow": "&gt; พร้อมแล้ว?",
        "cta_h2_html": "นำปัญหามาให้เรา<br><span class='accent'>เราจะส่งระบบกลับไป</span>",
        "cta_button": "คุยกับเรา →",
        "footer_tagline": "ระบบธุรกิจโฮสต์เองสำหรับ SME ในเอเชียตะวันออกเฉียงใต้",
        "footer_company": "บริษัท",
        "footer_legal": "ข้อกฎหมาย",
        "footer_reg": "เลขทะเบียน 0105569079253 · กรุงเทพฯ ประเทศไทย",
        "footer_built_html": f"สร้างในกรุงเทพฯ · อัปเดตล่าสุด {TODAY}",
    },
}

# ----------------------------------------------------------------------------
# CSS — single source of truth, dark glass aligned to the ALS brand kit
# ----------------------------------------------------------------------------
CSS = """
:root {
  --bg: #0A0C10;
  --bg-2: #0E1117;
  --bg-3: #14181F;
  --bg-elev: #1A1F28;
  --ink-strong: #FFFFFF;
  --ink: #F2F3F5;
  --ink-body: #D6D9DE;
  --ink-mute: #8A8F98;
  --ink-faint: #5A6068;
  --accent: #7EE8FA;
  --accent-active: #5AC4D8;
  --accent-soft: rgba(126,232,250,0.10);
  --accent-faint: rgba(126,232,250,0.04);
  --accent-blue: #3A6FF8;
  --accent-blue-soft: rgba(58,111,248,0.10);
  --warm: #E8C9A0;
  --warm-soft: rgba(232,201,160,0.10);
  --line: rgba(255,255,255,0.06);
  --line-2: rgba(255,255,255,0.14);
  --line-accent: rgba(126,232,250,0.30);
  --glass: rgba(14,17,23,0.55);
  --glass-strong: rgba(255,255,255,0.07);
  --success: #5DD37A;
  --error: #FF6B6B;
  --shadow-card: 0 1px 0 rgba(255,255,255,0.04) inset, 0 8px 32px rgba(0,0,0,0.4);
  --shadow-glow-cyan: 0 0 24px rgba(126,232,250,0.18);
  --shadow-glow-blue: 0 0 28px rgba(58,111,248,0.22);
  --ring-focus: 0 0 0 3px rgba(126,232,250,0.30);
  --t: 200ms cubic-bezier(0.4, 0, 0.2, 1);
}

* { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
html, body {
  background: var(--bg);
  color: var(--ink-body);
  font-family: 'Inter', 'IBM Plex Sans Thai', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  font-weight: 400;
  font-size: 16px;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow-x: hidden;
}

body {
  background:
    radial-gradient(circle at 80% 0%, rgba(126,232,250,0.08), transparent 50%),
    radial-gradient(circle at 0% 50%, rgba(58,111,248,0.06), transparent 60%),
    var(--bg);
  background-attachment: fixed;
  position: relative;
}

body::before {
  content: '';
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 0;
  opacity: 0.025;
  mix-blend-mode: overlay;
  background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0.5 0 0 0 0 0.5 0 0 0 0 0.5 0 0 0 0.4 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>");
}

body::after {
  content: '';
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 0;
  background-image:
    linear-gradient(rgba(255,255,255,0.02) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.02) 1px, transparent 1px);
  background-size: 64px 64px;
}

main, header, footer { position: relative; z-index: 1; }

a { color: var(--accent); text-decoration: none; transition: color var(--t); }
a:hover { color: var(--ink-strong); }
img { max-width: 100%; height: auto; display: block; }

::selection { background: var(--accent); color: var(--bg); }
:focus-visible { outline: none; box-shadow: var(--ring-focus); border-radius: 8px; }

.container { max-width: 1200px; margin: 0 auto; padding: 0 32px; }
.container-wide { max-width: 1280px; margin: 0 auto; padding: 0 32px; }

/* eyebrow */
.eyebrow {
  font-family: 'IBM Plex Mono', ui-monospace, 'SF Mono', Menlo, monospace;
  font-size: 12px;
  font-weight: 500;
  letter-spacing: 1.6px;
  text-transform: uppercase;
  color: var(--ink-mute);
  display: inline-block;
}
.eyebrow.accent { color: var(--accent); }
.section-head { margin-bottom: 56px; }
.section-head .eyebrow { margin-bottom: 16px; }
.section-head h2 {
  font-size: clamp(32px, 5vw, 56px);
  font-weight: 600;
  line-height: 1.05;
  letter-spacing: -1.5px;
  color: var(--ink-strong);
  max-width: 900px;
}
.section-head .lead {
  margin-top: 20px;
  font-size: 18px;
  line-height: 1.6;
  color: var(--ink-mute);
  max-width: 640px;
}

.accent { color: var(--accent); }
.warm, .warm-em { color: var(--warm); }
.warm-em { font-style: italic; }

/* --- top nav --- */
.top-nav {
  position: sticky;
  top: 0;
  z-index: 100;
  background: var(--glass);
  backdrop-filter: blur(20px) saturate(140%);
  -webkit-backdrop-filter: blur(20px) saturate(140%);
  border-bottom: 1px solid var(--line);
}
.top-nav-inner {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 32px;
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
}
.brand {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
  color: var(--ink-strong);
}
.brand img { width: 28px; height: 28px; }
.brand-name {
  font-size: 15px;
  font-weight: 600;
  letter-spacing: -0.2px;
  color: var(--ink-strong);
}
.nav-links {
  display: flex;
  gap: 4px;
  list-style: none;
}
.nav-links a {
  display: inline-block;
  padding: 8px 14px;
  font-size: 14px;
  font-weight: 500;
  color: var(--ink-mute);
  border-radius: 8px;
  transition: color var(--t), background var(--t);
}
.nav-links a:hover { color: var(--ink-strong); background: var(--glass-strong); }
.nav-right { display: flex; align-items: center; gap: 12px; }
.lang-switch {
  display: inline-flex;
  align-items: center;
  gap: 2px;
  padding: 3px;
  border: 1px solid var(--line-2);
  border-radius: 999px;
  font-family: 'IBM Plex Mono', ui-monospace, monospace;
  font-size: 11px;
  letter-spacing: 0.1em;
}
.lang-switch a {
  padding: 5px 10px;
  border-radius: 999px;
  color: var(--ink-mute);
  font-weight: 500;
  transition: all var(--t);
}
.lang-switch a:hover { color: var(--ink); }
.lang-switch a.active { background: var(--accent); color: var(--bg); }

.btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  height: 44px;
  padding: 0 22px;
  border-radius: 10px;
  font-family: inherit;
  font-size: 14px;
  font-weight: 600;
  letter-spacing: 0.2px;
  cursor: pointer;
  text-decoration: none;
  transition: all var(--t);
  white-space: nowrap;
  border: 1px solid transparent;
}
.btn-primary {
  background: var(--accent);
  color: var(--bg);
  box-shadow: var(--shadow-glow-cyan);
}
.btn-primary:hover {
  background: var(--accent-active);
  color: var(--bg);
  box-shadow: 0 0 18px rgba(126,232,250,0.32);
  transform: translateY(-1px);
}
.btn-secondary {
  background: var(--glass-strong);
  color: var(--ink);
  border-color: var(--line-2);
  backdrop-filter: blur(20px);
}
.btn-secondary:hover { background: rgba(255,255,255,0.10); color: var(--ink-strong); }
.btn-ghost {
  background: transparent;
  color: var(--ink);
  border-color: var(--line);
}
.btn-ghost:hover { border-color: var(--line-2); color: var(--ink-strong); }
.btn-sm { height: 36px; padding: 0 16px; font-size: 13px; }

/* --- hero --- */
.hero {
  padding: 96px 0 112px;
  position: relative;
}
.hero-grid {
  display: grid;
  grid-template-columns: 7fr 5fr;
  gap: 56px;
  align-items: center;
}
.hero-eyebrow { margin-bottom: 28px; color: var(--accent); }
.hero h1 {
  font-size: clamp(40px, 7.2vw, 88px);
  font-weight: 600;
  line-height: 1.0;
  letter-spacing: -3px;
  color: var(--ink-strong);
  margin-bottom: 28px;
}
.hero-lead {
  font-size: clamp(16px, 1.5vw, 19px);
  line-height: 1.6;
  color: var(--ink-mute);
  max-width: 560px;
  margin-bottom: 36px;
}
.hero-cta { display: flex; flex-wrap: wrap; gap: 12px; margin-bottom: 32px; }
.hero-chips { display: flex; flex-wrap: wrap; gap: 8px; }
.chip {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 14px;
  border: 1px solid var(--line-2);
  border-radius: 999px;
  background: var(--glass);
  backdrop-filter: blur(12px);
  font-family: 'IBM Plex Mono', ui-monospace, monospace;
  font-size: 11px;
  font-weight: 500;
  letter-spacing: 0.4px;
  color: var(--ink-body);
}
.chip .dot {
  width: 6px;
  height: 6px;
  border-radius: 999px;
  background: var(--success);
  box-shadow: 0 0 8px rgba(93,211,122,0.6);
}

/* --- logo stage (hero right) — orbital rings around centered logo --- */
.logo-stage {
  position: relative;
  aspect-ratio: 1 / 1;
  display: flex;
  align-items: center;
  justify-content: center;
  animation: fadeIn 1.2s 0.3s both ease-out;
}
.logo-stage .orbit {
  position: absolute;
  inset: 0;
  border: 1px solid var(--line);
  border-radius: 50%;
  animation: spin 60s linear infinite;
}
.logo-stage .orbit.o2 {
  inset: 8%;
  border-color: var(--line-2);
  animation-duration: 90s;
  animation-direction: reverse;
}
.logo-stage .orbit.o3 {
  inset: 18%;
  border-color: var(--line);
  animation-duration: 120s;
}
.logo-stage .orbit::before {
  content: '';
  position: absolute;
  top: -3px;
  left: 50%;
  width: 6px;
  height: 6px;
  background: var(--accent);
  border-radius: 50%;
  transform: translateX(-50%);
  box-shadow: 0 0 16px var(--accent);
}
.logo-stage .orbit.o2::before {
  background: var(--accent-blue);
  box-shadow: 0 0 12px var(--accent-blue);
  top: auto;
  bottom: -3px;
}
.logo-stage .orbit.o3::before {
  background: var(--warm);
  box-shadow: 0 0 10px var(--warm);
  left: -3px;
  top: 50%;
  transform: translateY(-50%);
}
.logo-stage .logo-wrap {
  position: relative;
  width: 62%;
  filter: drop-shadow(0 0 40px rgba(126,232,250,0.10));
}
.logo-stage .logo-wrap svg { width: 100%; height: auto; display: block; }
.logo-stage .corner {
  position: absolute;
  font-family: 'IBM Plex Mono', ui-monospace, monospace;
  font-size: 10px;
  letter-spacing: 1.4px;
  color: var(--ink-faint);
  text-transform: uppercase;
}
.logo-stage .corner.tl { top: 2%; left: 2%; }
.logo-stage .corner.tr { top: 2%; right: 2%; text-align: right; }
.logo-stage .corner.bl { bottom: 2%; left: 2%; }
.logo-stage .corner.br { bottom: 2%; right: 2%; text-align: right; }

@keyframes spin { to { transform: rotate(360deg); } }
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
@keyframes slideUp { from { opacity: 0; transform: translateY(22px); } to { opacity: 1; transform: translateY(0); } }

@media (prefers-reduced-motion: reduce) {
  .logo-stage, .logo-stage .orbit { animation: none; }
}

/* --- terminal artifact (used in live-ops section) --- */
.live-ops .terminal { max-width: 920px; margin: 0 auto; }
.terminal {
  background: var(--bg-3);
  border: 1px solid var(--line-2);
  border-radius: 14px;
  overflow: hidden;
  box-shadow: var(--shadow-card), var(--shadow-glow-cyan);
  backdrop-filter: blur(20px);
}
.term-bar {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 14px;
  border-bottom: 1px solid var(--line);
  background: var(--bg-2);
}
.term-bar .dots { display: flex; gap: 6px; }
.term-bar .dots span {
  width: 10px; height: 10px; border-radius: 999px;
  background: var(--line-2);
}
.term-bar .dots span:nth-child(1) { background: rgba(255,107,107,0.6); }
.term-bar .dots span:nth-child(2) { background: rgba(232,201,160,0.6); }
.term-bar .dots span:nth-child(3) { background: rgba(93,211,122,0.6); }
.term-bar .term-title {
  flex: 1;
  text-align: center;
  font-family: 'IBM Plex Mono', ui-monospace, monospace;
  font-size: 12px;
  color: var(--ink-faint);
  letter-spacing: 0.4px;
}
.term-body {
  padding: 24px 22px;
  font-family: 'IBM Plex Mono', ui-monospace, monospace;
  font-size: 13px;
  line-height: 1.65;
  color: var(--ink-body);
  white-space: pre-wrap;
}
.term-body .prompt { color: var(--accent); }
.term-body .ok { color: var(--success); }
.term-body .warn { color: var(--warm); }
.term-body .mute { color: var(--ink-faint); }

/* --- generic section --- */
section { padding: 96px 0; }
section.hero { padding: 96px 0 64px; }
section + section { padding-top: 96px; }
/* hairline divider between sections (subtle) */
section + section::before {
  content: '';
  display: block;
  max-width: 1200px;
  height: 1px;
  margin: 0 auto 96px;
  background: linear-gradient(90deg, transparent, var(--line), transparent);
}

/* --- services --- */
.services-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}
.service-card {
  position: relative;
  padding: 32px;
  background: var(--glass);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid var(--line-2);
  border-radius: 14px;
  box-shadow: var(--shadow-card);
  transition: transform var(--t), border-color var(--t), box-shadow var(--t);
  display: flex;
  flex-direction: column;
}
.service-card:hover {
  transform: translateY(-3px);
  border-color: var(--line-accent);
  box-shadow: var(--shadow-card), var(--shadow-glow-cyan);
}
.service-icon {
  width: 40px; height: 40px;
  display: grid;
  place-items: center;
  border-radius: 10px;
  background: var(--accent-soft);
  border: 1px solid var(--line-accent);
  color: var(--accent);
  margin-bottom: 24px;
}
.service-icon svg { width: 22px; height: 22px; stroke: currentColor; fill: none; stroke-width: 1.6; }
.service-idx {
  font-family: 'IBM Plex Mono', ui-monospace, monospace;
  font-size: 11px;
  letter-spacing: 1.4px;
  text-transform: uppercase;
  color: var(--ink-faint);
  margin-bottom: 12px;
}
.service-card h3 {
  font-size: 22px;
  font-weight: 600;
  line-height: 1.3;
  letter-spacing: -0.3px;
  color: var(--ink-strong);
  margin-bottom: 16px;
}
.service-card p {
  font-size: 15px;
  line-height: 1.6;
  color: var(--ink-body);
  margin-bottom: 24px;
  flex: 1;
}
.tag-row { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 24px; }
.tag {
  font-family: 'IBM Plex Mono', ui-monospace, monospace;
  font-size: 11px;
  letter-spacing: 0.3px;
  padding: 4px 10px;
  background: var(--glass-strong);
  border: 1px solid var(--line-2);
  border-radius: 999px;
  color: var(--ink-mute);
}
.service-link {
  font-family: 'IBM Plex Mono', ui-monospace, monospace;
  font-size: 12px;
  letter-spacing: 0.4px;
  color: var(--accent);
  font-weight: 500;
  text-transform: uppercase;
}

/* --- philosophy --- */
.philosophy {
  position: relative;
}
.philosophy-card {
  padding: 64px;
  border-radius: 20px;
  background: var(--bg-2);
  border: 1px solid var(--line-2);
  position: relative;
  overflow: hidden;
}
.philosophy-card::before {
  content: '';
  position: absolute;
  inset: 0;
  background:
    radial-gradient(circle at 20% 0%, rgba(232,201,160,0.10), transparent 60%),
    radial-gradient(circle at 100% 100%, rgba(126,232,250,0.06), transparent 50%);
  pointer-events: none;
}
.philosophy-card > * { position: relative; }
.philosophy-h2 {
  font-size: clamp(28px, 4vw, 44px);
  font-weight: 600;
  line-height: 1.1;
  letter-spacing: -1px;
  color: var(--ink-strong);
  margin-top: 24px;
  margin-bottom: 32px;
  max-width: 720px;
}
.philosophy-quote {
  font-size: clamp(20px, 2.4vw, 28px);
  line-height: 1.4;
  color: var(--ink);
  font-weight: 400;
  letter-spacing: -0.4px;
  max-width: 880px;
  position: relative;
  padding-left: 32px;
  border-left: 2px solid var(--warm);
}
.philosophy-sig {
  margin-top: 32px;
  font-family: 'IBM Plex Mono', ui-monospace, monospace;
  font-size: 13px;
  letter-spacing: 0.4px;
  color: var(--ink-mute);
}

/* --- stack grid --- */
.stack-grid {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 1px;
  background: var(--line);
  border: 1px solid var(--line);
  border-radius: 14px;
  overflow: hidden;
  backdrop-filter: blur(20px);
}
.stack-cell {
  padding: 24px 12px;
  background: var(--glass);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 10px;
  min-height: 110px;
  transition: background var(--t);
}
.stack-cell:hover { background: var(--bg-2); }
.stack-cell img {
  width: 32px;
  height: 32px;
  filter: brightness(0) invert(1);
  opacity: 0.75;
  transition: opacity var(--t);
}
.stack-cell:hover img { opacity: 1; }
.stack-cell span {
  font-family: 'IBM Plex Mono', ui-monospace, monospace;
  font-size: 11px;
  letter-spacing: 0.3px;
  color: var(--ink-mute);
  text-align: center;
}
.stack-cell:hover span { color: var(--ink); }

/* --- CTA band --- */
.cta-band {
  padding: 64px;
  border-radius: 20px;
  background:
    radial-gradient(circle at 80% 0%, rgba(126,232,250,0.15), transparent 60%),
    var(--bg-2);
  border: 1px solid var(--line-accent);
  box-shadow: var(--shadow-glow-cyan);
  text-align: center;
}
.cta-band .eyebrow { margin-bottom: 16px; color: var(--accent); }
.cta-band h2 {
  font-size: clamp(28px, 4.5vw, 48px);
  font-weight: 600;
  line-height: 1.1;
  letter-spacing: -1.2px;
  color: var(--ink-strong);
  margin-bottom: 32px;
}

/* --- footer --- */
.footer {
  border-top: 1px solid var(--line);
  padding: 64px 0 48px;
  margin-top: 80px;
}
.footer-grid {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1fr;
  gap: 32px;
  margin-bottom: 48px;
}
.footer-brand .brand { margin-bottom: 16px; }
.footer-tagline {
  font-size: 14px;
  color: var(--ink-mute);
  max-width: 320px;
  line-height: 1.55;
}
.footer-col h4 {
  font-family: 'IBM Plex Mono', ui-monospace, monospace;
  font-size: 11px;
  font-weight: 500;
  letter-spacing: 1.6px;
  text-transform: uppercase;
  color: var(--ink-mute);
  margin-bottom: 16px;
}
.footer-col ul { list-style: none; display: flex; flex-direction: column; gap: 10px; }
.footer-col a { font-size: 14px; color: var(--ink-body); }
.footer-col a:hover { color: var(--ink-strong); }
.footer-bottom {
  padding-top: 32px;
  border-top: 1px solid var(--line);
  display: flex;
  flex-wrap: wrap;
  gap: 24px;
  justify-content: space-between;
  align-items: center;
  font-size: 12px;
  color: var(--ink-faint);
  font-family: 'IBM Plex Mono', ui-monospace, monospace;
  letter-spacing: 0.3px;
}

/* --- responsive --- */
@media (max-width: 1024px) {
  .services-grid { grid-template-columns: repeat(2, 1fr); }
  .stack-grid { grid-template-columns: repeat(4, 1fr); }
  .hero-grid { grid-template-columns: 1fr; gap: 48px; }
  .footer-grid { grid-template-columns: 1fr 1fr; }
}
@media (max-width: 640px) {
  .container, .container-wide, .top-nav-inner { padding: 0 20px; }
  .nav-links { display: none; }
  section { padding: 72px 0; }
  .hero { padding: 56px 0 80px; }
  .services-grid { grid-template-columns: 1fr; }
  .stack-grid { grid-template-columns: repeat(3, 1fr); }
  .stack-cell { padding: 18px 6px; min-height: 96px; }
  .stack-cell img { width: 26px; height: 26px; }
  .philosophy-card { padding: 32px 24px; }
  .cta-band { padding: 40px 24px; }
  .footer-grid { grid-template-columns: 1fr; gap: 24px; }
  .term-body { font-size: 12px; padding: 18px 16px; }
}
"""

# ----------------------------------------------------------------------------
# Service icons (24px stroke icons, currentColor)
# ----------------------------------------------------------------------------
ICON_INFRA = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="18" height="6" rx="1.5"/><rect x="3" y="14" width="18" height="6" rx="1.5"/><circle cx="6.5" cy="7" r="0.8" fill="currentColor"/><circle cx="6.5" cy="17" r="0.8" fill="currentColor"/></svg>'
ICON_AI = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2v4M12 18v4M2 12h4M18 12h4M5 5l2.5 2.5M16.5 16.5L19 19M5 19l2.5-2.5M16.5 7.5L19 5"/><circle cx="12" cy="12" r="4"/></svg>'
ICON_BIZ = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="6" width="18" height="14" rx="1.5"/><path d="M3 10h18M8 6V4h8v2"/></svg>'
ICONS = [ICON_INFRA, ICON_AI, ICON_BIZ]

# ----------------------------------------------------------------------------
# Templates
# ----------------------------------------------------------------------------
def head(c, lang):
    canonical = f"{SITE}/{lang}/"
    alternates = "\n  ".join([
        f'<link rel="alternate" hreflang="{l}" href="{SITE}/{l}/" />'
        for l in ["en", "fr", "th"]
    ])
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#0A0C10">
<meta name="color-scheme" content="dark">
<title>{c['title']}</title>
<meta name="description" content="{c['meta_desc']}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{canonical}">
{alternates}
<link rel="alternate" hreflang="x-default" href="{SITE}/">
<link rel="icon" type="image/svg+xml" href="/als-mark.svg">
<link rel="apple-touch-icon" href="/als-mark.svg">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{c['title']}">
<meta property="og:description" content="{c['meta_desc']}">
<meta property="og:locale" content="{c['og_locale']}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{c['title']}">
<meta name="twitter:description" content="{c['meta_desc']}">
<meta name="twitter:image" content="{SITE}/og-image.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=IBM+Plex+Sans+Thai:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{CSS}</style>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{BRAND}",
  "url": "{SITE}",
  "logo": "{SITE}/als-mark.svg",
  "email": "{EMAIL}",
  "address": {{
    "@type": "PostalAddress",
    "addressLocality": "Bangkok",
    "addressCountry": "TH"
  }},
  "areaServed": ["Thailand", "Vietnam", "Singapore", "Southeast Asia"],
  "description": "{c['meta_desc']}"
}}
</script>
</head>
"""

def lang_pills(active):
    return '<div class="lang-switch" role="group" aria-label="Language">' + "".join(
        f'<a href="/{l}/" hreflang="{l}" class="{ "active" if l == active else "" }">{l.upper()}</a>'
        for l in ["en", "fr", "th"]
    ) + '</div>'

def nav(c, lang):
    return f"""<header class="top-nav">
  <div class="top-nav-inner">
    <a href="/{lang}/" class="brand">
      <img src="/als-mark.svg" alt="ALS mark" width="28" height="28">
      <span class="brand-name">Always Link Solutions</span>
    </a>
    <nav>
      <ul class="nav-links">
        <li><a href="#services">{c['nav_services']}</a></li>
        <li><a href="#stack">{c['nav_stack']}</a></li>
        <li><a href="#philosophy">{c['nav_philosophy']}</a></li>
        <li><a href="#contact">{c['nav_contact']}</a></li>
      </ul>
    </nav>
    <div class="nav-right">
      {lang_pills(lang)}
      <a href="mailto:{EMAIL}" class="btn btn-primary btn-sm">{c['nav_contact']}</a>
    </div>
  </div>
</header>
"""

def hero(c):
    return f"""<section class="hero container-wide">
  <div class="hero-grid">
    <div>
      <span class="eyebrow accent hero-eyebrow">{c['hero_eyebrow']}</span>
      <h1>{c['hero_h1_html']}</h1>
      <p class="hero-lead">{c['hero_lead']}</p>
      <div class="hero-cta">
        <a href="mailto:{EMAIL}" class="btn btn-primary">{c['hero_cta_primary']}
          <svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M1 7h12M8 2l5 5-5 5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </a>
        <a href="#services" class="btn btn-ghost">{c['hero_cta_secondary']}</a>
      </div>
      <div class="hero-chips">
        <span class="chip"><span class="dot"></span>{c['hero_chip_uptime']}</span>
        <span class="chip">{c['hero_chip_proxmox']}</span>
        <span class="chip">{c['hero_chip_open']}</span>
      </div>
    </div>
    <div class="logo-stage" aria-hidden="true">
      <div class="orbit"></div>
      <div class="orbit o2"></div>
      <div class="orbit o3"></div>
      <span class="corner tl">[01] BRAND</span>
      <span class="corner tr">v2026.05</span>
      <span class="corner bl">BKK</span>
      <span class="corner br">alwayslinksolutions.com</span>
      <div class="logo-wrap">{LOGO_SVG}</div>
    </div>
  </div>
</section>
"""

def services(c):
    cards = "\n".join(
        f"""    <article class="service-card">
      <div class="service-icon">{ICONS[i]}</div>
      <span class="service-idx">{s['idx']}</span>
      <h3>{s['h3_html']}</h3>
      <p>{s['p']}</p>
      <div class="tag-row">{ ''.join(f'<span class="tag">{t}</span>' for t in s['tags']) }</div>
      <a href="mailto:{EMAIL}" class="service-link">{c['service_more']}</a>
    </article>"""
        for i, s in enumerate(c['services'])
    )
    return f"""<section id="services" class="container">
  <div class="section-head">
    <span class="eyebrow accent">{c['services_eyebrow']}</span>
    <h2>{c['services_h2_html']}</h2>
    <p class="lead">{c['services_lead']}</p>
  </div>
  <div class="services-grid">
{cards}
  </div>
</section>
"""

def live_ops(c):
    return f"""<section class="container live-ops">
  <div class="section-head">
    <span class="eyebrow accent">{c['live_eyebrow']}</span>
    <h2>{c['live_h3']}</h2>
    <p class="lead">{c['live_lead']}</p>
  </div>
  <div class="terminal" aria-hidden="true">
    <div class="term-bar">
      <div class="dots"><span></span><span></span><span></span></div>
      <span class="term-title">{c['term_title']}</span>
    </div>
    <div class="term-body"><span class="prompt">$</span> systemctl is-active proxmox-cluster
<span class="ok">active</span>

<span class="prompt">$</span> docker ps --format '{{{{.Names}}}}' | wc -l
<span class="ok">42</span>  <span class="mute"># containers running</span>

<span class="prompt">$</span> ollama ps
<span class="mute">NAME           SIZE     PROCESSOR</span>
qwen3.6:35b    23 GB    <span class="ok">100% GPU</span>

<span class="prompt">$</span> curl -s alwayslinksolutions.com | grep '&lt;title&gt;'
<span class="warn">↳ {BRAND}</span>

<span class="prompt">$</span> als status
<span class="ok">→ all systems holding.</span></div>
  </div>
</section>
"""

def philosophy(c):
    return f"""<section id="philosophy" class="philosophy container">
  <div class="philosophy-card">
    <span class="eyebrow accent">{c['phil_eyebrow']}</span>
    <h2 class="philosophy-h2">{c['phil_h2']}</h2>
    <blockquote class="philosophy-quote">{c['phil_quote_html']}</blockquote>
    <div class="philosophy-sig">— {c['phil_sig']}</div>
  </div>
</section>
"""

def stack_section(c):
    cells = "\n".join(
        f'    <div class="stack-cell"><img src="/assets/logos/{slug}.svg" alt="{name}" loading="lazy" width="32" height="32"><span>{name}</span></div>'
        for name, slug in STACK
    )
    return f"""<section id="stack" class="container">
  <div class="section-head">
    <span class="eyebrow accent">{c['stack_eyebrow']}</span>
    <h2>{c['stack_h2']}</h2>
    <p class="lead">{c['stack_lead']}</p>
  </div>
  <div class="stack-grid">
{cells}
  </div>
</section>
"""

def cta(c):
    return f"""<section class="container">
  <div class="cta-band">
    <span class="eyebrow accent">{c['cta_eyebrow']}</span>
    <h2>{c['cta_h2_html']}</h2>
    <a href="mailto:{EMAIL}" class="btn btn-primary">{c['cta_button']}</a>
  </div>
</section>
"""

def footer(c, lang):
    return f"""<footer id="contact" class="footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="/{lang}/" class="brand">
          <img src="/als-mark.svg" alt="ALS mark" width="28" height="28">
          <span class="brand-name">Always Link Solutions</span>
        </a>
        <p class="footer-tagline">{c['footer_tagline']}</p>
      </div>
      <div class="footer-col">
        <h4>{c['nav_services']}</h4>
        <ul>
          <li><a href="#services">{c['services'][0]['h3_plain']}</a></li>
          <li><a href="#services">{c['services'][1]['h3_plain']}</a></li>
          <li><a href="#services">{c['services'][2]['h3_plain']}</a></li>
          <li><a href="#stack">{c['nav_stack']}</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>{c['footer_company']}</h4>
        <ul>
          <li><a href="#philosophy">{c['nav_philosophy']}</a></li>
          <li><a href="mailto:{EMAIL}">{c['nav_contact']}</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>{c['footer_legal']}</h4>
        <ul>
          <li><a href="/en/">EN</a> · <a href="/fr/">FR</a> · <a href="/th/">TH</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© {date.today().year} {BRAND} · {c['footer_reg']}</span>
      <span>{c['footer_built_html']}</span>
    </div>
  </div>
</footer>
"""

def build_one(lang):
    c = COPY[lang]
    html = head(c, lang)
    html += "<body>\n"
    html += nav(c, lang)
    html += "<main>\n"
    html += hero(c)
    html += services(c)
    html += live_ops(c)
    html += philosophy(c)
    html += stack_section(c)
    html += cta(c)
    html += "</main>\n"
    html += footer(c, lang)
    html += "</body>\n</html>\n"
    # collapse blank lines
    html = re.sub(r'\n\s*\n\s*\n+', '\n\n', html)
    out = ROOT / lang / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"  ✓ {lang}/index.html  {out.stat().st_size:>7} B")

def build_sitemap():
    urls = "\n".join(
        f'  <url><loc>{SITE}/{l}/</loc><xhtml:link rel="alternate" hreflang="{l}" href="{SITE}/{l}/"/><lastmod>{TODAY}</lastmod><priority>0.9</priority></url>'
        for l in ["en", "fr", "th"]
    )
    sm = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url><loc>{SITE}/</loc><lastmod>{TODAY}</lastmod><priority>1.0</priority></url>
{urls}
</urlset>
"""
    (ROOT / "sitemap.xml").write_text(sm, encoding="utf-8")
    print(f"  ✓ sitemap.xml")

if __name__ == "__main__":
    print(f"Building {BRAND} landing — dark glass brand kit")
    for lang in ["en", "fr", "th"]:
        build_one(lang)
    build_sitemap()
    print("Done.")
