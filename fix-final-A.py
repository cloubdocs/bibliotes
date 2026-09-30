import json, pathlib, re

GENERIC = "Dominio Público y Contenido Abierto"

HEADER_BUENO = f"""<header style="background:#dbeafe; padding:22px 0; display:flex; justify-content:center;">
  <div style="display:flex; align-items:center; gap:20px;">
    <img src="/bibliotes/img/robot_4_libros_gris.png" alt="robot" style="height:70px; width:auto;">
    <div>
      <h1 style="font-family: Georgia, serif; font-size:44px; margin:0; color:#1e3a8a; line-height:1;">Bibliot<span style="background:#1e40af; color:white; padding:2px 10px; border-radius:8px; margin-left:2px;">es</span></h1>
      <p style="margin:6px 0 0 0; font-weight:700; font-size:16px; color:#334155; font-family: system-ui, sans-serif;">{GENERIC}</p>
    </div>
  </div>
</header>"""

libros = json.loads(pathlib.Path("libros-A.json").read_text(encoding="utf-8"))

for libro in libros:
    path = pathlib.Path(f"alfabeto/A/{libro['slug']}/index.html")
    html = path.read_text(encoding="utf-8")

    # 1. Reemplaza TODO el header malo por el bueno con mascota y negrita
    html = re.sub(r'<header.*?</header>', HEADER_BUENO, html, count=1, flags=re.DOTALL | re.IGNORECASE)

    # 2. Pone la reseña correcta en la ficha blanca
    html = re.sub(r'<p class="synopsis">.*?</p>', f'<p class="synopsis">{libro["resena"]}</p>', html, count=1, flags=re.DOTALL)

    path.write_text(html, encoding="utf-8")
    print(f"✓ {libro['slug']}")

