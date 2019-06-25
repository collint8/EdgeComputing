import numpy as np
isImported = False
def Shuffle(data):
    np.random.shuffle(data)
    return data

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
	if N != 1:
            data[d:2*d] = temp
	return data
	
def segShift(data,N=5,M=2):
	D,L = np.shape(data)
	d = int(D/N)#data points per node
	r = int(d/M)#points per stub
	temp = np.zeros(shape=(r,L))
	for m in range(0,M):
		print('m=',m)
		k = 0
		for i in data[m*r:m*r+r,:]:
			temp[k,:] = i
			k = k+1
		print(temp)
		for n in range(0,N):
			inot = (-n*(m%(N-1)+1))%N*d+m*r
			iprm = (-1-n)*(m%(N-1)+1)%N*d+m*r
			data[inot:inot+r,:] = data[iprm:iprm+r,:]
			print(data)
		data[d*(m%(N-1)+1)+m*r:d*(m%(N-1)+1)+m*r+r,:] = temp
		print(data)
		
	return data 
if not isImported: 
	data = np.array([[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9]\
	,[9,10],[10,11],[11,12],[12,13],[13,14],[14,15]])
	print(data),
	print(segShift(data,N=5,M=3))
