// https://app.codesignal.com/challenge/6kwzQzNZ8KkGhLucf

	int v[][] = new int[22][22], n, C;

	int OneKnight(int N, int[] c, int[] d) {
		for (int[] a : v)
			Arrays.fill(a, 99);
		n = N;
		g(c[0], c[1]);
		return v[d[0]][d[1]];

	}

	void g(int x, int y) {
		if (x < 1 | x > n | y < 1 | y > n || v[x][y] <= C)
			return;
		v[x][y] = C++;
		g(x - 2, y - 1);
		g(x - 2, y + 1);
		g(x + 2, y - 1);
		g(x + 2, y + 1);
		g(x - 1, y + 2);
		g(x - 1, y - 2);
		g(x + 1, y + 2);
		g(x + 1, y - 2);
        C--;
	}
