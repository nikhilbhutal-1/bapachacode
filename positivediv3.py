def div3():
    num = int(input("Enter a number: "))
    if  num > 0 and num % 2 == 0:
        return "number is even and positive number"
    elif num < 0 :
        return "number is negative number"
    elif num % 3 == 0 :
        return "number is divisible by 3 and positive number"
    elif num == 0 :
        return"zero"

def main():
    print(div3())

main()            