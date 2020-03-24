
'''
Basic model: no retransmissions, only mean arrival rate of the poisson distribution as a parameter.
'''

__author__ = "Yang Yubei"
import numpy as np
import math, os
import matplotlib.pyplot as plt
import matplotlib
G = np.arange(start=0, stop=3, step=0.01)
S = []
for i in range(len(G)):
    S.append(G[i]*(math.exp(-2*G[i])))

plt.plot(G, S)
plt.title('Throughout for the various access modes', fontsize=10)
plt.xlabel('G (Offered Channel Traffic)')
plt.ylabel('S (Throughput)')
plt.text(2, 0.04, 'Pure Aloha')
plt.show()