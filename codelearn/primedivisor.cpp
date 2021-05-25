// https://codelearn.io/training/detail/114524
int primeDivisor(int a, int b, int k)
{
    static int sieve[10000001] = {0};
    for (int i = 2; i <= b; ++i) {
        if (sieve[i] > 0) continue;
        sieve[i] = 1;
        for (int j = i+i; j <= b; j += i) {
            sieve[j] += 1;
        }
    }
    int ans = 0;
    for (; a <= b; ++a) {
        if (sieve[a] == k) ans += 1;
    }
    return ans;
}

