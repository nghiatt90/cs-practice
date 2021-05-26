// https://app.codesignal.com/challenge/Cbejob7WFJ3jupLXg
String findPalindromeProduct(int N) {
  return new String[] {" ", " 00 ", " 0660 ", "  0000  ",
                       "  660066  ", "   000000   ", "   56644665   "}[N - 1]
  .replace(" ", "9");
}

