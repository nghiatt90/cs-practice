// https://app.codesignal.com/challenge/7Yi7P6LHoj8w95Hzc
int x[] = new int[2], i, j = -1;
String blackjack(int[] p) {
  for (; i < p.length; j = p[i++] < 1 ? i % 2 : j)
    if (j < 0) x[i % 2] += p[i];
    else x[j]+= p[i];
  return x[1] < 21 & x[1] > x[0] | x[0] > 21 ? "second" : "first";
}

