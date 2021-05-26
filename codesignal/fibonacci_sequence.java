// https://app.codesignal.com/challenge/qHEPWgvz3zeifrMsD
int l, i;
boolean Fibonacci_Sequence(int[] a) {
  for (; i < a.length; ++i) {
    if (a[i] % f(i) > 0) return false;
    l = a[i] / f(i) - l;
  }
  return l == 0;
}

int f(int n) {
  return n < 2 ? 1 : f(n - 1) + f(n - 2);
}

