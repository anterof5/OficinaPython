#!/usr/bin/python
# -*- coding: utf-8 -*-

nome = 'Antero' #string (texto)
idade = "37" #string (texto)
idade_numero = 37 #integer (inteiro)
altura = 1.68 #float (decimal)
vivo = True #Boolean (booleano)

print("Seu nome é %s" % nome)
print(f"Seu nome é {nome}")


# Faça um programa que peça dois números
# inteiros e imprima a soma desses dois números.

# Obs: inputs são dinâmicas
numero1 = input("Por favor, insira o primeiro número: ")
numero2 = input("Agora insira o segundo número: ")

soma = int(numero1) + float(numero2)
print("A soma dos valores é: %s" % soma)

# Operadores matemáticos
# Soma +
# Subtraçaõ -
# Multiplicação *
# Divisão /
# Exponenciação **
# Matemática () {} []

# Converta uma temperatura digitada em Celsius para
# Fahrenheit. F = 9*C/5 + 32

celsius = input("Por favor, insira a temperatura em graus Celsius: ")
fahrenheit = 9 * float(celsius) / 5 + 32
print("A temperatura em Fahrenheit é: %f" % conversao)

# Faça agora o contrário, de Fahrenheit para Celsius
c = (fahrenheit - 32) * 5/9
print(f"A temperatura em Celsius é: {c}")
