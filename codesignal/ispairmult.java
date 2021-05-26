// https://app.codesignal.com/challenge/KLY9zvSrteGjvTtGn
int i, j, l;
boolean isPairMult(int[] a, int N) {
  l = a.length;
  for (; i < l; ++i)
    for (j = i + 1; j < l; ++j)
      if (a[i] * a[j] == N) return true;
    return false;
}

