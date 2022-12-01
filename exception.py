# in python we use exception handling to handle runtime
# we put the block of code that we expecting error inside try block ,
# and the message we want to display if error occurs in expect part
#
# -try & except

a = int(input("enter the nukber"))
b = int(input("enter the nukber"))
try:
    div = a / b
    print(div)
except:
    print("not divible by 0")
#
# also,
# -try&except&else
#     in this else part works when there is no exception
#
# -try&except&finally
#     in it finally works when both exception and no exception
#
# and we can also give exception by name also
# nameerror
# zerodivisionerror
# valueerror