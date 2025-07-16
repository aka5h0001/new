def is_true(a):
    if(a<1):
        print(a,"is not a prime number")
        return
    for i in range(2,a):
        if (a%i==0):
            print(a,"is not prime")
            return
        else:
            print(a,"is  prime no.")
            return

is_true(3)
is_true(6)