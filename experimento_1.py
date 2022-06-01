import sys
from pathlib import Path
from functions.index import *
import random
from functions.encode import encode
from bitarray import bitarray, decodetree
from time import time
import pickle

def filter_list(values, x, idx):
    new_list = []
    for val in values:
        if (len(val) > idx and int(val[idx]) == x): new_list.append(val)
    return new_list


def get_portion_decode(j, k, bits, dendograma):
    dendograma_bitarray = {k: bitarray(v) for k, v in dendograma.items()}
    bits_removed = 0
    decode_txt = ""
    while(True):
        try:
            d = bits[j:j+k].decode(decodetree(dendograma_bitarray))
            decode_txt = "".join(d)
            break
        except Exception:
            bits_removed = bits_removed + 1
            k = k - 1
            if bits_removed == 100:
                break

    return decode_txt

def Extract(filename):
    verbose = None
    if(len(sys.argv) > 3):
        verbose = True

    bits = bitarray()
    dendograma = None
    with open('./data/encode/' + filename, 'rb') as fh:
        bits.fromfile(fh)

    with open('./data/encode/' + "d_" + filename, 'rb') as f:
        dendograma = pickle.load(f)

    n_bits = len(bits)
    print(filename,n_bits)
    k = random.randint(0,n_bits)
    
    txt = get_portion_decode(0, k, bits, dendograma)

    if(verbose): print(txt)
    print("(0, k): (", 0, " ,", k, ")")


def main():
    print(sys.argv)
    script = sys.argv[0]
    filename=sys.argv[1]
    repeticiones=sys.argv[2]
    print(len(filename))

    shannon=encode("s",filename)
    huffman=encode("h",filename)
    print()

    for i in range (int(repeticiones)):
        print("Ejecucion",i+1,"=")
        time_shannon1 = time()
        Extract(shannon)
        time_shannon2 = time()

        time_huffman1 = time()
        Extract(huffman)
        time_huffman2 = time()
        
        print("El tiempo de shannon:",time_shannon2-time_shannon1)
        print("El tiempo de huffman:",time_huffman2-time_huffman1)
        print()

    
    
if __name__ == '__main__':
   main()
