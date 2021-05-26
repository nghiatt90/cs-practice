// https://app.codesignal.com/challenge/yPBo72EQhBXZhcYJa
int a, b;
Object isFibonacci(int n) {
  for (b = 1; b < n; b += a, a = b - a);
  return b == n;
}

