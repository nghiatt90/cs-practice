// https://app.codesignal.com/challenge/svrc9LPrTp3BYkkGW
String longestCommonStartingSubstring(String[] a) {
  for (String s = a[0];; s = s.substring(0, s.length() - 1)) {
    boolean i = 0 < 1;
    for (String x : a)
       i &= x.startsWith(s); 
    if (i) return s;
  }
}

