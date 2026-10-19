import networkx as nx
import matplotlib.pyplot as plt

#instantiating a node class
class Node():
    def __init__(self, state, parent, hn=0):
        self.state = state
        self.parent = parent
        self.action = []
        self.hn = hn
    
    def add_action(self, action, gn):
        self.action.append((action, gn))
        return ((self.state, action.state), action.hn)

    def actions(self):
        for action in self.action:
            print(action[0].state, end =" ")

class AStar():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        c=float('inf')
        if self.empty():
            raise Exception("empty frontier")
        elif len(self.frontier)==1:
            index=0
        else:
            for node in self.frontier:
                parent=node.parent
                edgev=0
                for action in parent.action:
                    if(action[0]==node):
                        edgev=action[1]
                if(node.hn + edgev < c):
                    index = self.frontier.index(node)
        return self.frontier.pop(index)

#creating node
Arad = Node(state="Arad", parent=None, hn=366)
Zerind = Node(state="Zerind", parent=Arad, hn=374)
Oradea = Node(state="Oradea", parent=Zerind, hn=380)
Sibiu = Node(state="Sibiu", parent=Arad, hn=253)
Rimnicu_Vilcea = Node(state="Rimnicu Vilcea", parent=Sibiu, hn=193)
Craiova = Node(state="Craiova", parent=Rimnicu_Vilcea, hn=160)
Drobeta = Node(state="Drobeta", parent=Craiova, hn=142)
Mehadia = Node(state="Mehadia", parent=Drobeta, hn=0)
Timisoara = Node(state="Timisoara", parent=Arad, hn=329)
Lugoj = Node(state="Lugoj", parent=Mehadia, hn=0)
Pitesti = Node(state="Pitesti", parent=Craiova, hn=98)
Bucharest = Node(state="Bucharest", parent=Pitesti, hn=0)
Giurgiu = Node(state="Giurgiu", parent=Bucharest, hn=77)
Fagaras = Node(state="Fagaras", parent=Sibiu, hn=178)
Neamt = Node(state="Neamt", parent=None, hn=0)
Iasi = Node(state="Iasi", parent=Neamt, hn=0)
Vaslui = Node(state="Vaslui", parent=Iasi, hn=0)
Urziceni = Node(state="Urziceni", parent=Vaslui, hn=80)
Eforie = Node(state="Eforie", parent=None, hn=0)
Hirsova = Node(state="Hirsova", parent=Eforie, hn=0)

#instantiating a graph
Graph = nx.DiGraph()

pcost=dict([
    Arad.add_action(Timisoara, 118),
    Arad.add_action(Zerind, 75),
    Arad.add_action(Sibiu, 140),
    Zerind.add_action(Oradea, 71),
    Oradea.add_action(Sibiu, 151),
    Sibiu.add_action(Fagaras, 99),
    Sibiu.add_action(Rimnicu_Vilcea, 80),
    Craiova.add_action(Rimnicu_Vilcea, 146),
    Drobeta.add_action(Craiova, 120),
    Mehadia.add_action(Drobeta, 75),
    Lugoj.add_action(Mehadia, 70),
    Timisoara.add_action(Lugoj, 111),
    Craiova.add_action(Pitesti, 138),
    Pitesti.add_action(Rimnicu_Vilcea, 97),
    Rimnicu_Vilcea.add_action(Pitesti, 97),
    Pitesti.add_action(Bucharest, 101),
    Giurgiu.add_action(Bucharest, 90),
    Fagaras.add_action(Bucharest, 211),
    Neamt.add_action(Iasi, 87),
    Iasi.add_action(Vaslui, 92),
    Vaslui.add_action(Urziceni, 142),
    Urziceni.add_action(Bucharest, 85),
    Eforie.add_action(Hirsova, 86),
    Hirsova.add_action(Urziceni, 98),
])

pos = {
    "Arad": (1, 2),
    "Zerind": (1.5, 2.5),
    "Timisoara": (1.5, 1),
    "Lugoj": (3.7, 0.7),
    "Oradea": (2, 3),
    "Sibiu": (4.8, 1.8),
    "Rimnicu Vilcea": (6, 1.3),
    "Craiova": (6.7, -0.8),
    "Drobeta": (4, -0.6),
    "Mehadia": (4, 0.2),
    "Pitesti": (8.7, 1),
    "Bucharest": (12.5, 0),
    "Giurgiu": (12, -0.8),
    "Fagaras": (8.5, 1.8),
    "Neamt": (14, 3),
    "Iasi": (16, 2),
    "Vaslui": (15, 1),
    "Urziceni": (14, 0.5),
    "Eforie": (18, -0.8),
    "Hirsova": (16, 0.4)
}

#adding actions
Graph.add_edges_from(pcost.keys())

#drawing actions
nx.draw_networkx(Graph, pos, node_size=3000, node_color='orange', font_size=10, font_weight='bold', edge_color='gray')
nx.draw_networkx_edge_labels(Graph, pos, edge_labels=pcost)   
plt.show()


#setting the goal
goal = Bucharest

#empty solution
solution = []

#empty frontier
frontier = AStar()

#empty explored set
explored = []

#add the initial state to the frontier
frontier.add(Arad)

while True:
    #if the frontier is empty, then no solution
    if frontier.empty():
        raise Exception("no solution")

    #remove a node from the frontier
    print("frontier: ", end="")
    for front in frontier.frontier:
        print(front.state, end=", ")
    node = frontier.remove()
    print("\nremove: "+node.state)
    
    
    solution.append(node.state)

    #if node contains goal state, return the solution
    if goal.state == node.state:
        print("[SOLVED]:" + str(solution))
        break

    #adding to the explored set
    explored.append(node)
    print("explored: ", end="")
    for exp in explored:
        print(exp.state, end=", ")

    #expanding the node and adding the resulting node/s to the frontier
    print("\npossible action: ", end="")
    for action in node.action:
        if not frontier.contains_state(action[0]) and action[0] not in explored:
            print(action[0].state, end=", ")
            frontier.add(action[0])
        else:
            print("nah")
    print("\n\n")