// https://app.codesignal.com/challenge/MuRkfKz5vBSLHAQFB

	int v[][] = new int[20][20], t[][], i, j, r, c, m;

	int mirrors(int[][] T) {
		t = T;
		r = t.length;
		c = t[0].length;
		for (; i < r; ++i)
			for (j = 0; j < c; ++j)
				if (t[i][j] == -1)
					d(i, j);
		return m - 1;
	}

	void d(int i, int j) {
		if (i >= 0 & i < r & j >= 0 & j < c && t[i][j] < 1)
			if (v[i][j] < 1) {
				m += v[i][j] = 3;
				d(i - 1, j);
				d(i + 1, j);
				d(i, j - 1);
				d(i, j + 1);
			} else
				--m;
	}
