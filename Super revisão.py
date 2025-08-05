# SUPER REVISÃO - PYTHON MUNDO 1


# Neste projeto será demonstrado e explicado as principais funções.
# Serão mostradas linhas de código (basta remover o "#" dos comentários para executar)

# ---------------------------------------------------------
# MÓDULO 1 - Entrada e saída de variáveis:
# ---------------------------------------------------------

#nome =  input('Qual seu nome? ')
#idade = input('Quantos anos você tem? ')

# Duas formas de formatar strings:
# print('Olá {}! Você tem {} anos!'.format(nome, idade))
# print(f'Olá {nome}! Você tem {idade} anos!')

# EXEMPLO:
# Entrada: nome = Alex, idade = 30
# Saída: Olá Alex! Você tem 30 anos!

# ---------------------------------------------------------
# MÓDULO 2 - Tipos Primitivos e Conversão de Tipos
# ---------------------------------------------------------
# Tipos primitivos, segue abaixo alguns exemplos de primitivos:
# int: numeros inteiros ( 10, -4);
# float: numeros com casas decimais (3.14, 9.8888....)
# str : texto ou caracteres ("texto")
# boll : valores boleanos ( logico), (True, False)
# Exemplo:
#idade = int(input(' Quantos anos voce tem? ')) # int mostra que o numero é inteiro.
#altura = float(input(' Qual sua altura? ')) # float aqui pede numeres decimais
#str(print(' Seu nome é {}, voce tem {}, e sua altura é {}.' .format(nome, idade, altura)))
#str(print(f'Seu nome é {nome}, voce tem {idade} e sua altura é {altura}'))

# ---------------------------------------------------------
# Módulo 3 — Operadores Aritméticos
# ---------------------------------------------------------
#Aprederemos agora como funciona os operadores aritmetico e como ele spodem nos ajudar!
#| Operador | Função           | Exemplo  | Resultado |
#| -------- | ---------------- | -------- | --------- |
#| `+`      | Adição           | `2 + 3`  | `5`       |
#| `-`      | Subtração        | `5 - 2`  | `3`       |
#| `*`      | Multiplicação    | `4 * 2`  | `8`       |
#| `/`      | Divisão real     | `7 / 2`  | `3.5`     | A divisão / sempre retorna float (número com ponto).
#| `//`     | Divisão inteira  | `7 // 2` | `3`       | O operador // ignora as casas decimais (divisão inteira).
#| `%`      | Resto da divisão | `7 % 2`  | `1`       | O operador % é usado para verificar divisibilidade, paridade, etc.
#| `**`     | Potência         | `2 ** 3` | `8`       | A potência ** também pode ser usada para raízes
# segue abaixo exemplo:
#a = float(input('Digite um numero: '))
#b = float(input(' Digite um numero: '))
#s = a + b
#sub = a - b
#mult = a * b
#div = a / b
#divinteira = a // b
#restodadiv = a % b
#pote = a ** b
#print(' Olá {} ja sabemos que sua idade é {} e que sua altura é {}!' .format(nome, idade, altura))
#print(f'Agora vamos ver seu conhecimento em matematica!')
#print(f'Voce digitou o numero {a} e {b}, vamos ver agora suas operaçoes matematicas!.')
#print('Voce digitou o numero {} e {}, vamos ver agora suas operaçoes matematicas!.'.format(a, b))
#print(' A soma é {}, \n Subtração {}, \n Multiplicação {}, \n Divisão real {}, \n Divisão inteira {}, \n Resto da divisão {}, \n Potencia é {}.'
 #     .format(s, sub, mult, div, divinteira, restodadiv, pote ))

# ---------------------------------------------------------
# Módulo 4 — Manipulando Textos (Strings)
# ---------------------------------------------------------
# Modulo importante para entender como se formata textos, colocar en maisculo ou minusculo alem de pode contar letras procurar palavras e dividir strings.

#| Método               | Função                                                          |
#| -------------------- | --------------------------------------------------------------- |
#| `len()`              | Conta o número total de caracteres da string                    |
#| `count()`            | Conta quantas vezes um caractere/aparece                        |
#| `find()`             | Informa a posição de uma substring (ou -1 se não existir)       |
#| `'palavra' in frase` | Retorna `True` ou `False` se a palavra existir ou não na string |
#| `upper()`            | Converte para MAIÚSCULAS                                        |
#| `lower()`            | Converte para minúsculas                                        |
#| `capitalize()`       | Só a primeira letra da string em maiúscula                      |
#| `title()`            | Primeira letra de cada palavra em maiúscula                     |
#| `strip()`            | Remove espaços em branco do começo e do fim                     |
#| `split()`            | Divide a string em partes (gera uma lista)                      |
#| `' - '.join()`       | Junta elementos de uma lista com o separador que você quiser    |



# Vamos praticar com uma frase simples
frase = 'Curso em Vídeo Python'

# Tamanho da frase
#print(f"Tamanho da frase: {len(frase)} caracteres")

# Quantas vezes aparece a letra 'o'
#print(f"Quantidade de letras 'o': {frase.count('o')}")

# Posição onde começa a palavra 'Vídeo'
#print(f"Posição da palavra 'Vídeo': {frase.find('Vídeo')}")

# A palavra 'Android' existe?
#print(f"A palavra 'Android' está na frase? {'Android' in frase}")

# Transformações:
#print(f"Maiúsculas: {frase.upper()}")
#print(f"Minúsculas: {frase.lower()}")
#print(f"Primeira letra de cada palavra: {frase.title()}")
#print(f"Só a primeira letra da frase: {frase.capitalize()}")

# Removendo espaços das pontas
#espacada = '   Olá mundo   '
#print(f"Sem espaços nas pontas: '{espacada.strip()}'")

# Dividindo a frase em palavras
#print(f"Dividida em lista: {frase.split()}")

# Juntando com hífen
#print(f"Juntando com hífen: {'-'.join(frase.split())}")

# Exemplo
#nome = input(' Digite seu nome completo: ')
#print(f' Seu  nome completo é {nome}.')
#print(' Prazer {}!' .format(nome))
#print('Seu nome tem {} letras!' .format(len(nome) - 4) )
#print(f'Seu nome tem {(len(nome) - 4)} letras!')
#print(f' Seu nome todo em letra maiscula fica assim {nome.upper()}!')
#print(' Seu nome todo em letra maiscula fica assim {}!' .format(nome.upper()))
#primeiro_nome = nome.split()[0]
#print(f'Seu primeiro nome é {primeiro_nome} e ele tem {len(primeiro_nome)} letras.')

# ---------------------------------------------------------
# Módulo Módulo 5 — Listas (Variáveis Compostas)
# ---------------------------------------------------------

#| Comando                    | Função                                    |
#| -------------------------- | ----------------------------------------- |
#| `lista[i]`                 | Acessa o valor no índice `i`              |
#| `lista[i] = x`             | Altera o valor do índice `i` para `x`     |
#| `lista.append(x)`          | Adiciona `x` ao final da lista            |
#| `lista.insert(i, x)`       | Insere `x` na posição `i`                 |
#| `del lista[i]`             | Remove o elemento da posição `i`          |
#| `lista.pop(i)`             | Remove e retorna o valor da posição `i`   |
#| `lista.remove(x)`          | Remove a primeira ocorrência do valor `x` |
#| `len(lista)`               | Retorna o número de elementos da lista    |
#| `lista.sort()`             | Ordena a lista em ordem crescente         |
#| `lista.sort(reverse=True)` | Ordena em ordem decrescente               |
#| `lista.copy()`             | Cria uma cópia independente da lista      |

# Lista é uma estrutura que guarda vários valores dentro de uma mesma variável.
# Podemos colocar números, textos, misturar dados e acessar por índice (posição).

# Criando uma lista:
#notas = [8.5, 7.0, 10.0]
#nomes = ['Alex', 'Barbara', 'Bernardo']

# Acessando elementos por índice (começa do 0):
#print(nomes[0])  # Alex
#print(notas[2])  # 10.0

# Modificando um valor:
#notas[1] = 7.5  # Agora a segunda nota virou 7.5

# Adicionando novo valor:
#notas.append(9.0)  # Adiciona 9.0 no final da lista

# Removendo valor:
#notas.pop()        # Remove o último valor (9.0)
#notas.remove(7.5)  # Remove o valor 7.5

# Saber o tamanho da lista:
#print(len(nomes))  # Quantos nomes tem na lista

# Usando for com lista:
#for nome in nomes:
#    print(f"Olá, {nome}!")

# Enumerando os valores:
#for indice, nome in enumerate(nomes):
#    print(f"Na posição {indice} está o nome {nome}")

# Criando uma lista vazia e preenchendo com input:
#compras = []
#for i in range(3):
#    item = input("Digite um item de compra: ")
#    compras.append(item)

#print("Lista de compras:", compras)

# ---------------------------------------------------------
# Módulo 6 — Condições (if, elif, else)
# ---------------------------------------------------------

# O if é usado para tomar decisões com base em comparações lógicas.
# A estrutura básica é:
# if condição:
#     faça algo
# else:
#     faça outra coisa

#idade = int(input("Quantos anos você tem? "))

#if idade >= 18:
#    print("Você é maior de idade.")
#else:
#    print("Você é menor de idade.")

#| Operador | Significado      | Exemplo  |
#| -------- | ---------------- | -------- |
#| `==`     | igual a          | `a == b` |
#| `!=`     | diferente de     | `a != b` |
#| `>`      | maior que        | `a > b`  |
#| `<`      | menor que        | `a < b`  |
#| `>=`     | maior ou igual a | `a >= b` |
#| `<=`     | menor ou igual a | `a <= b` |

#| Operador | Significado   | Exemplo                              |
#| -------- | ------------- | ------------------------------------ |
#| `and`    | e             | `idade >= 18 and idade <= 30`        |
#| `or`     | ou            | `nome == "Alex" or nome == "Ana"`    |
#| `not`    | não (negação) | `not aprovado` (se for False → True) |

n1 = float(input(' Digite a primeira nota: '))
n2 = float(input(' Digite a segunda nota: '))
media = (n1 + n2) / 2
if media >= 7:
 print('✅ Voce foi aprovado')
elif 5 <= media < 7:
 print(' 🔄 Voce esta de recuperação!')
else:
 print(' ❌ Voce esta de reprovado!')

