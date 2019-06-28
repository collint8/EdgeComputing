import numpy as np
import matplotlib.pyplot as pt
import matplotlib

"""##	This file takes the loss functions generated from the agg main and plots them using 
##	matplotlib. It expects an K*tau by N+1 matrix of loss function values and a list of lables 
##	of length y. Along the x axis are the loss function values for each iteration.
##	Iterating through y iterates through the nodes. 
##"""
def ParsFile(fnIn,labellist):
	stypes = ['None','Random','RoundRobin','SegShift']
	avtypes = ['mean','median','med_avg']
	
	x,y = np.shape(fnIn)
	colorl = ['b','magenta','g','r','limegreen','fuchsia','midnightblue','darkorange',\
	'darkgreen','darkmagenta','gray','black','orange']
	fig1, axf1 = pt.subplots(figsize=(10,6))
	for i in range(0,y):
		pt.plot(fnIn[:,i], color=colorl[i],marker='.')    # def move_figure(f, x, y):
	
	def move_figure(f, x, y):
		"""Move figure's upper left corner to pixel (x, y)"""
		backend = matplotlib.get_backend()
		if backend == 'TkAgg':
			f.canvas.manager.window.wm_geometry("+%d+%d" % (x, y))
		elif backend == 'WXAgg':
			f.canvas.manager.window.SetPosition((x, y))
		else:
			f.canvas.manager.window.move(x, y)

	
	move_figure(fig1,0,0)
	fig1.suptitle(labellist,style='italic',weight='bold',size='x-large')
	#pt.legend()
	pt.ylabel('Loss Function',style='italic',weight='bold',size='large')
	pt.xlabel('Iterations',style='italic',weight='bold',size='large')
	pt.grid(True)
	pt.show()