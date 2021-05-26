// https://app.codesignal.com/challenge/hSufREZpTrzJpLk3h
int i, j, l, s, b[];
int pairwise(int[] a, int N) {
  for (b = new int[(l = a.length)]; i < l; ++i)
    for (j = i + 1; j < l; ++j)
    if (b[i] + b[j] + a[i] + a[j] == N) {
      b[i] = b[j] = 9;
      s += i + j;
    }
  return s;
}

