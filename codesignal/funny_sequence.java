// https://app.codesignal.com/challenge/XHERPbe8buy3h6KuT
int i, z = -1;
boolean Funny_Sequence(int[] a) {
  for (int x : a)
    i += (z *= -1) * x;
  return i == 0;
}

