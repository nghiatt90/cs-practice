// https://app.codesignal.com/challenge/ZMJNZNPzcNNS42eJR
    int m, t;
	Object subarraysearch(String S, String s) {
	  for (int c : s.toLowerCase().getBytes())
	    m = (t = S.toLowerCase().indexOf(c)) < m ? 99 : t;
	  return m < 99;
	}
