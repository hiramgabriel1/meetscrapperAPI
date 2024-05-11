import instaloader

loader = instaloader.Instaloader()
username = ''

try:
    profile = instaloader.Profile.from_username(loader.context, username)

    print("Nombre de usuario:", profile.username)
    print("Biografía:", profile.biography)
    print("Seguidores:", profile.followers)
    print("Siguiendo:", profile.followees)

    print("Información de las publicaciones:")
    print("Información de las publicaciones:")
    for post in profile.get_posts():
        print("Descripción:", post.caption)
        print("Hashtags:", post.caption_hashtags)
        print("Usuarios etiquetados:", post.tagged_users)

        for tag in post.tagged_users:
            print(tag)

except instaloader.exceptions.ProfileNotExistsException:
    print("El perfil especificado no existe.")
except instaloader.exceptions.ConnectionException:
    print("Error de conexión. Por favor, verifica tu conexión a internet.")
