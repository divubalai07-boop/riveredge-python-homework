name = input("Enter full name: ")
company = input("Enter company name: ")

x = name.split()


initials = x[0][0].upper() + "." + x[1][0].upper() + "." +  x[2].upper()
line1 = initials 
line2 = company + " Intern"

print("=" * 30)
print("| {:<27}|".format(line1))
print("| {:<27}|".format(line2))
print("=" * 30)