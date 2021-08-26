# SUBMITTING FOR EXTRA CREDIT

def sign(month, day):
    if ((month == 3 and day > 21) or (month == 4 and day < 20)):
        return "Aries"
    elif ((month == 4 and day > 19) or (month == 5 and day < 21)):
        return "Taurus"
    elif ((month == 5 and day > 20) or (month == 6 and day < 21)):
        return "Gemini"
    elif ((month == 6 and day > 20) or (month == 7 and day < 23)):
        return "Cancer"
    elif ((month == 7 and day > 22) or (month == 8 and day < 23)):
        return "Leo"
    elif ((month == 8 and day > 22) or (month == 9 and day < 23)):
        return "Virgo"
    elif ((month == 9 and day > 22) or (month == 10 and day < 23)):
        return "Libra"
    elif ((month == 10 and day > 22) or (month == 11 and day < 22)):
        return "Scorpio"
    elif ((month == 11 and day > 21) or (month == 12 and day < 22)):
        return "Sagittarius"
    elif ((month == 12 and day > 21) or (month == 1 and day < 20)):
        return "Capricorn"
    elif ((month == 1 and day > 19) or (month == 2 and day < 19)):
        return "Aquarius"
    elif ((month == 2 and day > 18) or (month == 3 and day < 20)):
        return "Pisces"
    else:
        return "INVALID_DATE"

def main():
    print("Please enter your birthday, without year, in the following format: Jun 24")
    month = int(input("Enter your birth month in numerical format: "))
    day = int(input("Date: "))
    your_sign = sign(month, day)
    
    print("Your sign is: %s" % your_sign)
main()