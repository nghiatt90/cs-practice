// https://app.codesignal.com/challenge/HAK2ZqSFc5JZmrQq2
function missingNumber(arr) {
  var n = arr.length,
      sum = 0,
      expectedSum = n * (n - 1) / 2;
  for(var i = 0; i < arr.length; i++) {
    sum += arr[i];
  }
  return expectedSum - sum;
}

