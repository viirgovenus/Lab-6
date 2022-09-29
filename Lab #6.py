
import string

# assigns character digit
def charVal(char : str) -> int:
    return (ord(char) - 65)

# checks digit to give corresponding value
def checkDigit(idNum : str) -> int:
    checkDigit = 0
    for index, value in enumerate(idNum[0:5]):
        checkDigit += (charVal(value) * (index + 1))
    for index, value in enumerate(idNum[5:10]):
        checkDigit += (int(value) * (index + 6))
    return checkDigit % 10

# varifies amount of digits
def varifyCheckDigit(idNum : str) -> tuple:
    if len(idNum) != 10:
        return "Length of the number must be 10"
    for index, value in enumerate(idNum[0:5]):
        if not value.isalpha():
            return "The first 5 characters must be A-Z. The invalid character at index {} is {}".format(index, value)
    for index, value in enumerate(idNum[7:]):
        if not value.isdigit():
            return "Last 3 characters must be between 0-9. The invalid character at index {} is {}".format((index+7), value)
    if getSchool(idNum) == "Invalid School":
        return "The sixth character must be 1-3"
    elif getGrade(idNum) == "Invalid Grade":
        return "The seventh character must be 1-4"
    elif checkDigit(idNum) != int(idNum[9]):
        return "Check digit {} does not match calculated value {}".format(idNum[9], checkDigit(idNum))
    else:
        return True

#gives school number
def getSchool(idNum : str) -> str:
    schools = {"1" : "School of Computing and Engineering SCE" , "2" : "School of Law", "3" : "College of Arts and Sciences"}
    if idNum[5] in schools:
        return schools[idNum[5]]
    else:
        return "Invalid School"

#gives grade
def getGrade (idNum : str) -> str:
    grades = {"1" : "Freshman" , "2" : "Sophomore" , "3" : "Junior" , "4" : "Senior"}
    if idNum[6] in grades:
        return grades[idNum[6]]
    else:
        return "Invalid Grade"

if __name__ == "__main__":

    print("{:^60}".format("Linda Hall"))
    print("{:^60}".format("Library Card Check"))
    print("="*60)

    while True:
        print()
        cardNum = input("Enter Library Card. Hit enter to exit ==> ".upper().strip())
        if cardNum == " ":
            break
        result = varifyCheckDigit(cardNum)
        if result == True:
            print("Library card is valid")
            print("This card belongs to a student in {}".format(getSchool(cardNum)))
            print("This card belongs to a {}".format(getGrade(cardNum)))
        else:
            print("Library card is invalid")
            print(result)
            
            
        

        
        
    
    
    


    

            
            
                                      
    
        
    
                       
    
