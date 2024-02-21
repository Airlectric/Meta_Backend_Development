def consecutive(n):
    if n == 0:
        return ""
    else:
        result = ""
        for i in range(1,n+1):
            result += str(i)
        return result
            


n = int(input())
print(consecutive(n))
