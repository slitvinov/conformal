import random
import conformal

size = 400
center = 500
random.seed(123455)
def gen():
    return int(random.uniform(center - size/2, center + size/2))

z = [ gen(), gen() ]
def nxt():
    x = gen()
    G = conformal.gamma("mean", z, eps)
    print(z)
    print(conformal.intervals(G), x, x in G)
    z.append(x)

nxt()
