'''
Non-Persistent CSMA:
'''
__author__ = 'Yang Yubei'

import math
a = 0.05
def nonP_CSMA(G):
    """
        :param G: offered channel traffic rate
        :return: S - throughput (utilization)
        """
    S = []
    for i in range(len(G)):
        S.append(
            (G[i] * (math.exp(-1 * a * G[i]))) /
            (G[i] * (1 + 2 * a) + math.exp(-1 * a * G[i]))
        )
    return S

