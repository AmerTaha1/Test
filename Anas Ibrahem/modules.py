def listmultiplcation(numbers):  
    for k in range(1,len(numbers)):
        numbers[k]=numbers[k]*numbers[k-1]
    return numbers[-1]

def Taxes(x):
    x*=x*0.14
    return x