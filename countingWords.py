introString = input('enter your introduction : ')
print(introString)
wordCount = 1
characterCount = 0
for character in introString:
    characterCount= characterCount + 1
    if(character==' '):
        wordCount= wordCount + 1
print("Number of words in the string: ")
print(wordCount)
print("Number of characters in the string: ")
print(characterCount)
