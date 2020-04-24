#!/usr/bin/env python

#DESAFIO REPETIÇÃO
#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
#Faça um programa capaz de gerar a série até o n−ésimo termo.
#Qual numero voce deseja receber a sequencia fibonacci? 34

count = 1
Fibonacci = 0

n = int(input('Digite um numero para ver em Fibonacci. '))

while n != 0:
    print('{}'.format(Fibonacci), end=' → ')
    Fibonacci = Fibonacci + count
    count = Fibonacci - count
    n -= 1
print('FIM')