# https://app.codesignal.com/challenge/icBpKWxzn8zEc8puy
int t;
int HalfSum(int[] A) {
  for (int x : A) t += x;
  for (int x : A) if (x == t/3) return x;
  return 0;
}

