#GCSE CompSci
#2.3 robust programs
#meaningful error messages 1

def options(num):
    if num == 1:
        return "Computer Science"
    elif num == 2:
        return "Music"
    elif num == 3:
        return "Dance"
    elif num == 4:
        return "PE"
    else:
        return "Not a valid option"
choice = int(input("What is your choice?"))
print(options(choice))
