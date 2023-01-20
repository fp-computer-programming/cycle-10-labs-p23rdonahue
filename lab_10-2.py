#author: RED 1/20/23
list= []
i=0
while i<5:
    i+=1
    num = int(input('number: '))
    if num%3 == 0:
        list.append(num)
    else:
        continue
    print(list)
