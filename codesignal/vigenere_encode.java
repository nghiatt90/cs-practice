// https://app.codesignal.com/challenge/qmoiMiFTtYPTTu7gF

	int i, t;
	String vigenere_encode(String m, String k) {
		String r = "";
		k = k.replace(" ", "");
		for (int x : m.getBytes())
			r += (char) (x < 33 ? x : 
				(t = x + k.charAt(i++ % k.length())) - (t < 220 ? 97 : 123));
		

		return r;
	}
