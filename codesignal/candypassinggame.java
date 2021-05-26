// https://app.codesignal.com/challenge/kxvYpdibf2sxpaxAM
Object candyPassingGame(int N) {
  int k = 1;
  for (; N - k > 2; k *= 2);
  return N - k > 0;
}

