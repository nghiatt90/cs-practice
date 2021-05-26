// https://app.codesignal.com/challenge/X4H8yt98JbDLbh3k8
int i, j, a[];
int[] findPermutation(int n, int[] p, int[] q) {
  a = new int[n];
  for (; i < n; i++)
    for (j = 0; j++ < n;)
      if (q[i] == p[j - 1])
        a[i] = j;
  return a;
}

