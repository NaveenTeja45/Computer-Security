if __name__=='__main__':
    f=open("input.txt","w+")
    D=[]
    n = 100000000
    print("naveen")
    prime = [True for i in range(n + 1)]
    p = 2
    t=0
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    s=""
    print("teja")
    for p in range(n + 1):
        if prime[p]:
            f.write(str(p)+" ")