import numpy as np
import os.path

def lerMatriz(instancia):
    caminho = r"C:\VsCode\AG (2025-01)\Introducao_Python\PrototipoSoftware\Datasets\\" + instancia + ".txt"

    try:
        with open(caminho, "rb") as f:
            data = np.genfromtxt(f, dtype="int32")
        
        return data
    
    except FileNotFoundError:
        return None