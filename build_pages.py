from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
IMG = ROOT / "images"
VID = ROOT / "videos"
DOCS = ROOT / "docs"
IMG.mkdir(exist_ok=True)
VID.mkdir(exist_ok=True)
DOCS.mkdir(exist_ok=True)

PRODUCTS = [
    {
        "slug": "noir-ambre",
        "name": "Noir Ambre",
        "notes": "Amber · Oud · Vanilla",
        "tag": "Icon",
        "category": "amber",
        "price": "CHF 280",
        "desc": "A deep, sensual amber composition inspired by warm desert evenings and polished black glass.",
        "top": "Bergamot · Saffron",
        "heart": "Rose · Jasmine · Amber",
        "base": "Oud · Vanilla · Musk",
        "story": "Noir Ambre opens with warm spice, moves into a resinous heart and settles into smooth vanilla woods.",
    },
    {
        "slug": "fleur-dor",
        "name": "Fleur d’Or",
        "notes": "Jasmine · Musk · Iris",
        "tag": "Radiant",
        "category": "floral",
        "price": "CHF 245",
        "desc": "A luminous floral fragrance with golden jasmine, clean musk and elegant iris powder.",
        "top": "Mandarin · Pear",
        "heart": "Jasmine · Iris",
        "base": "White Musk · Cashmere Wood",
        "story": "Fleur d’Or feels bright and polished, with soft flowers and a calm musky trail.",
    },
    {
        "slug": "midnight-oud",
        "name": "Midnight Oud",
        "notes": "Saffron · Rose · Oud",
        "tag": "Evening",
        "category": "oud",
        "price": "CHF 310",
        "desc": "A dramatic evening scent where saffron and velvet rose melt into dark, precious oud.",
        "top": "Saffron · Black Pepper",
        "heart": "Damask Rose · Patchouli",
        "base": "Oud · Ambergris · Smoke",
        "story": "Midnight Oud is made for evening wear: rich, confident and long lasting without feeling heavy.",
    },
    {
        "slug": "velvet-iris",
        "name": "Velvet Iris",
        "notes": "Iris · Violet · Sandalwood",
        "tag": "Powdery",
        "category": "powdery",
        "price": "CHF 230",
        "desc": "Soft, refined and close to the skin: a powdery iris wrapped in violet and creamy sandalwood.",
        "top": "Violet Leaf · Bergamot",
        "heart": "Iris · Orris Butter",
        "base": "Sandalwood · Musk",
        "story": "Velvet Iris is quiet luxury: textured, elegant and smooth from the first spray to the drydown.",
    },
    {
        "slug": "cedar-smoke",
        "name": "Cedar Smoke",
        "notes": "Cedar · Incense · Leather",
        "tag": "Smoky",
        "category": "woody",
        "price": "CHF 260",
        "desc": "A confident woody fragrance with dry cedar, mineral incense and a smooth leather finish.",
        "top": "Cardamom · Juniper",
        "heart": "Cedar · Incense",
        "base": "Leather · Vetiver",
        "story": "Cedar Smoke balances clean woods, soft smoke and leather for a sharp modern signature.",
    },
    {
        "slug": "rose-elixir",
        "name": "Rose Élixir",
        "notes": "Rose · Pink Pepper · Musk",
        "tag": "Romantic",
        "category": "floral",
        "price": "CHF 250",
        "desc": "A modern rose with sparkling pink pepper, transparent petals and a sensual musk trail.",
        "top": "Pink Pepper · Lychee",
        "heart": "Rose · Peony",
        "base": "Musk · Amber",
        "story": "Rose Élixir keeps rose fresh and contemporary with bright spice and a clean musky finish.",
    },
    {
        "slug": "golden-neroli",
        "name": "Golden Neroli",
        "notes": "Neroli · Citrus · White Tea",
        "tag": "New",
        "category": "fresh",
        "price": "CHF 225",
        "desc": "A crisp, sunlit fragrance with neroli, sparkling citrus and airy white tea.",
        "top": "Bitter Orange · Lemon Zest",
        "heart": "Neroli · White Tea",
        "base": "Clean Musk · Cedar",
        "story": "Golden Neroli is the bright morning scent of the collection: clean, energetic and precise.",
    },
    {
        "slug": "silver-musk",
        "name": "Silver Musk",
        "notes": "Musk · Aldehydes · Cotton",
        "tag": "Clean",
        "category": "fresh",
        "price": "CHF 215",
        "desc": "A minimal clean musk with bright aldehydes and a soft cotton-like texture.",
        "top": "Aldehydes · Bergamot",
        "heart": "Cotton Accord · Iris",
        "base": "White Musk · Ambrox",
        "story": "Silver Musk is understated and wearable, made for people who like freshness with polish.",
    },
    {
        "slug": "santal-veil",
        "name": "Santal Veil",
        "notes": "Sandalwood · Fig · Tonka",
        "tag": "Soft Wood",
        "category": "woody",
        "price": "CHF 275",
        "desc": "Creamy sandalwood, green fig and tonka create a warm, modern skin scent.",
        "top": "Fig Leaf · Cardamom",
        "heart": "Sandalwood · Cedar",
        "base": "Tonka · Musk",
        "story": "Santal Veil is warm and calm, with smooth woods designed to stay elegant all day.",
    },
    {
        "slug": "aqua-mirage",
        "name": "Aqua Mirage",
        "notes": "Sea Salt · Mint · Vetiver",
        "tag": "Fresh",
        "category": "fresh",
        "price": "CHF 235",
        "desc": "A mineral fresh fragrance with sea salt, cool mint and dry vetiver.",
        "top": "Mint · Grapefruit",
        "heart": "Sea Salt · Sage",
        "base": "Vetiver · Driftwood",
        "story": "Aqua Mirage is fresh without being loud: mineral, crisp and refined for everyday use.",
    },
]

CATEGORIES = [
    ("amber", "Amber", "Warm, resinous and elegant evening scents."),
    ("floral", "Floral", "Rose, jasmine and iris with a modern finish."),
    ("oud", "Oud", "Deep woods, saffron and darker signatures."),
    ("powdery", "Powdery", "Soft iris textures and close-to-skin elegance."),
    ("woody", "Woody", "Cedar, sandalwood and smoky materials."),
    ("fresh", "Fresh", "Clean citrus, musk and mineral freshness."),
]


def header(title, desc, current):
    nav = [
        ("index.html", "Home", "index"),
        ("collection.html", "Collection", "collection"),
        ("about.html", "House", "about"),
        ("contact.html", "Contact", "contact"),
    ]
    links = "\n".join(
        f'    <a href="{href}" {"aria-current=\"page\"" if key == current else ""}>{label}</a>'
        for href, label, key in nav
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{desc}">
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:wght@500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>
<div class="lux-loader" aria-hidden="true"><div><strong>L’ESSENCE</strong><span>Crafting Emotion</span></div></div>
<div class="cursor-dot" aria-hidden="true"></div>
<header class="site-header" data-header>
  <a class="brand" href="index.html" aria-label="L’Essence Startseite"><span>L’ESSENCE</span><small>Parfumerie</small></a>
  <button class="nav-toggle" type="button" aria-label="Menü öffnen" aria-expanded="false"><span></span><span></span></button>
  <nav class="nav" aria-label="Hauptnavigation">
{links}
  </nav>
</header>
"""


def footer():
    return """<footer class="footer">
  <div><strong>L’ESSENCE</strong><p>Fine fragrance atelier · Zürich · Since 2026</p></div>
  <p>© 2026 L’Essence Parfumerie. All rights reserved.</p>
</footer>
<script src="js/main.js"></script>
</body>
</html>
"""


def product_card(product):
    return f"""<article class="card product-card reveal" data-category="{product['category']}">
  <a class="product-image-link" href="product-{product['slug']}.html">
    <img src="images/{product['slug']}.jpg" alt="{product['name']} perfume bottle and visual artwork">
    <span class="quick-view">Explore</span>
  </a>
  <div class="product-body">
    <span class="tag">{product['tag']}</span>
    <div><h3>{product['name']}</h3><p>{product['notes']}</p><div class="price">{product['price']}</div></div>
    <a class="btn-detail" href="product-{product['slug']}.html">View details</a>
  </div>
</article>"""


def index_page():
    featured = "\n".join(product_card(p) for p in [PRODUCTS[6], PRODUCTS[0], PRODUCTS[8]])
    cats = "\n".join(
        f"""<a class="category-card" href="collection.html#{slug}" data-filter-link="{slug}">
  <span>{name}</span><p>{text}</p>
</a>"""
        for slug, name, text in CATEGORIES
    )
    return header("L’Essence Parfumerie | Luxury Fragrances", "A refined luxury perfume website for L’Essence Parfumerie.", "index") + f"""<main>
<section class="hero cinematic">
  <div class="liquid-bg" aria-hidden="true"><i></i><i></i><i></i></div>
  <div class="hero__content reveal">
    <p class="eyebrow">Private perfume atelier</p>
    <h1>Crafted for those who leave an impression.</h1>
    <p class="lead">Rare ingredients, careful maceration and polished compositions designed for people who notice details.</p>
    <div class="actions"><a class="btn btn--gold" href="collection.html">Discover Collection</a><a class="btn btn--ghost" href="about.html">Our House</a></div>
    <div class="stats">
      <div class="stat"><strong data-count="10">10</strong><p>signature fragrances</p></div>
      <div class="stat"><strong data-count="6">6</strong><p>product categories</p></div>
      <div class="stat"><strong data-count="100">100%</strong><p>hand finished</p></div>
      <div class="stat"><strong>2026</strong><p>founded in Zürich</p></div>
    </div>
  </div>
  <div class="hero__bottle reveal" aria-hidden="true"><div class="bottle"><span>L’ESSENCE</span></div><div class="floating-note n1">Amber</div><div class="floating-note n2">Iris</div><div class="floating-note n3">Oud</div></div>
</section>
<section class="section reveal">
  <p class="eyebrow">New and loved</p>
  <div class="section-heading"><h2>Modern classics for every presence.</h2><p>From luminous florals to smoky woods, every scent is balanced for depth, projection and refinement.</p></div>
  <div class="grid cards-3">{featured}</div>
</section>
<section class="section reveal">
  <p class="eyebrow">Categories</p>
  <div class="section-heading"><h2>Find the style that fits your moment.</h2><p>Each fragrance belongs to a clear scent family, so customers can compare the collection quickly.</p></div>
  <div class="category-grid">{cats}</div>
</section>
<section class="section split newsletter-section reveal">
  <div><p class="eyebrow">Newsletter</p><h2>Private launches, offers and fragrance notes.</h2><p>Subscribe for new releases, atelier events and limited editions.</p></div>
  <form class="card form newsletter-form" data-form-message="Thank you. You are now on the L’Essence newsletter list.">
    <label>Name<input type="text" name="name" placeholder="Your name" required></label>
    <label>Email<input type="email" name="email" placeholder="you@example.com" required></label>
    <label class="checkbox-row"><input type="checkbox" required> I agree to receive news from L’Essence.</label>
    <button class="btn btn--gold" type="submit">Join newsletter</button>
    <p class="form-status" aria-live="polite"></p>
  </form>
</section>
</main>""" + footer()


def collection_page():
    cards = "\n".join(product_card(p) for p in PRODUCTS)
    buttons = '<button class="filter-chip is-active" type="button" data-filter="all">All products</button>' + "\n".join(
        f'<button class="filter-chip" type="button" data-filter="{slug}">{name}</button>' for slug, name, _ in CATEGORIES
    )
    return header("Products | L’Essence Parfumerie", "Explore the L’Essence luxury perfume collection.", "collection") + f"""<main class="page">
<section class="section page-hero reveal">
  <p class="eyebrow">Collection</p>
  <h1>Ten signatures. One unmistakable house style.</h1>
  <p class="lead">Discover polished fragrances created for evenings, rituals and everyday elegance. Use the category filter to find your preferred scent family.</p>
</section>
<section class="section collection-stage">
  <div class="filter-bar reveal" aria-label="Product category filter">{buttons}</div>
  <div class="grid cards-3 product-grid" data-product-grid>{cards}</div>
</section>
</main>""" + footer()


def product_page(product):
    return header(f"{product['name']} | L’Essence Parfumerie", f"{product['name']} by L’Essence Parfumerie.", "collection") + f"""<main class="page">
<section class="section product-hero reveal">
  <div class="product-visual"><img src="images/{product['slug']}.jpg" alt="{product['name']} perfume bottle and visual artwork"></div>
  <div class="product-info">
    <p class="eyebrow">Eau de Parfum · 100 ml</p>
    <h1>{product['name']}</h1>
    <p class="lead">{product['desc']}</p>
    <p>{product['notes']}</p>
    <div class="scent-notes">
      <button class="note-pill" type="button"><span>Top</span><small>{product['top']}</small></button>
      <button class="note-pill" type="button"><span>Heart</span><small>{product['heart']}</small></button>
      <button class="note-pill" type="button"><span>Base</span><small>{product['base']}</small></button>
    </div>
    <div class="price price--large">{product['price']}</div>
    <div class="actions"><a class="btn btn--gold" href="#order">Order now</a><a class="btn btn--ghost" href="collection.html">Back to collection</a></div>
  </div>
</section>
<section class="section product-media reveal">
  <div>
    <p class="eyebrow">Fragrance film</p>
    <h2>See the mood of {product['name']}.</h2>
    <p>{product['story']}</p>
  </div>
  <video controls muted playsinline preload="metadata" poster="images/{product['slug']}.jpg">
    <source src="videos/{product['slug']}.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
</section>
<section class="section split reveal">
  <div><p class="eyebrow">Composition</p><h2>A polished structure from first impression to final trail.</h2></div>
  <p>Each note is selected for balance: a memorable opening, an elegant heart and a refined base that stays close to the skin while leaving a quiet signature.</p>
</section>
<section class="section order-section reveal" id="order">
  <div><p class="eyebrow">Online order</p><h2>Order {product['name']} directly.</h2><p>Fill in the form and the atelier will confirm availability, payment and delivery by email.</p></div>
  <form class="card form order-form" data-form-message="Thank you. Your order request for {product['name']} was recorded.">
    <input type="hidden" name="product" value="{product['name']}">
    <div class="field-grid">
      <label>Product<input type="text" value="{product['name']}" readonly></label>
      <label>Size<select name="size"><option>100 ml · {product['price']}</option><option>50 ml · sample request</option></select></label>
      <label>Quantity<input type="number" name="quantity" min="1" max="5" value="1" required></label>
      <label>Email<input type="email" name="email" placeholder="you@example.com" required></label>
    </div>
    <label>Full name<input type="text" name="name" placeholder="Your full name" required></label>
    <label>Delivery address<textarea name="address" rows="3" placeholder="Street, postcode, city" required></textarea></label>
    <label>Message<textarea name="message" rows="3" placeholder="Gift wrapping, pickup or special wishes"></textarea></label>
    <button class="btn btn--gold" type="submit">Send order request</button>
    <p class="form-status" aria-live="polite"></p>
  </form>
</section>
</main>""" + footer()


def about_page():
    return header("The House | L’Essence Parfumerie", "Learn about the L’Essence perfume house.", "about") + """<main class="page">
<section class="section page-hero centered reveal"><p class="eyebrow">The House</p><h1>A quiet perfume house built on memory, material and precision.</h1><p class="lead">L’Essence creates fragrances that feel personal, elegant and timeless — composed in small batches for people who prefer detail over noise.</p></section>
<section class="section editorial reveal"><div class="editorial-media"><img src="images/atelier.jpg" alt="Elegant L’Essence boutique interior"><div class="image-label">Zürich Atelier</div></div><div class="editorial-copy"><p class="eyebrow">Our story</p><h2>From a private ritual to a modern fragrance house.</h2><p>L’Essence began in a small Zürich atelier with handwritten formulas, amber glass bottles and one belief: a fragrance should not shout to be remembered.</p><p>We worked slowly — testing each composition on skin, fabric and time. Over months, a house language appeared: clean silhouettes, warm materials, quiet confidence and scents that stay elegant long after the first impression.</p><blockquote>“The most powerful fragrance is the one people remember after you leave.”</blockquote></div></section>
<section class="section values reveal"><div class="section-heading"><h2>Our philosophy</h2><p>Luxury, for us, is not noise. It is precision, patience and materials chosen with intention.</p></div><div class="grid cards-3"><article class="card value-card"><span>01</span><h3>Craftsmanship</h3><p>Small batches allow every bottle to be checked, aged and finished with care.</p></article><article class="card value-card"><span>02</span><h3>Rare Ingredients</h3><p>We use materials for texture and emotion: warm resins, polished woods and luminous florals.</p></article><article class="card value-card"><span>03</span><h3>Timeless Elegance</h3><p>Each perfume is edited until it feels modern, wearable and unmistakably refined.</p></article></div></section>
<section class="section editorial editorial--reverse reveal"><div class="editorial-copy"><p class="eyebrow">The atelier</p><h2>Designed for consultation, not mass production.</h2><p>Our boutique is calm, dark and intimate. Guests discover scents slowly, compare notes on blotters and skin, and leave with a fragrance that feels personal rather than obvious.</p><div class="signature-row"><span>10 perfumes</span><span>6 categories</span><span>Private service</span><span>Hand finished</span></div></div><div class="editorial-media"><img src="images/materials.jpg" alt="Perfume ingredients and golden botanical textures"><div class="image-label">Raw Materials</div></div></section>
</main>""" + footer()


def contact_page():
    return header("Contact | L’Essence Parfumerie", "Contact L’Essence Parfumerie for private consultations.", "contact") + """<main class="page">
<section class="section page-hero reveal"><p class="eyebrow">Contact</p><h1>Book a private fragrance consultation.</h1><p class="lead">For appointments, product questions or boutique reservations, our atelier will be pleased to assist you.</p></section>
<section class="section team-grid reveal">
  <article class="card value-card"><span>Owner</span><h3>Mattia Tuor</h3><p>Creative direction, fragrance selection and private consultations.</p></article>
  <article class="card value-card"><span>Atelier</span><h3>Samu Bayona</h3><p>Small batch production, quality checks and packaging.</p></article>
  <article class="card value-card"><span>Service</span><h3>Denis Clement</h3><p>Orders, appointments and customer care for the Zürich boutique.</p></article>
</section>
<section class="section contact-grid reveal">
  <div><div class="card contact-card"><h2>Atelier</h2><p>Email: <a href="mailto:atelier@lessence.com">atelier@lessence.com</a></p><p>Limmattalstrasse 180, 8049 Zürich</p><p>Tuesday – Saturday · 10:00 – 18:00</p></div><div class="card map-card"><iframe class="real-map" title="Map to L’Essence Parfumerie, Limmattalstrasse 180, Zürich" src="https://www.openstreetmap.org/export/embed.html?bbox=8.4949%2C47.3998%2C8.5034%2C47.4046&layer=mapnik&marker=47.4022094%2C8.4991142"></iframe><p class="map-caption">Limmattalstrasse 180 · 8049 Zürich</p></div></div>
  <form class="card form" data-form-message="Thank you. Your message has been prepared for the L’Essence team.">
    <label>Name<input type="text" name="name" placeholder="Your name" required></label>
    <label>Email<input type="email" name="email" placeholder="you@example.com" required></label>
    <label>Subject<select name="subject" required><option value="">Choose a subject</option><option>Product question</option><option>Order request</option><option>Private consultation</option><option>Press or partnership</option><option>Other question</option></select></label>
    <label>Message<textarea name="message" placeholder="How may we help?" rows="5" required></textarea></label>
    <button class="btn btn--gold" type="submit">Send request</button>
    <p class="form-status" aria-live="polite"></p>
  </form>
</section>
</main>""" + footer()


def ensure_extra_images():
    try:
        from PIL import Image, ImageDraw, ImageFilter
    except Exception:
        return

    colors = {
        "golden-neroli": ("#1d1608", "#d69b2d", "#fff0bb"),
        "silver-musk": ("#121417", "#8f9aa8", "#f4f7fb"),
        "santal-veil": ("#1d130d", "#8b5d38", "#e7c796"),
        "aqua-mirage": ("#07131a", "#188c99", "#b9fff5"),
    }
    for slug, palette in colors.items():
        out = IMG / f"{slug}.jpg"
        if out.exists():
            continue
        product = next(p for p in PRODUCTS if p["slug"] == slug)
        w, h = 900, 650
        base = Image.new("RGB", (w, h), palette[0])
        bg = tuple(int(palette[0].lstrip("#")[i : i + 2], 16) for i in (0, 2, 4))
        c1 = tuple(int(palette[1].lstrip("#")[i : i + 2], 16) for i in (0, 2, 4))
        c2 = tuple(int(palette[2].lstrip("#")[i : i + 2], 16) for i in (0, 2, 4))
        px = base.load()
        for y in range(h):
            for x in range(w):
                dx = (x - w * 0.55) / (w * 0.55)
                dy = (y - h * 0.38) / (h * 0.5)
                r = max(0, 1 - (dx * dx + dy * dy))
                px[x, y] = tuple(int(bg[i] * (1 - r * 0.72) + c1[i] * r * 0.56 + c2[i] * r * 0.18) for i in range(3))
        image = base.filter(ImageFilter.GaussianBlur(0.4)).convert("RGBA")
        draw = ImageDraw.Draw(image, "RGBA")
        for i in range(28):
            x = (i * 127) % w
            y = (i * 89) % h
            draw.ellipse((x - 60, y - 60, x + 120, y + 120), fill=(*c2, 20))
        cx, top, bw, bh = w // 2, 92, 190, 382
        draw.rounded_rectangle((cx - bw // 2, top + 62, cx + bw // 2, top + bh), radius=60, fill=(8, 7, 7, 170), outline=(*c2, 130), width=2)
        draw.rounded_rectangle((cx - 46, top + 12, cx + 46, top + 74), radius=10, fill=(*c1, 190), outline=(*c2, 130), width=1)
        draw.rectangle((cx - 86, top + 226, cx + 86, top + 314), fill=(255, 248, 222, 34), outline=(*c2, 90), width=1)
        draw.text((cx, top + 252), product["name"], fill=(*c2, 230), anchor="mm")
        draw.text((cx, top + 286), product["notes"], fill=(255, 250, 230, 180), anchor="mm")
        image.convert("RGB").save(out, quality=92)


def ensure_videos():
    for product in PRODUCTS:
        source = IMG / f"{product['slug']}.jpg"
        output = VID / f"{product['slug']}.mp4"
        if output.exists() or not source.exists():
            continue
        cmd = [
            "ffmpeg",
            "-y",
            "-loop",
            "1",
            "-t",
            "3",
            "-i",
            str(source),
            "-vf",
            "scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,format=yuv420p",
            "-movflags",
            "+faststart",
            str(output),
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)


def docs():
    (DOCS / "styleguide.md").write_text("""# Styleguide L’Essence

## Farben
| Element | Farbe |
|---|---|
| Hintergrund | `#050504`, `#0b0907` |
| Text hell | `#faf4ea` |
| Text sekundär | `#e7dccb` |
| Gold Akzent | `#c9a463`, `#f1d78f` |

## Typografie
| Bereich | Schrift |
|---|---|
| Titel | Playfair Display |
| Text, Navigation, Formulare | Inter |

## Gestaltung
Die Website nutzt dunkle Flächen, goldene Akzente, große Produktbilder, runde Buttons und klare Karten. Der Look soll hochwertig, ruhig und professionell wirken.
""")
    (DOCS / "wireframes.md").write_text("""# Wireframes

## Mobile
Header oben, Burger-Menü, danach Hero-Text, Produktkarten untereinander, Newsletter-Formular und Footer.

## Tablet
Header mit Navigation, Hero in einer Spalte oder zwei Spalten, Produktgrid mit zwei Spalten, Kontakt und Formulare untereinander.

## Desktop
Fixierter Header, großer Hero mit Produktvisual, Produktgrid mit drei Spalten, Detailseite mit Bild links und Inhalt rechts, darunter Video und Bestellformular.
""")
    (DOCS / "ki-einsatz.md").write_text("""# Dokumentation KI-Einsatz

## Eingesetzte KI-Tools
| Tool | Einsatz | Bewertung |
|---|---|---|
| ChatGPT / Codex | Codeanalyse, HTML/CSS/JS-Verbesserung, Produktdaten, Dokumentation | Sehr gut für Struktur, Vollständigkeit und Debugging |
| Bild-/Asset-KI bzw. generative Hilfe | Produktbilder und visuelle Ideen für Parfum-Artworks | Gut für schnelle hochwertige Visuals |

## Vergleich
ChatGPT/Codex war stärker für sauberen Code, Pflichtanforderungen und konsistente Seiten. Die Bild-KI war stärker für visuelle Wirkung und Produktbilder. Zusammen helfen beide Tools, schneller eine professionelle Website zu erstellen.

## Reflexion
KI wurde gezielt genutzt, um fehlende Funktionen zu erkennen, Produktseiten zu erweitern, Formulare zu verbessern und die Website prüfungsbereit zu machen. Der Code wurde trotzdem kontrolliert und an das bestehende Design angepasst.
""")


def main():
    ensure_extra_images()
    ensure_videos()
    (ROOT / "index.html").write_text(index_page())
    (ROOT / "collection.html").write_text(collection_page())
    (ROOT / "product.html").write_text(product_page(PRODUCTS[0]))
    for product in PRODUCTS:
        (ROOT / f"product-{product['slug']}.html").write_text(product_page(product))
    (ROOT / "about.html").write_text(about_page())
    (ROOT / "contact.html").write_text(contact_page())
    docs()


if __name__ == "__main__":
    main()
