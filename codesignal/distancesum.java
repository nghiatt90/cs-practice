// https://app.codesignal.com/challenge/9eHnvyY7Tv3KWmtcA
int distancesum(int n, int[] x) {
  n = 0;
  for (int i : x)
    for (int j : x)
      n = i > j ? n : j - i + n % 10000007;
  return n;
}

