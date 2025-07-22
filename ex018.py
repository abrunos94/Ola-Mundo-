# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenus
from math import hypot
co = float(input("Comprimento do cateto oposto:"))
ca = float(input("Comprimento do cateto adjacente:"))
#hip = (co ** 2 + ca ** 2) ** (1/2) -Essa é uma opçao sem importaçao
hip = hypot(co, ca)
print("A hipotenusa vai medir {:.2f}" .format(hip))