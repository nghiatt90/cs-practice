// https://app.codesignal.com/challenge/uSEGHsnm3SSYYSXNa
int maximumsubarray(int[] a) {
  int M = -999, m = M;
  for (int x : a) {
    m = m + x > x ? m + x : x;
    M = M > m ? M : m;
  }
  return M;
}

