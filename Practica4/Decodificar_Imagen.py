import base64
# DECODIFICAR IMAGEN 1
with open('mystery_img1.txt','r') as texto:
    leer = texto.read() 
texto.close()
decodificar = leer.encode('utf8')
with open('mistery_img1.png','wb') as file_to_save:
    decoded_image_data = base64.decodebytes(decodificar)
    file_to_save.write(decoded_image_data)
# DECODIFICAR IMAGEN 2
with open('mystery_img2.txt','r') as texto2:
    leer2 = texto2.read() 
texto2.close()
decodificar2 = leer2.encode('utf8')
with open('mistery_img2.png','wb') as file_to_save2:
    decoded_image_data2= base64.decodebytes(decodificar2)
    file_to_save2.write(decoded_image_data2)