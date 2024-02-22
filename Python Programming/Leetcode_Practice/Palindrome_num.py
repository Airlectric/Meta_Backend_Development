class Solution(object):
    def isPalindrome(self, x):
        num = str(x)
        delimeter = ''
        check = ''
        check = delimeter.join(num[::-1])
        if check == num:
            return True
        else:
            return False

numtest = Solution()
print(numtest.isPalindrome(-121))