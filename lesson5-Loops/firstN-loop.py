#WAP to find the sum of first  n numbers

n = int(input("Enter the value :"))

sum = 0
for i in range(n+1):
    sum += i

print("Total sum =" , sum)