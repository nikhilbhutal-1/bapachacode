def oddeven():
    num = int(input("enter number:"))
    if num % 2==0:
        return "even"
    elif num > 0:
        return "negative"
    else:
        return "odd"

def trueid():
    print(oddeven())
trueid()