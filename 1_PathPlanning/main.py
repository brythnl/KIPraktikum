from graph import *
from algorithms import *

# Test adjacency matrix
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
BFpath = BF_Search(romania, 'Bu' , 'Ti')
print("Breadth First Search:\n===============================")
print("path: ", BFpath[0])
print("cost: ", BFpath[1], '\n')

DFpath = DF_Search(romania, 'Bu' , 'Ti')
print("Depth First Search:\n===============================")
print("path: ", DFpath[0])
print("cost: ", DFpath[1], '\n')

UCpath = UC_Search(romania, 'Bu' , 'Ti')
print("Uniform Cost Search:\n===============================")
print("path: ", UCpath[0])
print("cost: ", UCpath[1], '\n')
