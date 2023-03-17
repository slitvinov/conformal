import random
import conformal


def gen():
    return int(random.gauss(mu, sigma))


def nxt():
    x = gen()
    G = conformal.gamma("mean", z, eps)
    print("z G x correct?:", z, conformal.intervals(G), x, x in G)
    z.append(x)


mu = 500
sigma = 100
eps = 0.05
random.seed(123455)
z = [gen(), gen()]
nxt()
nxt()
nxt()
