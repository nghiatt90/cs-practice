// https://app.codesignal.com/challenge/my7vfEMbycZvEu42i
int i;
int target_game(int[] V) {
  if (V.length < 2) return V[0] > 0 ? V[0] : 0;
  V[1] = Math.max(V[1], V[0]);
  for (i = 2; i < V.length; ++i) 
    V[i] = Math.max(V[i-1], V[i-2] + (V[i] > 0 ? V[i] : 0));
  return V[i-1];
}

