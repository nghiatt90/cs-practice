// https://app.codesignal.com/challenge/wh9aCn9qXWfv8tRsu
int i = 2, j, t;
int[] power(int X) {
  for (;; ++i)
    for (t = j = 1; t < X; ++j)
      if ((t *= i) == X) return new int[] {i, j};
}

