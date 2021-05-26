// https://app.codesignal.com/challenge/BnTbnMrdCmYjXY6KB

	int r[][], x, i, j;
	int[][] pyramidMatrix(int l) {
	  r = new int[l][l];
	  for (; x < l; x++)
	    for (i = x; i < l - x; ++i)
	      for (j = x; j < l - x;)
	        r[i][j++]++;
	   return r;
	}
