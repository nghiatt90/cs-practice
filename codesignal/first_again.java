// https://app.codesignal.com/challenge/ygdAxNGxQ3rKu8NA2
int i = 1, c = 1;
int first_again(int N) {
  for (; (i = i < N ? i * 2 : N * 4 - i * 2 - 1) > 1; ++c) ;
  return c;
}
