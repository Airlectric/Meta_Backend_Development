def check_num(n):
    if n % 2 == 0:
        if n >= 2 and n <= 5:
            return 'Not Weird'
        if n >= 6 and n <= 20:
            return 'Weird'
        if n > 20:
            return 'Not Weird'
    else:
        return 'Weird'
        
        
n = int(input())
print(check_num(n))
