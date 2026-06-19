
vowels="AIUOEaoiue"

str1="Krushna"

vowels_count=0

for ch in str1:

    if ch in vowels:

        print(ch)
        vowels_count+=1

print("count of vowels : ", vowels_count)