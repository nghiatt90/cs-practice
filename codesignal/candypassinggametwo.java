// https://app.codesignal.com/challenge/sEcGFsg6mPzvmJEp9
int i, p[], j;

	int candyPassingGameTwo(int N, int[] M) {
		p = new int[N];
		for (int k : M) {
			for (i = 0; i < k;)
				i += p[j = ++j % N] > 0 ? 0 : 1;
			++p[j];
			while (p[j = ++j % N] > 0)
				;
		}
		return j < 1 ? -1 : j;
	}
