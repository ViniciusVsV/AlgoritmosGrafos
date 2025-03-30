import igraph as ig
import matplotlib.pyplot as plt

def gerarGrafo(data):
    nVertices = data.shape[0]

    arestas = [(i, j, data[i, j]) for i in range(nVertices) for j in range(i + 1, nVertices) if data[i, j] > 0]

    grafo = ig.Graph(nVertices, [(i, j) for i, j, _ in arestas])

    grafo["title"] = "Grafo Gerado da Matriz"
    grafo.vs["name"] = [f"{i}" for i in range(nVertices)]
    grafo.es["weigth"] = [peso for _, _, peso in arestas]

    fig, ax = plt.subplots(figsize=(5,5))
    ig.plot(
        grafo,
        target=ax,
        layout="circle",
        vertex_size=30,
        vertex_color="steelblue",
        vertex_frame_width=4.0,
        vertex_frame_color="white",
        vertex_label=grafo.vs["name"],
        vertex_label_size=7.0,
        edge_width=1,
        edge_color="#AAA",
        edge_label=grafo.es["weigth"]
    )

    plt.show()

    return fig