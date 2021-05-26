// https://app.codesignal.com/challenge/EmACG6nhJfngWLnAd
int[] getCandyPosition(int N, int r, int c, int x) {
		  return x-- > N ? new int[] { -1, -1, -1 } :
			  new int[] { x / r / r + 1, r - x / r % r - 1, c - x % c - 1 };
		}
