import matplotlib
matplotlib.use("TkAgg")  # ให้กราฟเด้งใน PyCharm ได้แน่นอน

import matplotlib.pyplot as plt
import networkx as nx
from collections import deque


class Graph_Structure:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        if neighbor not in self.graph:
            self.graph[neighbor] = []
        self.graph[node].append(neighbor)
        self.graph[neighbor].append(node)

    def show_graph(self):
        for node, neighbors in self.graph.items():
            print(node, "->", neighbors)

    def plot_graph(self, highlight_nodes=None, title="Graph Structure"):
        plt.close('all')
        G = nx.Graph(self.graph)
        pos = nx.spring_layout(G, seed=42)
        plt.figure(figsize=(6, 4))

        colors = []
        for n in G.nodes():
            colors.append("orange" if (highlight_nodes and n in highlight_nodes) else "skyblue")

        nx.draw(
            G, pos,
            with_labels=True,
            node_color=colors,
            node_size=1100,
            font_size=13,
            font_weight="bold",
            edge_color="gray"
        )

        if highlight_nodes:
            for i, n in enumerate(highlight_nodes, start=1):
                x, y = pos[n]
                plt.text(x, y + 0.05, str(i), ha="center", va="bottom")

        plt.title(title)
        plt.tight_layout()
        plt.show()

    def bfs(self, start):
        visited = set()
        q = deque([start])
        order = []
        while q:
            u = q.popleft()
            if u not in visited:
                visited.add(u)
                order.append(u)
                for v in self.graph[u]:
                    if v not in visited:
                        q.append(v)
        print("BFS:", " → ".join(order))
        self.plot_graph(order, title="Breadth-First Search (BFS)")

    def dfs(self, start):
        visited = set()
        order = []

        def go(u):
            if u in visited:
                return
            visited.add(u)
            order.append(u)
            for v in self.graph[u]:
                go(v)

        go(start)
        print("DFS:", " → ".join(order))
        self.plot_graph(order, title="Depth-First Search (DFS)")


if __name__ == "__main__":
    g = Graph_Structure()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'E')
    g.add_edge('D', 'F')

    print("โครงสร้างกราฟ:")
    g.show_graph()

    g.bfs('A')
    g.dfs('A')
