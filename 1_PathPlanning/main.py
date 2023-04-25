from graph import *
from utils import *
from queue import *




#
#cost function
#return the cost of the chosen path
#

def cost(graph,path):
    node = graph.nodes[next((i for i,v in enumerate(graph.nodes) if v.name == path[0]), -1)]
    cost = 0
    for city in path :
        if node.name == city:
          continue
        for edge in node.edges:
            if edge.end.name == city:
                cost += edge.value
                node=edge.end
    return cost
#
#Breadth First Search algorithm
#return a list of the path, that should be taken based of the algorithm
#
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
        if node.parent : 
            node.value = node.parent.value + q[0]

        for neighbour in node.edges :
            if neighbour.end.name not in explored:
                queue.put((neighbour.value,neighbour.end,node))
                if neighbour.end.name == goal:
                        new_path = list(path)
                        new_path.append(neighbour.end.name)
                        parent = node
                        cost = node.value+neighbour.value
                        while parent !=0:
                             new_path.append(parent.name)
                             parent=parent.parent
                        new_path.reverse()
                        return [new_path,cost]
        explored.append(node.name)
    
    print("connecting path doesn't exist")
    return [path,cost]

#
#Depth First Search algorith
#return a list of the path, that should be taken based of the algorithm
#
def DF_Search(graph, start, goal):
    queue = LifoQueue()
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
        if node.parent : 
            node.value = node.parent.value + q[0]

        for neighbour in node.edges :
            if neighbour.end.name not in explored:
                queue.put((neighbour.value,neighbour.end,node))
                if neighbour.end.name == goal:
                        new_path = list(path)
                        new_path.append(neighbour.end.name)
                        parent = node
                        cost = node.value+neighbour.value
                        while parent !=0:
                             new_path.append(parent.name)
                             parent=parent.parent
                        new_path.reverse()
                        return [new_path,cost]
        explored.append(node.name)

    print("connecting path doesn't exist")
    return [path,cost]

#
#Depth First Search algorith
#return a list of the path, that should be taken based of the algorithm
#
def UC_Search(graph, start, goal):
    queue = PriorityQueue()
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
        if node.parent : 
            node.value = node.parent.value + q[0]

        for neighbour in node.edges :
            if neighbour.end.name not in explored:
                queue.put((neighbour.value,neighbour.end,node))
                if neighbour.end.name == goal:
                        new_path = list()
                        new_path.append(neighbour.end.name)
                        parent = node
                        while parent !=0:
                             new_path.append(parent.name)
                             parent=parent.parent
                        if cost == 0 :
                            cost = node.value+neighbour.value
                            path = new_path
                        elif (node.value+neighbour.value) <cost:
                            cost = node.value+neighbour.value
                            path = new_path
        if node.name != goal:      
            explored.append(node.name)
    if path[0]==goal:
        path.reverse()
        return [path,cost]
    print("connecting path doesn't exist")
    return [path,cost]





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

#romania.print()
BFpath=BF_Search(romania, 'Bu' , 'Ti')
print("path: ", BFpath[0])
print("cost: ",BFpath[1])
DFpath=DF_Search(romania, 'Bu' , 'Ti')
print("path: ", DFpath[0])
print("cost: ",DFpath[1])
UCpath=UC_Search(romania, 'Bu' , 'Ti')
print("path: ", UCpath[0])
print("cost: ",UCpath[1])
