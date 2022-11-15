import numpy as np
import matplotlib.pyplot as plt
import random


def A(B, z):
	x, y = z
	u, v = zip(*B)
	U = [(e, 1) for e in u]
	b, *rest = np.linalg.lstsq(U, v, rcond=None)
	res = b @ (x, 1)
	return (res - y)**2


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


z = [(e, random.gauss(4 * e, e)) for e in np.linspace(0, 1, 200)]
x = np.linspace(0, 1, 10)
y = np.linspace(-10, 10, 100)
Gamma = conformal(A, z, x, y, eps=0.01)
plt.scatter(*zip(*z), edgecolor='none', facecolor='C0')
for e, gamma in zip(x, Gamma):
	plt.scatter([e] * len(gamma),
	            gamma,
	            edgecolor='none',
	            facecolor='C1',
	            alpha=0.5)
plt.savefig("regression.pdf")
