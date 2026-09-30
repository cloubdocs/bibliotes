import json, pathlib, re, shutil

master_path = pathlib.Path("alfabeto/A/abel-sanchez/index.html")
master = master_path.read_text(encoding="utf-8")
libros = json.loads(pathlib.Path("libros-A.json").read_text(encoding="utf-8"))

# portada base para que no se vea roto hasta que subas las IA
base_img = pathlib.Path("assets/portadas/A/abel-sanchez.webp")

for libro in libros:
    if libro["slug"] == "abel-sanchez":
        continue
    
    dest = pathlib.Path(f"alfabeto/A/{libro['slug']}/index.html")
    dest.parent.mkdir(parents=True, exist_ok=True)
    
    html = master
    
    # 1. Título - reemplaza todos los "Abel Sanchez"
    html = html.replace("Abel Sanchez", libro["titulo"])
    
    # 2. Imagen de portada
    html = html.replace("abel-sanchez.webp", libro["imagen"])
    
    # 3. Autor - reemplaza el autor de Abel que está en la plantilla
    html = html.replace("Miguel de Unamuno", libro["autor"])
    
    # 4. Reseña - reemplaza el párrafo largo de la reseña (el primer <p> largo dentro del main)
    # Busca la reseña actual de Abel en la plantilla y la cambia por la del JSON
    html = re.sub(
        r'<p[^>]*>[^<]*Una (?:novela|historia) de[^<]{20,}?</p>',
        f'<p>{libro["resena"]}</p>',
        html,
        count=1,
        flags=re.DOTALL
    )
    # fallback si no encontró el patrón anterior
    if libro["resena"] not in html:
        html = re.sub(
            r'(<h1[^>]*>.*?</h1>.*?<p[^>]*>)([^<]{30,}?)(</p>)',
            rf'\1{libro["resena"]}\3',
            html,
            count=1,
            flags=re.DOTALL
        )
    
    # 5. Drive ID - reemplaza cualquier PEGA_AQUI_ID...
    html = re.sub(r'PEGA_AQUI_ID_[A-Z0-9_]+', libro["drive_id"], html)
    
    dest.write_text(html, encoding="utf-8")
    print(f"✓ {libro['slug']}")

    # crea portada placeholder si no existe
    dest_img = pathlib.Path(f"assets/portadas/A/{libro['imagen']}")
    if not dest_img.exists() and base_img.exists():
        shutil.copy(base_img, dest_img)
        print(f"  - placeholder portada {libro['imagen']}")

print("\nListo. 9 carpetas reales:")
