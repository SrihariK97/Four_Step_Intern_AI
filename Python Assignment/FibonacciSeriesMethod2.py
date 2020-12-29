def fibMethod2(n):
    a = -1
    b = 1
    c = 0
    print("\nMethod 2 :\n")
    for i in range(n):
        c = a + b
        print(c)
        a = b
        b = c


n = int(input("Enter the value :"))
fibMethod2(n)