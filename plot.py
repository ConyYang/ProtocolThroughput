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

G= np.arange(start=0, stop=100, step=0.01)

S_pA = pureAloha.pure_aloha(G)
S_sA = slottedAloha.slotted_aloha(G)
S_np = nonPersistent.nonP_CSMA(G)
S_op = onePersistent.oneP_CSMA(G)
S_pP = pPersistent.oneP_CSMA(G, 0.09, 0.02)


annot_max(S_pA, G, 0.28, 0.3, ax)
annot_max(S_sA, G, 0.32, 0.55, ax)
annot_max(S_np, G, 0.96, 0.9, ax)
annot_max(S_op, G, 0.82, 0.67, ax)
annot_max(S_pP, G, 0.98, 0.98, ax)


plt.plot(G, S_pP, 'steelblue', label='pPersistent_CSMA')
plt.plot(G, S_np, 'blueviolet', label='nonPersistent_CSMA')
plt.plot(G, S_op, 'lightseagreen', label='1 Persistent_CSMA')
plt.plot(G, S_sA, 'crimson', label='slotted_Aloha')
plt.plot(G, S_pA, 'chocolate', label='pure_Aloha')

plt.legend()
plt.xscale("log")
plt.show()