nums = [10,20,30,40,50,15]

left=0
right= len(nums)-1

while left < right:

    nums[left],nums[right]=nums[right],nums[left]

    left+=1
    right-=1

print(nums)