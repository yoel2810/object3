import unittest
from DiGraph import DiGraph

class MyTestCase(unittest.TestCase):

    def test_something(self):
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        self.assertEqual(len(g.nodes), 4)
        g.remove_node(3)
        self.assertEqual(len(g.nodes), 3)
        g.add_edge(0, 1, 5)
        g.add_edge(1, 2, 0.2)
        self.assertEqual(g.e_size(), 2)
        g.remove_edge(1, 2)
        self.assertEqual((1, 2, 0.2) in g.edges, False)
        self.assertEqual(g.e_size() == 1, True)
        g.remove_node(0)
        self.assertEqual(g.e_size() == 0, True)

if __name__ == '__main__':
    unittest.main()

