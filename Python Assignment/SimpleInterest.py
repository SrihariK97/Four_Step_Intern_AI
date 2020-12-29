def SimpleInterest(p,t,r):
    si=(p*t*r)/100
    print("Simple interest : ",si)
    print("Total amount : ",si+p)

p=int(input("Principal : "))
t=int(input("Time : "))
r=int(input("Rate of Interest : "))
SimpleInterest(p,t,r)