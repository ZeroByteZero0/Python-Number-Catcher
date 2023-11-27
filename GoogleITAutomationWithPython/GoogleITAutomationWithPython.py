#HI WHAT CAN YOU DO IN PYTHON?
    #create simple programs
#CAN YOU TELL ME ABOUT THE HISTORY OF PYTHON?
    #created by Guido Van Rossen in 1990s
#CAN YOU WRITE BASIC STATEMENTS, FUNCTIONS, PROGRAMS?
    #Basic statements
    #variable assignments
    #modulus functions
#CAN YOU RUN SCRIPTS THAT RETURN TEXT FILES LOGGED WITH DATA?
    #not off the top of my head
#CAN YOU WRITE SCRIPTS, PORT SCANNERS, WIRESHARK AUTOMATION SCRIPTS?
    #not off the top of my head
# semicolons after statements are allowed but rarely used
#** used for exponentiation
#// used for integer division
#: used for beginning an if statement or a while loop body

import os
from time import sleep

#Function returns whether a number is prime or not
def isPRIME(n):
    for e in range(2, 10000):
        if n % e == 0:
            return False
        else:
            return True


#function that takes input from a user
def getGud():
    #create something that can clear the screen between user inputs
    rejection_Count = 0
    for i in range(0, 100):

        #user basic info
        Name = input("What is your name?\n")
        Number = input("What's your number?\n")
        Sign = input("What's your sign?\n")
        os.system( 'cls' )


        #print("\n" + Name + "\n" + Number + "\n(Y/N): ")
        #os.system('cls')

        second_Answer = input("Coffee later tonight?\n(Y/N)?: ")
        
        if((second_Answer == "Y") or (second_Answer == "y")):
            file = open("numbers.txt", "a")
            file.write("Name: " + Name + "\nNumber: " + Number + "\nSign: " + Sign + " " + "\n\n")
            for i in range (0, 100):
            #i want to append a string using a for loop to create a cascading effect
            #right now the screen populates at once rather than cascade
                print(  
                    "X" + "O" + "X" + "O" + "X" + "O" + "X" + "O" + "X" + "O"  
                  + "X" + "O" + "X" + "O" + "X" + "O" + "X" + "O" + "X" + "O"
                  + "X" + "O" + "X" + "O" + "X" + "O" + "X" + "O" + "X" + "O" 
                  + "X" + "O" + "X" + "O" + "X" + "O" + "X" + "O" + "X" + "O"
                  + "X" + "O" + "X" + "O" + "X" + "O" + "X" + "O" + "X" + "O" 
                  + "X" + "O" + "X" + "O" + "X" + "O" + "X" + "O" + "X" + "O" 
                  + "X" + "O" + "X" + "O" + "X" + "O" + "X" + "O" + "X" + "O" 
                  + "X" + "O" + "X" + "O" + "X" + "O" + "X" + "O" + "X" + "O"
                  + "X" + "O" + "X" + "O" + "X" + "O" + "X" + "O" + "X" + "O" 
                  + "X" + "O" + "X" + "O" + "X" + "O" + "X" + "O" + "X" + "O" 
                  + "X" + "O" + "X" + "O" + "X" + "O" + "X" + "O" + "X" + "O" 
                  + "X" + "O" + "X" + "O" + "X" + "O" + "X"
                  )
            file.close()
            sleep(5)
            os.system('cls')

        else:                
            rejection_Count += 1            
            print(Name + " you're rejection #" + str(rejection_Count))
        
        
        sleep(2)
        os.system('cls')
        
        if Name == "Mon Cheri":
            break
getGud()

#test comment for push on Git!!!

