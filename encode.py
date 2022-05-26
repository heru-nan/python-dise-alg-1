import sys
from functions.index import *
from pathlib import Path
from bitarray import bitarray
from time import time
# TODO TASA DE COMPRESION Y ESPACIO UTILIZADO
# Media armonica


def main():
    print(sys.argv)
    script = sys.argv[0]
    flag = sys.argv[1]
    filename = sys.argv[2]

    type_of_compression = 'h'
    if(flag == "s"):
        type_of_compression = "s"

    txt = Path('./data/' + filename).read_text(encoding='Latin-1')

    print("Archivo cargado, ", get_size(txt))
    
    compress_time_1 =time()
    dendograma = huffman(txt) if type_of_compression == "h" else shannon_fano(txt)
    compress_time_2 =time()

    print("dendograma, ", get_size(dendograma))
    

    encode_time_1 = time()
    dendograma_bitarray = {k: bitarray(v) for k, v in dendograma.items()}
    bits = bitarray()
    bits.encode(dendograma_bitarray, txt)
    encode_time_2 = time()

    print("bitarray, ", get_size(bits))

    save_time_1 = time()
    with open('./data/encode/' + type_of_compression + "_" + filename, 'wb') as fh:
        bits.tofile(fh)
    save_time_2 = time()
    
    print("Tiempo de Compresion(Shannon o Huffman): ", compress_time_2-compress_time_1, " segundos")
    print("Tiempo de Codificacion a bitstram: ", encode_time_2-encode_time_1, " segundos")
    print("Tiempo de Guardad en archivo: ", save_time_2-save_time_1)
    print("Tiempo total: ", save_time_2 - compress_time_1, " segundos")

if __name__ == '__main__':
   main()

