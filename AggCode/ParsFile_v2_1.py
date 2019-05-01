import numpy as np
import matplotlib.pyplot as pt
import matplotlib


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