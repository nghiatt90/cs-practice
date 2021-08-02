# https://community.topcoder.com/stat?c=problem_statement&pm=16535

class TableTennisGame:
    def finalScore(self, a, b):
        if abs(a-b) > 2 or a+b < 11:
            return []
        if a+b > 20 and a != b:
            return []
        if a+b > 20:
            return [(a+b)//2+1, (a+b)//2-1]
        if a%2 == b%2 == 1:
            return []
        return [11, a+b-11]
