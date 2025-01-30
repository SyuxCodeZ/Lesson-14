# creating the function

def tip_perc(bill, tip):
    total = bill *(tip / 100)
    result = round(total, 2)
    print (f"Your Tip Is {result}")
bill = int(input("Enter Your Bill: "))
tip = int(input("Enter The Tip Percentage: "))

tip_perc (bill, tip)