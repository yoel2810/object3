import unittest
from GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
    def test_something(self):
        ga = GraphAlgo()
        ga.graph.add_node(0)
        ga.graph.add_node(1)
        ga.graph.add_node(2)
        ga.graph.add_node(3)
        ga.graph.add_node(4)
        ga.graph.add_node(5)
        ga.graph.add_edge(0, 5, 5.5)
        ga.graph.add_edge(5, 2, 9)
        ga.graph.add_edge(2, 0, 15)
        ga.graph.add_edge(4, 0, 0.2)
        ga.graph.add_edge(4, 2, 3.5)
        ga.graph.add_edge(4, 1, 1)
        ga.graph.add_edge(4, 3, 0.1)
        ga.graph.add_edge(1, 3, 6)
        ga.graph.add_edge(3, 1, 0.2)

        ga.save_to_json("ga_tets")
        ga.load_from_json("ga_tets")

        print(ga.connected_components())
        print(ga.connected_component(3))
        print(ga.shortest_path(4, 1))


if __name__ == '__main__':
    unittest.main()
