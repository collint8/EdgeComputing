import numpy as np
isImported = True
##	This File contains all the forms of shuffling used in our model
## 	Each one performs a simulated shuffle. It assumes that each node has the whole dataset
##  and will only perform calculations based on the section ascribed to its node number

##	Shuffle performs a complete randomization of the dataset. As each node performs this independantly,
##	their may be some points evaluated by multiple nodes simultaneously.
def Shuffle(data):
	np.random.shuffle(data)
	return data

## This form of shuffle rotates the entire dataset of one node to the next.
## Data from node n appears at node (n+1)%N
def rRobin(data,N=5,M=2):
	D,L = np.shape(data)
	d = int(D/N)
	temp = np.zeros(shape=(d,L))
	k = 0
	for i in data[0:d,:]:
			temp[k,:] = i
			k = k+1
	for n in range(0,N):
		inot = -n*d%D
		iprm = -(n+1)*d%D
		data[inot:inot+d,:] = data[iprm:iprm+d,:]
	data[d:2*d] = temp
	return data
	
##	Seg shift partitions the data held by each node into M smaller sections.
##	It then transfers each section to a different node (so long as M<N-1).
##	For each mth section in range (0,M) that section is transferred from node n
##	to node n+1+m%(N+1). Thus every section is always moved to a new node.
def segShift(data,N=5,M=2):
	D,L = np.shape(data)
	d = int(D/N)
	r = int(d/M)
	temp = np.zeros(shape=(r,L))
	for m in range(0,M):
		k = 0
		for i in data[m*r:m*r+r,:]:
			temp[k,:] = i
			k = k+1
		for n in range(0,N):
			inot = ((-n*m)%N*d)+m*r
			iprm = (-m-n*m)%N*d+m*r
			data[inot:inot+r,:] = data[iprm:iprm+r,:]
		data[(m-N*m)*d%D+m*r:(m-N*m)*d%D+m*r+r,:] = temp

	return data

## standardized usage for testing. 
if not isImported: 
	data = np.array([[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8]\
	,[9,9],[10,10],[11,11]])
	print(rrobin(data,N=2,M=3))