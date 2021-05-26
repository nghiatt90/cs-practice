// https://app.codesignal.com/challenge/KFZ3xzT9H4PdtYYFr
int i;
Object correct_parentheses(String s) {
  for (; i++ < 99;)
    s = s.replace("()", "").replace("[]", "");
  return s.length() < 1;
}

