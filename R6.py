n=int(input("enter n"))
f=1
for i in range(int(n/2)):
    i=i+2
    print(i)
    if n%i==0:
        f=0
        break
if f==1:
    print("{}is prime".format(n))
else:
    print("{}is not prime".format(n))
