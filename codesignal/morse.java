// https://app.codesignal.com/challenge/jJiu5tTR3H7vaPvak
String morse(String t) {
  String z = "                                                                 .---..-...-.---.-..-...---                                                                 -... .-..-.--.----. ..-..-                                                                  .-. -.. --.  --... -.-.-.                                                                  ..  . . - .   .-    - --.", s = "";
  char l;
  for (int c : t.toUpperCase().getBytes()) {
    if (c < 65) s += " ";
    else for (int i = 0; i < 4;)
      s += (l = z.charAt(i++ * 91 + c)) > 32 ? l : "";
    s += " ";
  }
  return s;
}

