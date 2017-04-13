

class Digrafo:
    """Grafo dirigido con un número fijo de vértices.

      Los vértices son siempre números enteros no negativos. El primer vértice es 0.

      El grafo se crea vacío, se añaden las aristas con agregarArista(). Una vez
      creadas, las aristas no se pueden eliminar, pero siempre se pueden añadir
      nuevas aristas."""

    def __init__(self, v):
        self.vertices = v
        self.aristas = 0
        self.adyacentes = dict()
        self.numeroDeCFC = 0
        self.componentesConexas = []
        for i in range(0, v, 1):
            self.adyacentes[i] = []

    def __str__(self):
        return str(self.adyacentes)

    def obtenerNumeroDeVertices(self):
        return self.vertices

    def obtenerNumeroDeAristas(self):
        return self.aristas

    def agregarArista(self, verticeOrigen, verticeDestino):
        self.adyacentes[verticeOrigen].append(verticeDestino)
        self.aristas += 1

    def adyacentesAlVertice(self, v):
        return self.adyacentes[v]

    def transponer(self):
        transpuestaDelGrafo = Digrafo(self.vertices)
        for i in self.adyacentes:
            for j in self.adyacentes[i]:
                transpuestaDelGrafo.agregarArista(j,i)
        return transpuestaDelGrafo

    #Imprime cada vertice con sus aristas
    def obtenerGrafo(self):
        s = "Vertice -> Adyacentes\n"
        for i in self.adyacentes:
            s += str(i) + " -> "
            for j in self.adyacentes[i]:
                s += str(j) + " "
            s += "\n"
        return s

    def dfsGrafoTranspuesto(self, v, visitado):
        # Marca el nodo actual como visitado y lo imprime
        visitado[v] = True

        self.componentesConexas.append(v)

        # Se repite para todos los vértices adyacentes al actual
        for i in self.adyacentes[v]:
            if visitado[i] == False:
                self.dfsGrafoTranspuesto(i, visitado)

    def dfsParaCalcularTf(self, v, visitado, pila):
        # Marca el nodo actual como visitado
        visitado[v] = True
        # Se repite para todos los vértices adyacentes al actual
        for i in self.adyacentes[v]:
            if visitado[i] == False:
                self.dfsParaCalcularTf(i, visitado, pila)
        pila.append(v)

    # Esta es la funcion principal que encuentra e imprime todas las CFC
    def imprimirCFC(self):

        pila = []

        # Marco todos los vertices como no visitados (DFS(G))
        visitado = [False] * (self.vertices)

        # Relleno la pila con los vertices de acuerdo con su tiempo de finalizacion
        for i in range(self.vertices):
            if visitado[i] == False:
                self.dfsParaCalcularTf(i, visitado, pila)

        # Calcula la transpuesta del Grafo
        grafoTranspuesto = self.transponer()

        # Marco todos los vertices como no visitados (DFS(Gt))
        visitado = [False] * (self.vertices)

        # Procesa todos los vértices en el orden definido por la pila
        while pila:
            i = pila.pop()
            if visitado[i] == False:
                grafoTranspuesto.dfsGrafoTranspuesto(i, visitado)
                self.numeroDeCFC += 1
                print(grafoTranspuesto.componentesConexas)
                grafoTranspuesto.componentesConexas.clear()

    def obtenerNumeroDeCFC(self):
        return self.numeroDeCFC