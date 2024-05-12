import instaloader
import requests

API_URL = 'http://localhost:5000/data-analyzer'

loader = instaloader.Instaloader()
username = 'hiram.dev'

try:
    profile = instaloader.Profile.from_username(loader.context, username)

    data_collected = {
        "nombrePersona": profile.username,
        "biografiaPersona": profile.biography,
        "seguidores": profile.followers,
        "siguiendo": profile.followees,
        "publicaciones": []
    }

    for post in profile.get_posts():
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
except instaloader.exceptions.ConnectionException:
    print("Error de conexión. Por favor, verifica tu conexión a internet.")
