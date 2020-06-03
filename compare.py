'''
Plot the functions
'''

__author__ = "Yang Yubei"

import numpy as np
import matplotlib.pyplot as plt

from AlohaProtocol import pureAloha
from AlohaProtocol import slottedAloha
from CSMAProtocol import nonPersistent
from CSMAProtocol import onePersistent
from CSMAProtocol import pPersistent

from plotMax import annot_max

'''
Plot the Graph Here 
'''
fig = plt.figure()
ax = fig.add_subplot(111)

plt.title('Throughout for the various access modes', fontsize=10)
plt.xlabel('G (Offered Channel Traffic)')
plt.ylabel('S (Throughput)')

G = np.arange(start=0, stop=100, step=0.01)
a = 0.02
colorList = ['#fe4a49', '#2ab7ca','orange']

S_np = nonPersistent.nonP_CSMA(G)
for i, p in enumerate(np.arange(0.01, 0.1, 0.04)):
    S_pP = pPersistent.oneP_CSMA(G, p, a)
    annot_max(S_pP, G, p * 10, p * 10, ax)
    plt.plot(G, S_pP, colorList[i], label=f'pP_CSMA p = {p:.2f}')

annot_max(S_np, G, 0.98, 0.8, ax)

plt.plot(G, S_np, 'black', label='nonP_CSMA')

plt.xlim((0.1, 100))
plt.legend(loc=2)
plt.xscale("log")
plt.show()
