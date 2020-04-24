#!/usr/bin/env python

#DESAFIO FUNÇÕES
#Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

numero = int(input('Entre com o numero... '));
print('Número informado ', numero)

numeroInvertido = int(str(numero)[::-1]);

print('O número invertido: ', numeroInvertido)