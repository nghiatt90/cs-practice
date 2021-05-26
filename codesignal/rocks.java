// https://app.codesignal.com/challenge/e2M6rhLcm5sC7qpwi
        int a, j = 1, k = 1, i;
        int Rocks(int n)
        {
            for (i = n; i > 9; k *= 10, i /= 10)
                a += 9 * k * j++;
            return a + (n - k + 1) * j;
        }
