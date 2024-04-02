import random

characters = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQSRTUVWXYZ0123456789!#$%&/()=-_[]"

n = int(input("Ingrese el número de caracteres que quiere en su contraseña:"))
password = ""

for i in range(n):
    password += random.choice(characters)

print(password)

end = input("Presione cualquier tecla para terminar (Pulse enter):")