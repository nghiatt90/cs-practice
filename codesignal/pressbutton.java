// https://app.codesignal.com/challenge/xWsspsYvuy9G6rSop
int i, x;
int pressButton(int n) {
  for (; ++i < n;)
    x += i * (n - i);
  return x + n;
}

