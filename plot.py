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
S_pP = pPersistent.oneP_CSMA(G)


S_pA_ymax = max(S_pA)
S_pA_xpos = S_pA.index(S_pA_ymax)
S_pA_xmax = G[S_pA_xpos]

S_sA_ymax = max(S_sA)
S_sA_xpos = S_sA.index(S_sA_ymax)
S_sA_xmax = G[S_sA_xpos]


S_np_ymax = max(S_np)
S_np_xpos = S_np.index(S_np_ymax)
S_np_xmax = G[S_np_xpos]

S_op_ymax = max(S_op)
S_op_xpos = S_op.index(S_op_ymax)
S_op_xmax = G[S_op_xpos]

S_pP_ymax = max(S_pP)
S_pP_xpos = S_pP.index(S_pP_ymax)
S_pP_xmax = G[S_pP_xpos]

def annot_max(xmax,ymax, a, b, ax=None):
    text= "G={:.3f}, S={:.3f}".format(xmax, ymax)
    if not ax:
        ax=plt.gca()
    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=60")
    kw = dict(xycoords='data',textcoords="axes fraction",
              arrowprops=arrowprops, bbox=bbox_props, ha="right", va="top")
    ax.annotate(text, xy=(xmax, ymax), xytext=(a,b), **kw)

annot_max(S_pA_xmax,S_pA_ymax ,0.28, 0.3, ax)
annot_max(S_sA_xmax,S_sA_ymax ,0.32, 0.55, ax)
annot_max(S_np_xmax,S_np_ymax ,0.96, 0.9, ax)
annot_max(S_op_xmax,S_op_ymax ,0.82, 0.67, ax)
annot_max(S_pP_xmax,S_pP_ymax ,0.98, 0.98, ax)

plt.plot(G, S_pP, 'steelblue', label='pPersistent_CSMA')
plt.plot(G, S_np, 'blueviolet', label='nonPersistent_CSMA')
plt.plot(G, S_op, 'lightseagreen', label='1 Persistent_CSMA')
plt.plot(G, S_sA, 'crimson', label='slotted_Aloha')
plt.plot(G, S_pA, 'chocolate', label='pure_Aloha')


plt.legend()
plt.xscale("log")
plt.show()