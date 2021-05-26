// https://app.codesignal.com/challenge/JCEntgL9siuS49mWZ
int c;
int diceProbability(int[] a, int[] b, int N) {
  for (int x : a)
    for (int y : b)
      c += x + y == N ? 1 : 0;
  return c;
}

