from itertools import combinations_with_replacement

def lexico(string,size):
    string = sorted(string)
    for combo in combinations_with_replacement(string, size):
        print(''.join(combo))
            
input_string , size = input().split()
size = int(size)
lexico(input_string, size)
