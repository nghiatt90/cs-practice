// https://app.codesignal.com/challenge/RaKD7DvDiQ3Agj4cv
int Superincreasing_knapsack_problem(int M, int N, int[] w) {
  N = 0;
  for (int i : w)
    N += N + i > M ? 0 : i;
  return N;
}

