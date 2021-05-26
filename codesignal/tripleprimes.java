// https://app.codesignal.com/challenge/xNkpTCjgLBmweDzjj

    int i, j, H = 100;	
    BigInteger c[] = new BigInteger[H], n[], t, r = BigInteger.ZERO, O = r;
	Vector<Integer>[] C = new Vector[H];
	int TriplePrimes(int N) {
		Arrays.fill(c, O);
		for (; i < H;)
			C[i++] = new Vector();
		for (; i < 999; ++i) {
			t = BigInteger.ONE;
			for (j = 1; ++j < 34;)
				if (i % j == 0) 
					t = O;
			c[i % H] = c[i % H].add(t);
			if (t.intValue() > 0)
				C[i / 10].add(i % H);
		}
		for (; N-- > 3;) {
			n = new BigInteger[H];
			Arrays.fill(n, O);
			for (j = 0; j < H; ++j)
				for (int k : C[j])
					n[k] = n[k].add(c[j]);				
			c = n;
		}
		for (i = 0; i < H; ++i)
			r = r.add(c[i]);
			
		return r.mod(new BigInteger("1000000009")).intValue();
	}
