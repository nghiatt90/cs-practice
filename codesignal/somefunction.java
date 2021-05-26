// https://app.codesignal.com/challenge/8JgfyuP5ecWjiF92E
	int i = 1, b = 1;
	Object someFunction(int n) {
		for (; ++i * i <= n;)
			b *= n % i;
		return n > 1 & b > 0;
	}

