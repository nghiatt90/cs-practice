# https://app.codesignal.com/challenge/LNL7T9Nj5tT2idHvn
int F[] = new int[99], i;
	String S = "New Folder";
	String New_Folder(String[] f) {
	    for (String s : f)
	        if (s.startsWith(S))
	        	F[s.endsWith(")") ? Integer.valueOf(s.substring(12, s.length() - 1)) : 0] = 1;
	    for (;F[i++] > 0;);
	    return S + (i < 2 ? "" : " (" + (i - 1) + ")");
	}
