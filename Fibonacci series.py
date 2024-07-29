fd=0
sd=1
n=int(input("Enter nth term you want : "))
print(fd)
print(sd)
for i in range (n-1):
    c=fd+sd
    print(fd+sd)
    fd=sd
    sd=c
    
