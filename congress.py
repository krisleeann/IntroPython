"""
Hi Ben, I apologize for submitting this assignment so late. I'd like to use my one free pass from the syllabus
for this pset, please. I was feeling incredibly sick (not covid related luckily) and wasn't able to do much.
"""

def eligibleForSenate(age, lengthOfCitizenship):
    # Must be 30 and a citizen for 9 years
    if ((age > 29) and (lengthOfCitizenship > 8)):
        return True
    else:
        return False

def eligibleForHouse(age, lengthOfCitizenship):
    # Must be 25 and a citizen for 7 years
    if ((age > 24) and (lengthOfCitizenship > 6)):
        return True
    else:
        return False

def checkEligibility(eligibleForSenate, eligibleForHouse):
    if eligibleForSenate == True and eligibleForHouse == True:
        print("The candidate IS eligible for election to either the House or the Senate.\n")
    if eligibleForSenate == True and eligibleForHouse == False:
        print("The candidate IS eligible for election to the Senate but is NOT eligible for election to the House.\n")
    if eligibleForHouse == True and eligibleForSenate == False:
        print("The candidate IS eligible for election to the House but is NOT eligible for election to the Senate.\n")
    if eligibleForSenate == False and eligibleForHouse == False:
        print("The candidate is NOT eligible for election to either the House or the Senate.\n")

def main():
    print("CONGRESS ELIGIBILITY\n")
    age = int(input("Enter your age in years: "))
    lengthOfCitizenship = int(input("Enter years of U.S. Citizenship: "))
    print()

    checkEligibility(eligibleForSenate(age, lengthOfCitizenship), eligibleForHouse(age, lengthOfCitizenship))

main()