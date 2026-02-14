import math
import time
import random

def insertion_sort(nums):
    print("Before: "+str(nums))
    start = time.time()

    for i in range(1,len(nums)):
        curr = nums[i]
        for j in range(1,i+1):
            if curr > nums[i-j]:
                if j == 1:
                    break
                else:
                    nums.pop(i)
                    nums.insert(i-j+1, curr)
                    break
            else:
                if j == i:
                    nums.pop(i)
                    nums.insert(i-j, curr)
                else:
                    pass

    end = time.time()
    print("After: "+str(nums))
    print(f"Time = {end - start}")

def counting_sort(nums):
    print("Before: "+str(nums))
    start = time.time()

    max_val = max(nums)
    min_val = min(nums)

    my_dict = {i: 0 for i in range(min_val, max_val + 1)}

    for num in nums:
        my_dict[num] = my_dict[num] + 1

    output = []
    for key, value in my_dict.items():
        for i in range(value):
            output.append(key) 

    end = time.time()
    print("After: "+str(output))
    print(f"Time = {end - start}")

def radix_sort(nums):
    print("Before: "+str(nums))
    start = time.time()

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

if __name__ == "__main__":
    # Custom testing array
    unsorted_array = [9,16,1009,46,268]

    # # Random range of consecutive numbers that have been shuffled
    # unsorted_array = list(range(random.randint(10,100)))
    # random.shuffle(unsorted_array)

    # # Consecutive numbers that are in decreasing order
    # unsorted_array = list(range(10**4)[::-1])

    insertion_sort(unsorted_array)
    counting_sort(unsorted_array)
    radix_sort(unsorted_array)
