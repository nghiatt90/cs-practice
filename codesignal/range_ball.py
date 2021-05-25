# https://app.codesignal.com/challenge/q7DBhbafrBKZ3gRLT
int range_ball(int N) {
    return N < 2 ? 0 : N * range_ball(N - 1) - N % 2 * 2 + 1;
}
