import sys
from functions.index import *
from pathlib import Path
from bitarray import bitarray
from time import time
import csv
from sys import getsizeof



def main():
    print(sys.argv)
    script = sys.argv[0]
    flag = sys.argv[1]
    filename = sys.argv[2]

    n_iter = 10
    type_of_compression = 'h'
    if(flag == "s"):
        type_of_compression = "s"

    txt = Path('./data/' + filename).read_text(encoding='Latin-1')

    print("Archivo cargado, ", get_size(txt))
    print(n_iter," Iteraciones..")

    rows = [["compresion", "codificacion", "guardado", "total", "espacio utilizado"]]


    for i in range(n_iter):
        print("iter ", i + 1)
        compress_time_1 =time()
        dendograma = huffman(txt) if type_of_compression == "h" else shannon_fano(txt)
        compress_time_2 =time()

        encode_time_1 = time()
        dendograma_bitarray = {k: bitarray(v) for k, v in dendograma.items()}

        bits = bitarray()
        bits.encode(dendograma_bitarray, txt)
        encode_time_2 = time()

        save_time_1 = time()
        with open('./data/encode/' + type_of_compression + "_" + filename, 'wb') as fh:
            bits.tofile(fh)
        save_time_2 = time()

        total_size = convert_size(getsizeof(dendograma) + getsizeof(dendograma_bitarray) + getsizeof(bits))

        rows.append([compress_time_2-compress_time_1,encode_time_2-encode_time_1,save_time_2-save_time_1,save_time_2 - compress_time_1, total_size])

   
    with open('./data/csv' + type_of_compression + '_10_time_results_' + filename + '.csv', 'w') as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow(row)
    


if __name__ == '__main__':
   main()

