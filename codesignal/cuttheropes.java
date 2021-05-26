// https://app.codesignal.com/challenge/Y8epWDRpDoKxvSyGY
int i, r[];
int[] CutTheRopes(int N, int[] a) {
  TreeMap<Integer, Integer> t = new TreeMap<Integer, Integer>();
  for (int k : a)
    t.put(k, t.get(k) == null ? 1 : t.get(k) + 1);
  r = new int[t.size()];
  r[i++] = N;
  for(int k : t.values()) {
    if (i == r.length) break;
    r[i] = r[i++ - 1] - k;
  }
  return r;
}

