import os
import sys
from ctypes import *

me = "conformal.py"
prefix = os.path.join(os.environ['HOME'], ".local")
path = os.path.join(prefix, "lib", "libconformal.so")
try:
    l = cdll.LoadLibrary(path)
except OSError:
    sys.stderr.write("%s: cannot find or open '%s'\n" % (me, path))
    raise
l.conformal_gamma.argtypes = [c_char_p, c_int, POINTER(c_int), c_double, c_int, POINTER(c_int)]

M = 1000
G = (c_int * M)()
def gamma(name, z, eps):
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
