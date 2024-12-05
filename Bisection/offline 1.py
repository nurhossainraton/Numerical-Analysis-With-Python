import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,0.12,0.001)
y=np.array(x**3 -0.18*x**2 +4.752*10**-4)

y1=0*x
plt.plot(x,y1)

plt.plot(x,y)
plt.xlabel(" X axis ")
plt.ylabel('Y axis: f(x)')
plt.show()
result=0

def fValue(x):
    return x**3- 0.18*x**2 +4.752e-4

def bisection(lower,upper,error,maxIteration):

    for i in range (1,maxIteration):
        if(i==1):
            prev=0
        xm = (upper + lower) / 2

        approxError=abs((xm-prev)/xm)
        if(approxError >  error):
            value = fValue(lower) * fValue(xm)
            if (value==0):
                print(xm)
                break
            elif(value <0):
                upper=xm;
            else:
                lower=xm

            prev = xm
        elif(approxError <error or i==maxIteration):
            print(f'The Root is ',xm)
            break

bisection(0,0.12,0.005,20)



def modifiedBisection(lower, upper, error, maxIteration):
    print("Table :")
    print("Iteration No           AprroxError (in percentage)")
    for i in range (1,maxIteration+1):
        if(i==1):
           prev=0
        xm = (upper + lower) / 2
        approxError=abs((xm-prev)/xm)*100
        if(i==1):
            print(f' {i} \t\t\t\t\t\t Not applicable')
        elif(i<10):
            print(f' {i} \t\t\t\t\t\t {approxError}')
        else:
            print(f' {i} \t\t\t\t\t {approxError}')

        value = fValue(lower) * fValue(xm)
        if (value==0):
            break
        elif(value <=0):
            upper=xm;
        else:
            lower=xm

        prev=xm
modifiedBisection(0,0.12,0.005,20)
errorTable=[]
list=[]
def setTable(l,u,maxIteration):
    prev = (l+u)/2


    for i in range(2, maxIteration+1):
        if fValue(prev) * fValue(l) > 0:
            l = prev
        else:
            u=prev
        xm = (l + u) / 2
        approxError = abs( (xm - prev) / xm)
        if fValue(xm) * fValue(l) > 0:
            l = xm
        else:
            u=xm
        prev = xm

        list = [i, xm,approxError * 100]

        errorTable.append(list)

def tableShow(cellText=None):
    a,tablePlot = plt.subplots(1, 1)
    column_labels = ["Iteration", "Approximate root", "Approximate relative error(%)"]
    tablePlot.axis('off')
    tablePlot.table(cellText=errorTable, colLabels=column_labels, loc='center')
    plt.show()
l=0
u=0.12

errorTable=[[1,(l+u)/2 , "Not Applicable"]]
setTable(l, u, 20)
tableShow()