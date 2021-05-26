// https://app.codesignal.com/challenge/Hg3tsduNFYegZHMkR
int j, n;
int judge(int[] v) {
  n = v[0];
  for (int i : v) n &= i;
  for (; n % 2 < 1 & n > 0; ++j, n /= 2);
  return n == 1 ? ++j : 0;
}

