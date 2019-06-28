import numpy as np
import pandas as pd

### read the converts a read .csv matrix into useable arrays. capable of variable lengths
### reads numPoint values out of dataset data, Converts values to be useable in SVM,
### and outputs them in the vectors x and y.
### Can skip the first offset values or select only the values found in case but
### default is read all values starting at 0


def pandaRead(numPoints, filepath=r"train.csv", offset=0, case=None):
	filepath = r'train.csv'
	data = pd.read_csv(filepath, skiprows=(numPoints*(offset)), nrows=numPoints).values
	D,L = np.shape(data)

	pointstart=0
	pointend = numPoints
	nData = np.zeros(shape=(D,L))
	x = np.array(data[pointstart:pointend,1:])/255
	y = np.array(data[pointstart:pointend,0])

	### Select particular values in case
	if case!=None:
		ttab = np.zeros(numPoints, dtype=bool)
		points = np.size(case)
		for i in range(0,points):
			ttab = ttab + (y==case[i])
		x = x[ttab,]
		y = y[ttab]
	### adjust y values to 1 if even and -1 if odd.

	for i in range(0, D):
		if y[i]%2 == 0:
			y[i] = 1
		else:
			y[i] = -1
	nData[:,0] = y
	nData[:,1:] = x
	return nData
if False:
    Data = pandaRead(4)
    print(Data)