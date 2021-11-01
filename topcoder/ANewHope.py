import math

class ANewHope:
    def count(self, firstWeek, lastWeek, D):
        m = 0
        d1, d2 = {}, {}
        for i, v in enumerate(firstWeek):
            d1[v] = i
        for i, v in enumerate(lastWeek):
            d2[v] = i
        for i in range(1, len(firstWeek)+1):
            m = max(m, math.ceil((d1[i]-d2[i])/(len(firstWeek)-D)))
        return int(m+1)
