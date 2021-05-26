// https://app.codesignal.com/challenge/uNNgc77ofuvtxhx2w
String SC(String s) {
    String r = "";
    for (int t : s.getBytes())
	r += (char)(t > 96 ? t - 32 : t > 64 ? t + 32 : t);
    return r;	
}
