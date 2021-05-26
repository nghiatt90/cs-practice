// https://app.codesignal.com/challenge/MbWcdJudZxEurPFKj
int s, i, k;
int Prime_sum(int A, int B)
{
  for (; A <= B; s += A > 1 ? A * k : 0, A++)
    for (k = i = 1; ++i * i <= A;)
      k &= A % i < 1 ? 0 : 1;
  return s;
}
