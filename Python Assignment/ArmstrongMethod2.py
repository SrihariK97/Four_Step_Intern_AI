# chech with this largest armstrong number 115132219018763992565095597973971522401

def ArmstrongMethod2(n):
    s, digit = 0, 0
    a = str(n)
    for i in a:
        digit += 1
    for i in a:
        i = int(i)
        s = s + (i ** digit)
    print("Method 2 :")
    print("Armstrong value : ", s)
    if (str(s) == a):
        print("{} is Armstrong Number".format(n))
    else:
        print("{} is not an armstrong number".format(n))


n = int(input("Enter the number : "))
ArmstrongMethod2(n)