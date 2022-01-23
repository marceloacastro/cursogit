linha = 1
coluna = 1

# Cria o calculo da Tabuada
while linha <= 10:
    while  coluna <= 10:
       print (linha * coluna, end = "\t")
       coluna = coluna + 1
    linha = linha + 1
    print()
    coluna = 1