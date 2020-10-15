import random
import conformal

N = 100
mu_sigma = ( (250, 50), (750, 25) )
prob = (0.25, 0.75)
eps = 0.05
random.seed()

def gen():
    mu, sigma = random.choices(mu_sigma, prob)[0]
    return int(random.gauss(mu, sigma))

z = [ gen(), gen(), gen(), gen(), gen(), gen(), gen() ]
def nxt():
    x = gen()
    G = conformal.gamma("mean", z, eps)
    z.append(x)
    return x in G

m = 0
for n in range(1, N + 1):
    m += 1 if nxt() else 0
print(m, n, 1 - m/n)
