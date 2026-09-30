import pathlib, re

LEYENDA = "Biblioteca Electrónica El Salvador"

HEADER = f"""<header style="background:#dbeafe; padding:22px 20px;">
  <div style="max-width:1000px; margin:0 auto; display:flex; align-items:center; justify-content:center; gap:20px;">
    <img src="/bibliotes/img/robot_4_libros_gris.png" alt="robot" style="height:70px; width:auto; flex-shrink:0;">
    <div style="text-align:left;">
      <h1 style="font-family: Georgia, serif; font-size:44px; margin:0; color:#1e3a8a; line-height:1;">Bibliot<span style="background:#1e40af; color:white; padding:2px 10px; border-radius:8px; margin-left:2px;">es</span></h1>
      <p style="margin:6px 0 0 0; font-weight:700; font-size:16px; color:#334155; font-family: system-ui, sans-serif;">{LEYENDA}</p>
    </div>
  </div>
</header>"""

for path in pathlib.Path("alfabeto/A").glob("*/index.html"):
    html = path.read_text(encoding="utf-8")
    html = re.sub(r'<header.*?</header>', HEADER, html, count=1, flags=re.DOTALL | re.IGNORECASE)
    path.write_text(html, encoding="utf-8")
    print(f"✓ {path.parent.name} -> {LEYENDA} centrado")

