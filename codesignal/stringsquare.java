// https://app.codesignal.com/challenge/oq5wmknjraeQE5RQq
    int a[], l, i, j, t;

	int stringSquare(String s) {
		l = s.length();
		a = new int[l];
		Arrays.fill(a, 9);
        for (;; i = t = 0) {
			for (; i < l; ++i) {
				t = t * 10 + a[i];
				for (j = i + 1; j < l; ++j)
					t = s.charAt(i) == s.charAt(j) & a[i] != a[j] ? -1 : t;
			} 
			if (t % Math.sqrt(t) == 0 & t > 0) return t;
			for (i = 1; i <= l; ++i)
				if (--a[l - i] >= 0) i = l;
				else a[l - i] = 9;
            if (a[0] < 1) return -1;
		}
	}
