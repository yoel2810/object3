from DiNode import DiNode
from GraphInterface import GraphInterface

class DiGraph(GraphInterface):

    def __init__(self):
        self.nodes = {}
        self.edges_number = 0
        self.mc = 0
        self.edges = []

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return self.edges_number

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.nodes[id1].get_in_edges()

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.nodes[id1].get_out_edges()

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self.nodes and id2 in self.nodes:
            if not id2 in self.nodes[id1].get_out_edges():
                self.nodes[id1].get_out_edges()[id2] = (id1, id2, weight)
                self.edges.append((id1, id2, weight))
                self.nodes[id2].get_in_edges()[id1] = (id1, id2, weight)
                self.edges_number = self.edges_number + 1
                self.mc = self.mc + 1
                return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes:
            return False
        else:
            self.nodes[node_id] = DiNode(node_id, pos)
            self.mc = self.mc + 1
            return True

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.nodes:
            del self.nodes[node_id]
            self.mc = self.mc + 1
            return True
        else:
            return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 in self.nodes and node_id2 in self.nodes:
            if node_id2 in self.nodes[node_id1].get_out_edges():
                self.edges.remove(self.nodes[node_id1].get_out_edges()[node_id2])
                del self.nodes[node_id1].get_out_edges()[node_id2]
                del self.nodes[node_id2].get_in_edges()[node_id1]
                self.mc = self.mc + 1
                return True
        return False

    def get_node(self, id: int) -> DiNode:
        if id in self.nodes.keys():
            return self.nodes[id]
        return None

    def get_all_e(self):
        return self.edges

    def __str__(self):
        #Graph: | V |= 4, | E |= 5
        return ("Graph: |V|=" + str(len(self.nodes)) + " , " + "|E|=" + str(self.e_size()))