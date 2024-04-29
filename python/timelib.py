import time

def filler(t):
    if len(t)<2:
        t ="0"+t
    return t

#pega um tempo em segundos e devolve uma string do tempo no formato HH:MM:SS
def converter(segundos):
    hora = filler(str(segundos//3600))
    minuto = filler(str((segundos%3600)//60))
    segundo = filler(str((segundos%3600)%60))
    return hora+":"+minuto+":"+segundo

algarismos = []
while True:
    tempo = input("Digite quanto tempo você quer que o timer dure (HH:MM:SS): ").replace(":","")
    if len(tempo) == 6 and tempo.isdigit() == True:
        break
    else:
        print("Erro, digite o valor desejado exatamente no modelo HH:MM:SS (preencha os zeros)")

for x in tempo:
    algarismos.append(str(x))

seg = int(algarismos[4]+algarismos[5])

min = int(algarismos[2]+algarismos[3])

hr = int(algarismos[0]+algarismos[1])
 
tempo = seg + (min * 60) + (hr * 3600)
if tempo > 359999: tempo = 359999
while True:
    time.sleep(1)
    tempo = tempo - 1
    print(converter(tempo))
    if tempo == 0:
        break

print("O tempo acabou!")

count = 1
while True:
    time.sleep(1)
    print("-"+converter(count))
    count = count + 1