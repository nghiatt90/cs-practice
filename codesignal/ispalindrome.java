// https://app.codesignal.com/challenge/P6bQYaobCb8f3j4Zy
    int x;
	boolean isPalindrome(String s) {
	  int[] a = new int[999];
	  for (int c : s.toCharArray())
	    x += --a[c] % 2 | 1;
	  return ~x < 1;
	}

