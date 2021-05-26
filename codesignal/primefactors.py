# https://app.codesignal.com/challenge/zjSMy2o5bxtaodmN9

	String primefactors(int n) {
		String r = "";
		for (int i = 1, t = n; ++i <= n;)
			for (; n % i < 1; n /= i)
				r += t > n ? "*" + i : i;
		return r;
	}
