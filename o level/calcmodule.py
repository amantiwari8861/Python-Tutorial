def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def multi(n1,n2):
    return n1*n2

def divide(n1,n2):
    try:
        if n2==0:
            raise RuntimeError("pls do not divide by zero")
    except:
        print("pls do not divide by zero")
        return
    
    return n1/n2

def volOfSphere(radius,PI=3.14):
    return 4/3*PI*radius**3