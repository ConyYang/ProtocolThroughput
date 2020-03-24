'''
SlottedAloha model:
'''
__author__ = 'Yang Yubei'

import math
def slotted_aloha(G):
    """
        :param G: offered channel traffic rate
        :return: S - throughput (utilization)
        """
    S = []
    for i in range(len(G)):
        S.append(G[i] * (math.exp(-1 * G[i])))
    return S