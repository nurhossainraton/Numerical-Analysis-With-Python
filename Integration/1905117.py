import numpy as np
import matplotlib.pyplot as plt

Cme= 5*10**(-4)

def fValue(x):
    neu=6.73* x + 6.725*10**(-8) + 7.26*10**(-4) * Cme
    denom= 3.62 * 10**(-12)* x + 3.908* 10**(-8)*x* Cme

    return ((neu/denom)*(-1))

def approxRelativeError(prev,current):

    return 100*abs((current-prev)/current)

def TrapezoidalRule(lower,upper,n):

    h=(upper-lower)/n
    result=0
    for i in range(n+1):
        if i==0 :
            result= result+ 0.5*h*fValue(lower)
        elif i==n:
            result=result+ 0.5*h*fValue(upper)
        else:
            result= result+ h*fValue(lower+i*h)
    return result


def SimpsonRuleSingleApproach(lower,upper,h):
    return ((h/3)*(fValue(lower)+ 4*fValue((lower+upper)/2)+ fValue(upper)))

def SimpsonRule(lower,upper,n):
    h=(upper-lower)/(2*n)
    result=0
    for i in range(n):
        result=result+SimpsonRuleSingleApproach(lower+(i*2*h),lower+((i+1)*2*h),h)
    return result

def Print(process,lower,upper):
    if(process==1):
        print()
        print('\t\t\t\t\t Using Trapezoidal Method')
        print('\t\t\t\t Value \t\t\t\t Absolute Approx Relative Error')
        valuelist=[]
        for i in range(1,6):
            tempValue=TrapezoidalRule(lower,upper,i)
            valuelist.append(tempValue)
            if(i==1):
                print(f'{i}\t\t {tempValue} \t\t\t N/A')
            else:
                error=approxRelativeError(valuelist[i-2],valuelist[i-1])
                print(f'{i}\t\t {tempValue} \t\t\t {error}')
    else:
        print()
        print("\t\t\t\t\t Using Simpson's 1/3 Rule")
        print('\t\t\t\t Value \t\t\t\t Absolute Approx Relative Error')
        valuelist = []
        for i in range(1,6):
            tempValue = TrapezoidalRule(lower, upper, i)
            valuelist.append(tempValue)
            if (i == 1):
                print(f'{i}\t\t {tempValue} \t\t\t N/A')
            else:
                error = approxRelativeError(valuelist[i - 2], valuelist[i - 1])
                print(f'{i}\t\t {tempValue} \t\t\t {error}')


print("Enter Number of Sub Sections: ")
n=int(input())
xInitial=1.22*10**(-4)
xFinal=xInitial/2

trapezoidResult=TrapezoidalRule(xInitial,xFinal,n)
simpsonRuleResult=SimpsonRule(xInitial,xFinal,n)

print(f'Using Trapezoid Rule,Required Time is :{trapezoidResult}')
Print(1,xInitial,xFinal)
print()
print(f'Using Simpsons Rule,Required Time is : {simpsonRuleResult} ')
Print(2,xInitial,xFinal)

xarr=[1.22*10**(-4),1.2*10**(-4),1*10**(-4),0.8*10**(-4),0.6*10**(-4),0.4*10**(-4),0.2*10**(-4)]
x_values=np.array(xarr)
y_values=SimpsonRule(xInitial,x_values,5)

plt.plot(x_values,y_values,color='red')
for i in range(len(xarr)):
    plt.plot(x_values[i],y_values[i],'go')
plt.xlabel('Oxygen Concentration (moles/cc)')
plt.ylabel('Time ')
plt.show()
