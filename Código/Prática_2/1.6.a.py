# -*- coding: utf-8 -*-

# Regressão linear
# Equações do formulário

import numpy as np
import matplotlib.pyplot as plt
X=np.array([0.00, 0.735, 1.363, 1.739, 2.805, 3.814, 4.458, 4.955 ,5.666, 6.329])
n_Pontos = len(X)


t = np.arange(0,n_Pontos,1)

plt.scatter(t,X)