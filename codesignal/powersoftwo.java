// https://app.codesignal.com/challenge/6TscjNr8sEEHage7g
int PowersOfTwo(int N)
    {
        return r(N, 256);
    }

    int r(int p, int m)
    {
        return p < 0 ? 0 : p < 2 | m < 2 ? 1 : r(p - m, m) + r(p, m / 2);
    }
