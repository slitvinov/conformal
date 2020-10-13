import random
import conformal

mu_sigma = ( (250, 50), (750, 25) )
prob = (0.25, 0.75)
eps = 0.05
random.seed(123455)

def gen():
    mu, sigma = random.choices(mu_sigma, prob)[0]
    return int(random.gauss(mu, sigma))

z = [ gen(), gen(), gen(), gen(), gen() ]
def nxt():
    x = gen()
    G = conformal.gamma("nn", z, eps)
    print(z)
    print(conformal.intervals(G), x, x in G)
    z.append(x)

nxt()
