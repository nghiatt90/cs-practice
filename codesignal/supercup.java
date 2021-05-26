// https://app.codesignal.com/challenge/mhQHptix9FRRyEmaz
String SuperCup(String s) {
  S = s;
  return l("zamalek") < l("alahly") ? "win" : "loss";
}

String S;
int l(String t) {
  int i = 0;
  for (int c : t.getBytes())
    for (; S.charAt(i++) != c ;);
    return i;
}

