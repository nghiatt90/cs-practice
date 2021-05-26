// https://app.codesignal.com/challenge/zgpinrRdAjF7BMGqs
int f[] = new int[999], i = -1;
int Majority_Element(int N, int[] A) {
  for (int k : A)
    i = ++f[k] > N / 2 ? k : i;
  return i;
}

