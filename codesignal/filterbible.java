// https://app.codesignal.com/challenge/sWJDFe5BBowCztTAJ
Object filterBible(String[] S, String b, String c) {
  String s = "";
  for (String t : S)
    s += t.startsWith(b + c) ? t + " " : "";
  return s.split(" ");
}

