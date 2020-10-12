#include <math.h>
#include "conformal.h"

static double A(int, const int *, int);

int
conformal_gamma(int n, int *z, double eps, int M, /**/ int *G)
{
    double an;
    double ai;
    int cnt;
    int i;
    int zi;
    int zn;

    for (zn = 0; zn < M; zn++) {
        cnt = 0;
        an = A(n, z, zn);
        for (i = 0; i < n; i++) {
            zi = z[i];
            z[i] = zn;
            ai = A(n, z, zi);
            z[i] = zi;
            if (ai >= an)
                cnt += 1;
        }
	G[zn] = cnt > eps * n;
    }
    return 0;
}

static double
A(int n, const int *B, int z)
{
    long m;
    int i;
    m = z;
    for (i = 0; i < n; i++)
        m += B[i];
    return fabs(m / (n + 1.0) - z);
}
