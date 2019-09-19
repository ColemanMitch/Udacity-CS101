# Write your code here
flower_dict = {}
letters =[]
flowers=[]
with open("flowers.txt") as f:
    for line in f:
        #print(line)
        letters.append(line.split(":")[0])
        flowers.append(line.split(": ")[1].split("\n")[0])
        #print(flowers)
# HINT: create a dictionary from flowers.txt

flower_dict = dict(zip(letters, flowers))
#print(flower_dict)
# HINT: create a function to ask for user's first and last name

first, last = input("Enter your First [space] Last name only: ").split()

first_letter = first[0].upper()

#(first_letter)
print("Unique flower name with the first letter: " + flower_dict[first_letter])
# print the desired output
