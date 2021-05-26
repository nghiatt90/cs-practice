// https://app.codesignal.com/challenge/LKb7WWgY5WtjTdtoF
int Num_Calc(int N) {
	return N < 3 ? 1 : 1 + Num_Calc(N % 2 < 1 ? N / 2 : N + 1);
}

