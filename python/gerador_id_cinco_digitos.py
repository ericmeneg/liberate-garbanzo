import random

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