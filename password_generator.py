# Use an import statement at the top
import random

word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function generate_password here
def generate_password():

	password = ""

	for i in range(3):
		random_word = word_list[random.randint(1,len(word_list)-1)] # -1
		# to avoid out of range error
		password = password + random_word

	return password
# It should return a string consisting of three random words
# concatenated together without spaces



# test your function
print(generate_password())
