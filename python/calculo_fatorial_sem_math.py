import math
n=int(input("Digite um número inteiro N: "))
print("Checagem com a biblioteca math:",math.factorial(n))
contagem = 1
resultado = n

if n == 0:
    resultado = 1
elif n<0:
    resultado = "indefinido"
else:    
    while contagem<n:
        resultado = resultado*(n-contagem)
        contagem = contagem + 1

print("Resultado:",resultado)