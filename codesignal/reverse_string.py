# https://app.codesignal.com/challenge/MLwxkbB5WcGwow2dC
String reverse_string(String s) {
  String r = "";
  for (char c : s.toCharArray())
    r = c < 97 ? r : c + r;
  return r;
}

