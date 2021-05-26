// https://app.codesignal.com/challenge/fMFam2r4FbszKvRcP
int i, p = 9;
int whichBusToTake(int n, String[] c, boolean[] g) {
  for (; i < c.length; ++i)
    if (g[i])
      if (c[i].equals("red")) return i;
      else p = i < p ? i : p;
  return p;
}

