def equalorgreat():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if num1 > num2:
        return " the first number is greater"
    elif num1 < num2:
        return "The second number is greater."
    else:
        return "the numbers are equal"
def main():
    print(equalorgreat())

main()        