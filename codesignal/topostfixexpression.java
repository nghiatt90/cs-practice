// https://app.codesignal.com/challenge/FPXR3wXfcGS7iDmKN
    int c, i;

	Object toPostFixExpression(String[] I) {
		String o = "  -+/*%", l = "", x = " ";
		Stack<Integer> s = new Stack();

		for (String t : I)
			if ((i = o.indexOf((c = t.charAt(0)))) >= 0) {
				while (!s.isEmpty() && s.peek() / 2 >= i / 2)
					l += o.charAt(s.pop()) + x;
				s.push(i);
			} else if (c < 41)
				s.push(0);
			else if (c < 42) {
				while (s.peek() > 0)
					l += o.charAt(s.pop()) + x;
				s.pop();
			} else
				l += t + x;

		while (!s.isEmpty())
			l += o.charAt(s.pop()) + x;
		return l.split(x);
	}
