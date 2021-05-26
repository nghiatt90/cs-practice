// https://app.codesignal.com/challenge/BMeWyyyqGC5Xf5m8T
int[] LineLandFuel(int i, int[] c) {
  int L = c.length - 1;
  return new int[] { 
    Math.max(c[i] - c[0], c[L] - c[i]), 
    i < 1 ? c[1] - c[0] : i == L ? c[i] - c[i - 1] :
      Math.min(c[i] - c[i - 1], c[i + 1] - c[i]) };
}

