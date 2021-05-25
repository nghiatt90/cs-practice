# https://app.codesignal.com/challenge/hBbuBTMsqMPfDwL6T
# def growingPlant(upSpeed, downSpeed, desiredHeight):
#     a = upSpeed - downSpeed
#     return max((desiredHeight - upSpeed + a - 1) // a, 0) + 1
#     
growingPlant = lambda x, y, z: max((z - y - 1) // (x - y), 0) + 1
