#Ugly Numbers
#Link: https://practice.geeksforgeeks.org/problems/ugly-numbers2254/1/#
# Approach:
# Initialize an array arr with 1(Default Ugly Number)
# Initialize three pointers p2,p3,p5 pointing to arr[0] 
# multiply value at each pointer p2,p3,p5 in arr with 2,3,5 respectively
# calculate the min and append it into arr
# increment pointer corresponding to min value by 1
# return value at (n-1)th index  #nth value

#Solution

class Solution:
	def getNthUglyNo(self,n):
		arr=[1]
		p2=0
		p3=0
		p5=0
		for i in range(2,n+1):
		   num2=arr[p2]*2
		   num3=arr[p3]*3
		   num5=arr[p5]*5
		   res=min(num2,num3,num5)
		   arr.append(res)
		   if(res==num2):
		       p2+=1
		   if(res==num3):
		       p3+=1
		   if(res==num5):
		       p5+=1
		return arr[n-1]
