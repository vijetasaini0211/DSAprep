#Subarray product less than k
#Link: https://practice.geeksforgeeks.org/problems/count-the-subarrays-having-product-less-than-k1708/1/
#Approach:
#Using sliding window technique
#Assign two variables: start and end 
#    update the value of count with size of window satisfying the condition(product<k)
#else:
#    remove element at start index(from window) till product>=k and update start=start+1
#    divide product by value at start index 


#Solution
class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        #Code here
        start,end,count=0,0,0
        product=1
        for end in range(n):
            product*=a[end]
            while(product>=k and start<end):
                product/=a[start]
                start+=1
            if(product<k):
                count+=end-start+1
        return count    
