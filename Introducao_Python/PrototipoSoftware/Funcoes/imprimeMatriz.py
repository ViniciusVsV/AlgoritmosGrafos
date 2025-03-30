import numpy as np

def imprimeMatriz(data):
    for row in data:
        print(" ".join(map(str, row)))