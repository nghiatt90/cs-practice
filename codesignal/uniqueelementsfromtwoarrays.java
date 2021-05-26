// https://app.codesignal.com/challenge/wziLptXRTBHf7ReAd
String[] uniqueElementsFromTwoArrays(int[] a, int[] b) {
  Set t = new TreeSet();
  for (int x : a) t.add(x);
  for (int x : b) t.add(x);
  String r = "";
  for (Object i : t) r += i + " ";
  return r.split(" ");
}
