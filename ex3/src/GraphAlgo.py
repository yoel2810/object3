from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from PriorityQueue import PriorityQueue
from DiGraph import DiGraph
from DiNode import DiNode
from typing import List
import json
import math
import networkx as nx
import matplotlib.pyplot as plt

class GraphAlgo (GraphAlgoInterface):

    def __init__(self, graph: GraphAlgoInterface = DiGraph()):
        self.graph = graph
        self.visited = {}
        self.stack = []
        self.lowlink = {}
        self.components = []
        self.time = 0

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name + ".json", 'r') as f:
                arr = json.load(f)
                self.graph = DiGraph()
                for n in arr["Nodes"]:
                    if "pos" in n.keys(): #if there is a position
                        self.graph.add_node(n["id"], n["pos"])
                    else:
                        self.graph.add_node(n["id"])

                for e in arr["Edges"]:
                    self.graph.add_edge(e["src"], e["dest"], e["w"])

                return True
        except:
            return False

    def save_to_json(self, file_name: str) -> bool:
        nodes = []
        edges = []
        for i in self.graph.get_all_v().keys():
            if self.graph.get_node(i).get_pos() != None: #if there is a position
                nodes.append({"pos": self.graph.get_node(i).get_pos()})
            nodes.append({"id": i})
            for e in self.graph.get_node(i).get_out_edges().values():
                edges.append({
                    "src": e[0],
                    "dest": e[1],
                    "w": e[2]
                })

        arr = {
            "Nodes": nodes,
            "Edges": edges
        }
        try:
            with open(file_name + ".json", 'w') as json_file:
                json.dump(arr, json_file)
                return True
        except:
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if id1 == id2:
            a = []
            a.append(self.graph.get_node(id1));
            return a

        visited = {}
        dijk = self.dijkstra(self.graph.get_node(id1))
        parents = dijk[0]
        path = []
        rev = []
        id3 = id2
        while(id1!=id2):
            path.append(id2)
            node = self.graph.get_node(id2)
            if node == None:
                return (math.inf, None)
            if not node.get_id() in visited.keys():
                visited[node.get_id()] = False
            else:
                if visited[node.get_id()] == True:
                    return (math.inf, None)
            visited[node.get_id()] = True
            if parents[node.get_id()] == None:
                return (math.inf, None)
            id2 = parents[node.get_id()].get_id()
        path.append(id2)
        for i in range(0, len(path)):
            rev.append(path[len(path) - 1 - i])


        ret = dijk[1][id3]
        #this.init(initg)
        if ret < 2147483647: #max integer
            return (ret, rev)
        else:
            return (math.inf, None)
        #this.init(initg);

    def dijkstra(self, s: DiNode):
        visited = {}
        parents = {}
        q = PriorityQueue()
        dist = {}
        for x in self.graph.get_all_v().keys():
            dist[x] = 9223372036854775807
            visited[x] = False
            parents[x] = None
            q.insert(self.graph.get_node(x))

        dist[s.get_id()] = 0

        while q.isEmpty() == False:
            u = q.delete(dist)
            for k in u.get_out_edges().keys():
                v = self.graph.get_node(k)
                if visited[k] == False:
                    t = dist[u.get_id()] + u.get_out_edges()[k][2]
                    if dist[v.get_id()] > t:
                        #q.remove(v)
                        dist[v.get_id()] = t
                        parents[v.get_id()] = u
                        #q.insert(v)
            visited[u.get_id()] = True
        return (parents, dist)

    def connected_component(self, id1: int) -> list:
        components = self.connected_components()
        for c in components:
            if id1 in c:
                return c
        return None

    def connected_components(self) -> List[list]:
        self.visited = {}
        self.stack = []
        self.lowlink = {}
        for node in self.graph.get_all_v().values():
            self.visited[node.get_id()] = False
            self.lowlink[node.get_id()] = 0

        self.components = []
        self.time = 0

        for node in self.graph.get_all_v().values():
            if self.visited[node.get_id()] == False:
                #self.dfs(node.get_id())
                self.dfs(node.get_id())

        return self.components;

    def dfs(self, key: int): #same thing but not recursive
        rec_stack = [key] #it's like recursive stack
        uIsComponentRoot = {}
        while len(rec_stack) != 0:
            key = rec_stack[-1]
            del rec_stack[-1]
            if not self.visited[key]:
                uIsComponentRoot[key] = True
                self.lowlink[key] = self.time
                self.time = self.time + 1
                self.stack.append(key)
                self.visited[key] = True
            recurse = False
            for j in self.graph.get_node(key).get_out_edges().keys():
                if not self.visited[j]:
                    rec_stack.append(key)
                    rec_stack.append(j)
                    self.visited[j] = False
                    recurse = True
                    break

                if self.lowlink[key] > self.lowlink[j]:
                    self.lowlink[key] = self.lowlink[j]
                    uIsComponentRoot[key] = False
            if recurse:
                continue

            if uIsComponentRoot[key] == True:
                component = []
                while True:
                    n = self.stack.pop()
                    component.append(n)
                    self.lowlink[n] = 9223372036854775807
                    if n == key:
                        break
                self.components.append(component)



    def dfs_recursive(self, key: int):

        self.lowlink[key] = self.time
        self.time = self.time + 1
        self.visited[key] = True
        self.stack.append(key)
        uIsComponentRoot = True;

        for v in self.graph.get_node(key).get_out_edges().keys():
            if self.visited[v] == False:
                self.dfs_recursive(v)

            if self.lowlink[key] > self.lowlink[v]:
                self.lowlink[key] = self.lowlink[v]
                uIsComponentRoot = False


        if uIsComponentRoot == True:
            component = []
            while (True):
                x = self.stack.pop();
                component.append(x);
                self.lowlink[x] = 9223372036854775807
                if (x == key):
                    break

            self.components.append(component)

    def plot_graph(self) -> None:
        g = nx.DiGraph()
        g.add_nodes_from(self.graph.get_all_v())
        g.add_weighted_edges_from(self.graph.get_all_e())
        pos = {}
        for n in self.graph.get_all_v().values():
            if n.get_pos() != None:
                x = n.get_pos().split(",")
                pos[n.get_id()] = (float(x[0]), float(x[1]))#(n.get_pos()[0], n.get_pos()[1])
                g.nodes[n.get_id()]['pos'] = pos[n.get_id()]
            else:
                pos = nx.spring_layout(g)
        nx.draw_networkx(g, pos)
        #labels = nx.get_edge_attributes(g, 'weight')

        #nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

        plt.show()
        return None