# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
n = str(input(' Digite seu nome completo:')).strip()
nome = n.split()
print(' É um prazer conhecer você!')
print(' Seu primeiro nome é {}.'.format(nome[0]))
print(' seu ultimo nome é {}.' .format(nome[len(nome)-1]))