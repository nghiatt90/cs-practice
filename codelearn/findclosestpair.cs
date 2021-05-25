// https://codelearn.io/training/detail/45162
int FindClosestPair(int[] numbers, int sum)
{
    var l = numbers.Length;
    var min_dis = l;
    var found = false;
    for (int i = 0; i < l; ++i) {
        for (int j = i+1; j < l && j < i + min_dis; ++j) {
            if (numbers[i] + numbers[j] == sum) {
                min_dis = j - i;
                found = true;
                break;
            }
        }
    }
    return found ? min_dis : -1;
}

