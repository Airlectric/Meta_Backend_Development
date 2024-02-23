class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        prefix = strs[0]

        for string in strs[1:]:
            i = 0
            while i < len(string) and i < len(prefix) and prefix[i] == string[i]:
                i += 1
            prefix = prefix[:i]
            if prefix == '':
                return ''
        return prefix
            
                   

        
