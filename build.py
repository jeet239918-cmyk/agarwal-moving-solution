"""Static site generator for Agarwal Moving Solution.
Run `python3 build.py` from this folder to regenerate every HTML page."""
from pathlib import Path
from html import escape
import re
import locations as LOC

ROOT = Path(__file__).parent
NAME = 'Agarwal Moving Solution'
TAGLINE = 'Corporate Relocation & Logistic Experts'
MOTTO = 'Trust • Reliability • Care'
PERSON = 'Sunil Kaushik'
PHONE = '+917015854009'
PHONE_SHOW = '+91 70158 54009'
WA = '917015854009'
MAIL = 'info@agarwalmovingsolution.co.in'
WEB = 'www.agarwalmovingsolution.co.in'
ADDRESS = 'No. 35, Abdul Kalam Nagar, 3rd Street, Sennerer Kuppam, Poonamallee, Chennai - 600056'
MAP = 'https://maps.google.com/maps?q=Abdul+Kalam+Nagar+Sennerer+Kuppam+Poonamallee+Chennai+600056&output=embed'

# ---------------------------------------------------------------- icons
P = {
 'home': '<path d="M3 11 12 4l9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/>',
 'office': '<rect x="4" y="3" width="12" height="18" rx="1"/><path d="M16 9h4v12h-4M8 7h1M11 7h1M8 11h1M11 11h1M8 15h1M11 15h1"/>',
 'car': '<path d="M3 16v-4l2-5h14l2 5v4z"/><path d="M3 12h18"/><circle cx="7.5" cy="16.5" r="1.8"/><circle cx="16.5" cy="16.5" r="1.8"/>',
 'warehouse': '<path d="M2 21V9l10-6 10 6v12"/><path d="M6 21v-9h12v9M6 15h12M6 18h12"/>',
 'box': '<path d="m12 3 8 4v10l-8 4-8-4V7z"/><path d="m4 7 8 4 8-4M12 11v10"/>',
 'dolly': '<path d="M4 3h3l3 13"/><rect x="10" y="6" width="9" height="8" rx="1" transform="rotate(-14 14 10)"/><circle cx="11" cy="19" r="2"/><path d="M13 18.5 21 17"/>',
 'door': '<path d="M5 21V4a1 1 0 0 1 1-1h9v18"/><path d="M15 5h4v16M3 21h18"/><circle cx="12" cy="12" r=".8"/>',
 'pin': '<path d="M20 10c0 5-8 12-8 12S4 15 4 10a8 8 0 1 1 16 0Z"/><circle cx="12" cy="10" r="2.6"/>',
 'shield': '<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/><path d="m8.5 12 2.5 2.5 4.5-5"/>',
 'phone': '<path d="M22 16.9v3a2 2 0 0 1-2.2 2A18 18 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7l.5 3a2 2 0 0 1-.6 1.8L7.1 10a14 14 0 0 0 6.9 6.9l1.5-1.9a2 2 0 0 1 1.8-.6l3 .5a2 2 0 0 1 1.7 2Z"/>',
 'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
 'chat': '<path d="M20.5 11.6A8.5 8.5 0 0 1 8 19l-4.5 1.5L5 16.2A8.5 8.5 0 1 1 20.5 11.6Z"/><path d="M9 9.5c0 3 2.5 5.5 5.5 5.5l1-1.5-2-1-1 .8a4 4 0 0 1-2-2l.8-1-1-2z"/>',
 'send': '<path d="m22 2-7 20-4-9-9-4z"/><path d="M22 2 11 13"/>',
 'sms': '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/><path d="M8 10h.01M12 10h.01M16 10h.01"/>',
 'check': '<path d="m5 12 4.5 4.5L19 7"/>',
 'arrow': '<path d="M5 12h14m-6-6 6 6-6 6"/>',
 'left': '<path d="M19 12H5m6-6-6 6 6 6"/>',
 'up': '<path d="m6 15 6-6 6 6"/>',
 'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 'rupee': '<circle cx="12" cy="12" r="9"/><path d="M8.5 7.5h7M8.5 10.5h7M9 7.5c4 0 4 6 0 6h-.5l5 4"/>',
 'badge': '<circle cx="12" cy="9" r="6"/><path d="m9 14-1.5 7L12 19l4.5 2L15 14"/><path d="m9.5 9 2 2 3-3.5"/>',
 'truck': '<path d="M2 6h12v10H2zM14 10h4l3 3v3h-7"/><circle cx="6" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/>',
 'users': '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><circle cx="17" cy="9" r="2.5"/><path d="M16 14a5 5 0 0 1 5.5 5"/>',
 'globe': '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
 'menu': '<path d="M4 7h16M4 12h16M4 17h16"/>',
 'close': '<path d="M6 6l12 12M18 6 6 18"/>',
 'user': '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
 'clip': '<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V3h6v1M9 10h6M9 14h6M9 18h3"/>',
 'plus': '<path d="M12 5v14M5 12h14"/>',
}
def icon(name, cls=''):
    return f'<svg class="i {cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{P[name]}</svg>'

LOGO_SVG = ('<svg class="logo-mark" viewBox="0 0 64 64" aria-hidden="true"><defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1">'
            '<stop offset="0" stop-color="#f3cf78"/><stop offset=".55" stop-color="#d49a38"/><stop offset="1" stop-color="#a86b22"/></linearGradient></defs>'
            '<path d="M32 2 60 9v26c0 14-12 23-28 27C16 58 4 49 4 35V9z" fill="url(#lg)"/>'
            '<path d="M32 7 55 13v22c0 11-9.5 18.5-23 22C18.5 53.5 9 46 9 35V13z" fill="none" stroke="#fff6" stroke-width="1.2"/>'
            '<path d="M32 14 47 50h-8l-3.2-8.5H28.2L25 50h-8zm0 12.5-3.4 9.5h6.8z" fill="#fff"/></svg>')

def logo(cls=''):
    return f'<a class="logo {cls}" href="index.html" aria-label="{NAME} home">{LOGO_SVG}<span class="logo-words"><strong>Agarwal</strong><small>MOVING SOLUTION</small></span></a>'

# ---------------------------------------------------------------- data
SERVICES = [
 # name, file, icon, image, short, long paragraphs, includes
 ('Household Shifting', 'home-shifting-service.html', 'home', '1.webp',
  'Complete home relocation – packing, loading, transport and unloading handled by one trained team.',
  ['Shifting a home means moving the things that matter most to your family. Our household shifting service covers every step, from a pre-move survey to careful unpacking at your new address.',
   'We use quality packing material for furniture, kitchenware, electronics and fragile items, label every carton, and plan the day around your building access and timings.'],
  ['Pre-move survey and quote', 'Multi-layer packing for fragile items', 'Furniture dismantling and reassembly', 'Loading, transport and unloading', 'Unpacking and placement on request']),
 ('Office & Corporate Relocation', 'office-shifting-service.html', 'office', '2.webp',
  'Planned office and corporate moves with minimum downtime for your business.',
  ['Corporate relocation is our core strength. We plan office moves floor by floor so that your team can get back to work as quickly as possible.',
   'Workstations, IT equipment, files and furniture are packed, tagged and moved in a sequence agreed with your facilities team – including weekend and after-hours moves.'],
  ['Move planning with your admin team', 'Tagging of desks, files and equipment', 'Safe handling of computers and servers', 'Weekend and night-time shifting', 'Employee relocation support']),
 ('Car & Bike Transportation', 'vehicale-transportation-services.html', 'car', '4.webp',
  'Safe transport of cars and two-wheelers in suitable carriers.',
  ['Moving your vehicle to another city? We arrange car and bike transportation in carriers suited to the vehicle, with proper loading and securing.',
   'Every vehicle is inspected and documented before loading so that you know its condition at pickup and at delivery.'],
  ['Car carrier and bike transport', 'Pre-loading inspection report', 'Secure loading and tie-down', 'Door pickup and delivery options', 'Transit insurance on request']),
 ('Warehouse & Storage', 'warehousing-and-storage-service.html', 'warehouse', '5.webp',
  'Short and long-term storage for household and commercial goods.',
  ['Between two homes, renovating, or need space for business stock? Our warehousing service gives you a secure place to keep goods for as long as you need.',
   'Goods are packed, listed and stored so that they can be retrieved and delivered when you are ready.'],
  ['Short and long-term storage', 'Inventory list of stored goods', 'Packed and palletised storage', 'Pickup and redelivery', 'Storage for household and business goods']),
 ('Packing & Unpacking', 'packing-and-unpacking-service.html', 'box', '7.webp',
  'Professional packing with quality material for every type of item.',
  ['Good packing is what keeps your goods safe on the road. Our team packs each item with the right material – bubble wrap, corrugated sheets, cartons and wooden crates where needed.',
   'At the destination we can unpack, remove the packing waste and help set up your space.'],
  ['Quality cartons and bubble wrap', 'Special packing for glass and electronics', 'Wooden crating for delicate items', 'Labelling of every carton', 'Unpacking and debris removal']),
 ('Loading & Unloading', 'loading-unloading-service.html', 'dolly', '8.webp',
  'Trained manpower for careful loading and unloading of goods.',
  ['Most damage happens while goods are being lifted and carried. Our trained loaders handle heavy furniture, appliances and cartons with the right technique and equipment.',
   'Goods are arranged inside the vehicle so that they stay stable throughout the journey.'],
  ['Trained loading staff', 'Handling of heavy and bulky items', 'Proper arrangement inside the vehicle', 'Staircase and lift handling', 'Unloading and placement']),
 ('Door-to-Door Moving', 'door-to-door-service.html', 'door', '9.webp',
  'One service from your old doorstep to your new one.',
  ['With door-to-door moving you deal with a single team for the whole move – packing at your old home, transport, and delivery to your new doorstep.',
   'You get one point of contact who keeps you updated at every step.'],
  ['Pickup from your doorstep', 'Packing, loading and transport', 'Delivery to your new address', 'Single point of contact', 'Updates during transit']),
 ('Local Shifting', 'local-area-shifting-service.html', 'truck', '10.webp',
  'Quick and affordable shifting within Chennai.',
  ['Moving within Chennai? Our local shifting service is planned to complete your move in the shortest possible time with the right vehicle size for your goods.',
   'We cover all major areas of Chennai and nearby suburbs.'],
  ['Same-day local moves', 'Right-size vehicle for your load', 'Packing and loading team', 'Transparent pricing', 'All Chennai areas covered']),
 ('Goods Insurance', 'goods-insurance-service.html', 'shield', '11.webp',
  'Transit insurance options to protect your goods while they move.',
  ['Even with careful handling, a long journey carries some risk. We can help you arrange transit insurance for your goods so that you move with peace of mind.',
   'Ask our team about the cover available and the terms that apply to your move.'],
  ['Transit insurance assistance', 'Declared value documentation', 'Guidance on claim process', 'Cover for household and office goods', 'Available on request']),
]
AREAS = ['Adyar', 'Alwarpet', 'Anna Nagar', 'ECR Road', 'Guduvancheri', 'KK Nagar', 'MRC Nagar', 'Navalur',
         'Nungambakkam', 'OMR Road', 'Tambaram', 'Velachery', 'Poonamallee', 'Porur', 'T Nagar', 'Sholinganallur']
def area_file(a): return 'packers-and-movers-' + a.lower().replace(' ', '-') + '.html'

# Approximate charges in INR: (labour, packing, transport, total) for low and high end.
PRICES = [
 ('1 BHK', (1400, 1500, 1800, 4700), (3100, 3100, 3400, 9600)),
 ('2 BHK', (2100, 1700, 2600, 6400), (3700, 4100, 4600, 12400)),
 ('3 BHK', (3100, 3700, 3600, 10400), (5200, 5800, 6300, 17300)),
 ('4 BHK', (4100, 5100, 4100, 13300), (5600, 7100, 7200, 19900)),
 ('Villa', (4600, 6600, 7200, 18400), (6100, 8900, 9900, 24900)),
 ('Small Office', (4200, 5100, 6100, 15400), (6800, 8200, 9800, 24800)),
 ('Medium Office', (5500, 10400, 10400, 26300), (10600, 15700, 20100, 46400)),
 ('Corporate Office', (9900, 12800, 16200, 38900), (20700, 24700, 35500, 80900)),
]
for _n, _lo, _hi in PRICES:
    assert sum(_lo[:3]) == _lo[3] and sum(_hi[:3]) == _hi[3], _n
    assert all(v % 1000 for v in _lo + _hi), _n

def inr(v): 
    s = str(v)
    return '₹' + (s[:-3] + ',' + s[-3:] if len(s) > 3 else s) if len(s) <= 5 else '₹' + s[:-5] + ',' + s[-5:-3] + ',' + s[-3:]

def price_table(title, note=None):
    cols = ['Labour Charges', 'Packing Charges', 'Transport Charges', 'Total Cost (Approx)']
    head = '<tr><th>Move Size</th>' + ''.join(f'<th>{c}</th>' for c in cols) + '</tr>'
    rows = ''.join('<tr><td data-label="Move Size"><b>' + n + '</b></td>' + ''.join(f'<td data-label="{cols[i]}">{inr(lo[i])} – {inr(hi[i])}</td>' for i in range(4)) + '</tr>' for n, lo, hi in PRICES)
    note = note or 'Approximate charges for local shifting. Your final price is confirmed after a free survey, based on the quantity of goods, floor, distance and services chosen.'
    return (f'<div class="ptable-wrap"><h3 class="ptable-title">{title}</h3><div class="ptable-scroll"><table class="ptable"><thead>{head}</thead><tbody>{rows}</tbody></table></div>'
            f'<p class="ptable-note">{note} <a href="tel:{PHONE}">Call {PHONE_SHOW}</a> for an exact quote.</p></div>')

NAV = [('Home', 'index.html'), ('About Us', 'about-us.html'), ('Services', 'services.html'), ('Network', 'network.html'),
       ('Pricing', 'pricing.html'), ('Gallery', 'gallery.html'), ('Enquiry', 'enquiry.html'), ('Contact Us', 'contact-us.html')]

# ---------------------------------------------------------------- layout
def header(active):
    links = ''.join(f'<a href="{h}" class="{"on" if h == active else ""}">{t}</a>' for t, h in NAV)
    sub = ''.join(f'<a href="{s[1]}">{s[0]}</a>' for s in SERVICES)
    nav = links.replace('<a href="services.html"', f'<div class="has-sub"><a href="services.html"', 1)
    nav = nav.replace('>Services</a>', f'>Services</a><button class="sub-toggle" type="button" aria-label="Show services" aria-expanded="false">{icon("plus")}</button><div class="sub">{sub}</div></div>', 1)
    nav = f'<div class="nav-head">{logo("logo-sm")}<button class="nav-close" type="button" aria-label="Close menu">{icon("close")}</button></div>' + nav + f'<div class="nav-foot"><a class="btn-gold" href="tel:{PHONE}">{icon("phone")}Call {PHONE_SHOW}</a><a class="btn-wa" href="https://wa.me/{WA}" target="_blank" rel="noopener">{icon("chat")}WhatsApp Us</a></div>'
    return f'''<div class="topbar"><div class="wrap topbar-in"><span>{icon('mail')}<a href="mailto:{MAIL}">{MAIL}</a></span><span class="tb-mid">{MOTTO}</span><span>{icon('phone')}<a href="tel:{PHONE}">{PHONE_SHOW}</a></span></div></div>
<header class="hdr"><div class="wrap hdr-in">{logo()}
<nav class="nav" id="nav" aria-label="Main menu">{nav}</nav>
<a class="btn-outline quote-btn" href="enquiry.html">Free Quote!</a>
<a class="hdr-call" href="tel:{PHONE}" aria-label="Call {PHONE_SHOW}">{icon('phone')}</a><button class="burger" aria-label="Open menu" aria-expanded="false" aria-controls="nav">{icon('menu')}</button></div></header><div class="nav-backdrop"></div>'''

def footer():
    menu = ''.join(f'<li><a href="{h}">{t}</a></li>' for t, h in NAV) + '<li><a href="privacy-policy.html">Privacy Policy</a></li><li><a href="terms-and-conditions.html">Terms &amp; Conditions</a></li>'
    serv = ''.join(f'<li><a href="{s[1]}">{s[0]}<span class="in-city"> in Chennai</span></a></li>' for s in SERVICES)
    return f'''<footer class="ftr"><div class="wrap">
<h2 class="ftr-title">{NAME} Chennai</h2>
<div class="ftr-grid">
<div class="ftr-img"><img src="assets/images/why.jpg" alt="Packed cartons ready for dispatch" loading="lazy"></div>
<div><h3>Our Profile</h3><p>{NAME} are {TAGLINE.lower()} based in Poonamallee, Chennai. We handle household, office and vehicle moves with a focus on {MOTTO.replace(' •', ',').lower()}.</p>
<h3>Get a Quote!</h3><p class="ftr-contact">{icon('user')}<span>{PERSON}</span></p><p class="ftr-contact">{icon('phone')}<a href="tel:{PHONE}">{PHONE_SHOW}</a></p><p class="ftr-contact">{icon('mail')}<a href="mailto:{MAIL}">{MAIL}</a></p><p class="ftr-contact">{icon('pin')}<span>{ADDRESS}</span></p></div>
<div><h3>Quick Links</h3><ul class="ftr-list">{menu}</ul></div>
<div><h3>What We Offer</h3><ul class="ftr-list">{serv}</ul></div>
</div></div>
<div class="ftr-bar"><div class="wrap ftr-bar-in"><span>© 2026 {NAME.upper()}. ALL RIGHTS RESERVED.</span><a href="https://{WEB}">{WEB}</a></div></div></footer>
<div class="float-left"><a class="fl-call" href="tel:{PHONE}" aria-label="Call us">{icon('phone')}</a><a class="fl-wa" href="https://wa.me/{WA}" target="_blank" rel="noopener" aria-label="WhatsApp us">{icon('chat')}</a></div>
<button class="to-top" aria-label="Back to top">{icon('up')}</button>
<nav class="mob-bar" aria-label="Quick contact"><a href="tel:{PHONE}">{icon('phone')}<span>Call Now</span></a><a href="mailto:{MAIL}">{icon('mail')}<span>Email</span></a><a href="https://wa.me/{WA}" target="_blank" rel="noopener">{icon('chat')}<span>WhatsApp</span></a><a href="enquiry.html">{icon('send')}<span>Enquiry</span></a><a href="sms:{PHONE}">{icon('sms')}<span>Message</span></a></nav>
<script src="assets/js/main.js" defer></script>'''

def page(title, desc, body, active):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(title)} | {NAME} – Packers and Movers in Chennai</title><meta name="description" content="{escape(desc, quote=True)}"><meta name="theme-color" content="#1b2238">
<link rel="icon" href="assets/images/favicon.svg"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=Barlow:wght@400;500;600;700&display=swap" rel="stylesheet"><link rel="stylesheet" href="assets/css/style.css"><script>document.documentElement.classList.add('js');setTimeout(function(){{if(!window.__rv)document.documentElement.classList.add('rv-off')}},2500)</script></head>
<body>{header(active)}<main>{body}</main>{footer()}</body></html>'''

def quote_form(title='GET A FREE QUOTE !', cls=''):
    return f'''<form class="qform {cls}" data-quote><h3>{title}</h3><div class="qgrid">
<input name="name" placeholder="Name" required autocomplete="name"><input name="date" type="date" aria-label="Moving date">
<input name="email" type="email" placeholder="Email" autocomplete="email"><input name="from" placeholder="Moving From" required>
<input name="mobile" type="tel" placeholder="Mobile No" required autocomplete="tel"><input name="to" placeholder="Moving To" required>
<select name="type" aria-label="Type of move"><option value="">Type of move</option><option>Household shifting</option><option>Office / corporate relocation</option><option>Car / bike transport</option><option>Warehouse &amp; storage</option><option>Other</option></select>
<select name="size" aria-label="Size"><option value="">Size (optional)</option><option>1 RK / 1 BHK</option><option>2 BHK</option><option>3 BHK</option><option>4 BHK / Villa</option><option>Office</option></select>
<textarea name="req" placeholder="Requirement" rows="3" class="full"></textarea></div>
<div class="qbtns"><button type="submit" class="btn-navy">Submit</button><button type="reset" class="btn-navy">Reset</button></div>
<small>Submitting opens WhatsApp with your details, ready to send to our team.</small></form>'''

def banner(title, crumb, img='3.webp'):
    return f'''<section class="pbanner" style="--bg:url('../images/{img}')"><div class="wrap"><h1>{title}</h1><p class="crumbs"><a href="index.html">Home</a> <span>›</span> {crumb}</p></div></section>'''

def sidebar():
    s = ''.join(f'<a href="{x[1]}">{icon(x[2])}{x[0]}</a>' for x in SERVICES)
    return f'''<aside class="side"><div class="side-box"><h3>Our Services</h3><div class="side-links">{s}</div></div>
<div class="side-call"><p>Need help planning your move?</p><a href="tel:{PHONE}">{icon('phone')}{PHONE_SHOW}</a><a class="btn-gold" href="enquiry.html">Get Free Quote</a></div></aside>'''

def section_head(small, big, center=False):
    return f'<div class="shead {"center" if center else ""}"><span class="kicker">{small}</span><h2>{big}</h2></div>'

def cta_band():
    return f'''<section class="band" style="--bg:url('../images/why.jpg')"><div class="wrap"><p class="band-top">HASSLE FREE</p><h2>PACKING AND MOVING SERVICES IN CHENNAI</h2>
<div class="band-btns"><a class="btn-gold shine" href="enquiry.html">Get Free Quote</a><a class="btn-white" href="tel:{PHONE}">{icon('phone')}Call {PHONE_SHOW}</a></div></div>{TRUCK}</section>'''

TRUCK = ('<div class="road" aria-hidden="true"><svg class="truck" viewBox="0 0 120 56"><rect x="2" y="8" width="70" height="34" rx="3" fill="#e0ad45"/>'
         '<text x="37" y="30" text-anchor="middle" font-family="Oswald,Arial" font-size="11" font-weight="700" fill="#1b2238">AGARWAL</text>'
         '<path d="M72 18h22l14 13v11H72z" fill="#9b1e28"/><path d="M77 22h15l9 9H77z" fill="#cfe0f5"/>'
         '<g class="wheel"><circle cx="22" cy="44" r="8" fill="#1b2238"/><circle cx="22" cy="44" r="3" fill="#ccc"/></g><g class="wheel"><circle cx="92" cy="44" r="8" fill="#1b2238"/><circle cx="92" cy="44" r="3" fill="#ccc"/></g></svg></div>')

STEPS = [('phone', 'Call or Enquire', 'Tell us what you are moving, from where and to where.'),
         ('clip', 'Free Survey & Quote', 'We check your goods and share a clear, written quote.'),
         ('box', 'Packing & Loading', 'Our team packs with quality material and loads safely.'),
         ('truck', 'Safe Delivery', 'Goods reach your new place on the agreed date.')]
def steps_block():
    st = ''.join(f'<div class="step"><span class="step-no">0{k+1}</span><span class="step-ic">{icon(i)}</span><h3>{t}</h3><p>{d}</p></div>' for k, (i, t, d) in enumerate(STEPS))
    return f'<section class="steps"><div class="wrap">{section_head("How It Works", "YOUR MOVE IN 4 SIMPLE STEPS", True)}<div class="steps-grid">{st}</div></div></section>'

WHY = ['On-Time Delivery', 'Secure Packaging', 'Insurance of Goods', 'Corporate Relocation Experts',
       'Trained & Verified Staff', 'Affordable Pricing', 'Quick Response', 'Local & Intercity Moves']
def why_block():
    items = ''.join(f'<li>{icon("arrow")}{w}</li>' for w in WHY)
    return f'''<section class="why"><div class="wrap why-grid"><div><h2 class="h-dark">Why Choose {NAME}?</h2><ul class="why-list">{items}</ul></div>
<div class="why-img"><img src="assets/images/7.webp" alt="Household goods wrapped and ready to move" loading="lazy"></div></div></section>'''

def service_cards(limit=None):
    out = ''
    for n, f, ic, img, short, *_ in SERVICES[:limit]:
        out += (f'<a class="scard" href="{f}"><span class="scard-img"><img src="assets/images/{img}" alt="{n} by {NAME}" loading="lazy"></span>'
                f'<span class="scard-ic">{icon(ic)}</span><span class="scard-body"><h3>{n}<span class="in-city"> in Chennai</span></h3><p>{short}</p><span class="more">Read More {icon("arrow")}</span></span></a>')
    return f'<div class="sgrid">{out}</div>'

def area_chips():
    return '<div class="chips">' + ''.join(f'<a href="{area_file(a)}">{icon("pin")}{a}</a>' for a in AREAS) + '</div>'

# ---------------------------------------------------------------- pages
def home():
    slides = [
      ('l1.jpg', 'Your trusted partner for <b>stress-free shifting.</b>', 'Household, office and vehicle moves across Chennai and India.'),
      ('abt.jpeg', 'Corporate relocation <b>done right.</b>', 'Planned office moves with minimum downtime for your business.'),
      ('3.webp', 'Logistics you can <b>rely on.</b>', 'Transport, warehousing and door-to-door delivery under one roof.'),
    ]
    sl = ''
    for k, (img, h, p) in enumerate(slides):
        sl += f'''<div class="slide {"on" if k == 0 else ""}"><img src="assets/images/{img}" alt="" {"" if k == 0 else 'loading="lazy"'}><span class="slide-stripe"></span><div class="slide-panel"><h2>{h}</h2><p>{p}</p>
<div class="slide-cta"><a class="btn-gold shine" href="enquiry.html">Get Free Quote {icon('arrow')}</a><a class="btn-ghost" href="tel:{PHONE}">{icon('phone')}Call Now</a></div>
<div class="slide-badges"><span>{icon('badge')}Verified Team</span><span>{icon('rupee')}Affordable Pricing</span><span>{icon('clock')}On-Time Delivery</span></div></div></div>'''
    dots = ''.join(f'<button class="{"on" if k == 0 else ""}" aria-label="Slide {k+1}"></button>' for k in range(len(slides)))
    hero = f'''<section class="hero" data-slider>{sl}<button class="sl-prev" aria-label="Previous slide">{icon('left')}</button><button class="sl-next" aria-label="Next slide">{icon('arrow')}</button><div class="sl-dots">{dots}</div></section>'''

    quote = f'''<section class="quote-sec"><div class="wrap quote-grid"><div class="quote-left">
<p class="gold-small">{TAGLINE}</p><div class="big-phone">{icon('phone')}<div><a href="tel:{PHONE}">{PHONE_SHOW}</a><span>{PERSON}</span></div></div>
<h2 class="h-blue">We handle your goods like they are our own.</h2><p class="h-sub">Get a free domestic &amp; corporate moving quote</p>
<img src="assets/images/8.webp" alt="Moving team loading goods" loading="lazy"></div>{quote_form()}</div></section>'''

    feats = [('24X7 SUPPORT', 'Our team is available to answer your calls and plan your move at any time.'),
             ('CORPORATE EXPERTS', 'Specialists in office and corporate relocation with minimum downtime.'),
             ('SAFE HANDLING', 'Quality packing material and trained staff for every item.'),
             ('PAN-INDIA MOVES', 'Local, intercity and long-distance shifting from Chennai.')]
    fic = ['clock', 'office', 'shield', 'globe']
    fl = ''.join(f'<div class="feat"><span class="feat-ic">{icon(fic[k])}</span><div><h4>{a}</h4><p>{b}</p></div><span class="feat-arrow">{icon("left")}</span></div>' for k, (a, b) in enumerate(feats))
    about = f'''<section class="about-split"><div class="about-blue">{fl}</div><div class="about-body"><div class="about-text">
<p class="welcome">Welcome to</p><h2 class="h-dark">{NAME}</h2><p class="paren">( {TAGLINE} )</p>
<p>{NAME} is a Chennai-based packing and moving company located in Poonamallee. We provide <b>corporate relocation</b>, <b>household shifting</b>, <b>car and bike transportation</b>, <b>warehousing</b> and <b>goods insurance</b> assistance for families and businesses.</p>
<p>Our work is built on three words – <b>trust, reliability and care</b>. Every move is planned with you, packed with quality material, and delivered on the agreed date.</p>
<a class="btn-navy" href="about-us.html">Read More</a></div>
<div class="about-circle"><img src="assets/images/abt.jpeg" alt="Goods packed for relocation" loading="lazy"><div class="circle-badge"><b>TRUST</b><span>RELIABILITY</span><b>CARE</b></div></div></div></section>'''

    services = f'''<section class="services"><div class="wrap"><div class="services-top">{section_head('Our Services', 'WE PROVIDE COMPLETE PACKING, MOVING &amp; LOGISTICS SERVICES')}
<p>{NAME} offers solutions for household shifting, office and corporate relocation, vehicle transportation, warehousing, packing, loading and goods insurance across Chennai.</p></div>{service_cards()}</div></section>'''

    network = f'''<section class="network"><div class="wrap">{section_head('Our Network', 'AREAS WE SERVE IN CHENNAI', True)}{area_chips()}<p class="center-note">Moving outside Chennai? We also handle intercity and all-India relocation. <a href="contact-us.html">Talk to us →</a></p><p class="center-note"><a class="btn-navy" href="network.html">View all {sum(len(g[3]) for g in GROUPS)} locations</a></p></div></section>'''
    pricing = f'<section class="pricing-sec"><div class="wrap">{section_head("Pricing", "PACKERS AND MOVERS CHARGES IN CHENNAI", True)}{price_table("Local Packers and Movers Charges in Chennai:")}<p class="center-note"><a class="btn-navy" href="pricing.html">See full pricing guide</a></p></div></section>'
    body = hero + quote + about + services + steps_block() + pricing + cta_band() + why_block() + network
    return page('Packers and Movers in Chennai', f'{NAME} – {TAGLINE} in Poonamallee, Chennai. Household shifting, office relocation, car transport and warehousing. Call {PHONE_SHOW}.', body, 'index.html')

def about_page():
    body = banner('About Us', 'About Us', 'abt.jpeg')
    body += f'''<section class="content"><div class="wrap two"><div class="prose">
<p class="welcome">Welcome to</p><h2 class="h-dark">{NAME}</h2><p class="paren">( {TAGLINE} )</p>
<p>{NAME} is a packing and moving company based at Abdul Kalam Nagar, Sennerer Kuppam, Poonamallee, Chennai. We help families and businesses relocate safely – whether it is a flat across the city, a full office, or a vehicle going to another state.</p>
<p>Corporate relocation and logistics are our speciality. We plan office moves in detail with your admin team, tag every asset, and schedule the move to keep business disruption as low as possible.</p>
<p>For households, we offer complete packing, loading, transport, unloading and unpacking with one team from start to finish.</p>
<h3>Our Values</h3><div class="values"><div>{icon('shield')}<b>Trust</b><span>Clear quotes and honest communication.</span></div><div>{icon('clock')}<b>Reliability</b><span>We turn up on time and deliver on the agreed date.</span></div><div>{icon('box')}<b>Care</b><span>Every item packed and handled with care.</span></div></div>
</div><div class="about-pic"><img src="assets/images/why.jpg" alt="Cartons and furniture packed for transport"><div class="pic-card">{icon('user')}<div><small>Contact Person</small><b>{PERSON}</b><a href="tel:{PHONE}">{PHONE_SHOW}</a></div></div></div></div></section>'''
    body += why_block() + cta_band()
    return page('About Us', f'Learn about {NAME}, {TAGLINE} in Chennai.', body, 'about-us.html')

def services_page():
    body = banner('Our Services', 'Services', '5.webp')
    body += f'''<section class="services"><div class="wrap"><div class="services-top">{section_head('What We Do', 'PACKING, MOVING &amp; LOGISTICS SERVICES')}<p>Choose a single service or let us handle your complete move. Every service can be combined into one plan and one quote.</p></div>{service_cards()}</div></section>''' + directory() + cta_band()
    return page('Our Services', f'Packing, moving and logistics services by {NAME} in Chennai.', body, 'services.html')

def service_page(s):
    n, f, ic, img, short, paras, inc = s
    ps = ''.join(f'<p>{p}</p>' for p in paras)
    li = ''.join(f'<li>{icon("check")}{x}</li>' for x in inc)
    body = banner(f'{n} in Chennai', f'<a href="services.html">Services</a> <span>›</span> {n}', img)
    body += f'''<section class="content"><div class="wrap with-side"><article class="prose"><img class="lead-img" src="assets/images/{img}" alt="{n}">
<h2 class="h-dark">{n} Services in Chennai</h2><p class="lead">{short}</p>{ps}<h3>What's Included</h3><ul class="ticks">{li}</ul>
<h3>Why book with {NAME}?</h3><p>We are {TAGLINE.lower()} with a trained team, quality packing material and a clear quote before we start. Call <a href="tel:{PHONE}">{PHONE_SHOW}</a> or fill the form below for a free estimate.</p>
{price_table(f'{n} Charges in Chennai:')}
{quote_form('REQUEST A FREE QUOTE', 'inline')}</article>{sidebar()}</div></section>'''
    return page(f'{n} in Chennai', f'{n} in Chennai by {NAME}. {short}', body, 'services.html')

def slug(x): return re.sub(r'[^a-z0-9]+', '-', x.lower()).strip('-')

# (key, region label, kind, names, filename pattern, breadcrumb label)
GROUPS = [
 ('pm-india', 'India', 'pm', LOC.INDIA, 'packers-and-movers-in-{s}.html'),
 ('pm-chennai', 'Chennai', 'pm', LOC.CHENNAI, 'packers-and-movers-{s}.html'),
 ('pm-tn', 'Tamil Nadu', 'pm', LOC.TAMIL_NADU, 'packers-and-movers-in-{s}-tamil-nadu.html'),
 ('pm-blr', 'Bangalore', 'pm', LOC.BANGALORE, 'packers-and-movers-in-{s}-bangalore.html'),
 ('cb-chennai', 'Chennai', 'cb', LOC.CHENNAI, 'car-bike-transport-in-{s}-chennai.html'),
 ('cb-tn', 'Tamil Nadu', 'cb', LOC.TAMIL_NADU, 'car-bike-transport-in-{s}-tamil-nadu.html'),
 ('cb-blr', 'Bangalore', 'cb', LOC.BANGALORE, 'car-bike-transport-in-{s}-bangalore.html'),
 ('cb-india', 'India', 'cb', LOC.INDIA, 'car-bike-transport-in-{s}.html'),
]
G = {g[0]: g for g in GROUPS}
def loc_file(key, name): return G[key][4].format(s=slug(name))
def loc_text(kind, name): return f'Packers and Movers in {name}' if kind == 'pm' else f'Car &amp; Bike Transport in {name}'
def group_title(g):
    key, region, kind = g[0], g[1], g[2]
    return region if kind == 'pm' else f'Car &amp; Bike Transport in {region}'

def directory():
    def card(g):
        items = ''.join(f'<li><a href="{loc_file(g[0], n)}">{loc_text(g[2], n)}</a></li>' for n in g[3])
        ic = 'pin' if g[2] == 'pm' else 'car'
        return (f'<div class="dir-card" data-dir-card><div class="dir-head">{icon(ic)}<h3>{group_title(g)}</h3><span class="dir-count">{len(g[3])}</span></div>'
                f'<ul class="dir-list">{items}</ul><p class="dir-empty" hidden>No matching place</p></div>')
    pm = ''.join(card(g) for g in GROUPS if g[2] == 'pm')
    cb = ''.join(card(g) for g in GROUPS if g[2] == 'cb')
    total = sum(len(g[3]) for g in GROUPS)
    return f'''<section class="directory"><div class="wrap">{section_head('Our Network', 'PACKERS AND MOVERS NETWORK', True)}
<p class="center-note top">From our base in Poonamallee, Chennai we handle local shifting across Chennai and relocation to and from cities across Tamil Nadu, Bangalore and India.</p>
<label class="dir-search">{icon('pin')}<input type="search" placeholder="Search your city or area…" data-dir-search aria-label="Search locations"><span data-dir-total>{total} locations</span></label>
<h3 class="dir-group-title">Packers and Movers</h3><div class="dir-grid">{pm}</div>
<h3 class="dir-group-title">Car &amp; Bike Transportation</h3><div class="dir-grid">{cb}</div>
<p class="dir-none" hidden>No location found. <a href="contact-us.html">Ask us about your route →</a></p></div></section>'''

def network_page():
    body = banner('Our Network', 'Network', '10.webp') + directory() + cta_band()
    return page('Our Network', f'Packers and movers network of {NAME} – Chennai, Tamil Nadu, Bangalore and all India.', body, 'network.html')

def loc_page(key, idx):
    key, region, kind, names, _ = G[key]
    name = names[idx]
    here = f'{name}, {region}' if region not in ('India',) else name
    other_key = ('cb' if kind == 'pm' else 'pm') + key[2:]
    other = f'<a href="{loc_file(other_key, name)}">{loc_text(other_key[:2], name)}</a>'
    near = [names[(idx + d) % len(names)] for d in (-4, -3, -2, -1, 1, 2, 3, 4) if len(names) > 8]
    chips = ''.join(f'<a href="{loc_file(key, n)}">{icon("pin")}{n}</a>' for n in near)
    title = loc_text(kind, name).replace('&amp;', '&')
    if kind == 'pm':
        intro = {
         'Chennai': f'Looking for reliable packers and movers in {name}? {NAME} is based in Poonamallee, Chennai and handles household shifting, office relocation and vehicle transport for homes and businesses in {name} and nearby areas.',
         'Tamil Nadu': f'Moving to or from {name}? {NAME} plans relocations between Chennai and {name}, Tamil Nadu, as well as moves within the {name} area, with careful packing and safe transport.',
         'Bangalore': f'Shifting between Chennai and {name}, Bangalore – or moving within Bangalore? {NAME} handles household and office relocation on this route with careful packing and planned transport.',
         'India': f'Relocating from Chennai to {name}, or from {name} to Chennai? {NAME} arranges long-distance household, office and vehicle moves across India with one team managing your move from start to finish.'}[region]
        body2 = f'<p>We survey your goods, share a clear written quote, pack everything with quality material and deliver on the agreed date. Every move to or from {name} is planned around access, timing and the items you are moving.</p>'
        sv = ''.join(f'<li>{icon("check")}<a href="{s[1]}">{s[0]}</a></li>' for s in SERVICES)
        extra = f'<h3>Services for {name}</h3><ul class="ticks cols">{sv}</ul>'
        img = '1.webp'
    else:
        intro = {
         'Chennai': f'Need to move your car or bike in or out of {name}, Chennai? {NAME} arranges safe vehicle transport with proper loading, securing and doorstep delivery.',
         'Tamil Nadu': f'Transport your car or two-wheeler between Chennai and {name}, Tamil Nadu with {NAME}. Vehicles are inspected, loaded carefully and secured for the journey.',
         'Bangalore': f'Moving your car or bike between Chennai and {name}, Bangalore? {NAME} arranges vehicle transport with a pre-loading inspection and secure loading.',
         'India': f'Send your car or bike from Chennai to {name}, or bring it from {name} to Chennai. {NAME} arranges vehicle transportation across India.'}[region]
        body2 = '<p>Every vehicle is checked and documented before loading so you know its condition at pickup and at delivery. Transit insurance can be arranged on request.</p>'
        extra = f'<h3>What\'s included</h3><ul class="ticks">' + ''.join(f'<li>{icon("check")}{x}</li>' for x in ['Car and bike transport', 'Pre-loading inspection', 'Secure loading and tie-down', 'Door pickup and delivery options', 'Transit insurance on request']) + '</ul>'
        img = '4.webp'
    if kind == 'pm':
        ptab = price_table(f'Local Packers and Movers Charges in {name}:') if region == 'Chennai' else price_table(f'Packers and Movers Charges in {name}:', f'Approximate local shifting charges. For moves between Chennai and {name}, transport is priced by distance and quoted after a free survey.')
    else:
        ptab = ''
    crumb = f'<a href="network.html">Network</a> <span>›</span> {group_title(G[key])} <span>›</span> {name}'
    body = banner(title, crumb, img)
    body += f'''<section class="content"><div class="wrap with-side"><article class="prose"><h2 class="h-dark">{title}</h2>
<p class="lead">{intro}</p>{body2}{extra}
<div class="call-strip"><div><b>Call for a free quote</b><span>{PERSON} · {NAME}</span></div><a class="btn-gold shine" href="tel:{PHONE}">{icon('phone')}{PHONE_SHOW}</a></div>
{ptab}<p>Also see: {other}.</p>
<h3>Nearby locations</h3><div class="chips small">{chips}</div>
{quote_form(f'FREE QUOTE – {name.upper()}', 'inline')}</article>{sidebar()}</div></section>'''
    return page(title + (f', {region}' if region != 'India' else ''), f'{title} – {NAME}. Call {PHONE_SHOW} for a free quote.', body, 'network.html')

def pricing_page():
    body = banner('Pricing', 'Pricing', '7.webp')
    factors = [('box', 'Quantity of goods', 'Number of items, furniture and appliances to be packed and moved.'),
               ('pin', 'Distance', 'Local moves within Chennai or long-distance relocation to another city.'),
               ('office', 'Floor & access', 'Floor level, lift availability and parking at both addresses.'),
               ('shield', 'Extra services', 'Storage, vehicle transport, dismantling and transit insurance.')]
    f = ''.join(f'<div class="values-card">{icon(i)}<b>{t}</b><span>{d}</span></div>' for i, t, d in factors)
    body += f'''<section class="content"><div class="wrap">{section_head('Pricing Guide', 'PACKERS AND MOVERS CHARGES', True)}
<p class="center-note top">Transparent, approximate charges for local shifting in Chennai. Every quote is confirmed in writing after a free survey – no hidden costs.</p>
{price_table('Local Packers and Movers Charges in Chennai:')}
<h3 class="dir-group-title">What affects the price?</h3><div class="values four">{f}</div>
<div class="call-strip"><div><b>Get your exact price</b><span>{PERSON} · {NAME}</span></div><a class="btn-gold shine" href="tel:{PHONE}">{icon('phone')}{PHONE_SHOW}</a></div>
{quote_form('GET A FREE QUOTE', 'inline')}</div></section>''' + cta_band()
    return page('Packers and Movers Charges in Chennai', f'Approximate packers and movers charges in Chennai for 1 BHK to corporate office moves – {NAME}.', body, 'pricing.html')

def gallery_page():
    imgs = ['1.webp', '2.webp', '3.webp', '4.webp', '5.webp', '7.webp', '8.webp', '10.webp', '11.webp', 'l1.jpg', 'why.jpg', 'abt.jpeg']
    g = ''.join(f'<button class="gitem" data-full="assets/images/{i}"><img src="assets/images/{i}" alt="Gallery photo {k+1}" loading="lazy"></button>' for k, i in enumerate(imgs))
    body = banner('Gallery', 'Gallery', 'l1.jpg')
    body += f'<section class="content"><div class="wrap">{section_head("Our Work", "PHOTO GALLERY", True)}<div class="gallery">{g}</div></div></section><div class="lightbox" hidden><button aria-label="Close">{icon("close")}</button><img alt=""></div>'
    return page('Gallery', f'Photos from {NAME}.', body, 'gallery.html')

def enquiry_page():
    body = banner('Enquiry', 'Enquiry', '8.webp')
    body += f'''<section class="content"><div class="wrap enq"><div class="prose"><h2 class="h-dark">Get a Free Moving Quote</h2><p class="lead">Share a few details about your move and our team will call you back with a clear, no-obligation quote.</p>
<ul class="ticks">{''.join(f'<li>{icon("check")}{x}</li>' for x in ['Free pre-move survey', 'Transparent pricing', 'No obligation to book', 'Quick response on call and WhatsApp'])}</ul>
<div class="side-call"><p>Prefer to talk?</p><a href="tel:{PHONE}">{icon('phone')}{PHONE_SHOW}</a></div></div>{quote_form()}</div></section>'''
    return page('Enquiry', f'Request a free moving quote from {NAME}.', body, 'enquiry.html')

def contact_page():
    body = banner('Contact Us', 'Contact Us', '2.webp')
    cards = [('user', 'Contact Person', PERSON, None), ('phone', 'Call Us', PHONE_SHOW, f'tel:{PHONE}'), ('mail', 'Email Us', MAIL, f'mailto:{MAIL}'),
             ('globe', 'Website', WEB, f'https://{WEB}'), ('pin', 'Visit Us', ADDRESS, None)]
    c = ''.join(f'<div class="ccard">{icon(i)}<h3>{t}</h3>' + (f'<a href="{h}">{v}</a>' if h else f'<p>{v}</p>') + '</div>' for i, t, v, h in cards)
    body += f'''<section class="content"><div class="wrap"><div class="ccards">{c}</div><div class="contact-grid"><iframe title="Map to {NAME}" src="{MAP}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>{quote_form('SEND US YOUR REQUIREMENT')}</div></div></section>'''
    return page('Contact Us', f'Contact {NAME}, Poonamallee, Chennai. Call {PHONE_SHOW}.', body, 'contact-us.html')

def simple_page(title, file, paras):
    body = banner(title, title, '12.webp') + '<section class="content"><div class="wrap prose narrow">' + ''.join(f'<p>{p}</p>' for p in paras) + '</div></section>'
    return page(title, f'{title} – {NAME}.', body, '')

pages = {
 'index.html': home(), 'about-us.html': about_page(), 'services.html': services_page(), 'network.html': network_page(),
 'gallery.html': gallery_page(), 'enquiry.html': enquiry_page(), 'contact-us.html': contact_page(), 'pricing.html': pricing_page(),
 'privacy-policy.html': simple_page('Privacy Policy', 'privacy-policy.html', [
   'The enquiry forms on this website do not store your details on a server. When you submit a form, your details are placed into a WhatsApp message on your own device, and are only shared with our team if you choose to send it.',
   f'For any privacy question, email <a href="mailto:{MAIL}">{MAIL}</a>.']),
 'terms-and-conditions.html': simple_page('Terms & Conditions', 'terms-and-conditions.html', [
   'The final scope, price, schedule and terms of every move are confirmed in writing by our team before the move begins.',
   f'Please contact us at <a href="tel:{PHONE}">{PHONE_SHOW}</a> for full terms, including cancellation and insurance conditions.']),
 '404.html': simple_page('Page Not Found', '404.html', ['The page you are looking for could not be found. <a href="index.html">Go back to the home page</a>.']),
}
for s in SERVICES: pages[s[1]] = service_page(s)
for g in GROUPS:
    for i in range(len(g[3])): pages[loc_file(g[0], g[3][i])] = loc_page(g[0], i)
for fname, html in pages.items(): (ROOT / fname).write_text(html, encoding='utf-8')
urls = ''.join(f'<url><loc>https://{WEB}/{f if f != "index.html" else ""}</loc></url>' for f in pages if f != '404.html')
(ROOT / 'sitemap.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>', encoding='utf-8')
(ROOT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: https://{WEB}/sitemap.xml\n', encoding='utf-8')
print(f'Built {len(pages)} pages')
