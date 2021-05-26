// https://app.codesignal.com/challenge/iF4Dv43vEeZf7jXRH
int r[], i;

int Intruder(int m, int[] arr) {
  r = new int[9];
  for (int i : arr)
    r[i]++;
  for (; ;++i)
    if (r[i] > 0 & r[i] != m) 
      return i;
}

