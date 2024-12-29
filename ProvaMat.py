# media, moda, mediana, variancia, desv. padrao

lista = [5, 8, 10, 7]
tamanho_lista = len(lista)


# CALCULO MÉDIA
total = 0
for i in lista:
    total += i


media = total / tamanho_lista
print(f'a média é: {media:.2f}')

# CALCULO MODA

tabela = {}
for j in lista:
    tabela[j] = tabela.get(j, 0) + 1

# print(tabela)

maior_valor = 0
maior_chave = -1
for chave, valor in tabela.items():
    if valor > maior_valor:
        maior_valor = valor
        maior_chave = chave

moda_encontrada = False
for chave, valor in tabela.items():
    if valor == maior_valor:
        if not moda_encontrada:
            print(f'a moda é: {chave}', end=' ')
            moda_encontrada = True
        else:
            print(f'{chave}', end=' ')
print()

# CALCULO MEDIANA

lista_ordenada = sorted(lista)

valor1 = int(tamanho_lista / 2) - 1
valor2 = int(tamanho_lista / 2)

if tamanho_lista % 2 == 0:
    mediana = (lista_ordenada[valor1] + lista_ordenada[valor2]) / 2
else:
    mediana = lista_ordenada[valor2]

print(f'a mediana é: {mediana}')

# VARIANCIA
soma_variancia = 0
for i in lista:
    x = (i - media)**2
    soma_variancia += x

variancia = soma_variancia / tamanho_lista
print(f'a variância é: {variancia}')

# DESVIO PADRAO
desvio_padrao = variancia**0.5
print(f'o desvio padrão é: {desvio_padrao:.2f}')
