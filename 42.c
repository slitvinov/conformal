#include <stdio.h>
#include <stdlib.h>

enum { M = 1000 };
static int z[] =
    { 17, 20, 10, 17, 12, 15, 19, 22, 17, 19, 14, 22, 18, 17, 13, 12, 18,
15, 17 };
enum { n = sizeof z / sizeof *z };
static double A(int, const int *, int);
static const double eps = 0.1;

int
main()
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
        if (cnt > eps * n)
            printf("%d\n", zn);
    }

}

static double
A(int n, const int *B, int z)
{
    long m;
    int i;

    m = 0;
    for (i = 0; i < n; i++)
        m += B[i];
    return labs(m - n * z) / n;
}
