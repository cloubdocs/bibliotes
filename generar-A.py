import json, pathlib, re, shutil
master = pathlib.Path("alfabeto/A/abel-sanchez/index.html").read_text(encoding="utf-8")
libros = json.loads(pathlib.Path("libros-A.json").read_text(encoding="utf-8"))

for libro in libros:
    if libro["slug"] == "abel-sanchez":
        continue # este ya existe y está perfecto
    dest = pathlib.Path(f"alfabeto/A/{libro['slug']}/index.html")
    dest.parent.mkdir(parents=True, exist_ok=True)
    html = master
    # Reemplaza solo lo variable
    html = re.sub(r'<h1[^>]*>.*?</h1>', f'<h1 style="color:#1a4fb5; font-family:serif; font-size:38px; margin:0 0 8px 0;">{libro["titulo"]}</h1>', html, count=1, flags=re.DOTALL)
    # autor
    html = re.sub(r'Miguel de Unamuno', libro["autor"], html)
    # titulo en alt y textos
    html = html.replace("Abel Sanchez", libro["titulo"]).replace("abel-sanchez.webp", libro["imagen"])
    # reseña - reemplaza el <p> largo
    html = re.sub(r'Una novela sobre la amistad.*?\.', libro["resena"], html, count=1, flags=re.DOTALL)
    # drive_id y monetag
    html = html.replace("PEGA_AQUI_ID_ABEL", libro["drive_id"]).replace("PEGA_AQUI_ID_DE_ABEL", libro["drive_id"])
    dest.write_text(html, encoding="utf-8")
    print(f"Creada {dest}")

print("Listo. Ahora sube las portadas IA a assets/portadas/A/ con el mismo nombre que en el JSON")
