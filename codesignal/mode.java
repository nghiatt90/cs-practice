// https://app.codesignal.com/challenge/y7qyE8piNcpPtXSte
int m, f[];
Object mode(int[] a) {
  f = new int[999];
  for (int i : a)
    m = ++f[i] > m ? f[i] : m;
  List l = new Vector();
  for (int k : a)
    if (f[k]-- == m) l.add(k);
  return l.toArray();
}

