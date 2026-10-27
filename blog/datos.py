
import json
import os
from blog.modelos import Autor, Post

RUTA_ARCHIVO = "posts.json"


def cargar_posts():
  def cargar_posts():
    """Lee el JSON (diccionarios) y lo convierte en una lista de OBJETOS Post"""
    if not os.path.exists(RUTA_ARCHIVO):
        return []

    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        posts_cargados = []
        for item in datos:
            # Convertimos el autor
            datos_autor = item.get("autor", {})
            if isinstance(datos_autor, dict):
                autor_obj = Autor(
                    nombre=datos_autor.get("nombre", "Anónimo"),
                    bio=datos_autor.get("bio", ""),
                    especialidad=datos_autor.get("especialidad", ""),
                    redes_sociales=datos_autor.get("redes_sociales", {})
                )
            else:
                autor_obj = Autor(nombre=str(datos_autor))

            # Reconstruimos el objeto Post
            post_obj = Post(
                id=item.get("id"),
                titulo=item.get("titulo", ""),
                contenido=item.get("contenido", ""),
                autor=autor_obj,
                tags=item.get("tags", []),
                estado=item.get("estado", "publicado")
            )
            posts_cargados.append(post_obj)

        return posts_cargados

    except Exception as e:
        print(f"Error al cargar posts desde JSON: {e}")
        return []


def guardar_posts(lista_posts):
    """Toma una lista de OBJETOS Post, los convierte a DICCIONARIOS y los guarda en el JSON."""
    try:
        lista_diccionarios = [post.a_diccionario() for post in lista_posts]

        with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
            json.dump(lista_diccionarios, archivo, indent=4, ensure_ascii=False)
            
        return True
    except Exception as e:
        print(f"Error al guardar en JSON: {e}")
        return False
      
