// https://app.codesignal.com/challenge/SPsgrZx4s6uCZBx3D
int b, i;
boolean magic_square(int[][] a) {
  for (; i < 3; ++i)
    b |= a[i][0] + a[i][1] + a[i][2] - 15 
      |  a[0][i] + a[1][i] + a[2][i] - 15;
  return b == 0 & a[0][0] + a[1][1] + a[2][2] == 15;
}
