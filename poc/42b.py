#!/usr/bin/env python3

import statistics
import array

eps = 0.10
M = 1000


def Amean(B, z):
	return abs(statistics.mean(B) - z)


def Amedian(B, z):
	return abs(statistics.median(B) - z)


def Anear(B, z):
	return min(abs(b - z) for b in B)


A = Anear


def G(z):
	ans = []
	for zn in range(M):
		an = A(z, zn)
		cnt = 0
		for i, zi in enumerate(z):
			z[i] = zn
			ai = A(z, zi)
			z[i] = zi
			if ai >= an:
				cnt += 1
		if cnt > eps * len(z):
			ans.append(zn)
	return ans


Z = [
    17, 20, 10, 17, 12, 15, 19, 22, 17, 19, 14, 22, 18, 17, 13, 12, 18, 15, 17
]
print(G(Z))
