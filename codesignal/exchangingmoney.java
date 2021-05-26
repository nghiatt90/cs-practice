// https://app.codesignal.com/challenge/pZ6y2WKwNXjZeXZ6Y

	int c[] = {2, 5, 10, 20, 50};
	int exchangingmoney(int m) {
		return r(m, 4);
	}

    int r(int m, int i) {
    	return m == 0 ? 1 : m < 0 | i < 0 ? 0 : r(m, i - 1) + r(m - c[i] * 100, i);
    }
