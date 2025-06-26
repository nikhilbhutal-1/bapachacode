def leapyear():
    year = int(input("Enter a year: "))
    if year % 4 == 0 and year % 100 != 0 or (year % 400 == 0):
        return "its leap year"
    else :
        return "its not leap year"
    
def  main():
    print(leapyear())

main()    