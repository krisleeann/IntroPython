# BUG: Doesn't preseve individual vowels unless they're capitalized (which I know is because they're not in the list)
def advertisement(ad):
    
    vowels = ['a', 'e', 'i', 'o', 'u']

    for i in ad:
        if i in vowels:
            ad = ad.replace(i, "")

    return ad

def main():
    x = "Desirable unfurnished flat in quiet residential area"
    print(advertisement(x))
    
    x = "I'm selling: timeshare in west Maui with beautiful ocean views"
    print(advertisement(x))

main()
