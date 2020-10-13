import random
import conformal

mu = 500
sigma = 100
eps = 0.05
random.seed(123455)

def gen():
    return int(random.gauss(mu, sigma))

z = [ gen(), gen() ]
def nxt():
    x = gen()
    G = conformal.gamma("mean", z, eps)
    print("z G x correct?:", z, conformal.intervals(G), x, x in G)
    z.append(x)

nxt()
nxt()
nxt()
