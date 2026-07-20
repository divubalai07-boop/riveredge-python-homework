invoices = ['RE2026', 'R12026', 'REX206', 'RE20A6', 'RE12345']

for i in invoices:

    if len(i) != 6:
        print(i,"-> wrong length")

    elif not i[:2].isalpha():
        print(i,"-> letters part wrong")

    elif not i[2:].isdigit():
        print(i,"-> digits part wrong")
    else:
        print(i,"-> correct invoice")    