#!/usr/bin/python
# -*- coding: utf-8 -*-

tempo = {
        "dados": [
            {"cidade": "Porto Velho", "temp": 31, "escala": "celsius"},
            {"cidade": "Manaus", "temp": 29, "escala": "celsius"},
            {"cidade": "São Paulo", "temp": 14, "escala": "celsius"},
            ],
        "resultadosPorPag": 20,
        "tamanho": 3
        }
# Loop na chave que é uma lista de dicionários
for dados in tempo["dados"]:
    print(dados)
    print("Bom dia, a temperatura em %s é de %f " % (dados["cidade"], dados["temp"]))

# Print em uma chave do dicionário
print(tempo["tamanho"])

# Loop nas chaves do dicionário
for item in tempo:
    print(item)
