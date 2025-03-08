import urllib.request
import sys

# Verificar si se pasó el parámetro
if len(sys.argv) > 1:
    url = sys.argv[1]
    print(f"URL to be checked: {url}")

    # Haciendo la solicitud GET
    response = urllib.request.urlopen(url)

    # Leyendo la respuesta y decodificándola
    html = response.read().decode('utf-8')

    # Mostrando el contenido
    print(html)

    # Si quieres obtener solo el código de estado HTTP
    print(f"HTTP status code: {response.getcode()}")

else:
    print("Not received url.")


