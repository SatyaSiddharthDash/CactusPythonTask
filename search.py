from structures import Digraph
from collections import defaultdict
from itertools import zip_longest


def BFS(G: Digraph, source: int, reverse: bool = False):
    if source not in G.graph_dict:
        if source not in G.parent_dict:
            raise Exception("Source vertex not in graph")
    visited = defaultdict(bool)
    queue = []
    queue.append(source)
    visited[source] = True
    if reverse:
        while queue:
            s = queue.pop(0)
            yield visited
            for v in G.graph_dict[s]:
                if not visited[v]:
                    queue.append(v)
                    visited[v] = True
    else:
        while queue:
            s = queue.pop(0)
            yield visited
            for v in G.parent_dict[s]:
                if not visited[v]:
                    queue.append(v)
                    visited[v] = True


def check_visited(visited1: defaultdict, visited2: defaultdict) -> bool:
    for key in visited1.keys():
        if key in visited2.keys():
            if visited1[key] == visited2[key]:
                return key
    return -1


def find_LCA(G: Digraph, node1: str, node2: str, reverse: bool = False) -> str:
    if node1 not in G.graph_dict or node2 not in G.graph_dict:
        if node1 not in G.parent_dict or node2 not in G.parent_dict:
            raise Exception('Vertices not in Graph')
    visited1_default = defaultdict(bool)
    visited2_default = defaultdict(bool)
    visited1_default[node1] = True
    visited2_default[node2] = True
    common_vertices = set()
    for visited1, visited2 in zip_longest(BFS(G, node1, reverse),
                                          BFS(G, node2, reverse)):
        if not visited1:
            visited1 = visited1_default
        elif not visited2:
            visited2 = visited2_default

        common_vertex = check_visited(visited1, visited2)
        if common_vertex != -1:
            common_vertices.add(common_vertex)
        visited1_default = visited1
        visited2_default = visited2

    if common_vertices:
        return common_vertices

    return -1


def find_HCC(G: Digraph, node1: str, node2: str) -> str:
    return find_LCA(G, node1, node2, reverse=True)
