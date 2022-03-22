
# importei a biblioteca random para poder usar seus comandos
# de aleatoriedade no código.
import random

listaDeNomes = [

]

# Essa função adiciona nomes na array ListaDeNomes[]
def adicionarnomes():
    nome = input("digite um nome: ")
    listaDeNomes.append(nome)

# Aqui eu pergunto quantos nomes quero adicionar na lista, e executo 
# a função adicionarnomes() esse determinado número de vezes.
numero = int(input("Quantos nomes deseja adicionar: "))
for i in range(numero):
    adicionarnomes()


# Aqui eu uso o comando que queria da biblioteca random que importei
# na primeira linha do código!
escolhaPC = random.choice(listaDeNomes) # esse comando seleciona um objeto aleatorio dentro da lista/array que eu passar como parâmetro 
print("O Ganhador é", escolhaPC)




