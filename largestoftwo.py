def largest():
    num1 = int(input("enter num1:"))
    num2 = int(input("enter num2:"))
    if num1 > num2 :
        return "num1 is larger"
    else:
        return "num2 is larger"
    
def main():
    print(largest())

main()        