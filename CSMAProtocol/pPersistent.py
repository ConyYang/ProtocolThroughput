'''
P Persistent ALoha:
'''
__author__ = 'Yang Yubei'

import math

a = 0.01
p = 0.1
q = 1 - p

def oneP_CSMA(G):
    S = []
    for i in range(len(G)):
        S.append(cal_S(G[i]))
    return S


def cal_S(G_i):
    """
            :param G_i: offered channel traffic rate
            :return: S - throughput (utilization)
            """
    g = a * G_i
    Ps = get_Ps(G_i)
    Ps_i = get_Ps_i(G_i)
    t = get_t(G_i)
    t_i = get_t_i(G_i)
    pi0 = pi_0(G_i)

    var1 = (1-pi0) / pi0
    var3 = 1 - math.exp(-1 * g)
    if (var3 == 0):
        var3 += 0.00000001
    var2 = (((1 + a)/pi0) + (a / (var3)))
    S_i = (Ps_i + var1 * Ps) / (a * t_i + a * t * var1 + var2)

    return S_i

def pi_0(G):
    '''
    calculate for Ps and ts
    '''
    pi0 = math.exp(-1 * G * (1 + a))
    return pi0

def pii_0(G):
    '''
    calculate for Ps' and ts'
    '''
    g = G * a
    pii0 = math.exp(-1 * g)
    return pii0


def get_Ps(G):
    pi0 = pi_0(G)
    g = G * a
    '''
    v1 = pi0 ^p
    v2 = pi0 ^b
    v3 = gp
    v4 = q*(1-pi0)
    '''
    v1 = pow(pi0, p)
    v2 = pow(pi0, 1-q*q)
    v3 = g * p

    v4 = q * (1 - pi0)
    if (v4 == 0):
        v4 += 0.000000001

    v5 = (v1 - pi0)/(v4)
    v6 = (1 - math.exp(-1 * v3)) * (v2 - pi0)
    v7 = v4 - q * math.exp(-2 * v3) * (v4 - pi0)

    return (v5 - (v6 / v7))


def get_t(G):
    pi0 = pi_0(G)
    g = G * a

    v8 = pow(pi0, p) - pi0
    v9 = math.exp(-p * g)
    v10 = 1- pi0 - v8 * v9
    if (v10 == 0):
        v10 += 0.000000001
    return (v8 / v10)


def get_Ps_i(G):
    pii0 = pii_0(G)
    g = G * a
    '''
    v1 = pi0 ^p
    v2 = pi0 ^b
    v3 = gp
    v4 = q*(1-pi0)
    '''
    v1 = pow(pii0, p)
    v2 = pow(pii0, 1 - q * q)
    v3 = g * p
    v4 = q * (1 - pii0)
    if (v4 == 0):
        v4 += 0.000000001

    v5 = (v1 - pii0) / (v4)
    v6 = (1 - math.exp(-1 * v3)) * (v2 - pii0)
    v7 = v4 - q * math.exp(-2 * v3) * (v4 - pii0)

    return (v5 - (v6 / v7))


def get_t_i(G):
    pii0 = pii_0(G)
    g = G * a

    v8 = pow(pii0, p) - pii0
    v9 = math.exp(-p * g)
    v10 = 1 - pii0 - v8 * v9
    if (v10 == 0):
        v10 += 0.000000001
    return (v8 /v10)












