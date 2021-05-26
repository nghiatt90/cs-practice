# https://app.codesignal.com/challenge/RNeqCrz6ntZPCGMSu
int ReversePrime(int x, int p) {
  return new BigInteger("" + x).modInverse(new BigInteger("" + p)).intValue();
}

