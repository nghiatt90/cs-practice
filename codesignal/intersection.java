// https://app.codesignal.com/challenge/bgDn3JcceRhs9HDg8

	int j, f, c;

	Object intersection(int[][] a) {
		Set s = new TreeSet();
		for (int i : a[0]) {
			f = j = 0;
			for (int t : a[0]) f += t == i ? 1 : 0;
			for (int[] t : a) {
				c = 0;
				for (int x : t)
					c += x == i ? 1 : 0;
				j = c == f ? j : 1;
			}
			if (j < 1)
				s.add(i);
		}
		return new ArrayList(s);
	}
