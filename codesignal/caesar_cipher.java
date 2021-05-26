// https://app.codesignal.com/challenge/kgsdtAFeC7ZokjsZi
String Caesar_Cipher(String m, int s) {
		String r = "";
		for (int k : m.getBytes()) {
			int i = k - s;
			r += (char)(k < 65 | k > 90 & k < 97 | k > 122
				? k : i < 65 | i < 97 & k > 96
					? i + 26 : i);
		}
		return r;
	}
