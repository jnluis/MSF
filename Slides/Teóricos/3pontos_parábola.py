#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 18:26:38 2022

@author: joao
"""

import numpy as np

#ponto onde a função interseta o 0, tendo em conta outros pontos obidos pelo Método de Euler

def zerosv(xm1,xm2,xm3,ym1,ym2,ym3):
    xab= xm1-xm2
    xac= xm1-xm3
    xbc= xm2-xm3
    
    a = ym1/(xab*xac)
    b = -ym2/(xab*xbc) 
    c = ym3/(xac*xbc)
    
    am=a+b+c
    bm = a*(xm2+xm3)+b*(xm1+xm3)+c*(xm1+xm2)
    cm = a*xm2*xm3+b*xm1*xm3+c*xm1*xm2
    
    xzero = (bm+np.sqrt(bm*bm-4*am*cm))/(2*am)
    if xm3 > xm1 and (xzero< xm1 or xzero >xm3):
        xzero= (bm-np.sqrt(bm*bm-4*am*cm))/(2*am)
    if xm1> xm3 and (xzero < xm3 or xzero > xm1):
        xzero= (bm-np.sqrt(bm*bm-4*am*cm))/(2*am)
    
    xta = xzero-xm1
    xtb = xzero-xm2
    xtc = xzero-xm3
    yzero = a*xtb*xtc+b*xta*xtc+c*xta*xtb 
    return xzero, yzero
    
#print(zerosv(7,8.5,9.9,0.1,-0.05,-0.35))