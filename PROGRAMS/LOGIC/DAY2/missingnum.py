
nums = [1,2,3,4,5,7,8,9]
prevnum=nums[0]
missing=0


for i in range(1,len(nums)):

    if nums[i] != prevnum+1:

        missing=prevnum+1
        break

    prevnum=nums[i]


print(missing)


# OR
# nums = [1,2,3,4,5,7,8,9]
# prevNum = nums[0]
# nextVal = nums[0]
# for i in nums:
#     prevNum = i
#     if(i == nextVal):
#         pass
#     else:
#         print(nextVal)
#     nextVal = i+1


