// https://app.codesignal.com/challenge/QSNyYnw857gi7pubN
int i, c;
int notLucky(int N) {
  for (; i <= N; i += 13)
    c += (i + "").matches("[^47]*") ? 1 : 0;
  return c;
}

