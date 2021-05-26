// https://app.codesignal.com/challenge/PuLQr5L4yPMmWzdHK
	int t, k, i;
	int cake(int p) {
		for (t = p - 1; ++i * i <= p;)
			t = p % i > 0 ? t : 
				p / i % 2 < 1 ? 
                (k = i - 1 + p / i / 2) < t ? k : t : 
      			(k = i - 1 + p / i) < t ? k : t;

		return t;
	}
