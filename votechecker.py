def votechecker():
    age = int(input("enter your age:"))
    if age >= 18 and age <=80 :
        return "you are eligible to vote"
    else:
        return "you cannot vote"
    
def main():
    print(votechecker())

main()        