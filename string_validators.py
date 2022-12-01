
S= "pG6"

print (any(i.isalnum() for i in S))
print (any(i.isalpha() for i in S))
print (any(i.isdigit() for i in S))
print (any(i.islower() for i in S))
print (any(i.isupper() for i in S))














# or

# print(any(map(str.isalnum, S)))
# print(any(map(str.isalpha, S)))
# print(any(map(str.isdigit, S)))
# print(any(map(str.islower, S)))
# print(any(map(str.isupper, S)))


