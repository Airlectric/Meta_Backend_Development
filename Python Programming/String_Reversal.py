# word = 'Reversal'

# rev_word = word[::-1]

# print(rev_word)


#alternative method

def string_reversal(str):
    if len(str) == 0:
        return str
    else:
        return string_reversal(str[1:])+str[0]
    
str = 'reversal'
reverse =string_reversal(str)
print(reverse)