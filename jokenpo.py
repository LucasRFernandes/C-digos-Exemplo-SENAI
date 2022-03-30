import random # Importando a Lib de comandos de aleatoriedade

escolhas = [
    "pedra",
    "papel",
    "tesoura"
]


escolhaComputador = random.choice(escolhas)
escolhaJogador = input("Faça sua escolha: ")

# escolhas onde o computador ganha
if escolhaComputador == "pedra":
    if escolhaJogador == "tesoura":
        print("O Computador escolheu Pedra, e você tesoura, Você perdeu")

if escolhaComputador == "papel":
    if escolhaJogador == "pedra":
        print("O Computador escolheu Papel e você pedra, Você perdeu")

if escolhaComputador == "tesoura":
    if escolhaJogador == "papel":
        print("O Computador escolheu Tesoura e você Papel, Você perdeu")

# Escolhas onde o Jogador ganha

if escolhaJogador == 'pedra':
    if escolhaComputador == 'tesoura':
        print("O Computador escolheu Tesoura, e você pedra, Você Ganhou!")

if escolhaJogador == 'papel':
    if escolhaComputador == 'pedra':
        print("O Computador escolheu Pedra, e você Papel, Você Ganhou!")

if escolhaJogador == 'tesoura':
    if escolhaComputador == 'papel':
        print("O Computador escolheu papel, e você Tesoura, Você Ganhou!")

# Escolhas que dão empate
if escolhaJogador == 'papel':
    if escolhaComputador == 'papel':
        print("Os dois escolheram Papel, Empate!")

if escolhaJogador == 'pedra':
    if escolhaComputador == 'pedra':
        print("Os dois escolheram Pedra, Empate!")

if escolhaJogador == 'tesoura':
    if escolhaComputador == 'tesoura':
        print("Os dois escolheram Tesoura, Empate!")










