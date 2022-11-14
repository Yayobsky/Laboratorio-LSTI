import smtplib
import ssl
import getpass
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# OBTENER LOS DATOS PRINCIPALES PARA EL CORREO
recibir = input('Intorduzca el correo del remitente: ')
enviar = input('Introduzca el correo del emisor: ')
contraseña = getpass.getpass('Intorduzca su contraseña: ')
asunto = input('Asunto del correo: ')
cuerpo = input('Cuerpo del correo: ')
meme = input('Intorduzca la dirección del archivo: ')
nombre = input('Introduzca su nombre: ')

#CONSTRUCCIÓN DEL CORREO
correo = MIMEMultipart('alternartive')
correo['Subject'] = asunto
correo['From'] = enviar
correo['To'] = recibir

#CREACION DEL HTML
html ="""
<html>
<body>
    <b>Practica 12 - Envio de correos con Python</b><br>
    {}<br>
    <b>Correo enviado por: </b> {} <br>
<body>
</html>
""".format(cuerpo, nombre)

correo_HTML = MIMEText(html, 'html')
correo.attach(correo_HTML)

#AÑADIMOS LA IMAGEN
with open(meme, 'rb') as adjunto:
    contenido =MIMEBase("application", "octet-stream")
    contenido.set_payload(adjunto.read())
encoders.encode_base64(contenido)
contenido.add_header("Content-Disposition",f"attachment; filename= {meme}",)
correo.attach(contenido)
correo_completo = correo.as_string()

context = ssl.create_default_context()
with smtplib.SMTP('smtp.outlook.com', 587) as conn:
    conn.starttls(context=context)
    conn.login(enviar, contraseña)
    print("Sesión iniciada")
    conn.sendmail(enviar,recibir, correo_completo)
    print("Mensaje enviado")