# https://app.codesignal.com/challenge/5avWHrmrJa9cpQthC
d = []
m = numpy.zeros((555, 111))
for D in eval(dir()[0])[0]:
    for S in D:
        s = S[:5]
        d += [s]
        m[d.index(s), int(S.ljust(8, '0')[6:])] += 1
return m.sum() + sum(m.max(1)*3)
            

# def teacherHomework(week):
#     d = {}
#     marking_time = 0
#     keys = set()
#     for day in week:
#         for session in day:
#             d[session] = d.get(session, 0) + 1
#             keys.add(session[:5])
#             marking_time += 1
#     max_ = numpy.ones(len(keys))
#     for i, k in enumerate(keys):
#         for session, count in d.items():
#             if session[:5] == k:
#                 max_[i] = max(max_[i], count)

#     return sum(max_)*3 + marking_time

