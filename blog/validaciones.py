def validar_post(post):
     if type(post) != dict:
          return False 
     if "titulo" not in post:
        return False
     if "contenido" not in post:
        return False
     if "autor" not in post:
        return False
     if "tags" not in post:
        return False
     if "estado" not in post:
        return False
     if post["titulo"] == "":
        return False
     if post["contenido"] == "":
        return False
     if type(post["autor"]) != dict:
        return False
     if "nombre" not in post["autor"]:
        return False
     if type(post["tags"]) != list:
        return False
     estados_validos = ["borrador", "publicado", "archivado"]
     if post["estado"] not in estados_validos:
        return False
     return True