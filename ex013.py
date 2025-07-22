# Exercio que lé o preço de um produto e aplica um desconto de 5%
p = float(input("Qual o preço desse produto?R$"))
novo = p - (p * 5 / 100)
print(" O preço com desconto de 5% é R${}".format(novo))
