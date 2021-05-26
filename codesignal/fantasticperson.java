// https://app.codesignal.com/challenge/RJo5qAng8bA7B73Z4
int i, j;
int FantasticPerson(int n, boolean[][] t) {
  for (; i < n; j = 0, ++i) {
    for (boolean k : t[i])
      j |= k ? 0 : 1;
    if (j < 1) return i;
  }
  return -1;
}

