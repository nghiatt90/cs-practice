// https://app.codesignal.com/challenge/Wee7Fu36PDvvoagBG
int k;
int reverse_number(int n) {
  for (;n > 0; n /= 10)
    k = k * 10 + n % 10;
  return k;
}

