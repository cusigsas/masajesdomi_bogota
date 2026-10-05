# -*- coding: utf-8 -*-
"""Genera el sitio Thera+Vida: index, categorías, servicios, componentes, sitemap y robots."""
import json, os, html
from content_base import *
from content_services_a import SERVICES_A
from content_services_b import SERVICES_B
from content_tips import TIPS
from content_catalog import CATALOG, CATALOG_GROUPS, CATALOG_FAQS

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SERVICES = {**SERVICES_A, **SERVICES_B}
CAT_BY_SLUG = {c["slug"]: c for c in CATEGORIES}
e = html.escape

# Orden de servicios dentro de cada categoría
for c in CATEGORIES:
    for s in c["services"]:
        assert SERVICES[s]["cat"] == c["slug"], s

# ---------------------------------------------------------------- helpers
def article(name):
    first = name.split()[0].lower()
    fem = {"colocación", "podología", "rehabilitación", "terapia"}
    return ("la", "de la") if first in fem else ("el", "del")

def lower_first(t):
    return t[0].lower() + t[1:]

def jsonld(obj):
    return '<script type="application/ld+json">\n' + json.dumps(obj, ensure_ascii=False, indent=2) + "\n</script>"

PROVIDER = {
    "@type": "MedicalBusiness",
    "name": BRAND,
    "url": f"{DOMAIN}/",
    "telephone": PHONE_INTL,
}

def faq_schema(faqs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ],
    }

def breadcrumb_schema(items):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": u}
            for i, (n, u) in enumerate(items)
        ],
    }

def head(title, desc, path, css, schemas, root, og_img="imagen1.jpg"):
    canonical = f"{DOMAIN}/{path}" if path else f"{DOMAIN}/"
    css_links = "\n".join(f'  <link rel="stylesheet" href="{root}css/{c}">' for c in css)
    schema_html = "\n  ".join(jsonld(s) for s in schemas)
    return f"""<!doctype html>
<html lang="es-CO">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(title)}</title>
  <meta name="description" content="{e(desc)}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="{canonical}">

  <meta property="og:locale" content="es_CO">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{BRAND}">
  <meta property="og:title" content="{e(title)}">
  <meta property="og:description" content="{e(desc)}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{DOMAIN}/{og_img}">
  <meta name="twitter:card" content="summary_large_image">

  <link rel="icon" type="image/png" href="{root}favicon.png">
  <link rel="apple-touch-icon" href="{root}apple-touch-icon.png">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
{css_links}

  {schema_html}

  <!-- Google Analytics 4: reemplaza G-XXXXXXXXXX y descomenta
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-XXXXXXXXXX');</script>
  -->
  <!-- Meta Pixel: reemplaza TU_PIXEL_ID y descomenta
  <script>!function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');fbq('init','TU_PIXEL_ID');fbq('track','PageView');</script>
  -->
</head>"""

def body_open(root, wa, extra_class=""):
    cls = f' class="{extra_class}"' if extra_class else ""
    return f"""<body data-root="{root}" data-wa-msg="{e(wa)}"{cls}>
  <a class="skip-link" href="#contenido">Saltar al contenido</a>
  <div data-component="navbar"></div>
"""

def body_close(root):
    return f"""
  <div data-component="footer"></div>
  <div data-component="whatsapp-float"></div>

  <script src="{root}js/components-loader.js"></script>
  <script src="{root}js/main.js"></script>
</body>
</html>
"""

def paragraphs(ps, indent="          "):
    return "\n".join(f"{indent}<p>{e(p)}</p>" for p in ps)

def zones_section(title, text, alt=False, center=False):
    cls = "section section-alt" if alt else "section"
    head_cls = "section-head center" if center else "section-head"
    items = "\n".join(f"          <li>{z}</li>" for z in ZONES)
    return f"""
    <section class="{cls}" aria-labelledby="zonas-titulo">
      <div class="container">
        <div class="{head_cls}">
          <h2 id="zonas-titulo">{e(title)}</h2>
          <p>{e(text)}</p>
        </div>
        <ul class="zones{' zones-center' if center else ''}">
{items}
        </ul>
      </div>
    </section>"""

def faq_section(faqs, title="Preguntas frecuentes", alt=False):
    cls = "section section-alt" if alt else "section"
    items = "\n".join(
        f"""          <details>
            <summary>{e(q)}</summary>
            <p>{e(a)}</p>
          </details>""" for q, a in faqs)
    return f"""
    <section class="{cls}" aria-labelledby="faq-titulo">
      <div class="container">
        <div class="section-head">
          <h2 id="faq-titulo">{e(title)}</h2>
        </div>
        <div class="faq">
{items}
        </div>
      </div>
    </section>"""

def cta_band(title, text, wa, root):
    return f"""
    <section class="section cta-band">
      <div class="container narrow">
        <h2>{e(title)}</h2>
        <p>{e(text)}</p>
        <div class="btn-row">
          <a class="btn btn-whatsapp" data-wa="{e(wa)}" href="#">Agendar por WhatsApp</a>
          <a class="btn btn-outline" href="{root}catalogo.html">Ver catálogo</a>
        </div>
      </div>
    </section>"""

def write(path, content):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

VALUES_STRIP = """
    <section class="values" aria-label="Lo que nos define">
      <div class="container values-inner">
        <div class="value">
          <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 20.5s-7.5-4.6-7.5-10.2A4.3 4.3 0 0 1 12 7.6a4.3 4.3 0 0 1 7.5 2.7c0 5.6-7.5 10.2-7.5 10.2Z"/></svg>
          <span>Cuidado humano</span>
        </div>
        <div class="value">
          <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3 4.5 6v5.5c0 4.6 3.2 8.4 7.5 9.5 4.3-1.1 7.5-4.9 7.5-9.5V6L12 3Z"/><path d="M12 9v6M9 12h6"/></svg>
          <span>Atención segura</span>
        </div>
        <div class="value">
          <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8" r="3.6"/><path d="M4.5 20.5c.8-4 3.8-6.2 7.5-6.2s6.7 2.2 7.5 6.2"/></svg>
          <span>Enfoque personalizado</span>
        </div>
        <div class="value">
          <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 19C5 10 11 5 20 4c0 9-5 15-13 15H5Z"/><path d="M5 19c3-4 6-7 10-10"/></svg>
          <span>Bienestar integral</span>
        </div>
      </div>
    </section>"""

# ---------------------------------------------------------------- INDEX
def build_index():
    root = ""
    home_faqs = [
        ("¿Atienden masajes a domicilio en Bogotá las 24 horas?", "Sí. Atendemos todos los días, a cualquier hora, en Bogotá y municipios cercanos. Escríbenos por WhatsApp con tu dirección y el horario que prefieres."),
        ("¿Qué debo tener en casa para el masaje?", "Solo un espacio despejado de unos dos por dos metros. Llevamos la camilla, las sábanas, las toallas y los aceites."),
        ("¿Tienen consultorio o sede para ir?", "No. Thera+Vida atiende solo a domicilio: vamos a tu casa, apartamento, oficina u hotel."),
        ("¿Cuánto cuesta un masaje a domicilio en Bogotá?", "El valor depende del tipo de masaje o servicio, la duración y la zona de Bogotá. Te enviamos la cotización por WhatsApp antes de agendar, sin compromiso."),
        ("¿Además de masajes, qué otros servicios hacen?", "Hacemos drenaje linfático, enfermería a domicilio (curaciones, estomas, signos vitales y podología) y rehabilitación en cáncer de mama, linfedema, lipedema y compresión."),
    ]
    schema_main = {
        "@context": "https://schema.org",
        "@type": "MedicalBusiness",
        "name": BRAND,
        "alternateName": "Thera+Vida Rehabilitación y Servicios de Enfermería",
        "description": "Masajes a domicilio en Bogotá las 24 horas: masaje terapéutico, drenaje linfático, enfermería y rehabilitación en casa.",
        "url": f"{DOMAIN}/",
        "logo": f"{DOMAIN}/logo.png",
        "image": f"{DOMAIN}/imagen1.jpg",
        "telephone": PHONE_INTL,
        "priceRange": "$$",
        "hasMap": MAP_CID_URL,
        "areaServed": [{"@type": "City", "name": CITY}] + [{"@type": "Place", "name": f"{z}, {CITY}"} for z in ZONES],
        "openingHoursSpecification": {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "opens": "00:00", "closes": "23:59",
        },
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Servicios a domicilio en Bogotá",
            "itemListElement": [
                {"@type": "OfferCatalog", "name": c["h1"], "url": f"{DOMAIN}/{c['slug']}.html",
                 "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": SERVICES[s]["h1"],
                                      "url": f"{DOMAIN}/servicios/{s}.html"}} for s in c["services"]]}
                for c in CATEGORIES
            ],
        },
    }
    html_out = head(HOME["title"], HOME["desc"], "", ["global.css", "index.css"],
                    [schema_main, faq_schema(home_faqs)], root)
    html_out += body_open(root, HOME["wa"])
    html_out += f"""
  <main id="contenido">

    <!-- ============ HERO ============ -->
    <section class="home-hero">
      <div class="hero-bg" aria-hidden="true">
        <svg class="hero-waves" viewBox="0 0 1440 600" preserveAspectRatio="none">
          <path d="M0,120 C320,40 520,220 860,140 C1120,80 1300,120 1440,60 L1440,0 L0,0 Z" fill="currentColor" opacity=".08"/>
          <path d="M0,560 C260,470 560,600 900,520 C1160,460 1320,520 1440,480 L1440,600 L0,600 Z" fill="currentColor" opacity=".07"/>
        </svg>
        <span class="cross cross-1"></span><span class="cross cross-2"></span><span class="cross cross-3"></span>
      </div>
      <div class="container hero-grid">
        <div class="hero-copy">
          <h1>{e(HOME['h1'])}</h1>
          <p class="hero-lead">{e(HOME['lead'])}</p>
          <p class="hero-tagline">{e(HOME['tagline'])}</p>
          <div class="hero-cta">
            <a class="btn btn-catalog" href="catalogo.html">Ver catálogo de servicios</a>
          </div>
          <div class="hero-cta-secondary">
            <a class="btn btn-whatsapp" data-wa href="#">Agendar por WhatsApp</a>
            <a class="btn btn-outline" href="#servicios">Conocer servicios</a>
          </div>
        </div>
        <div class="hero-media">
          <img class="hero-img-main" src="imagen1.jpg" alt="Masajes a domicilio en Bogotá con Thera+Vida" width="1100" height="1240" fetchpriority="high">
          <img class="hero-img-small" src="imagen2.jpg" alt="Masaje terapéutico en casa en Bogotá" width="440" height="350">
        </div>
      </div>
    </section>
{VALUES_STRIP}
"""
    # Bloques de categoría (H2 = categoría secundaria + ciudad, enlazado)
    block_imgs = {
        "masaje-terapeutico-a-domicilio-bogota": ("imagen7.jpg", ("24", " h", "Disponibles todos los días")),
        "drenaje-linfatico-a-domicilio-bogota": ("imagen5.jpg", None),
        "enfermeria-a-domicilio-bogota": ("imagen4.jpg", (str(len(SERVICES)), "", "Servicios a domicilio")),
        "rehabilitacion-a-domicilio-bogota": ("imagen3.jpg", None),
    }
    for i, c in enumerate(CATEGORIES):
        img, counter = block_imgs[c["slug"]]
        alt_bg = " section-alt" if i % 2 else ""
        reverse = " split-reverse" if i % 2 else ""
        counter_html = ""
        if counter:
            counter_html = f"""
            <div class="counter">
              <span class="counter-number" data-end="{counter[0]}" data-suffix="{counter[1]}">{counter[0]}{counter[1]}</span>
              <span class="counter-label">{counter[2]}</span>
            </div>"""
        fig = f"""
          <figure class="media-with-counter">
            <img class="rounded" src="{img}" alt="{e(c['img_alt'])}" width="960" height="1280" loading="lazy">{counter_html}
          </figure>"""
        chips = "\n".join(f"            <li>{e(SERVICES[s]['name'])}</li>" for s in c["services"])
        text = list(c["home_text"])
        last = text.pop()
        # El último párrafo lleva el enlace con el texto ancla exacto de la categoría
        anchor = c["h1"].lower()
        last_html = e(last).replace(e(c["name"].lower()),
                                    f'<a href="{c["slug"]}.html">{e(c["name"].lower())}</a>', 1)
        copy = f"""
          <div class="split-copy">
            <h2><a href="{c['slug']}.html">{e(c['h1'])}</a></h2>
{paragraphs(text, '            ')}
            <p>{last_html}</p>
            <ul class="cat-services" aria-label="Servicios de {e(c['name'].lower())}">
{chips}
            </ul>
            <a class="btn btn-primary" href="{c['slug']}.html">Ver {e(c['menu'].lower())}</a>
          </div>"""
        inner = (copy + fig) if i % 2 else (fig + copy)
        sid = ' id="servicios"' if i == 0 else ""
        html_out += f"""
    <section class="section cat-block{alt_bg}"{sid}>
      <div class="container split{reverse}">{inner}
      </div>
    </section>
"""
    html_out += f"""
    <!-- ============ CÓMO FUNCIONA ============ -->
    <section class="section">
      <div class="container split">
        <figure>
          <img class="rounded" src="imagen2.jpg" alt="Terapeuta llegando a un domicilio en Bogotá" width="960" height="1280" loading="lazy">
        </figure>
        <div class="split-copy">
          <h2>Así funciona la atención a domicilio</h2>
          <p>Agendar es sencillo y puedes hacerlo a cualquier hora, porque atendemos las 24 horas.</p>
          <ol class="steps">
            <li><strong>Escríbenos por WhatsApp</strong><span>Cuéntanos qué servicio necesitas, para quién es y en qué parte de Bogotá estás.</span></li>
            <li><strong>Te enviamos la cotización</strong><span>Con el valor, la duración y el profesional disponible para el día y la hora que te sirvan.</span></li>
            <li><strong>Llegamos a tu casa</strong><span>Con la camilla, los insumos y todo lo necesario. Tú solo pones el espacio.</span></li>
          </ol>
          <a class="btn btn-primary" data-wa href="#">Agendar ahora</a>
        </div>
      </div>
    </section>

    <!-- ============ TU SALUD, NUESTRA PRIORIDAD ============ -->
    <section class="section section-tint">
      <div class="container split split-40">
        <div class="organic-media">
          <img class="organic" src="imagen6.jpg" alt="Paciente recibiendo atención a domicilio en Bogotá" width="800" height="900" loading="lazy">
          <img class="organic-small" src="imagen8.jpg" alt="Control de signos vitales a domicilio en Bogotá" width="600" height="420" loading="lazy">
          <div class="counter counter-floating">
            <span class="counter-number" data-end="100" data-suffix=" %">100 %</span>
            <span class="counter-label">Atención a domicilio</span>
          </div>
        </div>
        <div class="split-copy">
          <h2>Tu salud, nuestra prioridad</h2>
          <p>Trabajamos con profesionales calificados y confiables que entienden que entrar a una casa es un acto de confianza. Por eso cuidamos la puntualidad, el respeto por tu espacio y la comunicación con la familia durante todo el proceso.</p>
          <p>Nos adaptamos a tus horarios, incluso en la noche o en fines de semana, y si en una visita notamos algo que debe ver un médico, te lo decimos con claridad.</p>
          <p class="quote">Cuidado que se siente, resultados que se ven.</p>
        </div>
      </div>
    </section>
"""
    html_out += zones_section("Masajes a domicilio en toda Bogotá",
                              "Vamos a tu casa, apartamento, oficina u hotel en estas zonas de Bogotá y en municipios cercanos. Si no ves tu barrio, escríbenos y te confirmamos.",
                              alt=True)
    html_out += faq_section(home_faqs)
    html_out += f"""

    <!-- ============ CONTACTO ============ -->
    <section class="section contact" id="contacto">
      <div class="container contact-inner">
        <h2>Agenda tu cita y vamos hasta tu casa</h2>
        <dl class="contact-list">
          <div><dt>Teléfono y WhatsApp</dt><dd><a href="tel:{PHONE_INTL}">{PHONE_DISPLAY}</a></dd></div>
          <div><dt>Horario</dt><dd>24 horas, todos los días</dd></div>
          <div><dt>Cobertura</dt><dd>Solo a domicilio, en Bogotá y alrededores</dd></div>
        </dl>
        <a class="btn btn-whatsapp btn-large" data-wa href="#">Agendar por WhatsApp</a>
      </div>
    </section>

    <!-- ============ MAPA ============ -->
    <section class="map" aria-label="Thera+Vida en Google Maps">
      <iframe src="{MAP_IFRAME_SRC}" title="Thera+Vida en Google Maps" width="100%" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe>
    </section>
  </main>
"""
    html_out += body_close(root)
    write("index.html", html_out)

# ---------------------------------------------------------------- CATEGORÍAS
def build_category(c):
    root = ""
    path = f"{c['slug']}.html"
    crumbs = [("Inicio", f"{DOMAIN}/"), (c["name"], f"{DOMAIN}/{path}")]
    schema_service = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": c["h1"],
        "serviceType": c["name"],
        "description": c["desc"],
        "url": f"{DOMAIN}/{path}",
        "provider": PROVIDER,
        "areaServed": {"@type": "City", "name": CITY},
        "hasOfferCatalog": {
            "@type": "OfferCatalog", "name": c["h1"],
            "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": SERVICES[s]["h1"],
                                 "url": f"{DOMAIN}/servicios/{s}.html"}} for s in c["services"]],
        },
    }
    out = head(c["title"], c["desc"], path, ["global.css", "category-template.css"],
               [schema_service, breadcrumb_schema(crumbs), faq_schema(c["faqs"])], root, c["img"])
    out += body_open(root, c["wa"], "cat-page")
    index_links = "\n".join(
        f'            <li><a href="#{s}">{e(SERVICES[s]["name"])}</a></li>' for s in c["services"])
    out += f"""
  <main id="contenido">
    <section class="page-hero">
      <div class="container page-hero-grid">
        <div class="page-hero-copy">
          <nav class="breadcrumbs" aria-label="Migas de pan">
            <ol>
              <li><a href="index.html">Inicio</a></li>
              <li aria-current="page">{e(c['name'])}</li>
            </ol>
          </nav>
          <h1>{e(c['h1'])}</h1>
{paragraphs(c['intro'], '          ').replace('<p>', '<p class="lead">', 1)}
          <ul class="service-index" aria-label="Servicios en esta página">
{index_links}
          </ul>
          <div class="btn-row">
            <a class="btn btn-whatsapp" data-wa href="#">Agendar por WhatsApp</a>
            <a class="btn btn-outline" href="catalogo.html">Ver catálogo</a>
          </div>
        </div>
        <figure>
          <img class="page-hero-img" src="{c['img']}" alt="{e(c['img_alt'])}" width="900" height="1125" fetchpriority="high">
        </figure>
      </div>
    </section>
"""
    for i, s in enumerate(c["services"]):
        sv = SERVICES[s]
        alt_bg = "" if i % 2 else " section-alt"
        reverse = " split-reverse" if i % 2 else ""
        img, img_alt = (sv["img"], sv["img_alt"]) if i % 2 == 0 else (sv["img2"], sv["img2_alt"])
        fig = f"""
        <figure>
          <img class="rounded" src="{img}" alt="{e(img_alt)}" width="960" height="1280" loading="lazy">
        </figure>"""
        copy = f"""
        <div class="split-copy">
          <h2><a href="servicios/{s}.html">{e(sv['h1'])}</a></h2>
{paragraphs(sv['resumen'])}
          <div class="block-actions">
            <a class="more-link" href="servicios/{s}.html">Ver {e(lower_first(sv['name']))}</a>
            <a class="btn btn-whatsapp btn-small" data-wa="{e(sv['wa'])}" href="#">Preguntar por WhatsApp</a>
          </div>
        </div>"""
        inner = (copy + fig) if i % 2 else (fig + copy)
        out += f"""
    <section class="section service-block{alt_bg}" id="{s}">
      <div class="container split{reverse}">{inner}
      </div>
    </section>
"""
    why = "\n".join(f"          <li>{e(w)}</li>" for w in c["why"])
    out += f"""
    <section class="section">
      <div class="container split">
        <div class="split-copy">
          <h2>Por qué elegir nuestro servicio de {e(lower_first(c['name']))}</h2>
          <ul class="check-list">
{why}
          </ul>
          <a class="btn btn-primary" data-wa href="#">Agendar por WhatsApp</a>
        </div>
        <figure>
          <img class="rounded wide" src="{c['img2']}" alt="{e(c['img2_alt'])}" width="1200" height="900" loading="lazy">
        </figure>
      </div>
    </section>
"""
    out += zones_section(f"{c['name']} en estas zonas de Bogotá",
                         f"Llevamos el servicio de {lower_first(c['name'])} a casas, apartamentos y oficinas en estos barrios y localidades, y en municipios cercanos. Atendemos las 24 horas.",
                         alt=True)
    out += faq_section(c["faqs"], f"Preguntas frecuentes sobre {lower_first(c['name'])}")
    out += cta_band(f"Agenda {lower_first(c['name'])} en Bogotá",
                    "Escríbenos por WhatsApp, cuéntanos qué necesitas y te enviamos la cotización y la disponibilidad.",
                    c["wa"], root)
    out += "\n  </main>\n" + body_close(root)
    write(path, out)

# ---------------------------------------------------------------- SERVICIOS
def build_service(slug):
    sv = SERVICES[slug]
    c = CAT_BY_SLUG[sv["cat"]]
    root = "../"
    path = f"servicios/{slug}.html"
    art, art_de = article(sv["name"])
    name_l = lower_first(sv["name"])
    crumbs = [("Inicio", f"{DOMAIN}/"), (c["name"], f"{DOMAIN}/{c['slug']}.html"), (sv["name"], f"{DOMAIN}/{path}")]
    schema_service = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": sv["h1"],
        "serviceType": sv["name"],
        "description": sv["desc"],
        "url": f"{DOMAIN}/{path}",
        "image": f"{DOMAIN}/{sv['img']}",
        "provider": PROVIDER,
        "areaServed": [{"@type": "City", "name": CITY}] + [{"@type": "Place", "name": f"{z}, {CITY}"} for z in ZONES],
        "isRelatedTo": {"@type": "Service", "name": c["h1"], "url": f"{DOMAIN}/{c['slug']}.html"},
    }
    out = head(sv["title"], sv["desc"], path, ["global.css", "service-template.css"],
               [schema_service, breadcrumb_schema(crumbs), faq_schema(sv["faqs"])], root, sv["img"])
    out += body_open(root, sv["wa"], "svc-page")
    facts = "\n".join(f"            <li>{e(f)}</li>" for f in sv["facts"])
    que_es = paragraphs(sv["que_es"], "          ")
    benefits = "\n".join(f"            <li><strong>{e(t)}</strong>{e(d)}</li>" for t, d in sv["beneficios"])
    steps = "\n".join(f"            <li><strong>{e(t)}</strong><span>{e(d)}</span></li>" for t, d in sv["visita"])
    zones = "\n".join(f"            <li>{z}</li>" for z in ZONES)
    tip_label = {"Antes": "Antes de la sesión", "Durante": "Durante la sesión", "Después": "Después de la sesión"}
    tips = "\n".join(f"          <h3>{tip_label[t]}</h3>\n          <p>{e(d)}</p>" for t, d in TIPS[slug])
    siblings = "\n".join(
        f'              <li><a href="{s}.html">{e(SERVICES[s]["name"])}</a></li>'
        for s in c["services"] if s != slug)
    notice = f"""
          <div class="notice" role="note"><p><strong>Importante:</strong> {e(sv['cuidado'])}</p></div>""" if sv.get("cuidado") else ""
    out += f"""
  <main id="contenido">
    <section class="page-hero">
      <div class="container page-hero-grid">
        <div class="page-hero-copy">
          <nav class="breadcrumbs" aria-label="Migas de pan">
            <ol>
              <li><a href="../index.html">Inicio</a></li>
              <li><a href="../{c['slug']}.html">{e(c['name'])}</a></li>
              <li aria-current="page">{e(sv['name'])}</li>
            </ol>
          </nav>
          <h1>{e(sv['h1'])}</h1>
          <p class="lead">{e(sv['intro'][0])}</p>
          <ul class="quick-facts">
{facts}
          </ul>
          <div class="btn-row">
            <a class="btn btn-whatsapp" data-wa href="#">Agendar por WhatsApp</a>
            <a class="btn btn-outline" href="../catalogo.html">Ver catálogo</a>
          </div>
        </div>
        <figure>
          <img class="page-hero-img" src="../{sv['img']}" alt="{e(sv['img_alt'])}" width="900" height="900" fetchpriority="high">
        </figure>
      </div>
    </section>

    <section class="section">
      <div class="container content-grid">
        <article class="article">
{paragraphs(sv['intro'][1:], '          ')}
          <h2>{e(sv['que_es_title'])}</h2>
{que_es}
          <figure class="split-img">
            <img src="../{sv['img2']}" alt="{e(sv['img2_alt'])}" width="1200" height="750" loading="lazy">
          </figure>

          <h2>Beneficios {art_de} {e(name_l)}</h2>
          <ul class="benefits">
{benefits}
          </ul>

          <h2>¿Cómo es la visita a domicilio?</h2>
          <ol class="steps">
{steps}
          </ol>

          <h2>¿Para quién es {art} {e(name_l)}?</h2>
          <p>{e(sv['para_quien'])}</p>

          <h2>Recomendaciones para {art} {e(name_l)}</h2>
{tips}

          <h2>Precio {art_de} {e(name_l)} a domicilio en Bogotá</h2>
          <div class="price-box">
            <p>{e(sv['precio'])}</p>
            <a class="btn btn-whatsapp" data-wa="{e('Hola Thera+Vida, quiero la cotización de ' + art + ' ' + name_l + ' a domicilio en Bogotá.')}" href="#">Pedir cotización</a>
          </div>
{notice}

          <h2>Zonas de Bogotá donde hacemos {art} {e(name_l)}</h2>
          <p>Vamos a tu casa, apartamento u oficina en estos barrios y localidades, y en municipios cercanos. Si no ves tu zona, escríbenos y te confirmamos.</p>
          <ul class="zones">
{zones}
          </ul>
        </article>

        <aside class="aside" aria-label="Agenda y servicios relacionados">
          <div class="aside-card">
            <h3>Agenda a domicilio</h3>
            <p>Atendemos las 24 horas en Bogotá. Escríbenos y te enviamos la cotización y la disponibilidad.</p>
            <a class="btn btn-whatsapp" data-wa href="#">WhatsApp {PHONE_DISPLAY}</a>
          </div>
          <div class="aside-card">
            <h3>Más de {e(lower_first(c['name']))}</h3>
            <ul>
              <li><a class="parent-link" href="../{c['slug']}.html">{e(c['h1'])}</a></li>
{siblings}
            </ul>
          </div>
        </aside>
      </div>
    </section>
"""
    out += faq_section(sv["faqs"], f"Preguntas frecuentes sobre {art} {name_l}", alt=True)
    out += cta_band(f"¿Necesitas {art} {name_l} en casa?",
                    "Escríbenos por WhatsApp con tu barrio y el horario que prefieres. Atendemos las 24 horas, todos los días.",
                    sv["wa"], root)
    out += "\n  </main>\n" + body_close(root)
    write(path, out)


# ---------------------------------------------------------------- CATÁLOGO
ICON_NURSE = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="9" r="3.5"/><path d="M8 5.5 12 3l4 2.5"/><path d="M5 21c.6-4 3.4-6.3 7-6.3s6.4 2.3 7 6.3"/><path d="M12 16v3M10.5 17.5h3"/></svg>'
ICON_LOTUS = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 19c-3-2-4.5-5-4.5-8.5C9.5 11 11 12.5 12 14c1-1.5 2.5-3 4.5-3.5 0 3.5-1.5 6.5-4.5 8.5Z"/><path d="M12 14c-1-3-1-6.5 0-9 1 2.5 1 6 0 9Z"/><path d="M7.5 10.5C5 10.5 3 12 3 12s1.5 5 9 7M16.5 10.5C19 10.5 21 12 21 12s-1.5 5-9 7"/></svg>'

def build_catalog():
    root = ""
    path = "catalogo.html"
    crumbs = [("Inicio", f"{DOMAIN}/"), ("Catálogo", f"{DOMAIN}/{path}")]
    schema_catalog = {
        "@context": "https://schema.org",
        "@type": "OfferCatalog",
        "name": CATALOG["h1"],
        "url": f"{DOMAIN}/{path}",
        "itemListElement": [
            {"@type": "OfferCatalog", "name": g["title"],
             "itemListElement": [{"@type": "Offer", "areaServed": {"@type": "City", "name": CITY},
                                  "seller": PROVIDER,
                                  "itemOffered": {"@type": "Service", "name": SERVICES[sl]["h1"],
                                                  "url": f"{DOMAIN}/servicios/{sl}.html"}}
                                 for sl, _, _ in g["items"]]}
            for g in CATALOG_GROUPS
        ],
    }
    out = head(CATALOG["title"], CATALOG["desc"], path, ["global.css", "catalogo.css"],
               [schema_catalog, breadcrumb_schema(crumbs), faq_schema(CATALOG_FAQS)], root, "imagen7.jpg")
    out += body_open(root, CATALOG["wa"], "catalog-page")
    jump = "\n".join(f'          <li><a href="#{g["id"]}">{e(g["title"])}</a></li>' for g in CATALOG_GROUPS)
    out += f"""
  <main id="contenido">
    <section class="catalog-hero">
      <span class="cross cross-1" aria-hidden="true"></span>
      <span class="cross cross-2" aria-hidden="true"></span>
      <div class="container">
        <nav class="breadcrumbs" aria-label="Migas de pan">
          <ol>
            <li><a href="index.html">Inicio</a></li>
            <li aria-current="page">Catálogo</li>
          </ol>
        </nav>
        <h1>{e(CATALOG['h1'])}</h1>
        <div class="divider" aria-hidden="true">
          <svg viewBox="0 0 24 24"><path d="M12 20.5s-7.5-4.6-7.5-10.2A4.3 4.3 0 0 1 12 7.6a4.3 4.3 0 0 1 7.5 2.7c0 5.6-7.5 10.2-7.5 10.2Z"/></svg>
        </div>
        <p class="catalog-tagline">Enfermería con vocación, terapia con propósito.</p>
        <p class="lead">{e(CATALOG['lead'])}</p>
        <ul class="jump" aria-label="Ir a una sección del catálogo">
{jump}
        </ul>
      </div>
    </section>
{VALUES_STRIP}
"""
    def wa_msg(sl, label):
        art, _ = article(SERVICES[sl]["name"])
        return f"Hola Thera+Vida, vi el catálogo y quiero agendar {art} {lower_first(label)} a domicilio en Bogotá. ¿Qué disponibilidad tienen?"

    # --- Masajes (destacado)
    g = CATALOG_GROUPS[0]
    cards = ""
    for sl, label, text in g["items"]:
        sv = SERVICES[sl]
        tags = "\n".join(f"              <li>{e(t)}</li>" for t in sv["facts"][:2])
        cards += f"""
        <article class="massage-card">
          <img src="{sv['img']}" alt="{e(sv['img_alt'])}" width="900" height="675" loading="lazy">
          <div class="massage-body">
            <h3><a href="servicios/{sl}.html">{e(label)}</a></h3>
            <p>{e(text)}</p>
            <ul class="tags">
{tags}
            </ul>
            <div class="card-actions">
              <a class="btn btn-whatsapp" data-wa="{e(wa_msg(sl, label))}" href="#">{e(g['button'])}</a>
              <a class="details-link" href="servicios/{sl}.html">Ver detalles {article(sv['name'])[1]} {e(lower_first(label))}</a>
            </div>
          </div>
        </article>"""
    out += f"""
    <section class="section" id="masajes">
      <div class="container">
        <div class="group-head">
          <h2>{e(g['title'])}</h2>
          <p>{e(g['text'])}</p>
        </div>
        <div class="massage-grid">{cards}
        </div>
      </div>
    </section>
"""
    # --- Paneles: rehabilitación y enfermería
    panels = ""
    for g, icon, cls in [(CATALOG_GROUPS[1], ICON_LOTUS, " teal"), (CATALOG_GROUPS[2], ICON_NURSE, "")]:
        items = ""
        for sl, label, text in g["items"]:
            sv = SERVICES[sl]
            items += f"""
            <li class="panel-item">
              <img src="{sv['img']}" alt="{e(sv['img_alt'])}" width="152" height="152" loading="lazy">
              <div>
                <h3><a href="servicios/{sl}.html">{e(label)}</a></h3>
                <p>{e(text)}</p>
                <a class="btn btn-whatsapp" data-wa="{e(wa_msg(sl, label))}" href="#">{e(g['button'])}</a>
              </div>
            </li>"""
        panels += f"""
        <div class="panel" id="{g['id']}">
          <div class="panel-head{cls}">
            <span class="panel-icon">{icon}</span>
            <div>
              <h2>{e(g['title'])}</h2>
              <p>{e(g['text'])}</p>
            </div>
          </div>
          <ul class="panel-list">{items}
          </ul>
        </div>"""
    out += f"""
    <section class="section section-alt">
      <div class="container panels">{panels}
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="priority">
          <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 12.5s-4-2.4-4-5.4A2.3 2.3 0 0 1 12 5.7a2.3 2.3 0 0 1 4 1.4c0 3-4 5.4-4 5.4Z"/><path d="M3 14.5c1.5-.3 2.8.2 3.8 1.2l2.7 2.6c.6.6 1.6.6 2.2 0M21 14.5c-1.5-.3-2.8.2-3.8 1.2l-2.7 2.6c-.6.6-1.6.6-2.2 0"/><path d="M3 14.5V20M21 14.5V20"/></svg>
          <div>
            <h2>Tu salud, nuestra prioridad</h2>
            <p>Atención profesional en la comodidad de tu hogar o en el lugar que más te convenga.</p>
          </div>
          <p class="quote">Cuidado que se siente, resultados que se ven.</p>
        </div>

        <div class="agenda">
          <div>
            <h2>¡Agenda tu cita!</h2>
            <p>Contáctanos por WhatsApp, atendemos las 24 horas.</p>
          </div>
          <a class="btn btn-whatsapp" data-wa href="#">{PHONE_DISPLAY}</a>
        </div>

        <div class="badges">
          <div class="badge">
            <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-6.5-5.6-6.5-11a6.5 6.5 0 0 1 13 0c0 5.4-6.5 11-6.5 11Z"/><circle cx="12" cy="10" r="2.4"/></svg>
            <div><strong>Atención a domicilio</strong><span>Bogotá y alrededores</span></div>
          </div>
          <div class="badge">
            <svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3.5" y="5" width="17" height="15" rx="2"/><path d="M3.5 9.5h17M8 3v4M16 3v4"/><path d="M12 12.5v3l2 1.2"/></svg>
            <div><strong>Horarios flexibles</strong><span>24 horas, todos los días</span></div>
          </div>
          <div class="badge">
            <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3 4.5 6v5.5c0 4.6 3.2 8.4 7.5 9.5 4.3-1.1 7.5-4.9 7.5-9.5V6L12 3Z"/><path d="m9 12 2 2 4-4"/></svg>
            <div><strong>Profesionales</strong><span>Calificados y confiables</span></div>
          </div>
        </div>
      </div>
    </section>
"""
    out += zones_section("Llevamos el catálogo completo a tu casa",
                         "Todos los masajes y servicios del catálogo están disponibles a domicilio en estas zonas de Bogotá y en municipios cercanos.",
                         alt=True)
    out += faq_section(CATALOG_FAQS, "Preguntas sobre el catálogo")
    out += "\n  </main>\n" + body_close(root)
    write(path, out)

# ---------------------------------------------------------------- COMPONENTES
def build_components():
    sub = "\n".join(f'          <li><a href="{{{{ROOT}}}}{c["slug"]}.html">{e(c["h1"])}</a></li>' for c in CATEGORIES)
    navbar = f"""<header class="site-header" id="masthead">
  <div class="container header-inner">
    <a class="brand" href="{{{{ROOT}}}}index.html" aria-label="Thera+Vida, ir al inicio">
      <img src="{{{{ROOT}}}}logo-horizontal.png" alt="Thera+Vida" width="936" height="200">
    </a>
    <button class="menu-toggle" aria-expanded="false" aria-controls="menu-principal">
      <span class="menu-toggle-bar"></span>
      <span class="visually-hidden">Abrir menú</span>
    </button>
    <nav class="main-nav" id="menu-principal" aria-label="Menú principal">
      <a href="{{{{ROOT}}}}index.html">Inicio</a>
      <div class="has-sub">
        <button class="sub-toggle" aria-expanded="false" aria-controls="submenu-servicios">Servicios</button>
        <ul class="sub-menu" id="submenu-servicios">
{sub}
        </ul>
      </div>
      <a href="{{{{ROOT}}}}catalogo.html">Catálogo</a>
      <a class="btn btn-whatsapp btn-small" data-wa href="#">Agenda por WhatsApp</a>
    </nav>
  </div>
</header>
"""
    cols = ""
    for c in CATEGORIES:
        lis = "\n".join(f'          <li><a href="{{{{ROOT}}}}servicios/{s}.html">{e(SERVICES[s]["name"])}</a></li>' for s in c["services"])
        cols += f"""
      <div class="footer-col">
        <h3><a href="{{{{ROOT}}}}{c['slug']}.html">{e(c['name'])}</a></h3>
        <ul>
{lis}
        </ul>
      </div>"""
    footer = f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img class="footer-logo" src="{{{{ROOT}}}}logo.png" alt="Thera+Vida Rehabilitación y Servicios de Enfermería" width="729" height="473" loading="lazy">
        <p>Masajes, drenajes, enfermería y rehabilitación a domicilio en Bogotá.</p>
        <p class="footer-contact">
          <a href="tel:{PHONE_INTL}">{PHONE_DISPLAY}</a><br>
          Atención 24 horas, todos los días<br>
          Solo a domicilio, en Bogotá y alrededores
        </p>
        <a class="btn btn-whatsapp btn-small" data-wa href="#">Agenda por WhatsApp</a>
      </div>{cols}
    </div>
    <div class="footer-bottom">
      <p>© <span data-year></span> Thera+Vida. Rehabilitación y servicios de enfermería a domicilio en Bogotá.</p>
      <p>La información de este sitio es orientativa y no reemplaza la consulta con tu médico.</p>
    </div>
  </div>
</footer>
"""
    float_btn = """<a class="wa-float" data-wa href="#" aria-label="Escríbenos por WhatsApp"></a>
"""
    write("components/navbar.html", navbar)
    write("components/footer.html", footer)
    write("components/whatsapp-float.html", float_btn)

# ---------------------------------------------------------------- SITEMAP / ROBOTS
def build_sitemap():
    urls = [f"{DOMAIN}/", f"{DOMAIN}/catalogo.html"] + [f"{DOMAIN}/{c['slug']}.html" for c in CATEGORIES] + \
           [f"{DOMAIN}/servicios/{s}.html" for c in CATEGORIES for s in c["services"]]
    prio = lambda u: "1.0" if u.endswith("/") else ("0.9" if "/servicios/" not in u else "0.8")
    body = "\n".join(f"  <url><loc>{u}</loc><priority>{prio(u)}</priority></url>" for u in urls)
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}\n</urlset>\n')
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")

if __name__ == "__main__":
    build_components()
    build_index()
    for c in CATEGORIES:
        build_category(c)
        for s in c["services"]:
            build_service(s)
    build_catalog()
    build_sitemap()
    print("OK:", 2 + len(CATEGORIES) + len(SERVICES), "páginas")
