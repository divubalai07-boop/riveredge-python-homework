log = "py, PY,excel, py , ,SQL,excel,PY"

count = {}

for i in log.split(","):
    i = i.strip().upper()

    if i != "":
        count[i] = count.get(i, 0) + 1

print(count)

print("Most frequent:", max(count, key=count.get))