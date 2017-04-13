import digrafo

def main():

    grafo = digrafo.Digrafo(5)

    print(grafo.obtenerNumeroDeVertices())
    print(grafo.obtenerNumeroDeAristas())

    grafo.agregarArista(1, 0)
    grafo.agregarArista(0, 2)
    grafo.agregarArista(2, 1)
    grafo.agregarArista(0, 3)
    grafo.agregarArista(3, 4)

    print("El grafo G es: ")
    print(grafo.obtenerGrafo())

    print("El grafo G transpuesto es: ")
    print(grafo.transponer().obtenerGrafo())

    print("Estas son las componentes fuertemente conexas del grafo dado:")
    grafo.imprimirCFC()

    print("El grafo G tiene " + str(grafo.obtenerNumeroDeCFC()) + " componentes fuertemente conexas")

main()