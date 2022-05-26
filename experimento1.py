import sys
from pathlib import Path
from functions.index import *
import random

def Experimento1(toEncode,intentos):
    for i in range(intentos):
        k=random.randint(0,len(toEncode))
        porcion=""
        for j in range(0,k):
            porcion+=toEncode[j]
        dendogramaSf=shannon_fano(porcion)
        print("dendogramaSf realizado y su tamaño es:",get_size(dendogramaSf))
        dendogramaH=huffman(porcion)
        print("dendogramaH realizado y su tamaño es:",get_size(dendogramaH))


def main():
    print(sys.argv)
    script = sys.argv[0]
    flags=sys.argv[1]
    filename = sys.argv[2]
    txt = Path('./data/' + filename).read_text(encoding='Latin-1')
    print("Archivo cargado, ", get_size(txt))

    for i in range(flags):
        k=random.randint(0,len(txt))
        porcion=txt[0:k]
        #for j in range(0,k):
        #    porcion+=txt[j]
        dendogramaSf=shannon_fano(porcion)
        print("dendogramaSf realizado y su tamaño es:",get_size(dendogramaSf))
        dendogramaH=huffman(porcion)
        print("dendogramaH realizado y su tamaño es:",get_size(dendogramaH))

    


if __name__ == '__main__':
   main()
