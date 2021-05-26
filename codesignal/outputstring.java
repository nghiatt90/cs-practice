// https://app.codesignal.com/challenge/BTAenodSdh342juYM
    int i, j, f[] = new int[355];
	String outputString(String s) {
	  for (int a : s.getBytes())
        f[a]++;
      s = "";
      String m = s, t = s;
      for (; i < 355; ++i) {
        for (j = 0; j < f[i] / 2; ++j) {
          s += (char)i;
          t = (char)i + t;
        }
        m += f[i] % 2 > 0 ? (char)i : "";
      }
      return m.length() < 2 ? s + m + t : "imp";
	}
