// https://app.codesignal.com/challenge/dNuJoSYFHZnAKBajr
int hanoiNextDisk(int N) {
  return N & ~(N - 1);
}

