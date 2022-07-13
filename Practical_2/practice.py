R=int(input("Enter the no. of rows "))
C=int(input("Enter the no. of coloumn "))

A=[]
print("Enter the entries rowwose")
for i in range(R):
    a =[]
    for j in range(C):
        a.append(int(input()))
    A.append(a)    

print("The matrix A is ")
for i in range(R):
    for j in range(C):
        print(A[i][j], end =" ")
    print()

print("The Transpose matrix of A is ")
for i in range(C):
    for j in range(R):
        print(A[j][i], end =" ")
    print()