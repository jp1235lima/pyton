"""
Algoritimo que recebe três valores de segmentos de um triângulo
e retorna qual o tipo de triângulo
Autor: João Pedro de Lima Santos
"""
r1 = float(input('primeiro segmento: '))
r2 = float(input('segundo segmento: '))
r3 = float(input('tereceiro segmento: '))
if r1 < r2 +r3 and r2 < r1 + r3 and r3 < r1 + 2:
    print('Os segmentos acima podem formar um triângulo')
    if r1 == r2 == r3:
      print(' Equilátero! ')
    elif r1 != r2 != r3 != r1:
      print(' Escaleno! ')
    else:
        print(' Isósceles! ')
else:
    print(' Os segmentos acima não podem formar um triângulo !')
