// https://app.codesignal.com/challenge/Q8hrNfWQy3xwaPdsi
int i, j, s, l;
int charactersMatrix(String m, int r, int c) {
		byte[] b = m.toUpperCase().getBytes();
		l = b.length;
		for (; i < l; ++i)
			if (b[i] == 80) {
				if (i / c < r - 5) {
					s += b[i + c] == 72 & b[i + c + c] == 85 & b[i + 3 * c] == 79 & b[i + 4 * c] == 78
							& b[i + 5 * c] == 71 ? 1 : 0;
					if (i % c < c - 5)
						s += b[i + c + 1] == 72 & b[i + c + c + 2] == 85 & b[i + 3 * c + 3] == 79
								& b[i + 4 * c + 4] == 78 & b[i + 5 * c + 5] == 71 ? 1 : 0;
				}
				if (i % c < c - 5)
					s += b[i + 1] == 72 & b[i + 2] == 85 & b[i + 3] == 79 & b[i + 4] == 78 & b[i + 5] == 71 ? 1 : 0;
			}
		return s;
	}
