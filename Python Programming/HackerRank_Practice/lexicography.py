from itertools import combinations

def lexico(string,size):
    string = sorted(string)
    for r in range(1, size + 1):
        for combo in combinations(string, r):
            print(''.join(combo))
            
input_string , size = input().split()
size = int(size)
lexico(input_string, size)
