import sys
from functions.index import *
from pathlib import Path
from bitarray import bitarray

def main():
    print(sys.argv)
    script = sys.argv[0]
    filename = sys.argv[1]
    txt = Path('./data/' + filename).read_text(encoding='Latin-1')

    print("Archivo cargado, ", get_size(txt))
    
    # tiempo 1
    dendograma = huffman(txt)
    # tiempo 1
    
    # tiempo 2
    dendograma_bitarray = {k: bitarray(v) for k, v in dendograma.items()}
    bits = bitarray()
    bits.encode(dendograma_bitarray, txt)
    # tiempo 2

    # tiempo 3
    with open('./data/encode/' + "s_" + filename, 'wb') as fh:
        bits.tofile(fh)
    # tiempo 3


if __name__ == '__main__':
   main()

