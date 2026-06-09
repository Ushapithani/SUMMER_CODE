f = open("sample.txt", "w")
f.write("Hello, this is a sample file.\n")
f.write("This file is used for demonstrating file handling in Python.\n")
f.close()
f = open("sample.txt", "r")
print(f.read())
f.close()

# using with 
with open("sample.txt", "r") as f:
    content = f.read()
    print(content)

# append mode
with open("sample.txt", "a") as f:
    f.write("This line is appended to the file.\n")
with open("sample.txt", "r") as f:
    content = f.read()
    print(content)

# using seek 
with open("sample.txt", "r") as f:
    print(f.read(5))  # read 5 characters 
    f.seek(0)  
    print(f.read())  


# create a file as example txt with the content of your self inroduction using file modes r and w 
#1.find the length of the file 
#2.search the name present in the file or not
# 3 coount the number of vowels in the file 
# update the phone number into the file using append 
with open("example.txt", "w") as f:
    f.write("Hello, my name is usha.\n")
    f.write("I enjoy coding and learning new technologies.\n")
with open("example.txt", "r") as f:
    content = f.read()
    print(content)

# length
with open("example.txt", "r") as f:
    content = f.read()
    print("Length of the file:", len(content))
# search name 
with open("example.txt", "r") as f:
    content = f.read()
    name_to_search = "usha"
    if name_to_search in content:
        print(f"{name_to_search} is present in the file.")
    else:
        print(f"{name_to_search} is not present in the file.")
# count vowels 
with open("example.txt", "r") as f:
    content = f.read()
    vowels = "aeiouAEIOU"
    count = sum(1 for char in content if char in vowels)
    print("Number of vowels in the file:", count)
    # update phone number 
with open("example.txt", "a") as f:
    f.write("Phone number: 123-456-7890\n")
with open("example.txt", "r") as f:
    content = f.read()
    print(content)
f.close()






