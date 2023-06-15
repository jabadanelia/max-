while True:
    
    n = int(input("How much numbers want enter? "))
    if n < 4 or n%2 == 1 or n == 1:
        print("Please enter four or more number and only odd times!")
        continue
    else:
        break

num = []

for i in range(n):
    
    f = int(input("Please enter some whole numbers: "))
    num.append(f)


new_num = num.copy()

mksort = []

j = 0

while j <= len(num):
    
    if len(new_num) > 1:
        minimum = min(new_num)
        mksort.append(minimum)
        new_num.remove(minimum)
        

    elif len(new_num) == 1:
        mksort.append(new_num[0])
        new_num.remove(new_num[0])

   

    j += 1

print(mksort)
