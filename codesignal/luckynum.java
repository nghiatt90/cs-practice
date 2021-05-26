// https://app.codesignal.com/challenge/GGfixSdsDW2mCNnXP
int LuckyNum(int L, int R) {
  for (; L <= R; L++) {
    int t = L, k = 1;
    for (; t > 0; t /= 10)
      k *= t % 10 == 4 | t % 10 == 7 ? 1 : 0;
    if (k > 0) return L;
  }
  return -1;
}

