# pip install pywhatkit
# https://www.askpython.com/python-modules/python-pip
# https://www.google.com.pe/search?q=python+enviar+mensajes+whatsapp&source=hp&ei=mTYaZIvbJYnT1sQPwvK9-AU&iflsig=AK50M_UAAAAAZBpEqYrPMFJuMA-Ky3VD59sQOp5DwfCz&oq=python+enviar+mensaje+a+whatsapp&gs_lcp=Cgdnd3Mtd2l6EAMYADIGCAAQFhAeOgsILhCABBDHARDRAzoFCAAQgAQ6BQguEIAEOggILhCABBDUAjoOCC4QgAQQxwEQrwEQ1AI6CAgAEIAEEMkDOgcIABCABBATOggIABAWEB4QCjoICAAQFhAeEBM6BQghEKABOggIIRAWEB4QHVAAWMB6YOiCAWgecAB4AoAB0QGIAfMukgEHNDcuMTYuMZgBAKABAbABAA&sclient=gws-wiz#fpstate=ive&vld=cid:fbb26c29,vid:5tgsM9XrjRY,st:9

import pywhatkit

try:
    pywhatkit.sendwhatmsg("+51940696481", "HOLA NENA",20,19)
    print("Abriendo... Escanee codigo QR")
    print("Enviado exitosamente")

except:
    print("No se pudo encontrar")

