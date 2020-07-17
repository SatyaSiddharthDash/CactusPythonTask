class Graph(object):
    """
    A simple Python graph class, demonstrating the essential facts
    and functionalities of graphs.
    """

    def __init__(self, graph_dict: dict = {}):
        """
        Initializes a graph object
        If no dictionary is given,
        an empty dictionary will be used.
        Parameters:
            graph_dict(dict): Adjacency list to build graph
        """

        self.__graph_dict = graph_dict

    @property
    def graph_dict(self):
        return self.__graph_dict

    def vertices(self):
        """
        Returns the vertices of a graph
        Returns:
            (list):List of vertices
        """
        return list(self.__graph_dict.keys())

    def edges(self):
        """
        Returns the edges of a graph.
        Returns:
            (list):List of edges
        """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """
        If the vertex "vertex" is not in
        self.__graph_dict, a key "vertex" with an empty
        list as a value is added to the dictionary.
        Otherwise nothing has to be done.
        Parameters:
            vertex(str):Vertex to be added.
        Returns:
            None
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge: tuple):
        """
        Assumes that edge is of type tuple or list of tuples.
        If the corresponding vertices don't exist in the graph, they are added
        Parameter:
            edge(tuple): Edge to add.
        """
        vertex1, vertex2 = edge
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.__graph_dict[vertex1].append(vertex2)

    def __generate_edges(self) -> list:
        """
        A method generating the edges of the
        graph "graph". Edges are represented as sets
        with one (a loop back to the vertex) or two
        vertices.
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if (neighbour, vertex) not in edges:
                    edges.append((vertex, neighbour))
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res


class Digraph(Graph):
    """
    A simple Python digraph class, inherited from the Graph class.
    """

    def __init__(self, graph_dict: dict = {}):
        """
        Initializes a graph object
        If no dictionary is given,
        an empty dictionary will be used.
        Parameters:
            graph_dict(dict): Adjacency list to build graph
        """
        super().__init__(graph_dict)
        self.__graph_dict = self.graph_dict
        self.__parent_dict = self.generate_parent_dict(self.graph_dict)

    @property
    def parent_dict(self):
        return self.__parent_dict

    @staticmethod
    def generate_parent_dict(graph_dict: dict) -> dict:
        """
        Function to generate the parent dict from the graph_dict
        """
        parent_dict = {}
        for vertex in graph_dict:
            for child in graph_dict[vertex]:
                if child in parent_dict:
                    parent_dict[child].append(vertex)
                else:
                    parent_dict[child] = [vertex]

        return parent_dict

    def vertices(self):
        """
        Returns the vertices of a graph
        Returns:
            (list):List of vertices
        """
        return super().vertices()

    def edges(self):
        """
        Returns the edges of a graph.
        Returns:
            (list):List of edges
        """
        return self.__generate_edges()

    def add_vertex(self, vertex):

        super().add_vertex(vertex)
        if vertex not in self.__parent_dict:
            self.__parent_dict[vertex] = []

    def add_edge(self, edge):
        """
        Method to add a new edge to the graph.
        Note that it is added in both the graph_dict as well as the parent_dict
        """

        super().add_edge(edge)
        vertex2, vertex1 = edge
        self.add_vertex(vertex2)
        self.add_vertex(vertex1)
        self.__parent_dict[vertex1].append(vertex2)

    def __generate_edges(self) -> list:
        """
        A method generating the edges of the
        graph "graph".
        """
        edges = []
        for vertex in self.__graph_dict:
            for child in self.__graph_dict[vertex]:
                edges.append((vertex, child))
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def reverse(self):
        """
        In order to reverse the graph, we need to just swap the outbound 
        and inbound vertices
        """
        self.__graph_dict, self.__parent_dict = self.__parent_dict, self.__graph_dict
