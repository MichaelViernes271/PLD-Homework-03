#apple pos
"""
Programming Logic and Design: Homework 03
Author: Viernes, Michael
Submitted to: Mr. Madrigalejos
"""

print("----------------------------------------")
print("\t\tApples")
print("----------------------------------------")
    
def calcApples():
    "Calculates apples."
    savings = float(input("Amount of your money: "))
    apple = float(input("How much apple will you buy:: "))
    
    calcChange(savings, apple)

def calcChange(savings, apple):
    "Calculates change"
    money_change = savings - apple
    
    if money_change < 0:
        print("You had bought too many apples!")
        calcApples()
    else:
        print(f"You can buy {int(apple)} apples and" + 
        f" your change is {str(float(money_change))} pesos.")
    
    # testing pass kword
    pass

# main function call
def main():
    calcApples()
    
main()