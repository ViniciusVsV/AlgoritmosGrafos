import numpy as np

def imprimirMatriz(instancia, data):
    print(instancia + " " + str(data.shape))

    for row in data:
        print(" ".join(map(str, row)))