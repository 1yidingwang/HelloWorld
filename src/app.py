s = "abcdefgh"
for index in range(len(s)):
    if s[index] == 'e' or s[index] == 'u':
        print("There is an e or u")

for char in s:
    if char == 'e' or char == 'u':
        print("There is an e or u")

an_letter = 'aefhilmnorsxAEFHILMNORSX'
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))


for char in word:
    if char in an_letter:
        print("There is an: " + char)
    else:
        print("There is a: " + char)

for i in range(times):
    print(word, "!!!")

