import math
import random
import time


"""
Input - array in the variable nums: line 19
Output - array in stdout (terminal); Before and After array
    
Test cases:
1. [1,7,3,99321,10,4,11,24123,5] -> [1, 3, 4, 5, 7, 10, 11, 24123, 99321]
2. [5, 87, 23, 45, 91, 12, 67, 34, 56, 78, 9, 21, 33, 40, 55, 62, 70, 88, 99, 15, 28, 39, 47, 59, 66, 74, 82, 90, 3, 100] -> [3, 5, 9, 12, 15, 21, 23, 28, 33, 34, 39, 40, 45, 47, 55, 56, 59, 62, 66, 67, 70, 74, 78, 82, 87, 88, 90, 91, 99, 100]
3. list(range(10**4)[::-1]) -> Array of 1 to 10,000 in increasing order
4. [] -> []
5. [6, 7, 67667, 6, 67, 8394293, 66777, 6, 0, 6767, 123489, 98765321]
"""

# INPUT THE ARRAY HERE:
nums = []
random.shuffle(nums)


print("Before: "+str(nums))
start = time.time()

if len(nums) == 0:
        end = time.time()
        print("After: "+"[]")
        print(f"Time = {end - start}")
        exit()

digits = int(math.log10(max(nums))) + 1
for d in range(digits):
    # sorting the buckets
    bucket = [[],[],[],[],[],[],[],[],[],[]]
    for num in nums:
        if len(str(num)) >= d + 1:
            bucket[int(str(num)[len(str(num))-d-1])].append(num)
        else:
            bucket[0].append(num)
    
    # flatten the list and put it into nums
    nums = []
    for i in bucket:
        if len(i) != 0:
            for j in i:
                nums.append(j)

                
end = time.time()
print("After: "+str(nums))
print(f"Time = {end - start}")