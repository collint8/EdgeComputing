import numpy as np
import random
import time
import pandaRead

timelog = False
isImported = True #set to false to run immediately

### SVM Gradient Descent. Takes training vector x and lables y to perform T iterations. 
	###lambda and eta ajust the rate of convergence.
	### Outputs SVM vector w. And vector of loss functions fn for convergence analysis
		### would like fn to be an opaque variable to call only if desired
def svm(x,y,w,tau,eta=.01, lam=1):
	D, n = np.shape(x)
	#W = np.zeros(tau,n)
	fn = np.zeros(tau)
	for k in range( 0, int(tau)):
		dfn = np.zeros(n)
		for j in range(0 , D):
			wT = w.transpose()
			if (1-y[j]*np.dot(wT, x[j]))<0:
				max = 0
			else:
				max = 1-y[j]*np.dot(wT, x[j])
			fn[k] += ((lam/2)*np.dot(w, wT)**2 + (max**2)/2)/D
			for i in range(0,n):
				dfn[i] += (lam*w[i]-(y[j]*x[j,i])*max)/D
		w = w - eta*dfn
	return w, fn



### w is the weight, N is the node number. tau is the number of local uptdates 
	### before the global update. D is the number of data points. 

def NodeSVM(w, data, tau=10, eta=.01, lam=1):
	if timelog:
		starttime=time.time()	
		lasttime = starttime
	
	D,_ = np.shape(data)

	x = np.array(data[:,1:])
	y = np.array(data[:,0])
	#print("Data samples: %i, Iterations: %i" %(D,tau))
	if timelog:
		unpacktime = time.time() - lasttime
		lasttime = time.time()
		print("--- Unpacking %s seconds ---"%unpacktime)
	
	
	w, fn = svm(x,y,w,tau,eta,lam)
	#print(w)\

	if timelog:
		endtime= time.time() -lasttime
		lasttime = time.time()
		print("--- Computation %s seconds ---" %(endtime))
	
		totaltime = time.time() - starttime
		print("--- Total %s seconds ---" %(totaltime))
	
	return w, fn
if not isImported:
    data = pandaRead.pandaRead(4)
    w = np.zeros(784)
    N = 0
    w,fn = NodeSVM(w,data)

