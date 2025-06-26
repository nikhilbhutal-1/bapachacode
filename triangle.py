def triangle():
    a = int(input("Enter the first side of the triangle: "))
    b = int(input("Enter the second side of the triangle: "))
    c = int(input("Enter the third side of the triangle: "))
    if a + b > c and a + c > b and b + c > a :
        return "Valid Triangle"
    else:
        return "The given sides cannot form a triangle"
        

def main():
    print(triangle())

main()    