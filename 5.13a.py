import numpy as np
import matplotlib.pyplot as plt
import math

dt=0.001
tf=500.00
n=np.int(tf/dt)

t=np.linspace(0,tf,n+1)

potencia=0.4*735.49875
mu=0.004
Cres=0.9
A=0.3
densidade=1.225
massa=75
g=9.8
teta=math.radians(5)
v0x=1
fAtrito=-mu*massa*g*math.cos(teta)
#fAtrito=-mu*massa*g #segundo sugetsoa do Torres. Ver apontamentos

#Aqui uso n+1 por ser mais facil interpretar a formula da integração
vel=np.empty(n+1)
vx=np.empty(n+1)
x=np.empty(n+1)
ax=np.empty(n+1)
vx=np.empty(n+1)
aresx=np.empty(n+1)
fCil=np.empty(n+1)
vx[0]=v0x
x[0]=0
tolerancia=0.00000001
pesoX=-massa*g*math.sin(teta)

for i in range(0,n):
    vel[i]=np.sqrt(vx[i]**2)
    aresx[i]=-Cres/(2*massa)*A*densidade*vel[i]*vx[i]
    fCil[i]=potencia/(massa*vel[i])
    ax[i]=fAtrito/massa+aresx[i]+fCil[i]+pesoX/massa
    vx[i+1]=vx[i]+ax[i]*dt
    x[i+1]=x[i]+vx[i]*dt
    #velocidade terminal: considerar um valor muito pequeno a partir do qual e igual
    if (x[i+1]>=2000):
        print ("temp x=2km = ",t[i],"s")
        break

vel[i+1]=np.sqrt(vx[i+1]**2)




plt.figure()
plt.plot(t,vel)
# plt.plot(t,energia,label='W Res')
plt.ylabel('V (m/s)')
plt.xlabel( 't (s)' )
plt.grid()

plt.show()
