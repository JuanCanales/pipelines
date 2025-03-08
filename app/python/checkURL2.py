import urllib.request

# URL que quieres consultar
url = 'http://example.com'

# Haciendo la solicitud GET
response = urllib.request.urlopen(url)

# Leyendo la respuesta y decodificándola
html = response.read().decode('utf-8')

# Mostrando el contenido
print(html)

# Si quieres obtener solo el código de estado HTTP
print(f"Código de estado: {response.getcode()}")
