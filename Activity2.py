def cube(num):
    return num ** 3

def by_three(num):
    if num % 3 == 0:
        return cube(num)

    else:
        return False

num = int(input("Enter The Number You Want To Check If Divisible By 3: "))

print (by_three(num))