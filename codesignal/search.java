// https://app.codesignal.com/challenge/vTQKmkCeYw94Tb3co
int i;
String search(int[] a, int x) {
  for (; i < a.length; ++i) if (a[i] == x) return "" + i;
  return "Not found";
}

