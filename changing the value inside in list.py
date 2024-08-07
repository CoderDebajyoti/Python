# prompt: change the valu of index 3 and the new value is 80000

#create a list named "employee"and calcute the total salary 
employee=['a',10000,'b',9000,'c',15000,'d',17000]
employee[3] = 80000 # change the value of index 3
salary=0
for i in range(0,len(employee),2):
    salary+=employee[i+1]
print(salary) # prints 111000
