"""
Algoritimo que exibe uma lista de opções
adição, subtração, divisão, multiplicação e sair
Autor: João Pedro de Lima Santos
"""
def Soma(n1, n2):
    return n1 + n2

def Sub(n1, n2):
    return n1 - n2

def Div(n1, n2):
    return n1 / n2

def Mult(n1, n2):
    return n1 * n2

x = float(input("Valor 1: "))
y = float(input("Valro 2: "))

while True:
    operacao = int(input("1: Soma \n2: Sub \n3: Div \n4: Mult \n5: Saída: "))

    if operacao == 1:
        resultado = Soma(x, y)
        print("A soma é: ",resultado)
    elif operacao == 2:
        resultado = Sub(x, y)
        print("A subtração é: ", resultado)
    elif operacao == 3:
        resultado = Div(x, y)
        print("A divisão é: ", resultado)
    elif operacao == 4:
        resultado = Mult(x, y)
        print("A multiplicação é: ", resultado)

    elif operacao == 5:
        break
