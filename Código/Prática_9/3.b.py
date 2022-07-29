import numpy as np
import matplotlib.pyplot as plt
import math

dt=0.001
ti= 0
tf=50.00
n=int((tf-ti)/dt)

t=np.linspace(ti,tf,n)

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

#Aqui uso n+1 por ser mais facil interpretar a formula da integração --> nós usamos sempre n
vel=np.empty(n)
vx=np.empty(n)
x=np.empty(n)
ax=np.empty(n)
vx=np.empty(n)
aresx=np.empty(n)
fCil=np.empty(n)

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
    if (vel[i]-vel[i-1]<tolerancia):
        vTerminal=vel[i]
        print ("Velocidade terminal = ",vTerminal," m/s")
        break

vel[i+1]=np.sqrt(vx[i+1]**2)


plt.plot(t,vel, color="gold")
#plt.plot(t,energia,label='W Res')
plt.ylabel('V (m/s)')
plt.xlabel( 't (s)' )
plt.grid()
plt.title("Velocidade Terminal do ciclista com 5º de inclinação")
plt.show()
