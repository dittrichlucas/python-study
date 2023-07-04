nums = [1, 2, 3, 8, 9]
target = [3, 2, 1, 9, 8]

for key, value in enumerate(nums):
    nv = nums[key+1] if (key+1) < len(nums) else ''
    if value+1 == nv:
        print(value)
