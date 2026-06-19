
#  EXAMPLE 1 ------------------------------------------------------

# text=input("Enter the String : ")

# char_count={}
# for char in text:

#         if char in char_count:
          
#           char_count[char]+=1

#         else:
#              char_count[char] = 1


# print(char_count)

#  EXAMPLE 2  --------------------------------------------------------

from collections import Counter

text=input("Enter the String")

char=Counter(text)
print(char)



