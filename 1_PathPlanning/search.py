from queue import *
from graph import *


def BF_search(graph, start, goal):
    queue = Queue()
    queue.put(graph.nodes[next((i for i,v in enumerate(graph.nodes) if v.name == start), -1)])
    explored = []
    path=[]

    if start == goal:
        print("Start and goal is the same")
        return path

    while not queue.empty():
        node = queue.get()
        path.append(node.name)

        if node.name not in explored:
            neighbours = node.egdes  

            for neighbour in neighbours :
                new_path = list(path)
                new_path.append(neighbour[1])
                queue.put(graph.nodes[next((i for i,v in enumerate(graph.nodes) if v.name == neighbour[1].name), -1)])

                if neighbour == goal:
                    return new_path
            explored.append(node.name)

    print("connecting path doesn't exist")
    return path
