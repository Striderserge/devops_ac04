#Lucas Duarte Piza 1900561
#Sergio de Barros 1900950


import sys


def linhaSimples(n):
    for i in range(1,n+1,1):
        sys.stdout.write('-')    
    sys.stdout.write('\n')

def linhaDupla(n):
    for i in range(1, n+1, 1):
        sys.stdout.write('=') 
    sys.stdout.write('\n')

def linha(simbolo, n):
    for i in range(1, n+1, 1):
        sys.stdout.write(simbolo)
    sys.stdout.write('\n')
