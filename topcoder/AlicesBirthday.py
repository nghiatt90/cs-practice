# https://community.topcoder.com/stat?c=problem_statement&pm=16104

class AlicesBirthday:
    def partition(self, k):
        ans = []
        while k >= 3:
            ans.append(k)
            k -= 3
        if k == 2:
            ans.append(1)
        if k == 1:
            return [-1]
        return ans
