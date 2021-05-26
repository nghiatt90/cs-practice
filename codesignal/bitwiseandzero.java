// https://app.codesignal.com/challenge/XNS4R2nxHuob7C4Yr
int c;

	int bitwiseandzero(int n, int[] a) {
		for (int i : a)
			for (int j : a)
				c += i != j & (i & j) < 1 ? 1 : 0;
		
		return c;
	}
