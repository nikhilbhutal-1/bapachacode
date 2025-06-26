def div3():
    num = int(input("Enter a number: "))
    if num == 0:
        return "zero"
    elif num > 0 and num % 2 == 0 and num % 3 == 0:
        return "number is positive and even and divisible by 3"
    elif num > 0 and num % 2 == 0:
        return "number is positive and even"
    elif num > 0 and num % 3 == 0:
        return "number is divisible by 3 and positive number"
    elif num < 0:
        return "number is negative"
    else:
        return"invalid number"

def main():
    print(div3())

main()            