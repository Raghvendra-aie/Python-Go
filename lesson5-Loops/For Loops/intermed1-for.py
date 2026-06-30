#Find the largest number in nums = [3, 8, 1, 15, 7]

nums = [3, 8, 1, 15, 7]

largest = nums[0]

for num in nums:
    if num > largest :
        largest = num

print(largest)