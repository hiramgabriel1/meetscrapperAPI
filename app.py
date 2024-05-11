import instaloader

def scrape_instagram_profile(username):
    # Crea una instancia de Instaloader
    L = instaloader.Instaloader()

    try:
        # Obtén el perfil de Instagram
        profile = instaloader.Profile.from_username(L.context, username)

        # Imprime la información del perfil
        print(f"Username: {profile.username}")
        print(f"Biografía: {profile.biography}")
        print(f"Seguidores: {profile.followers}")
        print(f"Siguiendo: {profile.followees}")

        # Imprime las descripciones, etiquetados y hashtags de las publicaciones
        print("Publicaciones:")
        for post in profile.get_posts():
            print("- Descripción:", post.caption)
            print("- Etiquetados:", [tagged_user.username for tagged_user in post.tagged_users])
            print("- Hashtags:", [hashtag for hashtag in post.caption_hashtags])

    except Exception as e:
        print(f"Error al obtener el perfil de Instagram: {e}")

# Solicitar al usuario el nombre de usuario del perfil que desea scrapear
username_to_scrape = input("Ingrese el nombre de usuario del perfil que desea scrapear: ")

# Llama a la función de scrapping con el nombre de usuario especificado
scrape_instagram_profile(username_to_scrape)
