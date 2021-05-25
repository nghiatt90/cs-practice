# https://codelearn.io/training/detail/3918
def pairOfShoes(shoes):
    left = [x[1] for x in shoes if x[0] == 0]
    right = [x[1] for x in shoes if x[0] == 1]
    
    if len(left) != len(right):
        return False
    
    left.sort()
    right.sort()
    return all(left[i] == right[i] for i in range(len(left)))
