// https://app.codesignal.com/challenge/DXrnEgbSkkzewPaED
int i, c, s, l, k;
int Count_SubArrays(int[] a, int D) {
  l = a.length;
  for (; ++i < 1 << l; c += s % D < 1 ? 1 : 0)
    for (k = s = 0; k < l; )
      s += ((1 << k & i) >> k++) * a[l - k];
    return c;
}

