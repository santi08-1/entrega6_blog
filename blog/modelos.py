class Autor:
    def __init__(self, nombre, bio="", especialidad="", redes_sociales=None):
        self.nombre = nombre
        self.bio = bio
        self.especialidad = especialidad
        self.redes_sociales = redes_sociales if redes_sociales is not None else {}

    def a_diccionario(self):
        return {
            "nombre": self.nombre,
            "bio": self.bio,
            "especialidad": self.especialidad,
            "redes_sociales": self.redes_sociales
        }


class Post:
    def __init__(self, id, titulo, contenido, autor, tags=None, estado="publicado"):
        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.tags = tags if tags is not None else []
        self.estado = estado

    def a_diccionario(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.a_diccionario(),
            "tags": self.tags,
            "estado": self.estado
        }


class Blog:
    def __init__(self):
        self.posts = []

    def crear_post(self, post):
        if self.validar_post(post):
            self.posts.append(post)
            return True
        return False

    def obtener_todos(self):
        return self.posts

    def listar_posts(self):
        if not self.posts:
            print("\nNo hay posts disponibles.")
            return

        print("\n--- PUBLICACIONES DEL BLOG ---")
        for p in self.posts:
            print(f"[{p.id}] {p.titulo} - Autor: {p.autor.nombre} - Estado: {p.estado}")

    def buscar_por_titulo(self, texto):
        return [p for p in self.posts if texto.lower() in p.titulo.lower()]

    def filtrar_por_tag(self, tag):
        return [p for p in self.posts if tag.lower() in [t.lower() for t in p.tags]]

    def validar_post(self, post):
        if not post.titulo or not post.contenido or not isinstance(post.autor, Autor):
            return False
        return True