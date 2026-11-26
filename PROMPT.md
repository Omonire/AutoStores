# AutoStore landing-page prompt

Use the prompt below with an AI designer, coding assistant, or image generator when you need to recreate or extend the AutoStore landing page.

```text
Create a polished, responsive landing page for AutoStore, a web-based online marketplace that connects students, individual sellers, store owners and buyers.

Business context:
AutoStore is similar to Jiji.ng. Sellers list products with images, descriptions, prices and categories. Buyers browse, search, filter, view product details, see seller information and contact sellers to enquire or buy. The MVP does NOT include in-app payments, delivery tracking, reviews, ratings or a mobile app.

Target users:
1. Students selling textbooks, phones, laptops, clothes, shoes, bags, furniture and hostel belongings.
2. Store owners such as fashion, electronics, food and beauty vendors.
3. Buyers who want to discover products without visiting multiple stores or relying on WhatsApp statuses and word of mouth.

Core value proposition:
"Making it easier for people to sell what they have and find what you need."

Tone and visual direction:
- Clean, modern, trustworthy and approachable.
- Marketplace energy: bold headline, obvious search bar, clear calls to action.
- Primary colour: warm Jiji-like orange (#F68B1E), with deep ink (#171717), cream (#FFF8F1) and white surfaces.
- Friendly but not playful; no childish illustrations or emojis.
- Use generous whitespace, rounded cards, subtle shadows and strong typography.

Required page sections:
1. Sticky header with AutoStore logo, links to How it works, Categories, About, and a "Start selling" CTA.
2. Hero: headline "Sell what you have. Find what you need.", supporting copy, a prominent product search bar, quick category tags, and two buttons: "Browse listings" and "Start selling".
3. Proof strip with simple stats for the three seller/buyer groups and MVP scope.
4. Problem section explaining that buying and selling currently depends on WhatsApp, groups and word of mouth.
5. Categories grid: Textbooks, Phones & Tech, Fashion, Furniture, Beauty, Food.
6. How it works: seller registers, uploads a product, buyer discovers it, buyer contacts seller, both agree on payment and pickup/delivery.
7. Audience section with three cards: Students, Store owners, Buyers.
8. Sample listing card showing product title, price, seller name, condition badge and "Contact seller" button.
9. Closing CTA: "Your next sale is one listing away." with a "Create a listing" button.
10. Footer with product name, category, target audience and MVP note.

Technical constraints:
- Implement as a Flask/Jinja template in templates/index.html using the shared base.html layout.
- Let FSCSS own the entire visual system in static/src/style.fscss, compiled by build.py into public/style.css for local serving and Vercel CDN delivery.
- Use semantic component classes in templates (for example hero-inner, listing-card, premium-card, flow-card) instead of utility classes.
- Do not load Tailwind or any other CSS framework.
- Use the vanilla Motion CDN script from static/js/main.js for Framer-style intro, scroll reveal, counters, parallax, tilt and magnetic buttons; do not add React.
- Keep all icons and product visuals as CSS shapes, letters or inline SVG; do not depend on external image URLs.
- Fully responsive from 320px upward.
- Accessible: semantic headings, labelled form input, visible focus states, sufficient colour contrast.
- Respect prefers-reduced-motion for all decorative movement.

Visual upgrade direction:
- Bright marketplace luxe: cream canvas, white surfaces, oversized Playfair Display headline, crisp Manrope body copy, gold-orange gradient accents.
- Peak premium feel: generous whitespace, frosted glass chips, layered shadows, 3D tilt on cards, subtle shimmer, and a warm gold closing CTA.
- Avoid childish illustrations, emojis and dense boilerplate layouts.

Deliverable:
Return a production-ready index.html, base.html, style.fscss and main.js that match this brief, plus a short note listing the sections built.
```
