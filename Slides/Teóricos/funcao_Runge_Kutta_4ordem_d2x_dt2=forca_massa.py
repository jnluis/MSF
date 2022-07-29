#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 09:59:24 2022

@author: joao
"""
def acelera(t,x,vx):
    ax= g-g/vT **2*np.abs(vx)*vx
    return ax


def rk4(t,x,vx,dt):
    """
    Integração numérica de equação diferencial de 2ª ordem:
			d2x/dt2 = ax(t,x,vx)    com dx/dt= vx    de valor inicial
	Erro global:  proporcional a dt**4
    acelera=dvx/dt=Força(t,x,vx)/massa      : acelera é uma FUNÇÃO
    input:  t = instante de tempo
            x(t) = posição
            vx(t) = velocidade
            dt = passo temporal 
    output: xp = x(t+dt)
		    vxp = vx(t+dt)
    """
    ax1=acelera(t,x,vx)
    c1v=ax1*dt
    c1x=vx*dt
    ax2=acelera(t+dt/2.,x+c1x/2.,vx+c1v/2.)
    c2v=ax2*dt
    c2x=(vx+c1v/2.)*dt			# predicto:  vx(t+dt) * dt
    ax3=acelera(t+dt/2.,x+c2x/2.,vx+c2v/2.)
    c3v=ax3*dt
    c3x=(vx+c2v/2.)*dt
    ax4=acelera(t+dt,x+c3x,vx+c3v)
    c4v=ax4*dt
    c4x=(vx+c3v)*dt
      
    xp=x+(c1x+2.*c2x+2.*c3x+c4x)/6.
    vxp=vx+(c1v+2.*c2v+2.*c3v+c4v)/6.
    return xp,vxp