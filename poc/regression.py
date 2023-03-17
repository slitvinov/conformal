import numpy as np
import matplotlib.pyplot as plt
import random


def A(B, z):
    x, y = zip(*B)
    xy = sum(a * b for a, b in zip(x, y))
    xx = sum(a * a for a in x)
    beta = xy / xx
    u, v = z
    return (beta * u - v)**2


def conformal(A, eps, z, x, y):
    n = len(z) + 1
    Am = A(z, (x, y))
    cnt = 1
    for i in range(n - 1):
        zp = z[:i] + z[i + 1:] + [(x, y)]
        if A(zp, z[i]) >= Am:
            cnt += 1
            if cnt > eps * n:
                return True
    return False


z = [(x, random.gauss(4 * x, x))
     for x in (random.uniform(0, 1) for i in range(200))]
eps = 0.05
gamma = [(x, y) for x in np.linspace(0, 1, 10)
         for y in np.linspace(-10, 10, 100) if conformal(A, eps, z, x, y)]
plt.scatter(*zip(*z))
plt.scatter(*zip(*gamma), alpha=0.5)
plt.show()
