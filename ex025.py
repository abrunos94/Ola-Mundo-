# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
cid = str(input(" Em qual cidade voce nasceu?")).strip()
print(cid[:5].upper() == "SANTO")