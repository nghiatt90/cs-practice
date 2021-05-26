// https://app.codesignal.com/challenge/M7ZaZfyfH3KfJHEMw
double l, r, t;
double SqrRotBab(double n, double e) {
  for (r = n; Math.abs(n - r * r) > e; r = (l + n / l) / 2, l = t)
    t = r;
  return Math.floor(r * 100000)/100000;
}

