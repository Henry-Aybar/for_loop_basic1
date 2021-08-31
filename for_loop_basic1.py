# 1. Basic
for x in range(151): # will print 0-150
    print(x)

# 2. Multiples of 5
for x in range(5,1001,5): # From 5 to 1000 incramented by 5
    print(x) 

# 3. Counting, the Dojo Way
def Dojo():
    for num in range(1,101):          # ===============================
        if num % 10 == 0:             # the larger mod comes first    || 
            print("Coding Dojo",num)  # then work way down to lower   ||
        elif num % 5 == 0:            # mods to yeild result.         ||
            print("Coding",num)       # smaller will over write the   ||
        else:                         # larger and both will show     ||
            print(num)                # ===============================
Dojo()

# 4. Whoa, That Sucker's Huge
sum =0
for x in range(1,500001): # From 1 to 500000 incramented by 1
    sum += x
print(sum)


# 5. Countdown by Fours
for x in range(2018,0,-4): # From 2018 to 1 decramented by 4
    print(x) 

# 6. Flexable Coutner
lowNum = 2
highNum = 9
mult = 3

for num in range(lowNum, highNum +1, 1): # high num + 1 to include number, incrament by 1 to inclued all posible numbers
    if num % mult == 0:                  # then % mult value == 0
        print(num)
