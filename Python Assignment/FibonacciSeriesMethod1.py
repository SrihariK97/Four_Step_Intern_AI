def fibMethod1(n):
    a = n - 2
    i, j = 0, 1
    print("\nMethod 1 :\n")
    print(i)
    print(j)
    while (a > 0):
        s = i + j
        i = j
        j = s
        print(s)
        a = a - 1

n = int(input("Enter the value :"))
fibMethod1(n)