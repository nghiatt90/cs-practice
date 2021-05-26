// https://app.codesignal.com/challenge/rhnnzuauedhucZ298

	String O = "-+/*", T = "";
	int r, l, x, a, b;
	Stack<Integer> s = new Stack(), e = new Stack();

	int RomanExpression(String S) {
		for (char c : S.toCharArray()) {
			if (c > 64) {
				T += c;
				++l;
				continue;
			}
			if (l > 0) {
				byte[] B = T.getBytes();
				for (r = x = 0; x < l - 1;)
					r += (s(B[x]) < s(B[x + 1]) ? -1 : 1) * s(B[x++]);
				e.push(r + s(B[l - 1]));
			}
			T = "";
			l = 0;
			x = O.indexOf(c);

			if (x > -1)
				if (s.size() < 1)
					s.push(x);
				else {
					while (s.size() > 0)
						if (s.peek() / 2 >= x / 2)
							e();
						else
							break;
					s.push(x);
				}
			else if (c == 40)
				s.push(-2);
			else if (c == 41) {
				while (s.peek() > -2)
					e();
				s.pop();
			}
		}
		while (s.size() > 0)
			e();
		
		return e.pop();
	}

	void e() {
		r = s.pop();
		a = e.pop();
		b = e.pop();
		e.push(r < 1 ? b - a : r < 2 ? b + a : r < 3 ? b / a : b * a);
	}

	int s(byte c) {
		return c < 68 ? 100 : c < 69 ? 500 : c < 75 ? 1 : c < 77 ? 50 : c < 78 ? 1000 : c < 87 ? 5 : 10;
	}
