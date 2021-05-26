// https://app.codesignal.com/challenge/WbFaNFbynoz4xTduD
int Digital_sum(int a) {
  return a< 10 ? a : Digital_sum(a/10 + a %10);
}

