// https://app.codesignal.com/challenge/AYM6krjvPPfkg6EPP
String matrix(String N) {
		BigDecimal n = new BigDecimal(N), t = new BigDecimal(2);
		return "" + n.pow(2).subtract(n).add(t).multiply(t);
	}
