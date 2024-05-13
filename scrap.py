import instaloader
import requests
import random

API_URL = 'http://localhost:5000/data-analyzer'

# Función para leer proxies desde un archivo de texto
def read_proxies_from_file(filename):
    with open(filename) as f:
        proxies = f.read().splitlines()
    return proxies

# Función para realizar una solicitud utilizando un proxy aleatorio
def make_request_with_proxy(url, proxies):
    # Seleccionar un proxy aleatorio de la lista
    proxy = random.choice(proxies)
    try:
        # Realizar la solicitud utilizando el proxy seleccionado
        response = requests.get(url, proxies={"http": proxy, "https": proxy})
        return response
    except Exception as e:
        print("Error al hacer la solicitud:", e)
        return None

# Usuarios de Instagram
userPublic = 'mentesprogramadoras'
userPrivate = 'brissita7'
userAlone = 'danteyahir'

# Archivo de proxies
proxy_file = 'valid_proxies.txt'

# Leer proxies desde el archivo
proxies = read_proxies_from_file(proxy_file)

# Crear instancia de Instaloader
loader = instaloader.Instaloader()

try:
    # Obtener perfil de usuario
    profile = instaloader.Profile.from_username(loader.context, userPublic)

    data_collected = {
        "nombrePersona": profile.username,
        "biografiaPersona": profile.biography,
        "seguidores": profile.followers,
        "siguiendo": profile.followees,
        "publicaciones": []
    }

    # Límite de publicaciones
    MAX_POSTS = 4

    # Obtener publicaciones del perfil
    for post in profile.get_posts():
        if len(data_collected["publicaciones"]) >= MAX_POSTS:
            break
        post_data = {
            "descripcionPost": post.caption,
            "hashtags": post.caption_hashtags,
            "amigosMencionados": [loader.check_profile_id(tag).username for tag in post.tagged_users]
        }
        data_collected["publicaciones"].append(post_data)
    
    # Realizar solicitud a la API utilizando un proxy aleatorio
    response = make_request_with_proxy(API_URL, proxies)

    if response and response.status_code == 200:
        print("Datos enviados exitosamente a la API.")
    else:
        print("Error al enviar los datos a la API:", response.text)

except instaloader.exceptions.ProfileNotExistsException:
    print("El perfil especificado no existe.")
except instaloader.exceptions.QueryReturnedNotFoundException as e:
    print(f"Error al obtener publicaciones: {e}")
