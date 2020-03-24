'''
Basic model:
'''
__author__ = 'Yang Yubei'

import math


def pure_aloha(G):
    """
    :param G: offered channel traffic rate
    :return: S - throughput (utilization)
    """
    S = []
    for i in range(len(G)):
        S.append(G[i] * (math.exp(-2 * G[i])))
    return S


def slotted_aloha(G):
    """
        :param G: offered channel traffic rate
        :return: S - throughput (utilization)
        """
    S = []
    for i in range(len(G)):
        S.append(G[i] * (math.exp(-1 * G[i])))
    return S


a = 0.4


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