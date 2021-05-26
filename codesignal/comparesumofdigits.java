// https://app.codesignal.com/challenge/wma68zRgKjRL9LwAo
int i;
int compareSumOfDigits(String N) {
  for (int k : N.getBytes())
    i += k % 2 > 0 ? k - 48 : 48 - k;
  return i;
}

