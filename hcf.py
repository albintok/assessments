
def compute_hcf(x, y):
# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if(x % i == 0 and y % i == 0):
            hcf =i
    return hcf

num1 = 20
num2 = 36

print("The H.C.F. is", compute_hcf(num1, num2))

#
# a = 36
# b = 20
# n = 0
#
# for i in range(1, min(a, b) + 1):
#     if a % i == b % i == 0:
#         n =i
#
# print(n)