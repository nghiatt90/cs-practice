// https://app.codesignal.com/challenge/Du9J6eFGDQFwBoMNd
int digitalroot(String n) {
  int k = 0;
  for (int i : n.getBytes())
    k += i - 48;
  return k < 10 ? k : digitalroot(k + "");
}

