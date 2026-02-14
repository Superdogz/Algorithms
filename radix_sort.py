import math
import random
import time

# nums = [9,16,1009,46,268]

nums = list(range(0,random.randint(10,1000)))
random.shuffle(nums)

digits = int(math.log10(max(nums))) + 1
print("Before: "+str(nums))
start = time.time()

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