from graph import *
from utils import *
from queue import *

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
            neighbours = node.edges  

            for neighbour in neighbours :
                new_path = list(path)
                new_path.append(neighbour.end)
                queue.put(graph.nodes[next((i for i,v in enumerate(graph.nodes) if v.name == new_path),-1)])

                if neighbour == goal:
                    return new_path
            explored.append(node.name)
    
    print(explored)
    print("connecting path doesn't exist")
    return path



romania = Graph( ['Or', 'Ne', 'Ze', 'Ia', 'Ar', 'Si', 'Fa', 
		      'Va', 'Ri', 'Ti', 'Lu', 'Pi', 'Ur', 'Hi',
		      'Me', 'Bu', 'Dr', 'Ef', 'Cr', 'Gi'],
		     [
			('Or', 'Ze', 71), ('Or', 'Si', 151), 
			('Ne', 'Ia', 87), ('Ze', 'Ar', 75),
			('Ia', 'Va', 92), ('Ar', 'Si', 140),
			('Ar', 'Ti', 118), ('Si', 'Fa', 99), 
			('Si', 'Ri', 80), ('Fa', 'Bu', 211),
			('Va', 'Ur', 142), ('Ri', 'Pi', 97),
			('Ri', 'Cr', 146), ('Ti', 'Lu', 111),
			('Lu', 'Me', 70), ('Me', 'Dr', 75),
			('Dr', 'Cr', 120), ('Cr', 'Pi', 138),
			('Pi', 'Bu', 101), ('Bu', 'Gi', 90),
			('Bu', 'Ur', 85), ('Ur', 'Hi', 98), 
			('Hi', 'Ef', 86)
		     ] )

path=BF_search(romania, 'Bu' , 'Ti')
print(path)
