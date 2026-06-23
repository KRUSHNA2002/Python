nums = [0,1,2,2,0,3,4,4,5]

j = 0

for i in range(len(nums)):

    is_duplicate = False

    # check if nums[i] appeared before index i
    for k in range(i):
        if nums[i] == nums[k]:
            is_duplicate = True
            break

    if not is_duplicate:
        nums[j] = nums[i]
        j += 1

print(nums[:j])