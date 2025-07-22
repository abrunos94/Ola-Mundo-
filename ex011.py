# Exercicio de conversão de Real para Dolar
# US$ 1,00 = R$5,58 (22/07/2025)
n1 = float(input("Digite o valor em Real que deseja converter:R$"))
d =  5.58
print(" Convertendo R${}, voce vai ter U${:.2f} na cotação de hoje" .format(n1, (n1/d)))