#Factorial of a number

a = int(input("Enter the number: "))
factorial=1
if a==0 or a==1 :
    print("Factorial is 1")
else:
    for i in range(1, a+1):
        factorial= factorial*i
    print("factorial of ", a, "is", factorial)


#average of 10 numbers

sum=0
for i in range(10):
    n=int(input("Enter the number: "))
    sum += n
average = sum/10
print("Average of given numbers are : " ,average)

#Fibonacci series

num = int(input("Enter the number: "))
n1 = 0
n2 = 1
print("Fibonacci series: ", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3,end=" ")




