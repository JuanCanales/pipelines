import urllib.request
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuración del correo
def enviar_email(remitente, destinatario, asunto, mensaje):
    try:
        # Servidor SMTP de Gmail
        servidor_smtp = "in-v3.mailjet.com"
        puerto_smtp = 587

        # Crear el mensaje
        msg = MIMEMultipart()
        msg["From"] = remitente
        msg["To"] = destinatario
        msg["Subject"] = asunto

        # Agregar cuerpo del mensaje
        cuerpo = MIMEText(mensaje, "plain")
        msg.attach(cuerpo)

        # Conectar al servidor SMTP
        with smtplib.SMTP(servidor_smtp, puerto_smtp) as servidor:
            servidor.starttls()  # Iniciar la conexión segura
            servidor.login(remitente, contraseña)  # Iniciar sesión
            servidor.send_message(msg)  # Enviar mensaje

        print("Correo enviado correctamente.")

    except Exception as e:
        print(f"Error al enviar el correo: {e}")




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

    status = response.getcode()
    # Si quieres obtener solo el código de estado HTTP
    print(f"HTTP status code: {status}")

    if status == 200:
        print(f"URL UP")
    else:
         print(f"URL DOWN  ( {status} )"
        # Datos para enviar el correo
        remitente = "juanluiscc@gmail.com"
        destinatario = "juanluiscc@gmail.com"
        asunto = "URL Down"
        mensaje = "URL DOWN  ( {status} )"
        contraseña = "50b7e929159b0ac52e58e0d63ad3c17a"
        

        # Llamar a la función para enviar el correo
        enviar_email(remitente, destinatario, asunto, mensaje, contraseña)

else:
    print("Not received url.")


