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


 
def main():
    print(sys.argv)
    script = sys.argv[0]
    filename=sys.argv[1]
    filename_dendograma=sys.argv[2]
    
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

    k = random.randint(0,n_bits)
    
    txt = get_portion_decode(0, k, bits, dendograma)

    if(verbose): print(txt)

    print("(0, k): (", 0, " ,", k, ")")

    print("Longitud de Bits: ", len(bits[0:k]))
    print("Longitud text: ", len(txt))
    

    
    
if __name__ == '__main__':
   main()
