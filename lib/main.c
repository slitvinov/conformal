#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const char *me = "libconformal";
typedef double (*Function)(int, const int *, int);
static double Amean(int, const int *, int);
static double Amedian(int, const int *, int);
static double Ann(int, const int *, int);
static int conformal_gamma0(int, int *, double, int, Function, int *);
int quick_select(int n, int *);

static const Function Functions[] = {Amean, Amedian, Ann};
static const char *Names[] = {"mean", "median", "nn"};

int conformal_gamma(const char *name, int n, int *z, double eps, int M,
                    /**/ int *G) {
  int i;

  for (i = 0; i < (int)(sizeof Names / sizeof *Names); i++)
    if (strcmp(Names[i], name) == 0)
      return conformal_gamma0(n, z, eps, M, Functions[i], G);
  fprintf(stderr, "%s:%d: (%s) unknown method name '%s'\n", __FILE__, __LINE__,
          me, name);
  fprintf(stderr, "%s:%d: (%s) possible values are\n", __FILE__, __LINE__, me);
  for (i = 0; i < (int)(sizeof Names / sizeof *Names); i++)
    fprintf(stderr, "%s:%d: (%s) '%s'\n", __FILE__, __LINE__, me, Names[i]);
  return 1;
}

static int conformal_gamma0(int n, int *z, double eps, int M, Function A,
                            /**/ int *G) {
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

static double Amean(int n, const int *B, int z) {
  long m;
  int i;

  m = z;
  for (i = 0; i < n; i++)
    m += B[i];
  return fabs(m / (n + 1.0) - z);
}

static double Ann(int n, const int *B, int z) {
  int i;
  int d;
  int dist;

  for (i = 0; i < n; i++) {
    d = abs(z - B[i]);
    if (i == 0 || d < dist)
      dist = d;
  }
  return dist;
}

static double Amedian(int n, const int *B0, int z) {
  int i;
  int m;
  int *B;

  if ((B = malloc((n + 1) * sizeof *B)) == NULL) {
    fprintf(stderr, "%s:%d: (libconformal) malloc failed\n", __FILE__,
            __LINE__);
    exit(2);
  }
  for (i = 0; i < n; i++)
    B[i] = B0[i];
  B[n] = z;
  m = quick_select(n + 1, B);
  free(B);
  return abs(m - z);
}
