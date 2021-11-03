#!/usr/bin/python
# -*- coding: utf-8 -*-

# Lista guarda variáveis
lista = ["Antero", "Aline", "Luana", "Maoly", "Pedro"]
lista2 = [2, "Letras", True, [0,1,2,3], {"chave": "valor"}]

# Acessar índice da lista através de números
# o primeiro é zero
print(lista[0]) #mostra o valor Antero

# Loop em lista dentro de um dicionário    
for itemLista in lista:
    print(itemLista)
    print(type(itemLista))

# Dicionários organizam dados através de chaves e valores
corPredileta = {"cor": "Azul"}
dic = {"cores": ["Azul", "Verde", "Vermelho"] }
tempo = {"dados": {"cidade": "Porto Velho", "temp": 31, "escala": "celsius"}}

# Dicionários podem ser agrupados em listas
listaDicionario = [{"nome": "Antero", "endereço": "Rua tal"},
                   {"nome": "Fulano", "endereço": "Rua X"}]

# Para acessar uma chave de um dicionário usamos esta sintaxe.
print(dic["cores"])

# Acessando um dicinário em uma lista e seus items.
for item in listaDicionario:
    print(type(item))
    print(item['nome'])


# Loop em lista dentro de um dicionário    
for itemLista in lista:
    print(itemLista)
    print(type(itemLista))

# Loop em lista dentro de um dicionário
for cor in dic["cores"]:
    print(cor)
