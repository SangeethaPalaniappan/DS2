class Solution:
    def mergeAlternately(self, word1, word2):
         # Created empty string to add each character in this empty string
        d=[None] * (len(word1)+len(word2)) 
        # if the length of the 1st word greater than 2nd then need to add the extra characters in the the 1st word
        j = 0
        maxLen = len(word1)
        if (len(word1)<len(word2)):
            maxLen = len(word2)
        for i in range(maxLen):
            if (i < len(word1)):
                d[j] = word1[i]
                j = j+1
            if (i < len(word2)):
                d[j] = word2[i]
                j = j+1
        return "".join(d) # return the final string      