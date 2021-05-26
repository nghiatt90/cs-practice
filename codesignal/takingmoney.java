// https://app.codesignal.com/challenge/cdEkYZdcG7JhsuCse
int k;
String TakingMoney(int N, int[] X) {
  for (int i : X) k |= i;
  return (k > 1 ? "" : "not ") + "ambiguous";
}

