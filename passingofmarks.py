def markscheck():
    marks = int(input("Enter your marks: "))
    if marks >= 75:
        return "You passed with distinction"
    elif marks >= 40:
        return "You passed"
    else:
        return "You failed"  
def main():
    print(markscheck())
main()     