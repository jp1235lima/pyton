"""
Algoritimo que recebe uma lista de valores
e retorna a soma e a média
Autor: João Pedro de Lima Santos
"""
#Definição da função
def soma(numeros):
    soma = sum(numeros)
    print(f'A soma é {soma}')
#Função da média
def media(valores):
    avg = sum(valores) / len(valores)
    print(f'\nA média é {avg}')
    
#Criação da lista
lista=[]

for a in range(5):
    lista.append(int(input('Coloque um número: ')))
soma(lista)
media(lista)
