#author: RED 1/20/23
list= [] # empty list
i=0
while i<5: #amount of inputs
    i+=1
    num = int(input('number: '))
    if num%3 == 0:
        list.append(num)
    else:
        continue # continue function
    print(list)
