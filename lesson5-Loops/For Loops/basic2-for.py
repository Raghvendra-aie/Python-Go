tup = (1,2,4,6,8,9,12,15,19,23,26,34,23,876,665,44,787,33,9098,35,12,11,234)
print()

x = int(input("Enter the above value:"))

idx = 0
for el in tup:
    if(el == x):
        print(x , "found at" , "Index",idx)
        
    idx += 1