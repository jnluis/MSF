import numpy as np
import matplotlib.pyplot as plt

t=np.array([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5])
s=np.array([0.1, 1.4, 1.7, 6.5, 7.7, 10.4, 19.5, 26.1, 26.5, 45.9, 52.5])

npontos = len(t)

x=t
y=s

def regressaoLinear(x, y):
    npontos=x.size
    
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
    
    return m, dm, b, db, r2


logx= np.log(t)
logy=np.log(s)
xmax=np.max(logx)*1.1
xmin=np.min(logx)*0.9

x = np.linspace(xmin, xmax, 100)
m= regressaoLinear(logx, logy)[0]
dm = regressaoLinear(logx, logy)[1]
b=regressaoLinear(logx, logy)[2]
db = regressaoLinear(logx, logy)[3]
r2 = regressaoLinear(logx, logy)[4]

print()
print("m +/-dm = {:0.8f} +/- {:0.8f}".format(m,dm))
print("b +/-db = {:0.8f} +/- {:0.8f}".format(b,db))
print("r2 = {:0.8f}".format(r2))

plt.plot(x,m*x+b)
plt.plot(logx, logy, "ro")
plt.show()