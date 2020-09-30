#include <stdio.h>
#include <stdlib.h>
#include <math.h>

static int z[] =
    { 17, 20, 10, 17, 12, 15, 19, 22, 17, 19, 14, 22, 18, 17, 13, 12, 18,
15, 17 };
static double A(int, const int *, int);
static int conformal_gamma(int, int *z, double, int M, /**/ int*);

int
main()
{
    double eps;
    int n;
    int zn;
    int M;
    int *G;

    M = 1000;
    G = malloc(M * sizeof *G);
    for (zn = 0; zn < M; zn++)
      G[zn] = 0;
    eps = 0.05;
    n = sizeof z / sizeof *z;
    conformal_gamma(n, z, eps, M, G);
    for (zn = 0; zn < M; zn++)
      if (G[zn])
	printf("%d\n", zn);
    free(G);
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

static int
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
