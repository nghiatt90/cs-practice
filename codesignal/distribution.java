// https://app.codesignal.com/challenge/7SSunqhjiRGCGiXLf
float s, l;
double distribution(String t, String c) {
  for (int k : t.getBytes()) {
    s += k == c.charAt(0) ? 1 : 0;
    l += k > 32 ? 1 : 0;
  }
  return l < 1 ? 0 : s / l;
}

