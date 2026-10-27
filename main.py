from blog.datos import cargar_posts, guardar_posts
from blog.modelos import Blog
from blog.menu import mostrar_menu 

def main():
    mi_blog = Blog()
    mi_blog.posts = cargar_posts() or []
    mostrar_menu(mi_blog)
    guardar_posts(mi_blog.posts)

    
if __name__ == "__main__":
    main() 