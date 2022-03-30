import random
import time
import os





escolhaComputador = random.randint(1,10)


while True:
    valorUsuario = int(input("Qual o número?: "))
    if valorUsuario == escolhaComputador:
        print("você acertou, parabéns")
        exit()
    if valorUsuario < escolhaComputador:
        print("Maior, tente de novo")
        time.sleep(3)
        os.system("cls")
    if valorUsuario > escolhaComputador:
        print("Menor, tente de novo")
        time.sleep(3)
        os.system("cls")