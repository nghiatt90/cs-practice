// https://app.codesignal.com/challenge/dsHrXPyRTWZL2rrc3
int p[] = new int[1000001], c, i = 1, j;
int Sum_prime_numbers(int N) {
  for (; i++ < N;)
    if (p[i] < 1)
      for (c = (c + i) % 256, j = i; j <= N; j += i)
        p[j] = 1;
  
  return c;
}

