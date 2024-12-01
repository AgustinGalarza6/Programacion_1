import bcrypt

'''

txt = input("Ingrese un texto: ")
pwd = txt.encode('utf-8')
salt = bcrypt.gensalt()
encript = bcrypt.hashpw(pwd, salt)
print(encript)

'''
pwd = b'$2b$12$qgb2310yzsZeOb6Kw7LQmu8HYTFonCnf415nnqDCGXF2DxKBqkjMi'
txt = bytes(input("Ingrese un texto: "), 'utf-8')

# Verificacion de contraseña encriptada.
while txt != pwd:
    if bcrypt.checkpw(txt, pwd):
        print("Encontraste la contraseña.")
        break
    else:
        print("No coincide.")
        txt = bytes(input("Ingrese un texto: "), 'utf-8')

