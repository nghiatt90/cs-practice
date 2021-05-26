// https://app.codesignal.com/challenge/XjYS83B6vYMEvuBGq
int p, m = 9, t;
int BestMAtch(int N, int[] a, int[] z) {
  for (; --N > 0; )
    for (t = a[N] - z[N]; t < m; m = t)
      p = N;
  return p;
}

