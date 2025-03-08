import urllib.request
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Argumentos de este script : URL + APIKEY + SECRETKEY
# APIKEY y SECRETKEY del smtp server

# URL de test error : https://auth.hostinger.com/dksldfls

# Configuración del correo
def enviar_email(origen, destinatario, asunto, mensaje, APIKEY, SECRETKEY):
    try:
        # Servidor SMTP de Gmail
        servidor_smtp = "in-v3.mailjet.com"
        puerto_smtp = 587

        # Crear el mensaje
        msg = MIMEMultipart()
        msg["From"] = origen
        msg["To"] = destinatario
        msg["Subject"] = asunto

        # Agregar cuerpo del mensaje
        cuerpo = MIMEText(mensaje, "plain")
        msg.attach(cuerpo)

        # Conectar al servidor SMTP
        with smtplib.SMTP(servidor_smtp, puerto_smtp) as servidor:
            servidor.starttls()  # Iniciar la conexión segura
            servidor.login(APIKEY, SECRETKEY)  # Iniciar sesión
            servidor.send_message(msg)  # Enviar mensaje

        print("Correo enviado correctamente.")

    except Exception as e:
        print(f"Error al enviar el correo: {e}")



def main():
    print("Programa principal.")

    # Verificar si se pasaron los parametros
    print(f"Parameters received :  {sys.argv}")
    if len(sys.argv) > 3:
        url = sys.argv[1]
        print(f"URL to be checked: {url}")
    
        APIKEY = sys.argv[2]
        SECRETKEY = sys.argv[3]
        origen = "juanluiscc@gmail.com"
        try:
            # Haciendo la solicitud GET
            print("Url open... ")
            response = urllib.request.urlopen(url)
    
            # Leyendo la respuesta y decodificándola
            print("Reading response... ")
            html = response.read().decode('utf-8')
    
            # Mostrando el contenido
            print(html)
    
            status = response.getcode()
            # Si quieres obtener solo el código de estado HTTP
            print(f"HTTP status code: {status}")
    
            if status == 200:
                print(f"URL UP")
            else:
                print(f"URL DOWN  ( {status} )")
            
                # Datos para enviar el correo
                destinatario = "juanluiscc@gmail.com"
                asunto = "URL Down"
                mensaje = "URL DOWN  ( URL :{url} )"
            
            
    
                # Llamar a la función para enviar el correo
                print("Sending email... ")
                enviar_email(origen, destinatario, asunto, mensaje, APIKEY, SECRETKEY)
                
        except Exception as e:
            print(f"Error getting the URL: {e}")
    
            # Datos para enviar el correo
            destinatario = "juanluiscc@gmail.com"
            asunto = "URL Down"
            mensaje = "URL DOWN  ( URL :{url}   HTTP Status :{status} )"
            
            # Llamar a la función para enviar el correo
            enviar_email(origen, destinatario, asunto, mensaje, APIKEY, SECRETKEY)
    else:
        print("Not received url.")



if __name__ == "__main__":
    main()

