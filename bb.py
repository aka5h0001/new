a = int(input("Enter thr number : "))
def prime (a):
    count = 0
    for i in range(1,a+1):
        if a%i == 0:
            count += 1
    if count==2:
        print(a,"is prime number")
print(prime(20))
    
