# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 13:14:25 2020

@author: Neelima Sunku
"""

#Linear search
#Algorithm
#Step1 : Start from leftmost element of arr [] and on eby one compare each element 
#of arr[]
#Step2 : if x matches with an element return the index
#Step3 : If x doesnt match with any elements return -1

def search(arr,n,x):
    for i in range(len(arr)):
        if (arr[i] == x):
            return i
        
    return -1


arr = [2,3,4,10,40]
x = 10
n = len(arr)

#Function call

result = search(arr,n,x)
if(result == -1):
    print(x, "is not present in array")
else:
    print(x, "is present in location", result)
    
    
#Time complexity of the above program in O(n)
#worst case complexity can be reduced from O(n) to o(1) if element forund at last
#Worst case complexity can be reduced to o(n/2) from o(n) if element is not found