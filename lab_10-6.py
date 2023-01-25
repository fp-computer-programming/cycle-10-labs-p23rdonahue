#author: RED 1/15/23

def add_nums(numbers):
    try:
        number = int(input("Number: "))
        for x in range(0,len(numbers)):
            numbers[x] += number
            
    except TypeError:
        print("Input a valid number")
    print(f'passed list: {numbers}; user input:{number}')

add_nums([1,2,3,4,5])
add_nums([4,5,6,7,8])
add_nums([10,12,154,18])


