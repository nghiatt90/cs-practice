// https://app.codesignal.com/challenge/n3s66HzZTXJuvc5o9
int f, i;
String RSA_SKG(int N) {
  String s = "";
  for (f = N / 3 * 3; f >= 0; f -= 3)
    if ((N - f) % 5 < 1) {
      for (; i < f; ++i)
        s += "5";
      for (; i < N; ++i)
        s += "3";
      return s;
    }
  return "-1";
}

