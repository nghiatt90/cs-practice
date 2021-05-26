// https://app.codesignal.com/challenge/yRRvMHgtSy7cdgvJN
int trivia_game(int[] s, int j, int h) {
    int X = s[0] * 2, H = s[2], J = s[1],
        S[] = { J - j, J + j, H - h, H + h }, a = 0;
    Arrays.sort(S);
    for (int x : S)
	a = X > x ? x - s[0] + 1 : a;
    return a < 0 | J - j > X | H - h > X ? 0 : a;
}

