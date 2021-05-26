// https://app.codesignal.com/challenge/2mKoQwiJtZvypPF9o
int c, i;
int FindString(String m, String f) {
  for (; i < m.length();)
    c += m.substring(i++).startsWith(f) ? 1 : 0;
  return c;
}

