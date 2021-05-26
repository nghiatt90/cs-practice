// https://app.codesignal.com/challenge/njPsmK5owxizxsTby
boolean Tic_Tac_Toe(String[][] a) {
  return a[0][2].equals(a[1][2]) & a[0][2].equals(a[2][2])
       | a[0][0].equals(a[2][2]);
}

