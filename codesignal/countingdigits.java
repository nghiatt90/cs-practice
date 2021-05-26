// https://app.codesignal.com/challenge/gFiwQrkzufWjkscNA



	int i, j = 1, r;

	int CountingDigits(int N) {

	  for (; N >= j; j *= 10)

	    r += 9 * ++i * j;

	  return r - (j - N - 1) * i;

	}

