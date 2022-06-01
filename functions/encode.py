from functions.index import *
from pathlib import Path
from bitarray import bitarray
import pickle

def encode(typeEncode,filename):
    flag = typeEncode

    type_of_compression = 'h'
    if(flag == "s"):
        type_of_compression = "s"

    txt = Path('./data/' + filename).read_text('Latin-1')

    print("Archivo cargado, ", get_size(txt))
    
    dendograma = huffman(txt) if type_of_compression == "h" else shannon_fano(txt)

    dendograma_bitarray = {k: bitarray(v) for k, v in dendograma.items()}
    bits = bitarray()
    bits.encode(dendograma_bitarray, txt)

    with open('./data/encode/' + type_of_compression + "_" + filename, 'wb') as fh:
        bits.tofile(fh)

    with open('./data/encode/d_' + type_of_compression + "_" + filename, 'wb') as f:
        pickle.dump(dendograma, f)
    
    return (type_of_compression + "_" + filename)
 


