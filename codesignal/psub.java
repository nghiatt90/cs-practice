// https://app.codesignal.com/challenge/DxcMp75J9PyEAeXgp
int pSub(std::string s) {
	int i, j = 0, k, N = s.length(), t, R[2][N + 1];
	s = " " + s + "	";

	for (; j < 2; j++)
		for (R[j][0] = t = 0, i = 1; i <= N; i += k) {
			for (; s[i - t - 1] == s[i + j + t]; t++) ;
			for (R[j][i] = t, k = 0; R[j][i - ++k] != t - k & k < t;)
				R[j][i + k] = std::min(R[j][i - k], t - k);
			t -= t > k ? k : t;
		}

	for (j = i = 0; ++i <= N;)
		j += R[0][i] + R[1][i];
	return j + N;
}
