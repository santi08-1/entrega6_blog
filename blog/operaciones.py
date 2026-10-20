def listar_posts(lista):
    print("--- LISTA DE POSTS ---")
    for post in lista:
        titulo = post.get("titulo", "Sin título")
        autor = post.get("autor", {})
        nombre_autor = autor.get("nombre", "Sin autor")
        print(f"• Título: {titulo} | Autor: {nombre_autor}")


def buscar_por_titulo(lista, termino):
     print(f"--- RESULTADOS DE BÚSQUEDA PARA: '{termino}' ---")
     busqueda = termino.lower()

     for post in lista:
            titulo = post.get("titulo", "")
            if busqueda in titulo.lower() and titulo != "":
                autor = post.get("autor", {})
                nombre_autor = autor.get("nombre", "Sin autor")
                print(f"• Título: {titulo} | Autor: {nombre_autor}")

def filtrar_por_tag(lista, tag):
     print(f"--- FILTRANDO POSTS POR TAG: '{tag}' ---")
     busqueda = tag.lower()
     for post in lista:
      lista_tags = post.get("tags", [])
     for t in lista_tags:
            if busqueda == t.lower():
                titulo = post.get("titulo", "Sin título")
                autor = post.get("autor", {})
                nombre = autor.get("nombre", "Sin autor")
                print(f"• Título: {titulo} | Autor: {nombre}")
                break