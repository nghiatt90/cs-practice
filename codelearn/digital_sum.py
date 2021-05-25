# https://codelearn.io/training/detail/34612
def digital_sum(number):
    if number < 10:
        return number
    s = 0
    while number:
        s += number % 10
        number //= 10
    return digital_sum(s)
