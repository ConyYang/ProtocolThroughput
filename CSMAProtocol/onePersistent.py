'''
One Persistent ALoha:
'''
__author__ = 'Yang Yubei'

import math
a = 0.05

def oneP_CSMA(G):
    """
            :param G: offered channel traffic rate
            :return: S - throughput (utilization)
            """
    S = []
    for i in range(len(G)):
        S.append(
            (G[i] * (1 + G[i] + a * G[i] * (1 + G[i] + a * G[i] / 2))
             * math.exp(-1 * G[i] * (1 + 2 * a))) /
            (G[i] * (1 + 2 * a) - (1 - math.exp(1 - math.exp(-1 * a * G[i])))
             + (1 + a * G[i]) * math.exp(-1 * G[i] * (1 + a)))
        )
    return S