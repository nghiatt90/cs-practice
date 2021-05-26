// https://app.codesignal.com/challenge/ByxfF6Tdu6hrTKxwF
byte c, b[];
int zero_and_one(String s) {
  b = s.getBytes();
  for (int z : b)
    c += (z == b[0]) ? 1 : -1;
  return c;
}

