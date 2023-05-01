from utils import *
from queue import *

# return the cost of the chosen path
def cost(graph, path):
    node = graph.nodes[next((i for i,v in enumerate(graph.nodes) if v.name == path[0]), -1)]
    cost = 0
    for city in path:
        if node.name == city:
          continue
        for edge in node.edges:
            if edge.end.name == city:
                cost += edge.value
                node = edge.end
    return cost


# Breadth First Search
# return a list of the path, that should be taken based of the algorithm
def BF_Search(graph, start, goal):
    queue = Queue()
    queue.put((0,graph.nodes[next((i for i,v in enumerate(graph.nodes) if v.name == start), -1)],0))
    explored = []
    path=[]
    cost = 0

    if start == goal:
        print("Start and goal is the same")
        return [path,cost]

    while not queue.empty():
        q = queue.get()
        node = q[1]
        node.parent=q[2]
        if node.parent:
            node.value = node.parent.value + q[0]

        for neighbour in node.edges:
            if neighbour.end.name not in explored:
                queue.put((neighbour.value,neighbour.end,node))
                if neighbour.end.name == goal:
                        new_path = list(path)
                        new_path.append(neighbour.end.name)
                        parent = node
                        cost = node.value + neighbour.value
                        while parent != 0:
                             new_path.append(parent.name)
                             parent = parent.parent
                        new_path.reverse()
                        return [new_path, cost]
        explored.append(node.name)

    print("connecting path doesn't exist")
    return [path, cost]


# Depth First Search
# return a list of the path, that should be taken based of the algorithm
def DF_Search(graph, start, goal):
    queue = LifoQueue()
    queue.put((0,graph.nodes[next((i for i,v in enumerate(graph.nodes) if v.name == start), -1)],0))
    explored = []
    path = []
    cost = 0

    if start == goal:
        print("Start and goal is the same")
        return [path, cost]

    while not queue.empty():
        q = queue.get()
        node = q[1]
        node.parent = q[2]
        if node.parent:
            node.value = node.parent.value + q[0]

        for neighbour in node.edges:
            if neighbour.end.name not in explored:
                queue.put((neighbour.value,neighbour.end,node))
                if neighbour.end.name == goal:
                        new_path = list(path)
                        new_path.append(neighbour.end.name)
                        parent = node
                        cost = node.value + neighbour.value
                        while parent != 0:
                             new_path.append(parent.name)
                             parent = parent.parent
                        new_path.reverse()
                        return [new_path, cost]
        explored.append(node.name)

    print("Connecting path doesn't exist")
    return [path, cost]


# Uniform Cost Search
# return a list of the path, that should be taken based of the algorithm
def UC_Search(graph, start, goal):
    queue = PriorityQueue()
    queue.put((0,graph.nodes[next((i for i,v in enumerate(graph.nodes) if v.name == start), -1)],0))
    explored = []
    path = []
    cost = 0

    if start == goal:
        print("Start and goal is the same")
        return [path, cost]

    while not queue.empty():
        q = queue.get()
        node = q[1]
        node.parent = q[2]
        if node.parent:
            node.value = node.parent.value + q[0]

        for neighbour in node.edges:
            if neighbour.end.name not in explored:
                queue.put((neighbour.value, neighbour.end, node))
                if neighbour.end.name == goal:
                        new_path = list()
                        new_path.append(neighbour.end.name)
                        parent = node
                        while parent != 0:
                             new_path.append(parent.name)
                             parent=parent.parent
                        if cost == 0:
                            cost = node.value + neighbour.value
                            path = new_path
                        elif (node.value + neighbour.value) < cost:
                            cost = node.value + neighbour.value
                            path = new_path
        if node.name != goal:
            explored.append(node.name)
    if path[0] == goal:
        path.reverse()
        return [path, cost]
    print("Connecting path doesn't exist")
    return [path, cost]


