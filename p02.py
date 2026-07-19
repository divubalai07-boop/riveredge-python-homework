total_money= int(input("Enter total amount: "))
people = int(input("Enter number of people: "))

if people == 0:
    print("Cannot divide by 0 people.")
else:
    shareofmoney= total_money // people
    piggy_bank = total_money % people

    print("Each pays: Rs", shareofmoney)
    print("Piggy bank gets: Rs", piggy_bank)