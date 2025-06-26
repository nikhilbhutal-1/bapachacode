def angles():
    num = int(input(" enter angle :"))
    if num < 90 :
        return "acute"
    elif num == 90 :
        return "right"
    elif num > 90 and num < 180 :
        return "obtuse"
    elif num == 180:
        return "straight"
    elif num > 180 and num < 360:
        return "reflex"
    else:
        return "invalid"  
    
def main():
    print(angles())

main()        