'''
Plot the functions
'''

__author__ = "Yang Yubei"
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib
import throughputFunc

plt.title('Throughout for the various access modes', fontsize=10)
plt.xlabel('G (Offered Channel Traffic)')
plt.ylabel('S (Throughput)')

G= np.arange(start=0, stop=10, step=0.01)

S_pA = throughputFunc.pure_aloha(G)
S_sA = throughputFunc.slotted_aloha(G)
S_np = throughputFunc.nonP_CSMA(G)
S_op = throughputFunc.oneP_CSMA(G)

plt.plot(G, S_pA,'chocolate')
plt.plot(G, S_sA,'crimson')
plt.plot(G, S_np,'blueviolet')
plt.plot(G, S_op,'lightseagreen')

#plt.text(2, 0.04, 'Pure Aloha')
#plt.text(2, 0.28, 'Slotted Aloha')
#plt.text(3.0, 0.16, 'Non-Persistent CSMA')
print(S_op)
plt.show()