#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import math


infile=open('dados.txt','r')
the=[0]
w=[0]
a=[0]
e=[0]
t=[0]
de=[0]


for line in infile:
	x,y,z,v,b = line.split()
	the.append(float(x))
	w.append(float(y))
	a.append(float(z))
	e.append(float(v))
	t.append(float(b))



plt.figure(figsize=(8,5), dpi=96)
plt.axis([-1,20,-5,5])
plt.xticks(np.linspace(0,10,11,endpoint=True))

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
ax.xaxis.set_label_coords(0.5, -0.025)
ax.yaxis.set_label_coords(0.0000005, 0.5)


plt.rc('text', usetex=True) 
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
plt.xlabel(r'\textit{Tempo $(s)$}')
plt.ylabel(r'\textit{The $(Rad)$}')

#plt.yticks(np.linspace(-10,10,5,endpoint=True),
#	[r'$- A$',r'$- \frac{A}{2}$','',r'$\frac{A}{2}$',r'$A$'])
plt.title(r'Pendulo com arrasto - ThexT', fontsize=18)


plt.plot(t,the,'b',linewidth=1, label=r'\textit{$\gamma = 0.9 $ $W_0 = 10 rad/s$}' ) 
plt.legend(bbox_to_anchor=(1.1, 1), loc=1, borderaxespad=0.)
plt.savefig("verlettheg09.pdf",dpi=96)


# graf 2
plt.figure(figsize=(8,5), dpi=96)
plt.axis([-1,40,-15,15])
plt.xticks(np.linspace(0,10,11,endpoint=True))

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
ax.xaxis.set_label_coords(0.5, -0.025)
ax.yaxis.set_label_coords(0.0000005, 0.5)


plt.rc('text', usetex=True) 
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
plt.xlabel(r'\textit{Tempo $(s)$}')
plt.ylabel(r'\textit{W $(\frac{rad}{s})$}')

#plt.yticks(np.linspace(-10,10,5,endpoint=True),
#	[r'$- A$',r'$- \frac{A}{2}$','',r'$\frac{A}{2}$',r'$A$'])
plt.title(r'Pendulo com arrasto - WxT', fontsize=18)


plt.plot(t,w,'b',linewidth=1, label=r'\textit{$\gamma = 0.9 $ $W_0 = 10 rad/s$}' )  
plt.legend(bbox_to_anchor=(1.1, 1), loc=1, borderaxespad=0.)
plt.savefig("verletwg09.pdf",dpi=96)

infile.close()
  
