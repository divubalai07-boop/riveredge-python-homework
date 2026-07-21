#salary slip num to wordds
ones = ["zero","one","two","three","four","five","six","seven","eight","nine",
        "ten","eleven","twelve","thirteen","fourteen","fifteen",
        "sixteen","seventeen","eighteen","nineteen"]

tens = ["","","twenty","thirty","forty","fifty",
        "sixty","seventy","eighty","ninety"]

def amount_in_words(n):
    ans = " "

    if n >= 1000:
        ans += ones[n//1000] + " thousand "
        n = n % 1000

    if n >= 100:
        ans += ones[n//100] + " hundred "
        n = n % 100

    if n >= 20:
        ans += tens[n//10] + " "
        n = n % 10

    if n > 0 and n < 20:
        ans += ones[n]

    print(ans + " rupees")

amount_in_words(9999)
amount_in_words(807)