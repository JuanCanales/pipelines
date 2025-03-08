# pipelines
examples of pipelines with github actions

- Dockerfile.1 : openjdk + debian + python
- Dockerfile.2 : debian

- checkURL : Arranca un runner de ubuntu, donde se instala python, y ejecuta un script de python para chequear la URL que se le pasa como parametro (parametro que se pide al lanzarlo manualmente). Y si la URL responde con un status <> 200, envia un email.

