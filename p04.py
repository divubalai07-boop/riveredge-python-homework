#attendence cleaner 
raw = ['  divyesh BALAI', 'rajat  ', 'Divyesh Balai', 'RAJAT', 'khushi shah', ' Khushi  Shah ']

clean = []

for name in raw:
    name = " ".join(name.split())   # word split and join to remove extra spaces
    name = name.title()             # show in proper case title ,capatilize first letter of each word

    if name not in clean:
        clean.append(name)

clean.sort() #alphabetical order

print("Clean list:", clean)
print("Duplicates removed:", len(raw) - len(clean))
