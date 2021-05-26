// https://app.codesignal.com/challenge/xRtmD6q3DFDYrnubA
int x;
Object Anagram(String a, String b) {
  for (int i : a.getBytes())
    x += i;
  for (int i : b.getBytes())
    x -= i;
  return x == 0;
}

