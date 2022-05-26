import datetime
year = int(input("Year: "))
month = int(input("Month: "))
day = int(input("Day: "))
indate = datetime.datetime(year,month,day) #Converts input into datetime format

newday = indate.toordinal() #Converts input into day number

num1 = int(input("Input number: "))

daychanged = newday+num1 #Adds num1 to given date

finaldate = datetime.date.fromordinal(daychanged) #Turns the new day back into a datetime

print(str(finaldate) + " is " + str(num1) + " days away.")
