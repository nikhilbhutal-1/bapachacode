def div2and5():
    num = int(input("enter number: "))
    if num % 2 == 0 and num % 5 == 0:
        return "number is divisible by both 2 and 5"
    elif num % 2 == 0:
        return "number is divisible by 2"
    elif num % 5 == 0:
        return "number is divisible by 5"
    else: 
        return "number is not divisible by both 2 and 5"
    
def main():
    print(div2and5())

main()
    