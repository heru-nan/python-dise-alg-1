import sys
from pathlib import Path
from functions.index import *
import random
from time import time

def main():
    print(sys.argv)
    script = sys.argv[0]
    flags=sys.argv[1]
    filename = sys.argv[2]

    txt = Path('./data/' + filename).read_text(encoding='Latin-1')

    for i in range(int(flags)):
        k=random.randint(0,len(txt))
        porcion=txt[0:k]
        print("intento ",i," de Experimento 1 para la procion T[0...",k,"]:")
        #for j in range(0,k):
        #    porcion+=txt[j]
        shannon_time_1 =time()
        dendogramaSf=shannon_fano(porcion)
        shannon_time_2 =time()
        
        huffman_time_1 =time()
        dendogramaH=huffman(porcion)
        huffman_time_2 =time()
        
        print("Tiempo de Extraccion de prefijos utilizando Shannon: ", shannon_time_2-shannon_time_1, " segundos")
        print("Tiempo de Extraccion de prefijos utilizando Huffman: ", huffman_time_2-huffman_time_1, " segundos")
        print()

    


if __name__ == '__main__':
   main()
