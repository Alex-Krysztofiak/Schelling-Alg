print("This program helps you determine the amount to tip")
bill = float(input("Enter the amount of the bill(e.g. 34.50): "))
percent = float(input("Enter the tip percentage (e.g. 20 for 20%): "))
percent = percent/100
tip = bill*percent
total = bill + tip
print("the tip should be {0}".format(tip))
print("the total (bill plus tip) should be {:.2f}".format(total))
