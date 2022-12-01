
n=int(input("enter the number of test cases"))

for i in range(n):
    try:
        a = int(input("enter the number"))
        b = int(input("enter the number"))
        res = a / b
    except Exception as e:
        print("error ",e)
    else:
        print("the result =", res)

#

# n=int(input("enter the number of test cases"))
# lst1=[]
# for i in range(n):
#     # try:
#         lst=input("enter the list").split()
#         lst1+=lst
# print(lst1)
#     #
    #     res = a / b
    # except(ZeroDivisionError, ValueError) as e:
    #     print("an error occured", e)
    # else:
    #     print("the result =", res)


