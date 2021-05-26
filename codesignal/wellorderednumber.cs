// https://app.codesignal.com/challenge/ffqt8JakCqyNKBMDc
    boolean wellOrderedNumber(int n) {
		return n < 10 || n % 100 / 10 < n % 10 & wellOrderedNumber(n / 10);
	}


