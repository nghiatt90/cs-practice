// https://codelearn.io/training/detail/35052
function spiralMatrix(n){
    var m = new Array(n);
    for (var i = 0; i < m.length; i++) {
        m[i] = new Array(n);
    }

    var i = 0, j = -1;
    var dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];
    
    var current_dir = 0;
    var x = 1;
    while (x <= n*n) {
        var ii = dirs[current_dir][0], jj = dirs[current_dir][1];
        if ((i+ii < 0 || i+ii >= n || j+jj < 0 || j+jj >= n) || (m[i+ii][j+jj] > 0)) {
            current_dir = (current_dir + 1) % 4;
            ii = dirs[current_dir][0];
            jj = dirs[current_dir][1];
        }
        i += ii;
        j += jj;
        m[i][j] = x++;
    }
    return m;
}
