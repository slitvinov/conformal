from ctypes import cdll, c_char_p, c_int, c_double, POINTER
import collections
import math
import os
import statistics
import sys


def ini():
	dirname = os.path.dirname(__file__)
	path = os.path.join(dirname, "libconformal.so")
	try:
		l = cdll.LoadLibrary(path)
	except OSError:
		sys.stderr.write("%s: cannot find or open '%s'\n" % (me, path))
		raise
	l.conformal_gamma.argtypes = [
	    c_char_p, c_int,
	    POINTER(c_int), c_double, c_int,
	    POINTER(c_int)
	]
	G = (c_int * M)()
	return l, G


def fisher(z, eps):
	import scipy.stats
	n = len(z) + 1
	m = statistics.mean(z)
	s2 = statistics.variance(z)
	t = scipy.stats.t.ppf(1 - eps / 2, n - 2)
	d = t * math.sqrt(s2) * math.sqrt(n / (n - 1))
	return set(i for i in range(M) if m - d < i <= m + d)


def gamma(name, z, eps):
	'''Return the conformal prediction set. z is a list-like container of
	examples, eps is a probability of error, name is a string
	indicating nonconformity measure, possible values are "nn"
	(nearest neighbor), "mean", "median".

	>> conformal.gamma("nn", [1, 1, 2, 2, 3, 1, 1], 0.05)
	{0, 1, 2, 3, 4}
	'''

	from ctypes import c_int, c_char_p
	n = len(z)
	z = (c_int * n)(*z)
	name = c_char_p(name.encode('utf-8'))
	rcode = l.conformal_gamma(name, n, z, eps, M, G)
	if rcode != 0:
		sys.stderr.write("%s: conformal_gamma failed\n" % me)
		raise
	ans = set()
	for i, e in enumerate(G):
		if e == 1:
			ans.add(i)
	return ans


def intervals(G):
	ans = 0
	i = 0
	ans = []
	while True:
		while i < M and i not in G:
			i += 1
		if not i < M:
			break
		j = i
		while j < M and j in G:
			j += 1
		ans.append((i, j))
		i = j
	return ans


def plot(z, G, x, ax=None):
	return plot2(z, [G], x, ax)


def plot2(z, G, x, ax=None):
	import itertools
	import numpy as np
	import matplotlib.pyplot as plt
	from matplotlib.ticker import MaxNLocator
	colors = ['green', 'orange']
	cnt = collections.Counter(z)
	if ax is None:
		fig, ax = plt.subplots()
	ax.set_xlim(xmin=-1, xmax=M + 1)
	ax.yaxis.set_major_locator(MaxNLocator(integer=True))
	for a, b in cnt.items():
		ax.vlines(x=a, ymin=0, ymax=b, color='blue')
	y = 0
	for g, color in zip(G, itertools.cycle(colors)):
		for a, b in intervals(g):
			ax.hlines(y, xmin=a, xmax=b, label='x', linewidth=4, color=color)
		y -= 0.1
	ax.plot(x, 0, color='red', marker='o', markersize=12)
	return ax


l, G = ini()
me = "conformal.py"
M = 1000
