import instaloader
import requests
loader = instaloader.Instaloader()
loader.context.login("usernameInstagramAqui", "Contraseña")

API_URL = 'http://localhost:5000/data-analyzer'

# users
userPublic = 'denxcxrx'
userAlone = 'danteyahir' 
userPrivate = 'briss'

try:
    profile = instaloader.Profile.from_username(loader.context, userPublic)

    data_collected = {
        "nombrePersona": profile.username,
        "biografiaPersona": profile.biography,
        "seguidores": profile.followers,
        "siguiendo": profile.followees,
        "publicaciones": []
    }

    MAX_POSTS = 7
    for post in profile.get_posts():
        if len(data_collected["publicaciones"]) >= MAX_POSTS:
            break
        post_data = {
            "descripcionPost": post.caption,
            "hashtags": post.caption_hashtags,
            "amigosMencionados": [loader.check_profile_id(tag).username for tag in post.tagged_users]
        }
        data_collected["publicaciones"].append(post_data)
    
    response = requests.post(API_URL, json=data_collected)

    if response.status_code == 200:
        print("Datos enviados exitosamente a la API.")
    else:
        print("Error al enviar los datos a la API:", response.text)

except instaloader.exceptions.ProfileNotExistsException:
    print("El perfil especificado no existe.")
except instaloader.exceptions.QueryReturnedNotFoundException as e:
    print(f"Error al obtener publicaciones: {e}")
