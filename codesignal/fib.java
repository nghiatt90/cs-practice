// https://app.codesignal.com/challenge/CxqWckTqFwRTTAfrd
int F[], i;
int Fib(int N) {
  F = new int[100];
  F[i = 2] = 1;
  for (; ++i <= N;)
    F[i] = (F[i-1] + F[i-2]) % 1000000007;
  return F[N];
}

