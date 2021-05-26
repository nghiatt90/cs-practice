// https://app.codesignal.com/challenge/ihCrv87fdvkBhPMjq
int i;
String piglatin(String w) {
  for (; w.matches("[^aiueoy].*"); ++i)
    w = w.substring(1) + w.charAt(0);
    
  return w += i < 1 ? "way" : "ay";
}

