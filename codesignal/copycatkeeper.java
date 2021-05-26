// https://app.codesignal.com/challenge/ztKKQySBtPTHBHTNa
object copycatKeeper(string[][] b) {
    for (var j = 0; j < 56; ++j) {
        var a = new List<string>();
        foreach (var r in b)
            if (j < r.Length)
                a.Add(r[j]);
        a.Sort(string.CompareOrdinal);
        for (var i = 0; i < b.Length; ++i)
            if (j < b[i].Length) {
                b[i][j] = a[0];
                a.RemoveAt(0);
            }
    }
    return b;
}
