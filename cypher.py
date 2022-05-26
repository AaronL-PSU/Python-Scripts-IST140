file= open("C:\\Users\\Aaron\\Desktop\\PSU FILES\\Semester 2 - Spring 2021\\IST 140\\input output\\READ.txt", "r")
lines=file.read()
plain=lines.lower()
while True:
    key = int(input("Enter the key size 'The value should be between 1 and 25'\n"))
    if key > 0 and key < 26:
        break
        print('key size has to be between 1 and 25')
cesar = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
counter = 0
encrypted=""
for i in plain:
    for j in cesar:
        if i == j:
            e = cesar[counter + key]
            encrypted = encrypted + e
            break
        counter += 1
    counter = 0
print(encrypted)
f= open("C:\\Users\\Aaron\\Desktop\\PSU FILES\\Semester 2 - Spring 2021\\IST 140\\input output\\encrypted.txt","w")
f.write(encrypted)
f.close()
