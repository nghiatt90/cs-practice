// https://app.codesignal.com/challenge/PukdZ4XAz4rmqY9fp
int l, c, m;
int StudyingHours(int n, int[] a) {
  for (int i : a) {
    c = i < l ? 1 : c + 1;
    m = c > m ? c : m;
    l = i;
  }
  return m;
}

