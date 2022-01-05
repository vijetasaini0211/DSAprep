# Encoding(run-length)
# Link: https://practice.geeksforgeeks.org/problems/run-length-encoding/1/#
#Concept: strings
#Approach:
# use two pointer variables with initial position=0 and an empty string
# using while loop check whether(arr[start]==arr[end]) then update end till condition satisfies
# concatenate arr[start] and end-start(count) to the string
# assign value of end into start


#Solution:

def encode(arr):
    ans=""
    start=0
    end=0
    
    while(end<len(arr)):
        while(end<len(arr) and arr[start]==arr[end]):
            end+=1
        ans+=arr[start]+str(end-start)
        start=end
    return ans
