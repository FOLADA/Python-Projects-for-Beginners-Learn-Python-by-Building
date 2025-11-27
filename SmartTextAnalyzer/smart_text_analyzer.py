sentence = input("Please enter a sentence and our system will do the magic!")


character_number = len(sentence)

words = sentence.split()
word_number = len(words)

# Longest word
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

# Vowel count
vowels = ["a", "e", "i", "o", "u"]
vowel_count = 0
for char in sentence.lower():
    if char in vowels:
        vowel_count += 1

# Uppercase and lowercase versions
uppercase_version = sentence.upper()
lowercase_version = sentence.lower()

# Word frequency
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# Print results
print("Number of characters:", character_number)
print("Number of words:", word_number)
print("Longest word:", longest_word)
print("Number of vowels:", vowel_count)
print("Uppercase version:", uppercase_version)
print("Lowercase version:", lowercase_version)

print("Word frequencies:")
for word, count in frequency.items():
    print(word, ":", count)
