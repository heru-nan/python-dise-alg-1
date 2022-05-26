import sys
from functions.index import *
from pathlib import Path
from bitarray import bitarray, decodetree
from time import time
import pickle



def main():
    print(sys.argv)
    script = sys.argv[0]
    filename = sys.argv[1]
    filename_dendograma = sys.argv[2]

    compress_time_1 = time()
    bits = bitarray()
    dendograma = None
    with open('./data/encode/' + filename, 'rb') as fh:
        bits.fromfile(fh)

    with open('./data/encode/' + filename_dendograma, 'rb') as f:
        dendograma = pickle.load(f)

    dendograma_bitarray = {k: bitarray(v) for k, v in dendograma.items()}

    bits_removed = 0
    while(True):
        try:
            d = bits.decode(decodetree(dendograma_bitarray))
            decode_txt = "".join(d)
            break
        except:
            bits_removed = bits_removed + 1
            bits.pop()
            if bits_removed == 100:
                break

    with open('./data/decode/' + filename, 'w', encoding='Latin-1') as fh:
        fh.write(decode_txt)
    save_time_2 = time()
    
    print("Tiempo total: ", save_time_2 - compress_time_1, " segundos")
    print("Bits erroneos removidos: ", bits_removed)

if __name__ == '__main__':
   main()

