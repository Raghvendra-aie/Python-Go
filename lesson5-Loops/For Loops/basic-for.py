#Search the number of x in tuple using loop
print(1,2,4,6,8,9,12,15,19,23,26)
print()
tup = (1,2,4,6,8,9,12,15,19,23,26)
x = int(input("Enter the above value:"))

idx = 0
for el in tup:
    if(el == x):
        print(x , "found at" , "Index",idx)
        
    idx += 1