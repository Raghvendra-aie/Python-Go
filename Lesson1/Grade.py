#how many grade you got 

marks = int(input("Enter Your Marks :"))

if(100 > marks > 90):
    print("Grade A+")
elif (90 > marks > 80):
    print("Grade A")
elif (80 > marks > 70):
    print("Grade B")
elif(70 > marks > 60 ):
    print("Grade C")
else:
    print("try next year")