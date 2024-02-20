#Algorithm for a palindrome

def isPalindrome(str):

    for id,x in enumerate(str):
        if str[id-1] != str[id-1]:
            print(str[id-1])
            print(str[id-1])
            return False
    return True

print(isPalindrome('racecar'))