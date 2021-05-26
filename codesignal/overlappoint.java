// https://app.codesignal.com/challenge/X3W56qBKtHSZFkR4N
int x, y, c, j;
int overlapPoint(int[] a, int[] b) {
  for (x = -9; ++x < 9; )
    for (y = -9; ++y < 9; )
      c += (j = (x - a[0])) * j + (j = (y - a[1])) * j <= a[2] * a[2]
         & (j = (x - b[0])) * j + (j = (y - b[1])) * j <= b[2] * b[2]
         ? 1 : 0;
  return c;
}

