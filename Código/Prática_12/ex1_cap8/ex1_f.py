
import matplotlib.pyplot as plt
import numpy as np

def abfourier(tp,xp,it0,it1,nf):
#
# cálculo dos coeficientes de Fourier a_nf e b_nf
#       a_nf = 2/T integral ( xp cos( nf w) ) dt   entre tp(it0) e tp(it1)
#       b_nf = 2/T integral ( xp sin( nf w) ) dt   entre tp(it0) e tp(it1)    
# integracao numerica pela aproximação trapezoidal
# input: matrizes tempo tp   (abcissas)
#                 posição xp (ordenadas) 
#       indices inicial it0
#               final   it1  (ao fim de um período)   
#       nf índice de Fourier
# output: af_bf e bf_nf  
# 
    dt=tp[1]-tp[0]
    per=tp[it1]-tp[it0]
    ome=2*np.pi/per

    s1=xp[it0]*np.cos(nf*ome*tp[it0])
    s2=xp[it1]*np.cos(nf*ome*tp[it1])
    st=xp[it0+1:it1]*np.cos(nf*ome*tp[it0+1:it1])
    soma=np.sum(st)
    
    q1=xp[it0]*np.sin(nf*ome*tp[it0])
    q2=xp[it1]*np.sin(nf*ome*tp[it1])
    qt=xp[it0+1:it1]*np.sin(nf*ome*tp[it0+1:it1])
    somq=np.sum(qt)
    
    intega=((s1+s2)/2+soma)*dt
    af=2/per*intega
    integq=((q1+q2)/2+somq)*dt
    bf=2/per*integq
    return af,bf

#--------------------------------------------------------------------------------#

ind = np.transpose([0 for i in range(1000)])

afo = np.zeros(15) #número de frequências
bfo  = np.zeros(15)

m = 1
k = 1
g=9.8

xeq = 0
b=0.05
f=7.5
wf=1

t0 = 0
tf =400
dt = 0.0001

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

x = np.empty(n)
v = np.empty(n)
a = np.empty(n)
Ep = np.empty(n)
Ec = np.empty(n)
EM = np.empty(n)


x[0] = 0
v[0] = 0

a[0] = (-k*x[0] - b * v[0] + f*np.cos(wf*t[0]))/m

countMax=0

for i in range(n-1):   
    a[i+1] = (-k*x[i] - b * v[i] + f*np.cos(wf*t[i]))/m
    v[i+1] = v[i] +a[i+1]*dt 
    x[i+1] = x[i] +v[i+1]*dt
    Ep[i] = 0.5*k* x[i]**2
    Ec[i] = m*0.5*v[i]**2
    EM[i] = Ec[i] + Ep[i]
    if (t[i]>200 and x[i-1]<x[i]>x[i+1] and i>0 ):
        countMax = countMax+1
        ind[countMax] = int(i)
    
Ep[n-1] = 0.5*k*x[n-1]**2
Ec [n-1]= m*0.5*v[n-1]**2
EM[n-1] = Ec[n-1] + Ep[n-1]

t0 = ind[countMax-1]
t1 = ind[countMax]

for i in range(15):
    af, bf=abfourier(t,x,t0,t1,i)
    afo[i] = af
    bfo[i] = bf

ii = np.linspace(0,14,15)
plt.figure()
plt.xlabel("n")
plt.bar(ii,afo, label="| a_n |")
plt.legend()
plt.show()

ii = np.linspace(0,14,15)
plt.figure()
plt.xlabel("n")
plt.bar(ii,bfo, label="| b_n |")
plt.legend()
plt.show()