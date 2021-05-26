// https://app.codesignal.com/challenge/XedR33Z7cGMNqmJNh

	int L, i, j, k, c, m, l;

	int strings(String S) {
		L = S.length();
		for (; i < L; ++i)
			for (j = i + 1; j <= L; ++j)
				for (c = k = 0; k <= L - j + i; m = c > m ? c : m)
					l = (c += S.substring(i, j)
                         .equals(S.substring(k, k++ + j - i)) ? 1 : 0) < m 
					     | c == m & j - i < l ? l : j - i;
		return l;
	}
