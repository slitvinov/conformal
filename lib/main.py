from ctypes import *
l = cdll.LoadLibrary("./libconformal.so")
l.conformal_gamma.argtypes = [c_char_p, c_int, POINTER(c_int), c_double, c_int, POINTER(c_int)]
z = [ 17, 20, 10, 17, 12, 15, 19, 22, 17, 19, 14, 22, 18, 17, 13, 12, 18,
      15, 17 ]
n = len(z)
z = (c_int * n)(*z)
eps = 0.1
M = 1000
G = (c_int * M)()
rcode = l.conformal_gamma(b"nn", n, z, eps, M, G)

def to_set(a):
    s = set()
    for i, e in enumerate(a):
        if e == 1:
            s.add(i)
    return s

print(to_set(G))
