import random
n = int(input("Digite o número de carácteres que a sua senha terá: "))

letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

letrasupper = letras.copy()
count = 0
for x in letrasupper:
    letrasupper[count] = letrasupper[count].upper()
    count = count + 1

numeros = [0,1,2,3,4,5,6,7,8,9]

simbolos = ["!","@","#","$","%","^","&","*",")","(","-","=","_","+","<",">",";",":","?","~","[","]","{","}"]

senha = []
for x in range(1,n+1):
    add = random.choice([letras,letrasupper,numeros,simbolos])
    add = random.choice(add)
    senha.append(add)

senhastr = ""
for item in senha:
    item = str(item)
    senhastr = senhastr + item

print(senhastr)

'''
antigo gerador de id de 5 digitos
def gen_num():
    num = random.randint(0,9)
    return str(num)

def gen_id():
    id = gen_num()
    while True:
        id = id + gen_num()
        if len(id)== 5:
            break
    return id

print(gen_id())
'''