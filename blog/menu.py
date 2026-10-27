from blog.modelos import Autor, Post
from blog.datos import guardar_posts
def mostrar_menu(blog):
    while True:
        print("\n--- MENU DEL BLOG ---")
        print("1. Ver todos los posts")
        print("2. Buscar por titulo")
        print("3. Crear post")
        print("4. Filtrar por tag")
        print("5. Salir")

        opcion = input("Elegi una opcion (1-5): ")

        if opcion == "1":
            blog.listar_posts()
        elif opcion == "2":
            titulo = input("Ingresá el titulo a buscar: ")
            resultados = blog.buscar_por_titulo(titulo)
            if resultados:
                for p in resultados:
                    print(f"[{p.id}] {p.titulo} - Autor: {p.autor.nombre}")
            else:
                print("No se encontraron posts con ese titulo.")
        elif opcion == "3":
            titulo = input("Título del post: ")
            contenido = input("Contenido: ")
            tags_input = input("Tags (separados por comas): ")
            tags = [tag.strip() for tag in tags_input.split(",")]
            
            nombre_autor = input("Nombre del autor: ")
            especialidad = input("Especialidad del autor: ")
            redes_sociales = input("Redes sociales del autor: ")
            
            nuevo_autor = Autor(nombre=nombre_autor, especialidad=especialidad, redes_sociales={"red": redes_sociales})
            nuevo_id = len(blog.posts) if blog.posts else 1
            nuevo_post = Post(id=nuevo_id, titulo=titulo, contenido=contenido, autor=nuevo_autor, tags=tags)
            
       
            if blog.crear_post(nuevo_post):
                guardar_posts(blog.posts)
                print("¡Post creado y guardado exitosamente!")
            else:
                print("Error: El post no pasó la validación.")
            print("Post creado exitosamente.")
        elif opcion == "4":
            tag = input("Ingresá el tag a buscar: ")
            resultados = blog.filtrar_por_tag(tag)
            if resultados:
                for p in resultados:
                    print(f"[{p.id}] {p.titulo} - Tags: {', '.join(p.tags)}")
            else:
                print("No se encontraron posts con ese tag.")
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, elegí una opción del 1 al 5.")