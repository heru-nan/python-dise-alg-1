import heapq
import numpy as np
import collections

# Implemetación adaptada de https://rosettacode.org/wiki/Huffman_coding#Python
def huffman(arr):
    dendograma = [[frequencia/len(arr), [simbolo, ""]] for simbolo, frequencia in collections.Counter(arr).items()]
    heapq.heapify(dendograma)
    # Crear el código
    while len(dendograma) > 1:
        lo = heapq.heappop(dendograma)
        hi = heapq.heappop(dendograma)
        for codigo in lo[1:]:
            codigo[1] = '0' + codigo[1]
        for codigo in hi[1:]:
            codigo[1] = '1' + codigo[1]
        heapq.heappush(dendograma, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    dendograma = sorted(heapq.heappop(dendograma)[1:])
    dendograma = {simbolo : codigo for simbolo, codigo in dendograma} 

    # texto_codificado = ""
    # for letra in arr:
    #     texto_codificado += dendograma[letra]
    
    # if (len(texto_codificado)% 8 != 0):
    #     texto_codificado= texto_codificado.ljust(((8-len(texto_codificado)% 8))+len(texto_codificado),'1')
    # code = (texto_codificado[:1000])

    
    return dendograma


def decoding_huffman(arr_codificado,dendograma):
    dendograma_inverso =  {codigo: simbolo for simbolo, codigo in dendograma.items()}
    #print(dendograma_inverso)

    codigo = ""
    decodeStr = ""
    for bit in arr_codificado:
        codigo += bit
        if codigo in dendograma_inverso:
            decodeStr = decodeStr + dendograma_inverso[codigo]
            codigo = ""
    return decodeStr