# https://app.codesignal.com/challenge/3BEisz8mXqYRpSupn
string alpha3(string s) {
    var t = s.Select(c => (c - 6) % 10).ToArray();
    t = t[0] % 2 == 1 ? t : t.Reverse().ToArray();
    var i = Array.FindIndex(t, x => x != 0);
    if (i < 0) return "0";
    s = "";
    for (; i < t.Length; ++i) s += t[i];
    return s;
}
