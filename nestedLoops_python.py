# Nested loops examples

# 1.

for i in range (1,11):
    for j in range (1,11):
        print (i*j, end = " ")
    print(' ')

# 2.

rows = 5
for i in range(1,rows+1):
    for j in range(1,i+1):
        print("*",end = " ")
    print(' ')

# 3.

names = ["Anand","Charles","Yassen"]

for name in names:
    count = 0
    while count < 5:
        print(name,end=" ")
        count = count + 1
    print(' ')
        
# Break Nested loop
for i in range (1,4):
    for j in range(1,4):
        if j==i:
            break
    print(i,j)

# Nested while loop
i = 1
while i <= 5:
    j=1
    while j<=10:
        print(j,end=" ")
        j =j +1
    i = i+1
    print('')

    
    
