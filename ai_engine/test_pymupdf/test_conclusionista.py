from typing import Callable

import pymupdf
from time import time

# Un buen PDF cargado de paginas en https://digibug.ugr.es/handle/10481/52309
doc = pymupdf.open("PDF/test.pdf") # open a document

def test_1():
    text = ""
    di = time()

    for page in doc: # iterate the document pages
        text += page.get_text("text")

    df = time()
    return df-di



def test_2():
    text = ""
    di = time()

    for page in doc: # iterate the document pages
        blocks = page.get_text("blocks")
        text += "\n".join(block[4] for block in blocks) # El 4-index es el texto

    df = time()
    return df-di


def testador (times:int, func: Callable[[], float]):
    time_list = []
    for i in range(times):
        time_list.append(test_1())
    print(f" Para \033[34m{times} veces\033[0m con \033[35m{func.__name__}\033[0m \033[36m{(sum(time_list) / times):.6f}\033[0m segs de promedio")

if __name__ == '__main__':
    # Lo ejecutamos para que se compile
    test_1()
    test_2()

    testador(times=100, func=test_2)
    testador(times=100, func=test_1)
    testador(times=100, func=test_2)
    testador(times=100, func=test_1)

    # Resultados:
    #  Para 100 veces con test_2 0.554719 segs de promedio
    #  Para 100 veces con test_1 0.551076 segs de promedio
    #  Para 100 veces con test_2 0.575311 segs de promedio
    #  Para 100 veces con test_1 0.551000 segs de promedio
    #
    #  En promedio ambas son igual de rapidas.
    #  'text'  es mas simple y facil de entender
    #
    #

