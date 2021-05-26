// https://app.codesignal.com/challenge/C6C8dC6bfGq5wu9ah
int i, k;
boolean palindrome_prime(int N) {
  for (i = 1; ++i < N;)
    k = N % i < 1 ? 1 : k;
  return k < 1 & N > 1 & (N + "").equals(new StringBuffer(N + "").reverse().toString());
}

