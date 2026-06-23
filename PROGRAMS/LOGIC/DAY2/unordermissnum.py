nums = [11, 55, 88, 3, 9, 46, 99, 109]

larnum = 0

for i in nums:
    if i > larnum:
        larnum = i

print("Largest:", larnum)

for k in range(1, larnum):
    found = False

    for n in nums:
        if n == k:
            found = True
            break

    if not found:
        print(k)