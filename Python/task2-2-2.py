import simplecrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

with open('passwords.txt') as inp:
    for line in inp:
        pwd = line.strip()
        try:
            print(simplecrypt.decrypt(pwd,encrypted).decode('utf8'))
        except simplecrypt.DecryptionException:
            print('Bad password: '+pwd)
        