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

def find_correct_left_position(bits, j, k, dendograma):
    n_iter = 0
    flag = True
    j = j - 1
    while(flag):
        
        print(j)
        d_list = list(dendograma.values())
        for idx, bit in enumerate(bits[j:j+k]):
            d_list = filter_list(d_list, bit, idx)
            if(len(d_list) == 1): 
                print(d_list)
                flag = False
                break
            if(len(d_list) == 0):
                j = j + 1
                break

        if(n_iter == 100):
            flag=False
        
        n_iter = n_iter + 1

    return j


def main():
    print(sys.argv)
    script = sys.argv[0]
    flags=sys.argv[1]
    filename=sys.argv[2]
    filename_dendograma=sys.argv[3]

    bits = bitarray()
    dendograma = None
    with open('./data/encode/' + filename, 'rb') as fh:
        bits.fromfile(fh)

    with open('./data/encode/' + "d_" + filename, 'rb') as f:
        dendograma = pickle.load(f)

    n_bits = len(bits)

    j = random.randint(0,n_bits)
    k = random.randint(j,n_bits)

    j = find_correct_left_position(bits, j, k, dendograma)

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
    
if __name__ == '__main__':
   main()
