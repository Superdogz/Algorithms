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

if __name__ == "__main__":
    for i in range(5):
        # unsorted = list(range(random.randint(10,100)))
        # random.shuffle(unsorted)
        unsorted = list(range(10**4)[::-1]) #This is the worst case scenario

        insertion_sort(unsorted) #in place sorting even through there is a unsorted and sorted variable
        print()
        
        


                
