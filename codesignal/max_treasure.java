// https://app.codesignal.com/challenge/grwY9WYjBTyJHy4Bb
int n, i, k, c, s, p;
int max_treasure(int N, int[][] C, int P)
{
  for (; ++i < 1 << N; n = p > P | s < n ? n : s)
    for (k = i, c = N, s = p = 0; k > 0; 
         s += k % 2 * C[--c][0],
         p += k % 2 * C[c][1], 
         k /= 2) ;
  return n;
}
