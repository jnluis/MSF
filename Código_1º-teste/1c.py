import numpy as np
import matplotlib.pyplot as plt


t=np.array([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5])
s=np.array([0.1, 1.4, 1.7, 6.5, 7.7, 10.4, 19.5, 26.1, 26.5, 45.9, 52.5])
npontos = len(s)

x=t**2.011
y=s

xy=x*y 
x2=x*x
y2=y*y

sx=x.sum()
sy=y.sum()
sxy=xy.sum()
sxx=x2.sum()
syy=y2.sum()

n=npontos
rn=n*sxy-sx*sy
rd=(n*sxx-sx**2)*(n*syy-sy**2)
r2=rn**2/rd
r=np.sqrt(r2)
m=(n*sxy-sx*sy)/(n*sxx-sx**2)
dm=abs(m)*np.sqrt((1/r**2-1)/(n-2))
bn=sxx*sy-sx*sxy  
bd=n*sxx-sx**2
b=bn/bd
db=dm*np.sqrt(sxx/n)

print()
print("m +/-dm = {:0.8f} +/- {:0.8f}".format(m,dm))
print("b +/-db = {:0.8f} +/- {:0.8f}".format(b,db))
print("r2 = {:0.8f}".format(r2))
 
z=np.polyfit (x,y,1)
M=z[0] 
B=z[1] 

plt.scatter(x, y) 
plt.plot(x,x*M+B) 
plt.xlabel("t^2.011") 
plt.ylabel("s(m)")
plt.show()

