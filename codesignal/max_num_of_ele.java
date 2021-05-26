// https://app.codesignal.com/challenge/3MPvaaMr3njACFFd5
int s, c, m, i, l, j, b, r;
int max_num_of_ele(int S, int[] L) {
  l = L.length;
  for (; i < 1 << l; ++i)
    for (b = c = s = 0, j = i; j > 0; 
         m = s == S & c > m ? c : m, j /= 2) {
      c += r = j % 2;
      s += r * L[l - ++b];
    }
  return m;
}

