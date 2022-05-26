rev = []
  
n = int(input("Enter number of items : "))
  
for i in range(0, n):
    item = int(input())
    rev.append(item)
      
rev.reverse()
print (rev)
