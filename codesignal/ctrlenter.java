// https://app.codesignal.com/challenge/a7RyKLYHAGq9tnjk2
String CtrlEnter(String s) {
  s = s.charAt(2) == 'w' ? s : "www." + s;
  return s.indexOf('.', 4) > 0 ? s : s + ".com";
}
