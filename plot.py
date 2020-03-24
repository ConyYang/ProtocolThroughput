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
import matplotlib.patches as mpatches
'''
Plot the Graph Here 
'''

plt.title('Throughout for the various access modes', fontsize=10)
plt.xlabel('G (Offered Channel Traffic)')
plt.ylabel('S (Throughput)')

G= np.arange(start=0, stop=100, step=0.01)

S_pA = pureAloha.pure_aloha(G)
S_sA = slottedAloha.slotted_aloha(G)
S_np = nonPersistent.nonP_CSMA(G)
S_op = onePersistent.oneP_CSMA(G)
S_pP = pPersistent.oneP_CSMA(G)



plt.plot(G, S_pP, 'steelblue', label='pPersistent_CSMA')
plt.plot(G, S_np, 'blueviolet', label='nonPersistent_CSMA')
plt.plot(G, S_op, 'lightseagreen', label='1 Persistent_CSMA')
plt.plot(G, S_sA, 'crimson', label='slotted_Aloha')
plt.plot(G, S_pA, 'chocolate', label='pure_Aloha')

plt.legend()
plt.xscale("log")
plt.show()