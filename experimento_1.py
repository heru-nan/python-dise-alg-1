import sys
from pathlib import Path
from functions.index import *
import random
from bitarray import bitarray, decodetree
from time import time
import pickle

def filter_list(values, x, idx):
    new_list = []
    for val in values:
        if (len(val) > idx and int(val[idx]) == x): new_list.append(val)
    return new_list


def get_portion_decode(k, bits, dendograma):
    dendograma_bitarray = {k: bitarray(v) for k, v in dendograma.items()}
    bits_removed = 0
    decode_txt = ""
    aux=k
    while(True):
        try:
            d = bits[0:aux].decode(decodetree(dendograma_bitarray))
            if(len(d)<k):
                dif=k-len(d)
                aux+=dif
                continue
            if(len(d)==k):
                decode_txt = "".join(d)    
                break
            aux+=1
        except:
            bits_removed = bits_removed + 1
            aux = aux + 1
            if bits_removed == 10000000:
                break
    
    return decode_txt

def Extract(filename,k):
    bits = bitarray()
    dendograma = None
    with open('./data/encode/' + filename, 'rb') as fh:
        bits.fromfile(fh)
    with open('./data/encode/' + "d_" + filename, 'rb') as f:
        dendograma = pickle.load(f)
    
    time_1 = time()
    txtRecuperado = get_portion_decode(k, bits, dendograma)
    time_2 = time()
    return time_2-time_1


def main():
    print(sys.argv)
    script = sys.argv[0]
    filename=sys.argv[1]
    repeticiones=sys.argv[2]
    
    txt = Path('./data/' + filename).read_text(encoding='Latin-1')#recuperamos el texto 
    shannon=("s_" + filename)#codificamos el texto entregado
    huffman=("h_" + filename)
    print()

    for i in range (int(repeticiones)):
        k=random.randint(0,len(txt))
        print("Ejecucion",i+1,"desde T[0...",k ,"] =")
        time_shannon=Extract(shannon,k)
        time_huffman=Extract(huffman,k)
        
        
        print("El tiempo de shannon:",time_shannon)
        print("El tiempo de huffman:",time_huffman)
        print()

    
    
if __name__ == '__main__':
   main()
