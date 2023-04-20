'''
Escreva um programa que recebe uma lista de números
inteiros como entrada e retorna a soma dos elementos da lista.
'''
import os
os.system('clear')

print('Enter a list of numbers with comma')
user_input = input('>>> ')


user_input = [int(x) for x in user_input.split(',')]

sum_list = 0

for number in user_input:

    sum_list += number

print(sum_list)

"""
Escreva uma função chamada soma_quadrados que recebe dois números 
inteiros como parâmetros e retorna a soma dos seus quadrados. Em seguida
escreva um programa que solicita que o usuário digite dois números inteiros,
chama a função soma_quadrados com esses números e exibe o resultado.

#formula 

a² + b²
onde "a" e "b" são os números que queremos elevar ao quadrado e somar.

#exemplo de saida

Digite um número inteiro: 3
Digite outro número inteiro: 4
A soma dos quadrados de 3 e 4 é 25.
"""

def soma_quadrados(x, y):

    x = user_int**2
    y = user_int_two**2

    return x , y

print('Enter 2 numbers with comma')
user_number = input('>>> ')
user_number_two = input('>>> ')

if user_input:
    user_int = int(user_number)
    user_int_two = int(user_number_two)
    print(f'O quadrado de {user_number} e {user_number_two} e {soma_quadrados(user_input, user_int_two)}')
else:
    print('Erro')

'''
Escreva uma função em Python que recebe uma lista de números como parâmetro e 
retorna a média desses números. Em seguida, escreva um programa que pede ao usuário 
para digitar uma lista de números separados por vírgulas, 
chama a função para calcular a média desses números e exibe o resultado na tela.

A fórmula para calcular a média de uma lista de números é simples: basta somar todos os 
elementos da lista e dividir o resultado pelo número de elementos na lista. Matematicamente, 
a fórmula para calcular a média pode ser escrita da seguinte forma:

Média = (x1 + x2 + ... + xn) / n

Onde:

    x1, x2, ..., xn são os elementos da lista de números.
    n é o número de elementos na lista.
'''

def Num_list(numeros):

    soma = sum(user_entry)
    media = soma / len(numeros)
    return media

print('Enter a list o numbers to know the avarege, do not forget to use comma (1,2,3)')
user_entry = input('>>> ')

user_entry = [int(i) for i in user_entry.split(',')]
print(f'The avarage is', Num_list(user_entry))






















