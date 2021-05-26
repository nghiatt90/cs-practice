// https://app.codesignal.com/challenge/i5LfbEQizJnZfDpZ9
    int s;
	int sumofoddnumbers(int a, int b) {
	  for (; ++a < b; s %= 1e7 + 7)
		  s += a % 2 * a;
	  return s;
	}
