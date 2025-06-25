def negvalue():
    value = int(input(" enter value:"))    
    if value > 0:
        return "positive"
    elif value == 0:
        return "zero"
    else:
        return "negative"
def num():
     print(negvalue())
    
num()
