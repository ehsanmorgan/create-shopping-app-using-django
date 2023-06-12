import random

def genritecode(length=12):
    x='1,2,3,4,5,a,s,d,6,7,8'
    return ''.join(random.choice(x) for _ in range(length))