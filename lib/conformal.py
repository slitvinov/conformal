import os
import sys
import collections

me = "conformal.py"
M = 1000
def ini():
    from ctypes import cdll, c_char_p, c_int, c_double, POINTER
    prefix = os.path.join(os.environ['HOME'], ".local")
    path = os.path.join(prefix, "lib", "libconformal.so")
    try:
        l = cdll.LoadLibrary(path)
    except OSError:
        sys.stderr.write("%s: cannot find or open '%s'\n" % (me, path))
        raise
    l.conformal_gamma.argtypes = [c_char_p, c_int, POINTER(c_int), c_double, c_int, POINTER(c_int)]
    G = (c_int * M)()
    return l, G

l, G = ini()

def gamma(name, z, eps):
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
    ans = [ ]
    while True:
        while i <  M and i not in G:
            i += 1
        if not i < M:
            break
        j = i
        while j < M and j in G:
            j += 1
        ans.append((i, j))
        i = j
    return ans

def plot(z, G, x, ax = None):
    import matplotlib.pyplot as plt
    from matplotlib.ticker import MaxNLocator
    cnt = collections.Counter(z)
    inter = intervals(G)
    if ax is None:
        fig, ax = plt.subplots()
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    for a, b in cnt.items():
        ax.vlines(x=a, ymin=0, ymax=b, linewidth=2, color='blue')
    for a, b in inter:
        ax.hlines(y=0, xmin=a, xmax=b, label='x', linewidth=4, color='green')
    ax.plot(x, 0, color='red', marker='o', markersize=12)
    return ax
