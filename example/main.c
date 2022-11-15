#include <stdio.h>
#include <stdlib.h>
#include <conformal.h>

const char *me = "example/main.c";

int
main(int argc, const char **argv)
{
  const char *name;
  enum {M = 1000};
  double eps;
  int G[M];
  int n;
  int i;
  int z[] = {17, 20, 10, 17, 12, 15, 19, 22, 17, 19, 14, 22, 18, 17, 13, 12, 18, 15, 17};
  argv++;
  if (*argv == NULL) {
    fprintf(stderr, "%s: needs a method name (mean, median, or nn)\n", me);
    exit(2);
  }
  name = *argv++;
  if (*argv == NULL) {
    fprintf(stderr, "%s: needs epsilon\n", me);
    exit(2);
  }
  eps = atof(*argv++);
  n = sizeof z/sizeof *z;
  if (conformal_gamma(name, n, z, eps, M, G) != 0) {
    fprintf(stderr, "%s: conformal_gamma failed\n", me);
    exit(2);
  }
  for (i = 0; i < M; i++)
    if (G[i])
      printf("%d ", i);
  printf("\n");
}
