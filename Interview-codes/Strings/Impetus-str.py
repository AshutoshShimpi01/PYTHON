
input_string = "my name is ashutosh"
words = input_string.split()
capitalized_words = []

# Use a for loop to iterate through each word
for word in words:
    # Capitalize the first letter (word[0]) and append the rest (word[1:])
    capitalized_word = word[0].upper() + word[1:]
    capitalized_words.append(capitalized_word)

# Join the list of capitalized words back into a single string
output_string = " ".join(capitalized_words)
print(output_string)


My Name Is Ashutosh
