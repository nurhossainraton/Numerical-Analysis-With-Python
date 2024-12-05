import numpy as np

"""From the equation x^2+y^2+ax+by+c=0:
   The circle passes through the points (-2,0),(-1,7),(5,-1)
   Putting these points,we get the equations
   2a+0b-c = 4
   a-7b-c = 50
   5a-b+c=-26    respectively
   We will use gaussian elimination to solve these euations
"""

def pivotingElement(A,index):
     max=index
     for i in range(index+1,n):
         if(abs(A[i][index])> abs(A[max][index])):
             max=i
     return max

def showSteps(A, B):
    print("Array A:")
    for i in range (0,n):
        for j in range (0,n):
            print("{:.4f}".format(A[i][j]), end="  ")
        print()
    print("Ärray B:")
    for i in range (0,n):
        print("{:.4f}".format(B[i]))
    print()


def GaussianElimination(A,B,pivot=True,showall=True):
    if(pivot):
        if(showall):
            showSteps(A,B)
        for i in range(0,n-1):
            max=pivotingElement(A,i)
            A[[i,max]]=A[[max,i]]
            B[i],B[max]=B[max],B[i]

            for j in range(i+1,n):
                tempA=A[i]*(A[j][i]/A[i][i])
                const=B[i]*(A[j][i]/A[i][i])
                A[j]=np.subtract(A[j],tempA)
                B[j]-=const
                if(showall):
                    showSteps(A,B)
    else:
        if (showall):
            showSteps(A, B)
        for i in range(0, n - 1):
            for j in range(i+1,n):
                tempA=A[i]*(A[j][i]/A[i][i])
                const=B[i]*(A[j][i]/A[i][i])
                A[j]=np.subtract(A[j],tempA)
                B[j]-=const
                if(showall):
                    showSteps(A,B)
    X=np.empty(shape=(n),dtype=np.float64,order='F')
    for i in reversed(range(n)):
        sum=0
        for j in range(i+1,n):
            sum+=X[j]*A[i][j]
        X[i]=(B[i]-sum)/A[i][i]
    return X
n=int(input())
A=np.empty(shape=(n,n),dtype=np.float64,order='C')
B=np.empty(shape=(n),dtype=np.float64,order='F')
for i in range(0,n):
    x=input().split()
    for j in range (0,n):
        A[i][j]=float(x[j])
for i in range(0,n):
    B[i]=float(input())


var=GaussianElimination(A,B,True,True)
print("The value of the variables (a,b,c) are: ")
for i in range (0,n):
    print("{:.4f}".format(var[i]))



