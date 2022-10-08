import base64
try:
    archivo_lectura = open('hola_mundo.c','r')
    archivo_escritura = open('hola_mundo_codificado.c','w')
    texto_sin_codificar = archivo_lectura.read()
    texto_codificado = base64.b64encode(bytes(texto_sin_codificar,'UTF-8'))
    archivo_escritura.write(str(texto_codificado))
    print('*************************************************************************************')
    print('El archivo ha sido decodificado con exito :)')
    print('*************************************************************************************')
except:
    print("El archivo no ha podido ser codificado :'(")