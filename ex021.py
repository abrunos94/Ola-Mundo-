# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
n1 = input(" Primeiro aluno: ")
n2 = input(" Segundo aluno: ")
n3 = input(" Terceiro aluno: ")
n4 = input(" Quarto   aluno: ")
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(" A ordem de apresentação sera:")
print(lista)
# O shuffle emparalha a lista de forma aleatorica.