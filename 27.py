#building a translator
def translator(string):
    translate = ''
    for letter in string:
        if letter in "AEIOUaeiou":
            translate += 'g'
        else:
            translate += letter
    return translate

string = input("Enter a string: ")
print(translator(string))
