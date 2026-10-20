def mostrar_menu(blog):
    while True:
        print("\n--- MENU DEL BLOG ---")
        print("1. Ver todos los posts")
        print("2. Buscar por titulo")
        print("3. Filtrar por tag")
        print("4. Salir")

        opcion = input("Elegi una opcion (1-4): ")

        if opcion == "1":
            blog.listar_posts()
        elif opcion == "2":
            titulo = input("Ingresá el título a buscar: ")
            resultados = blog.buscar_por_titulo(titulo)
            if resultados:
                for p in resultados:
                    print(f"[{p.id}] {p.titulo} - Autor: {p.autor.nombre}")
            else:
                print("No se encontraron posts con ese título.")
        elif opcion == "3":
            tag = input("Ingresá el tag a buscar: ")
            resultados = blog.filtrar_por_tag(tag)
            if resultados:
                for p in resultados:
                    print(f"[{p.id}] {p.titulo} - Tags: {p.tags}")
            else:
                print("No se encontraron posts con ese tag.")
        elif opcion == "4":
            print("\n¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intentá de nuevo.")

    

      

       