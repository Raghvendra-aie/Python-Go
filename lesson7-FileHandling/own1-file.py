#I making this code where I make the file and searching the words is exist or not in file 😎

with open("Poem.txt","w") as f:
    f.write("THE ROAD NOT TAKEN\n")
    f.write("           ~Robert Forst\n")
    f.write("Two roads diverged in a yellow wood,\nAnd sorry I could not travel both\n")
    f.write("And be one traveler,long I stood\nAnd looked down one as far as I could\nTo where it bent in the undergrowth,\n")


word = input("Enter the Word : ")

def find_words():
 with open("Poem.txt","r") as f:
    data = f.read()
    if (data.find(word) != -1):
        print("Exist 😍")
    else:
        print("Not Exist 😒")

find_words()


