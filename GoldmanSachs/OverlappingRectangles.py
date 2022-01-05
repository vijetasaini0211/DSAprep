#Overlapping Rectangles
# Link: https://practice.geeksforgeeks.org/problems/overlapping-rectangles1924/1/
#Approach:
#Check whether r1 and r2 satisfies below given conditions:
# r1 is left of r2
# r1 is right of r2
# r1 is above r2
# r2 is above r1
# if any of above condition is satisfied return false (rectangles cannot overlap)  else return true
#Time complexity: O(1)



class Solution:
    
    def doOverlap(self, L1, R1, L2, R2):
        #code here
        if(R1[1]>L2[1] or R2[1]>L1[1]):
            return 0
        if(L2[0]>R1[0] or L1[0]>R2[0]):
            return 0
        return 1    
