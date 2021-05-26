// https://app.codesignal.com/challenge/x4fZa7bZEXooqTkPX
int i, j;
int[][] Simple_Task(int N, int M, String[][] t) {
  int[][] r = new int[N][M];
  for (; i < N; ++i)
    for (j = 0; j < M;)
      r[i][j] = t[i][j++].charAt(0) < 47 ? 0 : 1;
  return r;
}

