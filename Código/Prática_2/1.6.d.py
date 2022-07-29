# -*- coding: utf-8 -*-

# Regressão linear
# Equações do formulário

import numpy as np
import matplotlib.pyplot as plt

X=np.array([0.00, 0.735, 1.363, 1.739, 2.805, 3.814, 4.458, 4.955 ,5.666, 6.329])
n_Pontos = len(X)


t = np.arange(0,n_Pontos,1)

plt.scatter(t,X)
plt.xlabel("t (min) ")
plt.ylabel("X (km) ")
#Truque para não ter de alterar o código abaixo: identificar x e y corretamente
x=t
y=X
def regressao_linear(x,y):
    npontos=x.size

    xy=x*y# element by element product
    x2=x*x
    y2=y*y

    sx=x.sum()
    sy=y.sum()
    sxy=xy.sum()
    sxx=x2.sum()
    syy=y2.sum()

    #print("sx,sy,sxy,sxx,syy")
    #print(sx,sy,sxy,sxx,syy)
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
    print('m +/-dm= ',m ,"+/-", dm)
    print('b +/-db= ',b ,"+/-",db)
    print('r2= ',r2)
    return m,b

result = regressao_linear (t,X)
#1.6.b
print("A resposta do ciclista manter a mesma velocidade no percurso depende do gráfico, se estamos a considerar os pontos ou a reta de ajuste")
print("")
# Se fosse a reta, a velocidade é uniforme
#Caso contrário, varia

#1.6.c
print("A velocidade média é ",result[0]," km/min")
print("")

#1.6.d
reta = np.polyfit(x,y,1)
decl = reta[0]
orde = reta[1]
print("m= ",decl)
print("b= ",orde)
print("Sim, os valores concordam com os valores calculados na alínea b' ")

#1.6.e
print("")
velo_conv = result[0] *60
print("A velocidade em km/h é", velo_conv)








