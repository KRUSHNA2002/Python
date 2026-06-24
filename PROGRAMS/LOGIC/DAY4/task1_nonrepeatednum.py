nums = [4, 5, 1, 2, 1, 4, 5,4]

# notrepeat = []

# for i in range(len(nums)):
#     count = 0

#     for j in range(len(nums)):
#         if nums[i] == nums[j]:
#             count += 1

#     if count == 1:
#         notrepeat.append(nums[i])

# print(notrepeat)

freq={}

for num in nums:
   if num in freq:
      freq[num]+=1
   else:
      freq[num]=1

for num in nums:
   
   if freq[num] == 1 :
      print(num)
      print(freq)
      break
