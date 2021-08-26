def easter():
    y = (int(input("Enter a year: ")))
    a = y % 19
    b = int(y / 100)
    c = y % 100
    d = int(b / 4)
    e = b % 4
    g = int((8 * b + 13) / 25)
    h = (19 * a + b - d - g + 15) % 30
    j = int(c / 4)
    k = c % 4
    m = int(((a+11) * h) / 319) 
    r = ((2 * e + 2 * j - k - h + m + 32) % 7)
    n = int((h - m + r + 90) / 25)
    p = ((h - m + r + n + 19) % 32)

    if n == 3:
        month = ("March") 
    else:
        month = ("April")

    print(month, p)   

def main(): 
    easter()

main()