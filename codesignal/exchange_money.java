// https://app.codesignal.com/challenge/7ub6gj9pr3KRxYzRG
int exchange_money(int money) {
  return r(money, 17);
}
	
int r(int m, int c) {
  return m < 0 | c < 1 ? 0 : 
		 m < 2 ? 1 : r(m, c - 1) + r(m - c * c, c);
}
