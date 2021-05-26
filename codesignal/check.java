// https://app.codesignal.com/challenge/nySdqwHjfDXrnag8F
Object Check(String N) {
  return new BigInteger(N).mod(new BigInteger("11")).intValue() < 1;
}

