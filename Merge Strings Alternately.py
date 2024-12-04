class Solution(object):
    def mergeAlternately(self, word1, word2):
        i = 0
        j = 0
        res = ''
        #both i and j in bounds
        while i<len(word1) and j<len(word2):
            res += word1[i] + word2[j]
            i+=1
            j+=1
        # j is out of bounds, i in bounds
        while i<len(word1):
            res += word1[i]
            i += 1

        while j<len(word2):
            res += word2[j]
            j += 1
        
        return res

