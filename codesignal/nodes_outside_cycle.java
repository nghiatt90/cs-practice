// https://app.codesignal.com/challenge/MfEREnFCkJ45S6hJd
int r, i, n;
int nodes_outside_cycle(int N, int[] p) {
  for (; i < N; ++i) {
    boolean[] b = new boolean[N];
    for (n = i; !b[n]; n = p[n]) b[n] = true;
    r += n == i ? 0 : 1;
  }
  return r;
}

