import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')
fig, axs = plt.subplots(3, sharex=True, sharey=True)

def graphplot(filename):
	fig.suptitle('Computer Information\nClient : '+filename[:-4])	
	def animate(i):
		global file
		graph_data = open("data/"+filename,'r').read()
		lines = graph_data.split('\n')
		xc = []
		yc = []
		xr = []
		yr = []
		xd = []
		yd = []
		for line in lines:
			if len(line) > 1:
				info=line.split('-')
				cpu  = info[0]
				ram  = info[1]
				disk = info[2]
				xcpu,ycpu = cpu.split(',')
				xram,yram =ram.split(',')
				xdisk,ydisk =disk.split(',')
				xc.append(float(xcpu))
				yc.append(float(ycpu))
				xr.append(float(xram))
				yr.append(float(yram))
				xd.append(float(xdisk))
				yd.append(float(ydisk))
		
		axs[0].clear()
		axs[0].plot(xc, yc,'b')
		axs[1].clear()
		axs[1].plot(xr, yr,'r')
		axs[2].clear()
		axs[2].plot(xd, yd,'g')
		axs[0].set(xlabel='', ylabel='CPU USAGE')
		axs[1].set(xlabel='', ylabel='RAM USAGE')
		axs[2].set(xlabel='TIME', ylabel='DISK USAGE')


	ani = animation.FuncAnimation(fig, animate, interval=500.)
	plt.show()
	plt.close()