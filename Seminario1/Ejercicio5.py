import sys
from typing import List


def primos() :
    p=2
    while True:
        if es_primo(p):
            yield p
        p+=1


def es_primo(num):
    cont=0
    if num==2:
        return True
    for i in range(1,num+1):
        if num%i==0:
            cont+=1
    if cont==2:
        return True
    return False

def squares1():
    n=1
    while True:
        yield n**2+1
        n+=1

def almost_squares():
    s=squares1()
    p=primos()
    sc=next(s)
    pr=next(p)
    while True:
        if sc==pr:
            yield pr
            sc=next(s)
            pr=next(p)
        else:
            if sc<pr:
                sc=next(s)
            else:
                pr=next(p)

def process(n: int) -> List[int]:
    n=almost_squares()
    return n

def read_data(f) -> List[int]:
    l=int(f.readline())
    return l

def show_results(lista: List[int]):
    for i in lista:
        print(i)
        print()

if __name__== "__main__":
    n=read_data(sys.stdin)
    l=process(n)
    show_results(l)