# cores no terminal
# style = 0, 1, 4, 7.
# text = 30, 31, 32, 33, 34, 35, 36, 37.
# back = 40, 41, 42, 43, 44, 45, 46, 47.
# O comando é \033[style;text,back(fundo) e no fim do string e so colocar \033[m para o formartaçao naoir ir ate o fim
print('\033[0;30;41m Ola mundo\033[m')
print('\033[1;37;41m Ola mundo\033[m')
print('\033[7;30;47m Ola mundo\033[m')
print('\033[0;32;44m Ola mundo\033[m')
