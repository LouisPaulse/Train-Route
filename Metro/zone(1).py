import turtle as t
from tkinter import *
from metrorail_network2 import * # use the file that initializes the stations

## Louis: 3728436
## Martin: 3708931

z = []
epsilon = []

beta = open('stationsLoc.dat','r')
for line in beta:
	delta = line[:line.index('\n')]
	exec('z.append({})'.format(delta))


win = t.Screen()
win.title('Please click on origin station')
win.bgpic('CT_RailMap.gif')
win.setup(800,800)


def offsite(gamma):
	print(gamma, "ssss")
	global z
	global epsilon
	for station in z:
		sigma = gamma.upper()
		if station[2].code == sigma: 
			if len(epsilon) is 0:
				win.title('Please click on destination station')
				epsilon.append(station[2])
			else:
				win.title('Please click on origin station')
				x = epsilon[0].route_to(station[2])
				print(x)
				epsilon = []
			print(station[2].name)
			return
	print('Not FOUND')

def mapped():
	mu  = Tk()
	mu.title('Choose station manually')
	psi = StringVar()
	iota = Label(mu, text='Enter Station short code :')
	iota.grid(row=1, column=0)
	pi = Entry(mu, textvariable=psi)
	pi.grid(row=1, column=1)
	nu = Button(mu, text='Go', command=lambda:offsite(pi.get()))
	nu.grid(row=1, column = 2)
	

# on the original picture radius of the circles(station) is 10px
def x_y_co(x, y):
	global epsilon
	for t in z:
		x0 = t[0]-10
		x1 = t[0]+10
		y0 = t[1]-10
		y1 = t[1]+10
		if (x >= x0) and (x <= x1):
			if (y >= y0) and (y <= y1):
				if len(epsilon) is 0:
					epsilon.append(t[2])
					win.title('Please click on destination station')
				else:
					epsilon[0].route_to(t[2])
					epsilon = []
					win.title('Please click on origin station')
				print(t[2].name)
				return
	mapped()
#	print('Map')

win.onscreenclick(x_y_co)
t.mainloop()
