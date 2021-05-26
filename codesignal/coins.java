// https://app.codesignal.com/challenge/Dc6J2ypb3rtDdcLvd

	int A[], R, N;

	int coins(int n, int S, int[] a) {
		for (A = a, N = n; --n >= 0;)
			R += r(S, n);
		return R;
	}
	
	int r(int s, int i) {
		return (s -= A[i]) < 0 ? 0 : s < 1 ? 1 : S(i, s);
	}
	
	int S(int j, int s) {
		int r = 0, i = j;
		for (; ++i < N;)
			r += r(s, i);
		return r;
	}
