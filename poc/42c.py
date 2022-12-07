#!/usr/bin/env python3

import random
import sys
import scipy.stats
import statistics

eps = 0.20
M = 1000


def A(B, z):
	z0 = statistics.mean(B)
	ans = abs(z0 - z)
	return ans


def G(z):
	ans = set()
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
			ans.add(zn)
	return ans


Z = [
    17, 20, 10, 17, 12, 15, 19, 22, 17, 19, 14, 22, 18, 17, 13, 12, 18, 15, 17
]


def gen():
	#return Z.pop()
	return int(random.gauss(mu, sigma))


mu = 500
sigma = 100
n = 2000
z = []
z.append(gen())
correct = total = 0
for i in range(n - 1):
	x = gen()
	g = G(z)
	print("%03d-%03d" % (min(g), max(g)))
	if x in g:
		correct += 1
	total += 1
	print("%03d/%03d = %.0f" % (correct, total, correct / total * 100))
	z.append(x)

print(correct / total)
