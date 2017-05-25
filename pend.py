#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import math


x=input("valor de w_0 ?")
y=input("valor de gamma ?")

w=[x]
the=[0.]
a=[0.]
at=[0.]
wt=[0.]
t=[0.]
e=[0.]
de=[0.]
dt=0.01
m=1
l=10
g=9.8
gama=y


for tt in range(10000):

   the.append((the[-1]+w[-1]*dt+0.5*a[-1]*dt**2))
   at.append(-(w[0]**2)*math.sin(the[-1]) - gama*w[-1])
   wt.append(w[-1]+0.5*(a[-1]+at[-1])*dt)
   at.append(-(wt[0]**2)*math.sin(the[-1]) - gama*wt[-1])
   w.append(w[-1]+0.5*(a[-1]+at[-1])*dt)
   a.append(-(w[0]**2)*math.sin(the[-1])-gama*w[-1])
   t.append(t[-1]+dt)
   e.append((w[-1]**2)/2 + m*g*(l-l*math.cos(the[-1])))
   
   
outfile=open('dados.txt','w')
for i in range(len(t)):
		outfile.write("%s	%s	%s	%s	%s \n" % (the[i],w[i],a[i],e[i],t[i]))
outfile.close()
	
