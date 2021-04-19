import math
def binary_search(arr, low, high, x,a):
    a=a+1
   # print(a)
    if high >= low:
        mid = (high + low) // 2
        if int(arr[mid])*int(arr[mid]) == x:
            return arr[mid]
        elif int(arr[mid])*int(arr[mid]) > x:
            return binary_search(arr, low, mid - 1, x,a)
        else:
            return binary_search(arr, mid + 1, high, x,a)
 
    else:
        return -1
if __name__=='__main__':
    D=[]
    f=open("input.txt","r")
    r=f.read()
    D=r.split(" ")
    D=D[:-1]
    print("last five prime numbers : "+str(D[-5:]))
    t=len(D)
    print("total prime numbers less than 10^8 is : "+str(t))
    print("Max steps will be taken to find p==q or not is : "+str(int(math.log(t,2))+1))
    n=input("Enter n (p*q) where p,q are primes and p,q < 10^8 : ")
    print("n is : "+str(n))
    r=binary_search(D,0,t,n,0)
    if r!=-1:
        print("p = q and p is : "+str(r))
    else:
        print("p and q are not same")