// https://codelearn.io/training/detail/34890
int digitsCount(int l, int r)
{
    int pmax = 0;
    int counter[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    for (; l<=r; ++l) {
        int t = l;
        while (t) {
            int d = t % 10;
            t /= 10;
            if (++counter[d] > counter[pmax] || (counter[d] == counter[pmax] && d < pmax)) {
                pmax = d;
            }
        }
    }
    return pmax;
}

