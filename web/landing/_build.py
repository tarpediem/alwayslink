"""
Build script for Always Link Solutions landing v2.
Generates FR / EN / TH index.html from a shared template + content dict.
Also emits sitemap.xml, robots.txt, llms.txt.
"""
from pathlib import Path
import json

OUT = Path(__file__).parent
SITE = "https://alwayslinksolutions.com"
BRAND = "Always Link Solutions"
EMAIL = "hello@alwayslinksolutions.com"
PHONE = "+66 (0) xx xxx xxxx"
CITY = "Bangkok"

# ---------------------------------------------------------------------------
# Logo grid — ~36 tools the agency works with, organized by lane
# (paths relative to site root; served from /assets/logos/ per deploy structure)
# ---------------------------------------------------------------------------
STACK = [
    # Infra / OS
    ("Proxmox",        "/assets/logos/proxmox.svg"),
    ("Docker",         "/assets/logos/docker.svg"),
    ("Kubernetes",     "/assets/logos/kubernetes.svg"),
    ("Linux",          "/assets/logos/linux.svg"),
    ("Ubuntu",         "/assets/logos/ubuntu.svg"),
    # Dev
    ("Python",         "/assets/logos/python.svg"),
    ("FastAPI",        "/assets/logos/fastapi.svg"),
    ("TypeScript",     "/assets/logos/typescript.svg"),
    ("Node.js",        "/assets/logos/node.svg"),
    ("Bun",            "/assets/logos/bun.svg"),
    ("Rust",           "/assets/logos/rust.svg"),
    ("Go",             "/assets/logos/go.svg"),
    # Databases
    ("PostgreSQL",     "/assets/logos/postgresql.svg"),
    ("Redis",          "/assets/logos/redis.svg"),
    ("Neo4j",          "/assets/logos/neo4j.svg"),
    ("ChromaDB",       "/assets/logos/chromadb.svg"),
    # AI / LLM
    ("Ollama",         "/assets/logos/ollama.svg"),
    ("Claude",         "/assets/logos/claude-ai.svg"),
    ("OpenAI",         "/assets/logos/openai.svg"),
    ("HuggingFace",    "/assets/logos/huggingface.svg"),
    ("LangChain",      "/assets/logos/langchain.svg"),
    # Automation / business
    ("n8n",            "/assets/logos/n8n.svg"),
    ("Odoo",           "/assets/logos/odoo.svg"),
    ("Mailcow",        "/assets/logos/mailcow.svg"),
    ("Nextcloud",      "/assets/logos/nextcloud.svg"),
    ("OnlyOffice",     "/assets/logos/onlyoffice.svg"),
    # Network / cloud
    ("Cloudflare",     "/assets/logos/cloudflare.svg"),
    ("Nginx",          "/assets/logos/nginx.svg"),
    ("Tailscale",      "/assets/logos/tailscale.svg"),
    ("OPNsense",       "/assets/logos/opnsense.svg"),
    # Dev tools
    ("GitHub",         "/assets/logos/github.svg"),
    ("Obsidian",       "/assets/logos/obsidian.svg"),
    # Self-host
    ("Home Assistant", "/assets/logos/home-assistant.svg"),
    ("Jellyfin",       "/assets/logos/jellyfin.svg"),
    # CI/IaC
    ("Terraform",      "/assets/logos/terraform.svg"),
    ("Ansible",        "/assets/logos/ansible.svg"),
]

# ---------------------------------------------------------------------------
# Content per language
# ---------------------------------------------------------------------------
CONTENT = {
    "en": {
        "dir": "ltr",
        "html_lang": "en",
        "title": "Always Link Solutions — Infrastructure, AI & Automation for SME in Southeast Asia",
        "desc": ("Bangkok-based IT consulting for SME in Thailand and Southeast Asia. "
                 "Proxmox, Docker, Odoo ERP, self-hosted AI, automation with n8n. "
                 "Sober, durable infrastructure that runs in production."),
        "keywords": ("IT consulting Thailand, DevOps Bangkok, Proxmox Southeast Asia, "
                     "Odoo ERP SME, self-hosted AI, n8n automation, RAG LLM, "
                     "Linux migration, business systems Vietnam, BOI Cat 8.1"),
        "og_locale": "en_US",
        "nav": {"services": "Services", "approach": "Approach",
                "work": "Work", "contact": "Contact"},
        "brand_tag": "IT Consulting · SEA",
        "version": "v2026.04",
        "cta_primary": "Get in touch",
        "cta_secondary": "Our approach",
        "hero_eyebrow": "IT Consulting · Southeast Asia",
        "hero_title_parts": [
            ("Infrastructure, ", False),
            ("AI", True),  # italic serif
            (" & automation for connected SME.", False),
        ],
        "hero_lede": ("From Bangkok we design and operate sober, durable technical stacks — "
                      "Proxmox, Docker, Linux, Odoo, self-hosted RAG and LLM pipelines, n8n workflows. "
                      "Systems that run in production, not in slides."),
        "stack_eyebrow": "The Stack",
        "stack_title": "What we build with.",
        "stack_lede": ("A curated set of tools we've operated for years — open-source where it matters, "
                       "proprietary where it saves time, and always owned by the client."),
        "services_eyebrow": "Services",
        "services_title": "Four disciplines, one operating mode.",
        "services": [
            {
                "tag": "01",
                "title": "Infrastructure & Operations",
                "desc": ("Proxmox clusters, LXC / Docker, Linux migrations, 3-2-1 backup "
                         "with ZFS + Proxmox Backup Server + Acronis. We put durability first, "
                         "optimize second."),
            },
            {
                "tag": "02",
                "title": "AI, RAG & LLM Pipelines",
                "desc": ("Self-hosted Ollama or hybrid Claude/OpenAI. Retrieval over your own data "
                         "with PostgreSQL + pgvector, ChromaDB, Neo4j graphs. No data leaves "
                         "unless you want it to."),
            },
            {
                "tag": "03",
                "title": "ERP & Business Systems",
                "desc": ("Odoo Enterprise deployment, migrations (consolidation, version upgrades), "
                         "integration with MobiPOS, Mailcow, Nextcloud, OnlyOffice. Real ERP, "
                         "not spreadsheets plus hope."),
            },
            {
                "tag": "04",
                "title": "Automation & Workflows",
                "desc": ("n8n, MCP servers, Python glue. We automate the dull parts so your "
                         "team focuses on decisions — invoicing, reporting, document processing, "
                         "cross-system sync."),
            },
        ],
        "approach_eyebrow": "How we work",
        "approach_title": "Patient infrastructure, honest automation.",
        "approach_lede": ("We don't sell dashboards. We build systems that still work on a "
                          "Sunday morning, that a new hire can grasp in a week, and that you "
                          "can take back to your own team whenever you want."),
        "approach_points": [
            ("No lock-in by default",
             "Open-source whenever possible. You keep ownership of the code, the data, and the admin credentials."),
            ("Thailand & SEA-native",
             "We know BOI, we know Thai banking APIs, we know the gap between international tools and local reality."),
            ("Small team, direct line",
             "You talk to the engineer who does the work. No account manager, no escalation tree."),
            ("Production first, slides last",
             "We ship to your production within weeks, not quarters. Documentation comes in English or French."),
        ],
        "case_eyebrow": "Case study",
        "case_title": "Three Odoo instances, consolidated into one.",
        "case_body": ("A Bangkok jewelry manufacturer was running three independent Odoo instances "
                      "— one per workshop — with no shared inventory, no consolidated accounting, "
                      "and monthly reports built in Excel. We unified them into a single "
                      "Odoo Enterprise instance, migrated three years of history, and connected "
                      "the POS + Mailcow + Nextcloud stack. Cut month-end closing from 9 days to 2."),
            "case_author": "Olivier Magnier · Founder",
        "contact_eyebrow": "Contact",
        "contact_title": "Tell us what's in production.",
        "contact_lede": ("Short email, clear context, realistic timeline. "
                         "We'll reply within one working day."),
        "contact_cta": "Email us",
        "footer_tag": ("Patient infrastructure, honest automation. "
                       "For SME growing across Southeast Asia."),
        "footer_contact": "Contact",
        "footer_services_h": "Services",
        "footer_services": ["Infrastructure", "AI & RAG", "ERP & Odoo", "Linux migration"],
        "footer_resources_h": "Resources",
        "footer_resources": [("Blog", "#"), ("Open Source", "https://github.com/tarpediem/alwayslink"), ("Case studies", "#")],
        "footer_copy": "© 2026 ALWAYS LINK SOLUTIONS CO., LTD.",
        "footer_coords": "CRAFTED IN BKK — 13.7563°N, 100.5018°E",
    },
    "fr": {
        "dir": "ltr",
        "html_lang": "fr",
        "title": "Always Link Solutions — Infrastructure, IA & Automation pour PME en Asie du Sud-Est",
        "desc": ("Conseil IT basé à Bangkok pour PME en Thaïlande et Asie du Sud-Est. "
                 "Proxmox, Docker, Odoo ERP, IA auto-hébergée, automatisation avec n8n. "
                 "Une infrastructure sobre et durable qui tient en production."),
        "keywords": ("conseil IT Thaïlande, DevOps Bangkok, Proxmox Asie du Sud-Est, "
                     "Odoo ERP PME, IA auto-hébergée, automatisation n8n, RAG LLM, "
                     "migration Linux, systèmes d'information Vietnam, BOI Cat 8.1"),
        "og_locale": "fr_FR",
        "nav": {"services": "Services", "approach": "Approche",
                "work": "Réalisations", "contact": "Contact"},
        "brand_tag": "IT Consulting · SEA",
        "version": "v2026.04",
        "cta_primary": "Nous contacter",
        "cta_secondary": "Notre approche",
        "hero_eyebrow": "IT Consulting · Asie du Sud-Est",
        "hero_title_parts": [
            ("Infrastructure, ", False),
            ("IA", True),
            (" & automation pour PME connectées.", False),
        ],
        "hero_lede": ("Depuis Bangkok, on conçoit et opère des stacks techniques sobres et durables — "
                      "Proxmox, Docker, Linux, Odoo, pipelines RAG et LLM auto-hébergés, workflows n8n. "
                      "Des systèmes qui tiennent en production, pas dans des slides."),
        "stack_eyebrow": "Le stack",
        "stack_title": "Ce avec quoi on construit.",
        "stack_lede": ("Un ensemble choisi d'outils qu'on opère depuis des années — open-source "
                       "quand ça compte, propriétaire quand ça fait gagner du temps, et toujours "
                       "propriété du client."),
        "services_eyebrow": "Services",
        "services_title": "Quatre disciplines, un seul mode opératoire.",
        "services": [
            {
                "tag": "01",
                "title": "Infrastructure & Ops",
                "desc": ("Clusters Proxmox, LXC / Docker, migrations Linux, backup 3-2-1 "
                         "avec ZFS + Proxmox Backup Server + Acronis. La durabilité avant "
                         "l'optimisation."),
            },
            {
                "tag": "02",
                "title": "IA, RAG & pipelines LLM",
                "desc": ("Ollama en auto-hébergé ou hybride Claude/OpenAI. Recherche sur vos "
                         "propres données avec PostgreSQL + pgvector, ChromaDB, graphes Neo4j. "
                         "Aucune donnée ne sort sans votre accord."),
            },
            {
                "tag": "03",
                "title": "ERP & systèmes métier",
                "desc": ("Déploiement Odoo Enterprise, migrations (consolidation, upgrades), "
                         "intégration avec MobiPOS, Mailcow, Nextcloud, OnlyOffice. De l'ERP "
                         "réel, pas des tableurs qu'on prie."),
            },
            {
                "tag": "04",
                "title": "Automation & workflows",
                "desc": ("n8n, serveurs MCP, scripts Python. On automatise les tâches répétitives "
                         "pour que vos équipes se concentrent sur les décisions — facturation, "
                         "reporting, traitement documentaire, synchro inter-systèmes."),
            },
        ],
        "approach_eyebrow": "Notre approche",
        "approach_title": "Infrastructure patiente, automation honnête.",
        "approach_lede": ("On ne vend pas des tableaux de bord. On construit des systèmes qui "
                          "fonctionnent encore le dimanche matin, qu'un nouvel arrivant "
                          "comprend en une semaine, et que vous pouvez ramener en interne "
                          "quand vous voulez."),
        "approach_points": [
            ("Pas de lock-in par défaut",
             "Open-source autant que possible. Vous restez propriétaire du code, des données, et des accès admin."),
            ("Ancrage Thaïlande & SEA",
             "On connaît BOI, les APIs bancaires thaïes, le décalage entre les outils internationaux et la réalité locale."),
            ("Petite équipe, ligne directe",
             "Vous parlez à l'ingénieur qui fait le travail. Ni account manager, ni arbre d'escalade."),
            ("Production d'abord, slides en dernier",
             "On livre en production en semaines, pas en trimestres. Doc en français ou anglais."),
        ],
        "case_eyebrow": "Cas client",
        "case_title": "Trois instances Odoo, consolidées en une seule.",
        "case_body": ("Un fabricant bijoutier de Bangkok tournait avec trois instances Odoo "
                      "indépendantes — une par atelier — sans inventaire partagé, sans "
                      "comptabilité consolidée, et des rapports mensuels faits sous Excel. "
                      "On a tout unifié dans une seule instance Odoo Enterprise, migré "
                      "trois ans d'historique, et connecté le stack POS + Mailcow + Nextcloud. "
                      "Clôture mensuelle passée de 9 à 2 jours."),
            "case_author": "Olivier Magnier · Founder",
        "contact_eyebrow": "Contact",
        "contact_title": "Racontez-nous ce qui tourne en production.",
        "contact_lede": ("Un email court, un contexte clair, un timing réaliste. "
                         "On répond sous un jour ouvré."),
        "contact_cta": "Nous écrire",
        "footer_tag": ("Infrastructure patiente, automation honnête. "
                       "Pour PME qui grandissent en Asie du Sud-Est."),
        "footer_contact": "Contact",
        "footer_services_h": "Services",
        "footer_services": ["Infrastructure", "IA & RAG", "ERP & Odoo", "Migration Linux"],
        "footer_resources_h": "Ressources",
        "footer_resources": [("Blog", "#"), ("Open Source", "https://github.com/tarpediem/alwayslink"), ("Cas clients", "#")],
        "footer_copy": "© 2026 ALWAYS LINK SOLUTIONS CO., LTD.",
        "footer_coords": "CRAFTED IN BKK — 13.7563°N, 100.5018°E",
    },
    "th": {
        "dir": "ltr",
        "html_lang": "th",
        "title": "Always Link Solutions — โครงสร้างพื้นฐาน, AI และระบบอัตโนมัติ สำหรับ SME ในเอเชียตะวันออกเฉียงใต้",
        "desc": ("บริษัทที่ปรึกษาด้าน IT ตั้งอยู่ที่กรุงเทพฯ ให้บริการ SME ในประเทศไทยและเอเชียตะวันออกเฉียงใต้. "
                 "Proxmox, Docker, Odoo ERP, AI ที่โฮสต์เอง, ระบบอัตโนมัติด้วย n8n. "
                 "โครงสร้างพื้นฐานที่ประณีตและยั่งยืน พร้อมใช้งานจริงในระบบ production."),
        "keywords": ("ที่ปรึกษา IT กรุงเทพ, DevOps ประเทศไทย, Proxmox เอเชียตะวันออกเฉียงใต้, "
                     "Odoo ERP SME, AI โฮสต์เอง, ระบบอัตโนมัติ n8n, RAG LLM, "
                     "การย้าย Linux, ระบบธุรกิจ เวียดนาม, BOI Cat 8.1"),
        "og_locale": "th_TH",
        "nav": {"services": "บริการ", "approach": "วิธีการทำงาน",
                "work": "ผลงาน", "contact": "ติดต่อ"},
        "brand_tag": "IT Consulting · SEA",
        "version": "v2026.04",
        "cta_primary": "ติดต่อเรา",
        "cta_secondary": "วิธีการทำงานของเรา",
        "hero_eyebrow": "IT Consulting · เอเชียตะวันออกเฉียงใต้",
        "hero_title_parts": [
            ("โครงสร้างพื้นฐาน, ", False),
            ("AI", True),
            (" และระบบอัตโนมัติสำหรับ SME ที่เชื่อมโยงกัน", False),
        ],
        "hero_lede": ("จากกรุงเทพฯ เราออกแบบและดำเนินงานสแตกเทคนิคที่ประณีตและยั่งยืน — "
                      "Proxmox, Docker, Linux, Odoo, ไปป์ไลน์ RAG และ LLM ที่โฮสต์เอง, เวิร์กโฟลว์ n8n "
                      "ระบบที่ทำงานได้จริงในโปรดักชัน ไม่ใช่แค่ในสไลด์"),
        "stack_eyebrow": "สแตก",
        "stack_title": "เครื่องมือที่เราใช้สร้างงาน",
        "stack_lede": ("ชุดเครื่องมือที่คัดสรรมาแล้วและเราใช้งานจริงมาหลายปี — โอเพนซอร์สในจุดสำคัญ "
                       "ซอฟต์แวร์เชิงพาณิชย์เมื่อช่วยประหยัดเวลา และลูกค้าเป็นเจ้าของทุกอย่างเสมอ"),
        "services_eyebrow": "บริการ",
        "services_title": "สี่สาขา หนึ่งวิธีการทำงาน",
        "services": [
            {
                "tag": "01",
                "title": "โครงสร้างพื้นฐานและการดำเนินงาน",
                "desc": ("คลัสเตอร์ Proxmox, LXC / Docker, การย้ายระบบ Linux, "
                         "การสำรองข้อมูลแบบ 3-2-1 ด้วย ZFS + Proxmox Backup Server + Acronis "
                         "ความยั่งยืนมาก่อนการปรับแต่ง"),
            },
            {
                "tag": "02",
                "title": "AI, RAG และไปป์ไลน์ LLM",
                "desc": ("Ollama แบบโฮสต์เอง หรือไฮบริดกับ Claude/OpenAI "
                         "ค้นหาข้อมูลภายในองค์กรของคุณด้วย PostgreSQL + pgvector, ChromaDB, กราฟ Neo4j "
                         "ข้อมูลไม่ออกจากระบบโดยที่คุณไม่อนุญาต"),
            },
            {
                "tag": "03",
                "title": "ERP และระบบธุรกิจ",
                "desc": ("การติดตั้ง Odoo Enterprise, การย้ายระบบ (รวมบัญชี, อัปเกรดเวอร์ชัน), "
                         "การเชื่อมต่อกับ MobiPOS, Mailcow, Nextcloud, OnlyOffice "
                         "ERP จริงๆ ไม่ใช่สเปรดชีตบวกความหวัง"),
            },
            {
                "tag": "04",
                "title": "ระบบอัตโนมัติและเวิร์กโฟลว์",
                "desc": ("n8n, MCP servers, สคริปต์ Python "
                         "เราทำให้งานซ้ำซากเป็นอัตโนมัติ เพื่อให้ทีมของคุณมุ่งเน้นที่การตัดสินใจ — "
                         "การออกใบแจ้งหนี้, รายงาน, ประมวลผลเอกสาร, การซิงค์ข้ามระบบ"),
            },
        ],
        "approach_eyebrow": "วิธีการทำงาน",
        "approach_title": "โครงสร้างพื้นฐานที่อดทน ระบบอัตโนมัติที่ซื่อสัตย์",
        "approach_lede": ("เราไม่ขายแดชบอร์ด เราสร้างระบบที่ยังทำงานได้ในเช้าวันอาทิตย์ "
                          "ที่พนักงานใหม่เข้าใจได้ในหนึ่งสัปดาห์ "
                          "และที่คุณสามารถรับกลับไปให้ทีมของคุณได้ทุกเมื่อ"),
        "approach_points": [
            ("ไม่มี vendor lock-in โดยดีฟอลต์",
             "ใช้โอเพนซอร์สเท่าที่ทำได้ คุณเป็นเจ้าของโค้ด ข้อมูล และสิทธิ์ผู้ดูแลระบบ"),
            ("เข้าใจประเทศไทยและ SEA",
             "เรารู้เรื่อง BOI, API ธนาคารไทย, ช่องว่างระหว่างเครื่องมือสากลกับความเป็นจริงในพื้นที่"),
            ("ทีมเล็ก ติดต่อตรง",
             "คุณคุยกับวิศวกรที่ทำงานจริง ไม่มี Account Manager ไม่มีโครงสร้างการส่งต่อ"),
            ("โปรดักชันก่อน สไลด์ทีหลัง",
             "เราส่งมอบเข้าโปรดักชันภายในไม่กี่สัปดาห์ ไม่ใช่หลายไตรมาส เอกสารเป็นภาษาอังกฤษหรือฝรั่งเศส"),
        ],
        "case_eyebrow": "ผลงาน",
        "case_title": "สาม Odoo รวมเป็นหนึ่ง",
        "case_body": ("ผู้ผลิตเครื่องประดับในกรุงเทพฯ ใช้ Odoo แยกกันสามระบบ — หนึ่งต่อหนึ่งโรงงาน — "
                      "ไม่มีคลังสินค้าร่วม ไม่มีบัญชีรวม และรายงานรายเดือนทำบน Excel "
                      "เรารวมทุกอย่างเข้าเป็น Odoo Enterprise เดียว ย้ายข้อมูลสามปี "
                      "และเชื่อมต่อ POS + Mailcow + Nextcloud "
                      "ปิดงบเดือนจาก 9 วัน เหลือ 2 วัน"),
            "case_author": "Olivier Magnier · ผู้ก่อตั้ง",
        "contact_eyebrow": "ติดต่อ",
        "contact_title": "บอกเราเรื่องระบบที่ใช้งานอยู่จริง",
        "contact_lede": ("อีเมลสั้นๆ บริบทที่ชัดเจน ระยะเวลาที่สมเหตุสมผล "
                         "เราตอบภายในหนึ่งวันทำการ"),
        "contact_cta": "ส่งอีเมลหาเรา",
        "footer_tag": ("โครงสร้างพื้นฐานที่อดทน ระบบอัตโนมัติที่ซื่อสัตย์ "
                       "สำหรับ SME ที่เติบโตในเอเชียตะวันออกเฉียงใต้"),
        "footer_contact": "ติดต่อ",
        "footer_services_h": "บริการ",
        "footer_services": ["โครงสร้างพื้นฐาน", "AI & RAG", "ERP & Odoo", "ย้ายระบบ Linux"],
        "footer_resources_h": "ทรัพยากร",
        "footer_resources": [("บล็อก", "#"), ("Open Source", "https://github.com/tarpediem/alwayslink"), ("ผลงาน", "#")],
        "footer_copy": "© 2026 ALWAYS LINK SOLUTIONS CO., LTD.",
        "footer_coords": "CRAFTED IN BKK — 13.7563°N, 100.5018°E",
    },
}

# ---------------------------------------------------------------------------
# Shared design tokens (Claude Design palette)
# ---------------------------------------------------------------------------
CSS = """
:root{
  --bg: #0A0C10;
  --bg-2: #0E1117;
  --ink: #F2F3F5;
  --ink-mute: #8A8F98;
  --ink-dim: #555A63;
  --line: rgba(255,255,255,0.06);
  --line-2: rgba(255,255,255,0.12);
  --accent: #7EE8FA;
  --accent-2: #3A6FF8;
  --warm: #E8C9A0;
  --serif: 'Instrument Serif', 'Noto Serif Thai', serif;
  --sans:  'Inter', 'IBM Plex Sans Thai', 'IBM Plex Sans Thai Looped', system-ui, sans-serif;
  --mono:  'Geist Mono', ui-monospace, 'SFMono-Regular', Consolas, monospace;
  --container: 1280px;
}
*, *::before, *::after { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body {
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  font-weight: 400;
  font-size: 16px;
  line-height: 1.55;
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
  min-height: 100vh;
  background-image:
    radial-gradient(1200px 600px at 80% -100px, rgba(58,111,248,0.10), transparent 60%),
    radial-gradient(900px 500px at 10% 120%, rgba(126,232,250,0.06), transparent 60%),
    linear-gradient(var(--bg), var(--bg));
}
a { color: inherit; text-decoration: none; }
.container { max-width: var(--container); margin: 0 auto; padding: 0 32px; }

/* -------- Header / nav -------- */
header.site {
  position: sticky; top: 0; z-index: 50;
  padding: 18px 0;
  backdrop-filter: blur(10px);
  background: rgba(10,12,16,0.72);
  border-bottom: 1px solid var(--line);
}
header.site .inner {
  display: flex; align-items: center; justify-content: space-between; gap: 24px;
}
.brand { display: flex; align-items: center; gap: 12px; font-family: var(--serif); font-size: 18px; font-weight: 500; letter-spacing: -0.01em; }
.brand svg { width: 28px; height: 28px; }
nav.main ul { list-style: none; padding: 0; margin: 0; display: flex; gap: 28px; font-size: 14px; }
nav.main a { color: var(--ink-mute); transition: color .2s; }
nav.main a:hover { color: var(--ink); }
.header-right { display: flex; align-items: center; gap: 18px; }
.lang-switcher { display: flex; gap: 2px; border: 1px solid var(--line-2); border-radius: 999px; padding: 4px; font-family: var(--mono); font-size: 11px; letter-spacing: 0.1em; }
.lang-switcher a {
  padding: 4px 10px; border-radius: 999px; color: var(--ink-mute); transition: all .2s; text-transform: uppercase;
}
.lang-switcher a.active { background: var(--ink); color: var(--bg); }
.lang-switcher a:hover:not(.active) { color: var(--ink); }
.btn {
  display: inline-flex; align-items: center; gap: 8px;
  padding: 10px 20px;
  border-radius: 999px;
  border: 1px solid var(--line-2);
  font-family: var(--mono); font-size: 13px; font-weight: 500;
  color: var(--ink);
  transition: all .25s;
}
.btn:hover { background: var(--ink); color: var(--bg); border-color: var(--ink); }
.btn-primary { background: var(--ink); color: var(--bg); border-color: var(--ink); }
.btn-primary:hover { background: var(--accent); border-color: var(--accent); }

/* -------- Section primitives -------- */
section { padding: 120px 0; position: relative; }
section.alt { background: var(--bg-2); }
.eyebrow { font-family: var(--mono); font-size: 12px; letter-spacing: 0.14em; text-transform: uppercase; color: var(--ink-mute); }
.eyebrow::before { content: "— "; color: var(--ink-dim); }
h1, h2, h3 { font-family: var(--serif); font-weight: 400; letter-spacing: -0.02em; margin: 0; }
h1 { font-size: clamp(40px, 7vw, 96px); line-height: 1.02; }
h2 { font-size: clamp(32px, 4.5vw, 56px); line-height: 1.08; }
h3 { font-size: 20px; line-height: 1.3; font-family: var(--sans); font-weight: 500; letter-spacing: -0.01em; }
p { color: var(--ink-mute); max-width: 65ch; }
p.lede { font-size: 18px; color: var(--ink-mute); max-width: 52ch; }
.italic { font-style: italic; color: var(--accent); }

/* -------- Hero -------- */
.hero { padding-top: 100px; padding-bottom: 160px; overflow: hidden; }
.hero .grid { display: grid; grid-template-columns: 1.35fr 1fr; gap: 80px; align-items: center; }
.hero h1 { margin-top: 24px; }
.hero .lede { margin-top: 28px; }
.hero .actions { display: flex; gap: 12px; margin-top: 36px; flex-wrap: wrap; }
.hero .vizbox { position: relative; min-height: 440px; display: flex; align-items: center; justify-content: center; }
.hero .mark { width: 120px; height: 120px; opacity: 0.95; }
.hero .mark-text { margin-top: 14px; font-family: var(--serif); font-size: 20px; letter-spacing: -0.01em; text-align: center; }
.hero .mark-sub { font-family: var(--mono); font-size: 10px; letter-spacing: 0.2em; color: var(--ink-dim); margin-top: 4px; text-align: center; }
.hero .orbit { position: absolute; border: 1px solid var(--line); border-radius: 50%; }
.hero .orbit.o1 { width: 340px; height: 340px; }
.hero .orbit.o2 { width: 480px; height: 480px; border-color: rgba(255,255,255,0.04); }
.hero .orbit.o3 { width: 620px; height: 620px; border-color: rgba(255,255,255,0.02); }
.hero .dot { position: absolute; width: 6px; height: 6px; border-radius: 50%; box-shadow: 0 0 20px currentColor; }
.hero .dot.warm { background: var(--warm); color: var(--warm); top: 30%; left: 50%; }
.hero .dot.cyan { background: var(--accent); color: var(--accent); top: 55%; right: 18%; }
.hero .dot.blue { background: var(--accent-2); color: var(--accent-2); bottom: 25%; right: 30%; }
.hero .meta-top { display: flex; justify-content: space-between; font-family: var(--mono); font-size: 11px; letter-spacing: 0.1em; color: var(--ink-dim); margin-bottom: 60px; }

/* -------- Services -------- */
.services-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1px; margin-top: 60px; background: var(--line); border: 1px solid var(--line); }
.service {
  background: var(--bg);
  padding: 48px 40px;
  transition: background .3s;
}
.service:hover { background: var(--bg-2); }
.service .tag { font-family: var(--mono); font-size: 11px; letter-spacing: 0.14em; color: var(--ink-dim); margin-bottom: 20px; }
.service h3 { font-family: var(--serif); font-size: 28px; font-weight: 400; letter-spacing: -0.01em; margin-bottom: 16px; }

/* -------- Stack logo grid -------- */
.stack-grid {
  margin-top: 60px;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(130px, 1fr));
  gap: 1px;
  background: var(--line);
  border: 1px solid var(--line);
}
.stack-item {
  background: var(--bg-2);
  padding: 28px 16px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  min-height: 120px;
  transition: background .25s;
}
.stack-item:hover { background: var(--bg); }
.stack-item img { width: 36px; height: 36px; opacity: 0.85; transition: opacity .25s; filter: saturate(0.9); }
.stack-item:hover img { opacity: 1; filter: none; }
.stack-item span { font-family: var(--mono); font-size: 11px; letter-spacing: 0.08em; color: var(--ink-mute); text-align: center; }

/* -------- Approach -------- */
.approach-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 80px; margin-top: 60px; }
.approach-points { display: flex; flex-direction: column; gap: 32px; }
.approach-point { padding-left: 20px; border-left: 1px solid var(--line-2); }
.approach-point h4 { margin: 0 0 8px; font-family: var(--sans); font-size: 15px; font-weight: 600; color: var(--ink); }
.approach-point p { margin: 0; font-size: 14px; }

/* -------- Case -------- */
.case {
  margin-top: 60px;
  padding: 56px;
  background: var(--bg-2);
  border: 1px solid var(--line);
  border-radius: 4px;
}
.case-body { font-family: var(--serif); font-size: clamp(22px, 2.5vw, 32px); line-height: 1.3; color: var(--ink); font-style: italic; margin: 24px 0 40px; }
.case-author { font-family: var(--mono); font-size: 12px; letter-spacing: 0.1em; color: var(--ink-mute); }
.case-author::before { content: "— "; color: var(--ink-dim); }

/* -------- Contact -------- */
.contact { text-align: center; padding: 160px 0; }
.contact h2 { margin: 24px auto 28px; }
.contact .lede { margin: 0 auto; text-align: center; }
.contact .btn { margin-top: 40px; }

/* -------- Footer -------- */
footer.site { padding: 80px 0 32px; border-top: 1px solid var(--line); background: var(--bg-2); }
footer.site .grid { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 48px; margin-bottom: 60px; }
footer.site h5 { font-family: var(--mono); font-size: 11px; letter-spacing: 0.14em; color: var(--ink-dim); margin: 0 0 16px; text-transform: uppercase; font-weight: 500; }
footer.site a, footer.site p { color: var(--ink-mute); font-size: 14px; line-height: 1.7; }
footer.site a:hover { color: var(--ink); }
footer.site ul { list-style: none; padding: 0; margin: 0; }
footer.site .brand-col { font-family: var(--serif); font-size: 15px; font-style: italic; color: var(--ink-mute); max-width: 30ch; }
footer.site .brand-col svg { margin-bottom: 18px; width: 32px; height: 32px; }
footer.site .bottom { display: flex; justify-content: space-between; padding-top: 32px; border-top: 1px solid var(--line); font-family: var(--mono); font-size: 11px; letter-spacing: 0.1em; color: var(--ink-dim); text-transform: uppercase; }

/* -------- Responsive -------- */
@media (max-width: 980px) {
  section { padding: 80px 0; }
  .hero { padding-bottom: 80px; }
  .hero .grid, .approach-grid { grid-template-columns: 1fr; gap: 48px; }
  .hero .vizbox { min-height: 280px; }
  .services-grid { grid-template-columns: 1fr; }
  footer.site .grid { grid-template-columns: 1fr 1fr; gap: 32px; }
  nav.main { display: none; }
  .container { padding: 0 20px; }
  footer.site .bottom { flex-direction: column; gap: 12px; }
}
@media (max-width: 520px) {
  .stack-grid { grid-template-columns: repeat(3, 1fr); }
  .stack-item { padding: 20px 8px; min-height: 96px; }
  .stack-item img { width: 28px; height: 28px; }
  footer.site .grid { grid-template-columns: 1fr; }
  .case { padding: 32px 24px; }
  .contact { padding: 100px 0; }
}
"""

# ---------------------------------------------------------------------------
# ALS mark SVG (small, inline for performance)
# ---------------------------------------------------------------------------
MARK_INLINE = '<svg viewBox="0 0 38 23" xmlns="http://www.w3.org/2000/svg" fill="currentColor" aria-label="ALS mark"><circle cx="4" cy="17" r="4"/><circle cx="21" cy="3" r="4"/><circle cx="34" cy="19" r="4"/><path d="M6 17 L21 5 L33 19 L15 18 L14 13 L26 13" stroke="currentColor" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'

# ---------------------------------------------------------------------------
# JSON-LD schema.org (Organization + LocalBusiness + ProfessionalService)
# ---------------------------------------------------------------------------
def jsonld(lang):
    c = CONTENT[lang]
    data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": ["Organization", "ProfessionalService"],
                "@id": f"{SITE}/#organization",
                "name": BRAND,
                "legalName": "Always Link Solutions Co., Ltd.",
                "description": c["desc"],
                "url": SITE,
                "logo": f"{SITE}/als-mark.svg",
                "email": EMAIL,
                "telephone": PHONE,
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": "Bangkok",
                    "addressCountry": "TH",
                },
                "areaServed": [
                    {"@type": "Country", "name": "Thailand"},
                    {"@type": "Country", "name": "Vietnam"},
                    {"@type": "Country", "name": "Singapore"},
                    {"@type": "Place", "name": "Southeast Asia"},
                ],
                "serviceType": [
                    "IT consulting",
                    "DevOps",
                    "Infrastructure engineering",
                    "AI automation",
                    "Odoo ERP consulting",
                    "Self-hosted AI & RAG",
                ],
                "knowsAbout": [
                    "Proxmox", "Docker", "Kubernetes", "Linux",
                    "Odoo", "PostgreSQL", "Ollama", "Claude API",
                    "LangChain", "n8n", "RAG architecture",
                ],
                "sameAs": ["https://github.com/tarpediem/alwayslink"],
            },
            {
                "@type": "WebSite",
                "@id": f"{SITE}/#website",
                "url": SITE,
                "name": BRAND,
                "description": c["desc"],
                "publisher": {"@id": f"{SITE}/#organization"},
                "inLanguage": c["html_lang"],
            },
        ],
    }
    return json.dumps(data, ensure_ascii=False, indent=2)

# ---------------------------------------------------------------------------
# Template
# ---------------------------------------------------------------------------
def render(lang):
    c = CONTENT[lang]
    url = f"{SITE}/{lang}/"

    # Hero headline with italic serif word
    h1_html = "".join(
        f'<span class="italic">{txt}</span>' if italic else txt
        for txt, italic in c["hero_title_parts"]
    )

    # Language switcher (hreflang + active state)
    lang_links = []
    for code in ["en", "fr", "th"]:
        cls = "active" if code == lang else ""
        lang_links.append(f'<a href="/{code}/" hreflang="{code}" class="{cls}">{code.upper()}</a>')
    lang_switcher = "".join(lang_links)

    # hreflang alternates
    alternates = []
    for code in ["en", "fr", "th"]:
        alternates.append(f'<link rel="alternate" hreflang="{code}" href="{SITE}/{code}/" />')
    alternates.append(f'<link rel="alternate" hreflang="x-default" href="{SITE}/en/" />')

    # Services cards
    services_html = "".join(
        f'''<article class="service">
          <div class="tag">{s["tag"]}</div>
          <h3>{s["title"]}</h3>
          <p>{s["desc"]}</p>
        </article>''' for s in c["services"]
    )

    # Stack logos grid
    stack_html = "".join(
        f'<div class="stack-item"><img src="{src}" alt="{name}" loading="lazy" /><span>{name}</span></div>'
        for name, src in STACK
    )

    # Approach points
    approach_html = "".join(
        f'<div class="approach-point"><h4>{title}</h4><p>{body}</p></div>'
        for title, body in c["approach_points"]
    )

    # Footer services / resources
    footer_services = "".join(f"<li>{s}</li>" for s in c["footer_services"])
    footer_resources = "".join(
        f'<li><a href="{href}">{label}</a></li>' for label, href in c["footer_resources"]
    )

    return f"""<!DOCTYPE html>
<html lang="{c['html_lang']}" dir="{c['dir']}">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
<title>{c['title']}</title>
<meta name="description" content="{c['desc']}" />
<meta name="keywords" content="{c['keywords']}" />
<meta name="author" content="Always Link Solutions" />
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1" />
<meta name="theme-color" content="#0A0C10" />
<meta name="color-scheme" content="dark" />

<!-- Canonical + hreflang -->
<link rel="canonical" href="{url}" />
{chr(10).join(alternates)}

<!-- Open Graph -->
<meta property="og:type" content="website" />
<meta property="og:title" content="{c['title']}" />
<meta property="og:description" content="{c['desc']}" />
<meta property="og:url" content="{url}" />
<meta property="og:site_name" content="{BRAND}" />
<meta property="og:locale" content="{c['og_locale']}" />
<meta property="og:image" content="{SITE}/og-image.png" />
<meta property="og:image:alt" content="Always Link Solutions — IT consulting based in Bangkok" />

<!-- Twitter -->
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{c['title']}" />
<meta name="twitter:description" content="{c['desc']}" />
<meta name="twitter:image" content="{SITE}/og-image.png" />

<!-- Icons -->
<link rel="icon" type="image/svg+xml" href="/als-mark.svg" />
<link rel="apple-touch-icon" href="/apple-touch-icon.png" />

<!-- Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@300;400;500;600;700&family=Geist+Mono:wght@400;500&family=Noto+Serif+Thai:wght@400;500;600;700&family=IBM+Plex+Sans+Thai:wght@300;400;500;600&family=IBM+Plex+Sans+Thai+Looped:wght@300;400;500;600&display=swap" rel="stylesheet" />

<!-- JSON-LD -->
<script type="application/ld+json">
{jsonld(lang)}
</script>

<style>{CSS}</style>
</head>
<body>

<header class="site">
  <div class="container inner">
    <a href="/{lang}/" class="brand">{MARK_INLINE} {BRAND}</a>
    <nav class="main"><ul>
      <li><a href="#services">{c['nav']['services']}</a></li>
      <li><a href="#approach">{c['nav']['approach']}</a></li>
      <li><a href="#work">{c['nav']['work']}</a></li>
      <li><a href="#contact">{c['nav']['contact']}</a></li>
    </ul></nav>
    <div class="header-right">
      <div class="lang-switcher">{lang_switcher}</div>
      <a href="#contact" class="btn btn-primary">./contact</a>
    </div>
  </div>
</header>

<main>

<section class="hero">
  <div class="container">
    <div class="meta-top">
      <span>[01] BRAND</span>
      <span>{c['version']}</span>
    </div>
    <div class="grid">
      <div>
        <span class="eyebrow">{c['hero_eyebrow']}</span>
        <h1>{h1_html}</h1>
        <p class="lede">{c['hero_lede']}</p>
        <div class="actions">
          <a href="#contact" class="btn btn-primary">{c['cta_primary']}</a>
          <a href="#approach" class="btn">{c['cta_secondary']}</a>
        </div>
      </div>
      <div class="vizbox">
        <div class="orbit o3"></div>
        <div class="orbit o2"></div>
        <div class="orbit o1"></div>
        <div class="dot warm"></div>
        <div class="dot cyan"></div>
        <div class="dot blue"></div>
        <div style="text-align:center; position: relative; z-index: 2;">
          <div class="mark" style="color: var(--ink);">{MARK_INLINE}</div>
          <div class="mark-text">{BRAND.upper()}</div>
          <div class="mark-sub">SOLUTIONS</div>
        </div>
      </div>
    </div>
  </div>
</section>

<section id="services" class="alt">
  <div class="container">
    <span class="eyebrow">{c['services_eyebrow']}</span>
    <h2 style="max-width: 16ch; margin-top: 12px;">{c['services_title']}</h2>
    <div class="services-grid">{services_html}</div>
  </div>
</section>

<section id="stack">
  <div class="container">
    <span class="eyebrow">{c['stack_eyebrow']}</span>
    <h2 style="margin-top: 12px;">{c['stack_title']}</h2>
    <p class="lede" style="margin-top: 20px;">{c['stack_lede']}</p>
    <div class="stack-grid">{stack_html}</div>
  </div>
</section>

<section id="approach" class="alt">
  <div class="container">
    <span class="eyebrow">{c['approach_eyebrow']}</span>
    <div class="approach-grid">
      <div>
        <h2 style="margin-top: 12px;">{c['approach_title']}</h2>
        <p class="lede" style="margin-top: 20px;">{c['approach_lede']}</p>
      </div>
      <div class="approach-points">{approach_html}</div>
    </div>
  </div>
</section>

<section id="work">
  <div class="container">
    <span class="eyebrow">{c['case_eyebrow']}</span>
    <div class="case">
      <div class="eyebrow" style="color: var(--ink-dim);">[Jewelry · Bangkok]</div>
      <h3 style="font-family: var(--serif); font-size: clamp(26px,3vw,36px); margin-top: 16px;">{c['case_title']}</h3>
      <p class="case-body">{c['case_body']}</p>
      <div class="case-author">{c['case_author']}</div>
    </div>
  </div>
</section>

<section id="contact" class="contact alt">
  <div class="container">
    <span class="eyebrow">{c['contact_eyebrow']}</span>
    <h2>{c['contact_title']}</h2>
    <p class="lede">{c['contact_lede']}</p>
    <a href="mailto:{EMAIL}" class="btn btn-primary">{c['contact_cta']} → {EMAIL}</a>
  </div>
</section>

</main>

<footer class="site">
  <div class="container">
    <div class="grid">
      <div class="brand-col">
        {MARK_INLINE}
        <p>{c['footer_tag']}</p>
      </div>
      <div>
        <h5>{c['footer_contact']}</h5>
        <ul>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>{PHONE}</li>
          <li>{CITY}</li>
        </ul>
      </div>
      <div>
        <h5>{c['footer_services_h']}</h5>
        <ul>{footer_services}</ul>
      </div>
      <div>
        <h5>{c['footer_resources_h']}</h5>
        <ul>{footer_resources}</ul>
      </div>
    </div>
    <div class="bottom">
      <span>{c['footer_copy']}</span>
      <span>{c['footer_coords']}</span>
    </div>
  </div>
</footer>

</body>
</html>
"""

def build_all():
    for lang in ["fr", "en", "th"]:
        out_dir = OUT / lang
        out_dir.mkdir(exist_ok=True)
        (out_dir / "index.html").write_text(render(lang))
        size = (out_dir / "index.html").stat().st_size
        print(f"  ✓ {lang}/index.html  {size:>7} B")

if __name__ == "__main__":
    build_all()
    print("Done.")
