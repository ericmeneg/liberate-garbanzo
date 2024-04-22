import math
n=int(input("Digite um número inteiro N: "))
print("Checagem com a biblioteca math:",math.factorial(n))
contagem = 1
resultado = n
while contagem<n:
    resultado = resultado*(n-contagem)
    contagem = contagem + 1
print("Resultado:",resultado)