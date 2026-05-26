#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
#an empty dictionary & add one by one. Use subject name as key & marks as value.

marks = {}

a = int(input("Enter the marks of Maths : "))
marks.update({"Maths" : a})

b = int(input("Enter the marks of Physics : "))
marks.update({"Physics" : b})

c = int(input("Enter the marks of Chemistry : "))
marks.update({"Chemistry" : c})

print(marks)