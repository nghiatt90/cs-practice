// https://app.codesignal.com/challenge/pZwhaskY2xtYQkaFj
int s, m, i, l, e, y;
Object is_cyclic_sorted(int[] a) {
  s = a.length;
  for (; m < s;)
    if ((y = a[m] - a[(m++ - 1 + s) % s]) > 0) ++i;
    else if (y < 0) ++e;
    else ++l;
  return s < 2 | l < 1 & (i < 2 | e < 2);
}

