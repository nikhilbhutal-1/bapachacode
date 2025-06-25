def divisible():
    num = int(input("enter value:"))
    if num % 5 == 0:
        return "divisible"
    else:
        return "not divisible"
    
def main():
    print(divisible())
        
main()    