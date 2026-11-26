def merge(A,B):
    n1=len(A)
    n2=len(B)
    merged=[0]*(n1+n2)
    i,j,k=0,0,0
    while(i<n1 and j<n2):
        if(A[i]<B[j]):
            merged[k]=A[i]
            i+=1
            k+=1
        else:
            merged[k]=B[j]
            j+=1
            k+=1
    while(i<n1):
        merged[k]=A[i]
        i+=1
        k+=1
    while(j<n2):
        merged[k]=B[j]
        j+=1
        k+=1
    print("Merged array:",merged)
A=[2,4,6,8,14,18,20,24]
B=[1,3,5,7,9,11]
merge(A,B)