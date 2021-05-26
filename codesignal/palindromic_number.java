// https://app.codesignal.com/challenge/PXLcKWx4E7NnSj8fj
String Palindromic_Number(int N) {
  String a = "" + N;
  for (; --N > 0;)
    a = N + a + N;
  return a;
}

