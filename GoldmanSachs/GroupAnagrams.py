#https://practice.geeksforgeeks.org/problems/print-anagrams-together/1/
#time complexity:O(n*m) (where n=size of array, m=size of each word)
#Approach:
#create a key with sorted word which contains list of original words
#select one element-> sort it->that is the key->store(append) original word to list corresponding to original key 
#return the dictionary using loop


class Solution:
    def Anagrams(self, words, n):
        d={}
        ans=[]
        for w in words:
            a=''.join(sorted(w))
            if(d.get(a,0)==0):
                d[a]=[w]
            else:
                d[a].append(w)
        ans=[]
        for x in d:
            ans.append(d[x])
        return ans    
