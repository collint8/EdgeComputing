import pandas as pd
import numpy as np

def AccTest(ww,testpoints=2000):
	totalpoints = 42000
	w = ww
	filepath = r'train.csv'
	testfile = filepath
	data = pd.read_csv(testfile, nrows=testpoints, skiprows = totalpoints-testpoints).values
	x, y = pandaRead(testpoints, data,0)
	acc = testW(w,x,y)
	return acc

def testW(win,x,y):
	w = np.array(win)
	#h should be approx y
	D,l = np.shape(x)
	h = np.dot(x,w.transpose())
	h[h>0] = 1
	h[h<0] = -1
	errcount = 0
	for i in range(0, D):
		if y[i] != h[i]:
			errcount += 1
	accuracy = (1-errcount/D)*100

	return accuracy

def pandaRead(numPoints, data, offset=0, case=None):
	x = np.array(data[:,1:])/255
	y = np.array(data[:,0])
	### adjust y values to 1 if even and -1 if odd.
	D,_ = np.shape(x)
	for i in range(0, D):
		if y[i]%2 == 0:
			y[i] = 1
		else:
			y[i] = -1
			
	return x,y
