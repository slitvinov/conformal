import random
import conformal
import matplotlib.pyplot as plt

mu_sigma = ( (250, 50), (750, 25) )
prob = (0.25, 0.75)
eps = 0.05
random.seed(123455)

def gen():
    mu, sigma = random.choices(mu_sigma, prob)[0]
    return int(random.gauss(mu, sigma))

z = [gen() for i in range(75)]
def nxt():
    plt.close()
    x = gen()
    Gnn = conformal.gamma("nn", z, eps)
    Gfisher = conformal.fisher(z, eps)
    ax = conformal.plot2(z, (Gnn, Gfisher), x)
    plt.show()
    #ax.get_figure().savefig("a.svg")
    z.append(x)

nxt()