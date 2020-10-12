#!/usr/bin/env python3

import math
import random
import scipy.stats
import statistics

eps = 0.05

def inter(z):
    n =  len(z) + 1
    m = statistics.mean(z)
    s2 = statistics.variance(z)
    t = scipy.stats.t.ppf(1 - eps/2, n - 2)
    d = t * math.sqrt(s2) * math.sqrt(n/(n - 1))
    return m - d, m + d

def gen():
    return random.gauss(mu, sigma)

mu = 0
sigma = 2
n = 100
z = [ ]
z.append(gen())
z.append(gen())
correct = total = 0
for i in range(n - 2):
    a, b = inter(z)
    x = gen()
    if a <= x < b:
        correct += 1
    total += 1
    z.append(x)
    
print(correct/total)
