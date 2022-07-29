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

def maxminv(xm1,xm2,xm3,ym1,ym2,ym3):
# Máximo ou mínimo usando o polinómio de Lagrange
# Dados (input): (x0,y0), (x1,y1) e (x2,y2)
# Resultados (output): xm, ymax
    xab=xm1-xm2
    xac=xm1-xm3
    xbc=xm2-xm3
    a=ym1/(xab*xac)
    b=-ym2/(xab*xbc)
    c=ym3/(xac*xbc)
    xmla=(b+c)*xm1+(a+c)*xm2+(a+b)*xm3
    xm=0.5*xmla/(a+b+c)
    xta=xm-xm1
    xtb=xm-xm2
    xtc=xm-xm3
    ymax=a*xtb*xtc+b*xta*xtc+c*xta*xtb
    return xm, ymax

t0 = 0.0
tf = 5
dt = 0.00001
n = int((tf-t0)/dt)
k = 2.0
m = 0.5
x0 = 1.5
v0 = 0.5
beta = 0.02
alfa = -0.1


t = np.zeros(n+1)
x = np.zeros(n+1)
vx = np.zeros(n+1)
ax = np.zeros(n+1)
emec = np.zeros(n+1)


x[0] = x0
vx[0] = v0


for i in range(n):
    t[i+1] = t[i] + dt
    ax[i] = (-k*x[i] - 3*alfa*x[i]**2 + 4*beta*x[i]**3)/m
    vx[i+1] = vx[i] + ax[i] * dt
    x[i+1] = x[i] + vx[i+1] * dt
    emec[i] = 0.5*m*vx[i]**2 + 0.5*k*x[i]**2 + alfa* x[i]**3 - beta * x[i]**4  # Emec = Ec + EpotElastica

emec[i+1] = 0.5*m*vx[i+1]**2 + 0.5*k*x[i+1]**2 + beta * x[i+1]**3

plt.title("Posição x tempo")
plt.plot(t,x)
plt.grid()
plt.show()

indMax = []
for i in range(n):
    if(x[i-1]<x[i] and x[i]>x[i+1] and t[i]>0):
        indMax.append(i)

indMin = []
for i in range(n):
    if(x[i-1]>x[i] and x[i]<x[i+1] and t[i]>0):
        indMin.append(i)

tmax = np.zeros(len(indMax))
xmax = np.zeros(len(indMax))
tmin = np.zeros(len(indMin))
xmin = np.zeros(len(indMin))
c=0
for i in indMax:
    tmax[c], xmax[c] = maxminv(t[i-1], t[i], t[i+1], x[i-1], x[i], x[i+1])
    c+=1

j=0
for i in indMin:
    tmin[j], xmin[j] = maxminv(t[i-1], t[i], t[i+1], x[i-1], x[i], x[i+1])
    j+=1

amplitude = np.mean(xmax)
print("Amplitude (Máximo):", amplitude) 
minimo = np.mean(xmin)
print("Mínimo:", minimo)
periodo = tmax[1]-tmax[0]
print("Período:", periodo)
freq = 1/periodo
print("Frequência:", freq)


xp = x[indMax[0]:indMax[1]]  # slices
tp = t[indMax[0]:indMax[1]]

it1 = int((tp[len(tp)-1]-tp[0])/dt)

af = []
bf = []
afbf = []
for i in range(10):
    afi, bfi = abfourier(tp, xp, 0, it1, i)
    afi = np.abs(afi)
    bfi = np.abs(bfi)
    af.append(afi)
    bf.append(bfi)
    afbf.append(np.sqrt(afi**2+bfi**2))
    print(i, "an:", afi, "  bn:", bfi, "  afbf:", np.sqrt(afi**2+bfi**2))

xaxis = [0,1,2,3,4,5,6,7,8,9]

plt.title("Coeficientes a (cosseno)")
plt.plot(xaxis, af, "o")
plt.grid()
plt.show()

plt.title("Coeficientes b (seno)")
plt.plot(xaxis, bf, "o")
plt.grid()
plt.show()

plt.title("Coeficientes somados")
plt.plot(xaxis, afbf, "o")
plt.grid()
plt.show()

print("Energia mecânica: ", emec[0])
plt.title("Energia mecância x tempo")
axis = plt.gca()
axis.set_ylim(0,50)
plt.plot(t,emec)
plt.show()