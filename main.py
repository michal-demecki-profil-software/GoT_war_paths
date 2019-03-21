from sys import argv, stdin, stdout
from typing import TextIO, List

import matplotlib.pyplot as plt
from networkx import DiGraph, draw_shell, bfs_edges


def get_input_stream(file_path=None):
    if file_path is None:
        return stdin
    return open(file_path, 'r')


def load_graph(input_stream: TextIO) -> DiGraph:
    graph = DiGraph()
    n = int(input_stream.readline())
    graph.add_nodes_from(range(1, n + 1))
    for _ in range(int(input_stream.readline())):
        edge_src, edge_dest = input_stream.readline().split(' ')
        graph.add_edge(int(edge_src), int(edge_dest))
    return graph


def draw_graph(graph):
    draw_shell(graph, with_labels=True, font_weight='bold')
    plt.show()


def get_paths(graph: DiGraph) -> List[List[int]]:
    paths = []
    same_node_edges = [src for src, dst in graph.in_edges() if src == dst]
    candidates = [node for node, degree in graph.in_degree() if degree == (0 + int(node in same_node_edges))]
    for candidate in candidates:
        new_graph = graph.copy()
        new_graph.remove_node(candidate)
        new_paths = []
        if graph.number_of_nodes() == 1:
            new_path = [candidate]
            new_paths.append(new_path)
        else:
            recursive_paths = get_paths(new_graph)
            for path in recursive_paths:
                new_path = [candidate]
                new_path.extend(path)
                if len(new_path) == graph.number_of_nodes():
                    new_paths.append(new_path)
        paths.extend(new_paths)
    return paths


def main(input_stream: TextIO):
    graph = load_graph(input_stream)
    war_paths = get_paths(graph)
    stdout.write(f"{(len(war_paths))}\n")
    for path in war_paths:
        path_str = ' '.join([str(city) for city in path])
        stdout.write(f"{path_str}\n")


if __name__ == '__main__':
    file_path = None
    if len(argv) == 2:
        file_path = argv[1]
    with get_input_stream(file_path) as stream:
        main(stream)
