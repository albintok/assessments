# problem 2
#
# lst=[51, 20, 32, 12, 78]
# lst1=[str(i) for i in lst]
# print(lst1)








# problem 1


A = ['1,2,3,4,5,6','8,9,10,11,12,13','15,16,17,18,19,20']
B = [7,14,21]
C=[str(i) for i in B]

A=[A[i]+","+C[i] for i in range(len(C))]
print(A)





