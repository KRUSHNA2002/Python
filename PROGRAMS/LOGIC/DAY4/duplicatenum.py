nums = [4, 5, 1, 2, 1, 4, 5,4]

duplicate=[]
for i in range(len(nums)):
    count=0
    for j in range(len(nums)):

        if nums[i] == nums[j]:

            count+=1
        else:
            count==1

    if count > 1:

        if nums[i] not in duplicate:

            duplicate.append(nums[i])

print(duplicate)