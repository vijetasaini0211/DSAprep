#Link: https://practice.geeksforgeeks.org/problems/find-the-position-of-m-th-item1723/1/


#Solution:
class Solution:
    def findPosition(self, N , M , K):
        # code here
        if((K+M-1)%N==0):
            return N
        else:
            return (K+M-1)%N
