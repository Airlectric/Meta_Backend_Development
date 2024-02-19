def sum_of(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(sum_of(5,3,4,3,5))
