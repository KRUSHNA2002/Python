list1 = [0,2,5,0,7,9,1,2]

j = 0

# Put non-zero elements at the front
for i in range(len(list1)):
    if list1[i] != 0:
        list1[j] = list1[i]
        j += 1

# Fill the remaining positions with zeros
while j < len(list1):
    list1[j] = 0
    j += 1

print(list1)