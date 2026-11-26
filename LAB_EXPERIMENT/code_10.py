def Power(x,n):
    if n==0:
        return 1
    temp=Power(x,n//2)
    if n%2==0:
        return temp*temp
    else:
        return x*temp*temp
x,n=2,-9
if n<0:
    print(1/Power(x,-1*n))   
else:
    print(Power(x,n))     