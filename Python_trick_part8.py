#Python program to compute the sum of elements of a given array of integers using map() function

from array import array
def array_sum(nums_arr):
    sum_n = 0
    for n in nums_arr:
        sum_n += n
    return sum_n
    
nums = array('i',[1,2,3,4,5,-15])
print("Original array:",nums)

nums_arr = list(map(int,nums))
sum = array_sum(nums_arr)
print(sum)