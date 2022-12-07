#!/usr/bin/env python3

import random
import sys
import statistics

eps = 0.20
M = 1000


def A(B, z):
	z0 = statistics.mean(B)
	ans = abs(z0 - z)
	return ans


def pz(z, zn):
	an = A(z, zn)
	z.append(zn)
	cnt = 0
	n = len(z)
	for i in range(n):
		z0 = z[:i] + z[i + 1:]
		a = A(z0, z[i])
		if a >= an:
			cnt += 1
	z.pop()
	return cnt / n


def G(z):
	ans = []
	for zn in range(M):
		p = pz(z, zn)
		if p > eps:
			ans.append(zn)
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
	print("%03d-%03d" % (min(G(z)), max(G(z))))
	if x in G(z):
		correct += 1
	total += 1
	print("%03d/%03d = %.0f" % (correct, total, correct / total * 100))
	z.append(x)

print(correct / total)
