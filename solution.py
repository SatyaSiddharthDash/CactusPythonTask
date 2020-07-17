from structures import Graph, Digraph
from cycles import strongly_connected_components
from search import find_LCA, find_HCC


def edges_iterator():
    with open('data.txt') as infile:
        header1 = infile.readline()
        header2 = infile.readline()
        for edge in infile.readlines():
            parent, child = edge.strip().split('\t')
            yield (int(parent), int(child))


if __name__ == "__main__":
    G = Digraph()

    # The following code imitates the graph given in the question
    G.add_edge((0, 1))
    G.add_edge((0, 2))
    G.add_edge((1, 3))
    G.add_edge((1, 4))
    G.add_edge((2, 5))
    G.add_edge((2, 6))
    G.add_edge((6, 7))
    G.add_edge((6, 8))
    G.add_edge((6, 9))
    G.add_edge((8, 10))
    G.add_edge((8, 11))
    G.add_edge((11, 12))
    G.add_edge((11, 13))
    G.add_edge((11, 14))

    # Uncomment the following lines in order to check if the algorithm works with cycles as well.
    # G.add_edge((4, 15))
    # G.add_edge((13, 15))
    # G.add_edge((15, 0))

    # Uncomment the following lines if you want to check of the algorithm works with more complicated cycles present
    # G.add_edge((4, 16))
    # G.add_edge((16, 17))
    # G.add_edge((17, 18))
    # G.add_edge((18, 19))
    # G.add_edge((19, 15))
    # G.add_edge((17, 1))
    # G.add_edge((15, 20))
    # G.add_edge((20, 8))
    # G.add_edge((8, 0))
    # G.add_edge((4, 2))
    # G.add_edge((2, 4))

    print(find_HCC(G, 2, 4))
    print(find_LCA(G, 4, 2))
