import numpy as np
import os

def salvarDados(instancia, data, imgGrafo):
    nlinhas, ncolunas = data.shape

    nomePasta = instancia.capitalize()
    os.makedirs(rf"C:\VsCode\AG (2025-01)\Introducao_Python\PrototipoSoftware\Resultados\{nomePasta}", exist_ok=True)

    caminho = rf"C:\VsCode\AG (2025-01)\Introducao_Python\PrototipoSoftware\Resultados\{nomePasta}\resultado_{instancia}.txt"
    resultado = f"{instancia} {nlinhas} {ncolunas}\n"

    with open(caminho, "w") as f:
        f.writelines(resultado)
    
    with open(caminho, "a") as f:
        np.savetxt(f, data, fmt="%d", delimiter=" ")

    caminho = rf"C:\VsCode\AG (2025-01)\Introducao_Python\PrototipoSoftware\Resultados\{nomePasta}\{instancia}.png"
    imgGrafo.savefig(caminho)