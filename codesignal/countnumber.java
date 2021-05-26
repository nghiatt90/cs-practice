// https://app.codesignal.com/challenge/vXL37GGfZ78K3GEob
int i, c;
	int CountNumber(int N, int X) {
	  for (; i++ < N;)
	    c += X % i > 0 | X / i > N ? 0 : 1;
	  return c;
	}
