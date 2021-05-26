// https://app.codesignal.com/challenge/y5bC94nb3e5YBH4f7
int[] sequence(int k, int y, int z) {
  int r[] = new int[z];
  for (; z > 0;)
    r[--z] = k * z - y + k;
  return r;
}

