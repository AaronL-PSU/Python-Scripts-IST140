file = open("C:\\Users\\Aaron\\Desktop\\PSU FILES\\Semester 2 - Spring 2021\\IST 140\\input output\\READ.txt", "r")
worddata = file.read()
words = worddata.split()
file.seek(0)
linedata = file.readlines()



print('Number of words:', len(words))
print('Number of lines:', len(linedata))
