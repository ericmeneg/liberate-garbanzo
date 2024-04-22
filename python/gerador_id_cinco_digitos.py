import random

def gen_num():
    num = random.randint(0,9)
    return str(num)

def gen_id():
    primeiro = gen_num()
    segundo = gen_num()
    terceiro = gen_num()
    quarto = gen_num()
    quinto = gen_num()
    print(primeiro+segundo+terceiro+quarto+quinto)

gen_id()