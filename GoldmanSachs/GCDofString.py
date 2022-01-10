#Link:https://leetcode.com/problems/greatest-common-divisor-of-strings/
#Approach:
#Calculate gcd of len(str1) and len(str2)
#check the condition s1+s2==s2+s1
#if above condition satisfies return the characters of string from 0 to gdc of both lengths
#else return empty string


#Solution
import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if(str1+str2==str2+str1):
            return str1[:math.gcd(len(str1),len(str2))]
        else:
            return ""
          
