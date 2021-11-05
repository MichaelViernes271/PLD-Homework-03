#name introduction
"""
Programming Logic and Design: Homework 03
Author: Viernes, Michael
Submitted to: Mr. Madrigalejos
"""

print("--------------------")
print("\tIntroduction")
print("--------------------")

# Getter functions.
def getName():
    name = input("Your name: ")
    return name
    
def getAge():
    age = input("Your age: ")
    return age
    
def getAddress():
    address = input("Your address: ")
    return address

def printInfo(userInfo):
    print(f"Hi, my name is {userInfo[0]}. I am {userInfo[1]} years old and I live in {userInfo[2]}.")

# define main program
def main():
    # Creating array.
    info = []
    try:
        info.append(getName())
        info.append(getAge())
        info.append(getAddress())
    except Error:
        print("Please put a proper input.")
    printInfo(info)
    
# call main program
main()