string = input("Enter a string: ")
display = input("Display alphabet or numbers?: ")

if display == "alphabet":
    for word in string.split():
       if word.isalpha():
            print(word)
if display == "numbers":
    for word in string.split():
       if word.isdigit():
            print(word)
