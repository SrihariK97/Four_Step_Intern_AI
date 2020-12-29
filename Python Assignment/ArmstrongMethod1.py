# chech with this largest armstrong number 115132219018763992565095597973971522401

def count(n):
    a = n
    count = 0
    while (a > 0):
        r = a % 10
        count += 1
        a = a // 10
    return count

def ArmstrongMethod1(n):
    a = n
    sum = 0
    while (a > 0):
        r = a % 10
        sum = sum + r ** count(n)
        a = a // 10
    print("Method 1 :")
    print("Armstrong value : ", sum)
    if (sum == n):
        print("{} is Armstrong Number".format(n))
    else:
        print("{} is not an armstrong number".format(n))

n = int(input("Enter the number : "))
ArmstrongMethod1(n)