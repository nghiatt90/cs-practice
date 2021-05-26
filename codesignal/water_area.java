// https://app.codesignal.com/challenge/oYCqpx7KWHGoh2cyM
int i, j, k, s;

	int water_area(int[] a) {
		for (; i < a.length; ++i)
			for (k = a[i]; ++k <= 9;) {
				boolean l = 0 > 1, r = l;
				for (j = 0; j < i;)
					l |= a[j++] >= k;
				for (j = i; ++j < a.length;)
					r |= a[j] >= k;
				s += l & r ? 1 : 0;
			}
		return s;
	}
