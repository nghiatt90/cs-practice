// https://app.codesignal.com/challenge/5cTLum4zq5X3fbQ9n
    String HackIt(String s) {
		String r = "";
		for (int k : s.getBytes()) 
r += (char) (k > 64 & k < 91 ? 155 - k : k > 96 & k < 123 ? 219 - k : k);		
		return r;
	}
