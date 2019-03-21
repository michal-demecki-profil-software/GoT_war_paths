import unittest

from networkx import DiGraph

from main import get_paths, get_input_stream, load_graph


class AcceptanceTests(unittest.TestCase):
    def test_sample0(self):
        expected = [
            [1, 2, 3, 4],
            [1, 2, 4, 3]
        ]
        with get_input_stream('sample0.input') as input_stream:
            graph = load_graph(input_stream)
        actual = get_paths(graph)
        self.assertEqual(expected, actual)

    def test_sample1(self):
        expected = []
        with get_input_stream('sample1.input') as input_stream:
            graph = load_graph(input_stream)
        actual = get_paths(graph)
        self.assertEqual(expected, actual)


class TestGetPaths(unittest.TestCase):
    def test_get_paths_zero_edges(self):
        expected = [[1]]
        graph = DiGraph()
        graph.add_node(1)
        actual = get_paths(graph)
        self.assertEqual(expected, actual)

    def test_get_paths_self_edge(self):
        expected = [[1]]
        graph = DiGraph()
        graph.add_node(1)
        graph.add_edge(1, 1)
        actual = get_paths(graph)
        self.assertEqual(expected, actual)

    def test_get_paths_two_separate_nodes(self):
        expected = [[1, 2], [2, 1]]
        graph = DiGraph()
        graph.add_nodes_from(range(1, 3))
        actual = get_paths(graph)
        self.assertEqual(expected, actual)

    def test_get_paths_two_connected_nodes(self):
        expected = [[1, 2]]
        graph = DiGraph()
        graph.add_nodes_from(range(1, 3))
        graph.add_edge(1, 2)
        actual = get_paths(graph)
        self.assertEqual(expected, actual)

    def test_get_paths_with_two_possibilities(self):
        expected = [[1, 2, 3], [1, 3, 2]]
        graph = DiGraph()
        graph.add_nodes_from(range(1, 4))
        graph.add_edge(1, 2)
        graph.add_edge(1, 3)
        actual = get_paths(graph)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
