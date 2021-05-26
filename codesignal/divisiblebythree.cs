// https://app.codesignal.com/challenge/XKbd2fZq6PrCN6y39
boolean divisibleByThree(String s) {
  char[] x = (s + '0').toCharArray();
  for (int i = 0; i < x.length - 1; ++i)
    r += f(x[i]) > f(x[i + 1]) ? -1 
    						   : x[i] % 2 > 0 || x[i] > 87 ? 1
                                 						   : 5;
  return r % 3 == 0;
}

int f(char x) {
  for (int i = 0;; ++i)
    if (c[i] == x) return i;
}

char[] c = { 'M', 'D', 'C', 'L', 'X', 'V', 'I', '0'};
int r;
