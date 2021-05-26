// https://app.codesignal.com/challenge/q4o6aFqSAuevoCGTq
int r;
int[] withdraw(int N) {
  if (N % 20 > 0) {
    r = 1;
    N -= 50;
  }
  return new int[] { N / 100, r, N % 100 / 20 };
}

