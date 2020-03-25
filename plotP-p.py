'''
Plot the functions
'''

__author__ = "Yang Yubei"
import numpy as np
import matplotlib.pyplot as plt

from CSMAProtocol import pPersistent

'''
Plot the Graph Here 
'''

plt.title('Throughout for the various access modes', fontsize=10)
plt.xlabel('G (Offered Channel Traffic)')
plt.ylabel('S (Throughput)')

G= np.arange(start=0, stop=100, step=0.01)

S_pP = pPersistent.oneP_CSMA(G)
plt.plot(G, S_pP,'lightseagreen')

plt.xscale("log")
plt.show()