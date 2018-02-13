from random import randint

# Number of words you want to get in your password
word_num = 5

# Import and organize the dictionaly of words
d = {}
with open("diceware.wordlist.asc", "r") as f:
    for item in f:
    	ssplit = item.split()
    	key = ssplit.pop(0)
    	d[key] = ssplit

# Generate and print!
random_num_sequence = ''
random_word_sequence = ''
for i in range(word_num):

    current = ''
    for i in range(5):
        random_num_sequence = random_num_sequence + str(randint(1, 6))
        current = current + str(randint(1, 6))

    random_num_sequence = random_num_sequence + ' '
    random_word_sequence = random_word_sequence + str(d[current][0]) + ' '

print (random_num_sequence)
print (random_word_sequence)
