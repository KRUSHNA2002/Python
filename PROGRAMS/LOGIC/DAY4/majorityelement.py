nums=[2,2,1,3,3,4,3,3,3,3,1,1,2,2]

freq={}

for num in nums:

    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1

for num in freq:

    if freq[num] > len(nums)/2:

        print(num)
print(freq[num])