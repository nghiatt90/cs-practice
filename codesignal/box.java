// https://app.codesignal.com/challenge/YwodwqkX52soqq7Co
int i, j;
String box(int n) {
  String s = "";
  if (n < 2) return n < 1 ? s : "*";
  for (; i < n; ++i) s += "*";
  s += "\n";
  for (; j < n - 2; ++j) {
    s += "*";
    for (i = 0; i < n - 2; ++i)
      s += " ";
    s += "*\n";
  }
  for (; n-- > 0;) s += "*";
  return s;
}

