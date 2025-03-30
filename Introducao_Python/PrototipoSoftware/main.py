from Funcoes.lerMatriz import lerMatriz
from Funcoes.salvarDados import salvarDados
from Funcoes.imprimirMatriz import imprimirMatriz
from Funcoes.gerarGrafo import gerarGrafo

while True:
    instancia = str(input("Digite o nome da instância a ser processada: "))
    if instancia == "":
        break

    data = lerMatriz(instancia)
    if data is None:
        print("Dataset não encontrado")
        continue

    imprimirMatriz(instancia, data)
    imgGrafo = gerarGrafo(data)

    salvarDados(instancia, data, imgGrafo)

    nomePasta = instancia.capitalize()
    print(f"Dados salvos em Resultados\\{nomePasta}\\resultado_{instancia}.txt\n")