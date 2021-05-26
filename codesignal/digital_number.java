// https://app.codesignal.com/challenge/sYudQvWiWKZcFAmXr
String s = "0020059086", z = "";
boolean digital_number(String n) {
  for (int x : n.getBytes())
    z = s.charAt(x - 48) + z;
  return z.equals(n);  
}

