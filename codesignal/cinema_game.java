// https://app.codesignal.com/challenge/c9Yd8xJ6kMrqZ7MKW
int i, w[] = new int[9999];
    String cinema_game(int N, int K, int[] r) {
	  for (; i++ < N;)
	    for (int k : r)
	      w[i] |= k > i || w[i - k] < 1 ? 1 : 0;
	  return w[N] < 1 ? "Felix" : "Tigran";
	}
