#Leet_Code_75 Problem 1 - Easy

# Merge String Alternately

class Solution:
    def mergeAlternately(word1, word2):
        d="" # Created empty string to add each character in this empty string
        
        # if the length of the 1st word greater than 2nd then need to add the extra characters in the the 1st word
        
        if len(word1)>len(word2): 
            for i in range(len(word2)):
                d+=word1[i]
                d+=word2[i]
            for x in range(len(word2),len(word1)):
                d+=word1[x]
            return d # return the final string  
        
        # if the length of the 2nd word greater than 1st then need to add the extra characters in the the 2nd word
        
        elif len(word1)<len(word2):
            for i in range(len(word1)):
                d+=word1[i]
                d+=word2[i]
            for x in range(len(word1),len(word2)):
                d+=word2[x]
            return d # return the final string  
        
        # if the length of 2 words are equal, then print the characters alternatively 
        
        else:
            for i in range(0,len(word2)):
                d+=word1[i]
                d+=word2[i]
            return d # return the final string


t=int(input("")) # test cases
for s in range(t):
    S=Solution
    word1=input("")
    word2=input("")   
    d=S.mergeAlternately(word1,word2)        
    print(d)