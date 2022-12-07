import numpy as np
import matplotlib.pyplot as plt
import random
import statistics
import math
import sys


def A(B, z):
	x, y = zip(*B)
	u, v = z
	n = len(x)
	xy = statistics.fsum(a * b for a, b in zip(x, y))
	xx = statistics.fsum(a * a for a in x)
	beta = xy / xx
	return (beta * u - v)**2


def conformal(A, z, xx, yy, eps=0.05):
	n = len(z) + 1
	Gamma = []
	for x in xx:
		gamma = []
		for y in yy:
			Am = A(z, (x, y))
			cnt = 1
			for i in range(n - 1):
				zp = z[:i] + z[i + 1:] + [(x, y)]
				if A(zp, z[i]) >= Am:
					cnt += 1
					if cnt > eps * n:
						gamma.append(y)
						break
		Gamma.append(gamma)
	return Gamma


def like(beta, s):
	n = len(z)
	sq = statistics.fsum((beta * a - b)**2 for a, b in z)
	return (-sq / s - n * math.log(s)) / 2


def metropolis(fun, draws, init, scale):
	x = init[:]
	p = fun(x)
	t = 0
	S = []
	accept = 0
	while True:
		S.append(x)
		if t >= draws:
			break
		xp = [e + random.gauss(0, s) for e, s in zip(x, scale)]
		t += 1
		pp = fun(xp)
		if pp > p or pp > p + math.log(random.uniform(0, 1)):
			x, p = xp, pp
			accept += 1
	sys.stderr.write("metropolis: accept = %g\n" % (accept / draws))
	return S


z = [ ]
for i in range(200):
	x = random.uniform(0, 1)
	y = 4 * x + random.gauss(0, x)
	z.append((x, y))
xy = statistics.fsum(a * b for a, b in z)
xx = statistics.fsum(a * a for a, b in z)
beta = xy / xx
s = statistics.variance(beta * a - b for a, b in z)
S = metropolis(lambda x: like(*x), 1000, (beta, s), [0.05, 0.05])

eps = 0.05
x = np.linspace(0, 1, 10)
y = np.linspace(-10, 10, 100)
Gamma = conformal(A, z, x, y, eps)
plt.scatter(*zip(*z), edgecolor='none', facecolor='C0')
for e, gamma in zip(x, Gamma):
	plt.scatter([e] * len(gamma),
	            gamma,
	            edgecolor='none',
	            facecolor='C1',
	            alpha=0.5)
for e in x:
	P = []
	for beta, s in S:
		P.append(random.gauss(beta * e, s))
	q = np.quantile(P, (eps, 1 - eps))
	plt.scatter([e] * len(q), q, edgecolor='none', facecolor='C2', alpha=0.5)
plt.savefig("regression.pdf")
