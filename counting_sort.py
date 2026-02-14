import time
import random


# nums = list(range(random.randint(10,100)))
# random.shuffle(nums)

nums = list(range(10**5)[::-1])


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