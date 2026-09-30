import json, pathlib, re

master_path = pathlib.Path("alfabeto/A/abel-sanchez/index.html")
master = master_path.read_text(encoding="utf-8")
libros = json.loads(pathlib.Path("libros-A.json").read_text(encoding="utf-8"))

# reseñas viejas que están pegadas en la plantilla y hay que reemplazar
OLD_RESENAS = [
    "Una novela sobre la amistad, la rivalidad y los celos que explora el conflicto interior de sus dos protagonistas a lo largo de sus vidas.",
    "Una historia de envidia y amistad entre Joaquin Monegro y Abel Sanchez a lo largo de su vida."
]

for libro in libros:
    if libro["slug"] == "abel-sanchez":
        continue
    
    dest = pathlib.Path(f"alfabeto/A/{libro['slug']}/index.html")
    html = master

    # 1. Titulo
    html = html.replace("Abel Sanchez", libro["titulo"])
    # 2. Imagen - solo el nombre
    html = html.replace("abel-sanchez.webp", libro["imagen"])
    # 3. Autor - el de la plantilla maestra es Unamuno
    html = html.replace("Miguel de Unamuno", libro["autor"])
    # 4. Drive ID
    html = re.sub(r'PEGA_AQUI_ID_[A-Z0-9_]+', libro["drive_id"], html)
    
    # 5. RESEÑA - reemplazo directo y a prueba de fallos
    for old in OLD_RESENAS:
        if old in html:
            html = html.replace(old, libro["resena"])
    
    # Si aún no se reemplazó, busca el primer <p> largo que sea la reseña
    if libro["resena"] not in html:
        html = re.sub(
            r'<p[^>]*>\s*Una (novela|historia) sobre.*?</p>',
            f'<p>{libro["resena"]}</p>',
            html,
            count=1,
            flags=re.DOTALL | re.IGNORECASE
        )

    dest.write_text(html, encoding="utf-8")
    print(f"✓ {libro['slug']} -> {libro['resena'][:40]}...")

print("\nReseñas arregladas")
