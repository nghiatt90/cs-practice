// https://app.codesignal.com/challenge/a2egxQqt45rvbMk65
int t[] = new int[9999], c;
int points(int N, int[] x, int[] y) {
  for (;N-- > 0;)
    c += t[x[N] * 97 + y[N]]++ < 1 ? 1 : 0;
  return c;
}

