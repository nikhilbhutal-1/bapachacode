def vowelchecker():
    char = input("enter character:")
    if char in ['a', 'i', 'u', 'e', 'o']:
        return "vowel"
    else:
        return "consonant"
    
def main():
    print(vowelchecker())

main()        
