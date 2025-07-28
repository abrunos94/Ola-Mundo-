# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
numero =  int(input(' Me diga um numero qulaquer: '))
resultado = numero % 2
if resultado == 0:
    print(' o numero {} é Par.' .format(numero))
else:
    print('o numnero {} é IMPAR. ' .format(numero))