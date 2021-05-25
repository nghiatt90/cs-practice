# https://codelearn.io/training/detail/9298
def sumOfConsecutive(n):
    cnt = 0
    for i in range(2, int(n**.5)+1):
        for k in i, n//i:
            # print(k)
            if n%k==0 and (n//k)&1 and k>=n//k//2:
                cnt += 1 if k!=n//k else .5
                # print('A')
            elif (n//k)&1 == 0 and n%k==(n//k)//2:
                cnt += 1
                # print('B')
    return int(cnt)
