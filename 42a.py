#!/usr/bin/env python3

import statistics

eps = 0.10
M = 1000
def A(B, z):
    return abs(statistics.mean(B) - z)

def A(B, z):
    return abs(statistics.median(B) - z)

def A(B, z):
    return min(abs(b - z) for b in B)

def pz(z, zn):
    an = A(z, zn)
    z = z + [zn]
    cnt = 0
    for i, zi in enumerate(z):
        ai = A(z[:i] + z[i+1:], zi)
        if ai >= an:
            cnt += 1
    return cnt/len(z)

def G(z):
    ans = [ ]
    for zn in range(M):
        p = pz(z, zn)
        if p > eps:
            ans.append(zn)
    return ans

Z = [17, 20, 10, 17, 12, 15, 19, 22, 17, 19, 14, 22, 18, 17, 13, 12, 18, 15, 17]
print(G(Z))
