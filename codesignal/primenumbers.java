// https://app.codesignal.com/challenge/SgR6FXwmCiJ2pjAKR
Object[] PrimeNumbers(int a, int b) {
  ArrayList r = new ArrayList();
  a = a < 2 ? 2 : a;
  for (; a <= b; ++a) {
    boolean x = false;
    for (int i = 2; i < a; ++i)
      x |= a % i < 1;
    if (!x) r.add(a);
  }
  return r.toArray(new Object[r.size()]);
}

