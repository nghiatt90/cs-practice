// https://app.codesignal.com/challenge/QSWtoLfcv68hrsWBg
#define E std::vector< int >
E permutation(int n, E v) {
  while(--n)
    std::next_permutation(v.begin(),v.end());
  return v;
}

