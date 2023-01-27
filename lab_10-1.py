#author: RED 1/20/23
sum = 0

while True: #making loop
    num = int(input('number: '))
    if num == -1: #making sure num doesnt equal -1
        print(sum)
        break #breaking at end
    sum += num


