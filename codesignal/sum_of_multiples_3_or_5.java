// https://app.codesignal.com/challenge/BRP4ALjJwPzvtEqy7
int s, i;
int Sum_Of_Multiples_3_Or_5(int N) {
  for (; ++i < N;)
    s += i % 3 * i % 5 < 1 ? i : 0;
  return s;
}

