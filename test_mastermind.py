import random


def run_game():
    num = random.randrange(1,8)
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")
    
    intake = int(input("Input 4 digit code: "))
    
    if(intake==num):
        
        print("great job! you're a mastermind!")

    else:
        level = 0
        while(intake!=num):
            level += 1      #variable will increment everytime the loop is executed
                            #tracks the guesses made
            count=0     #function used the count the string
            
            intake = str(intake) #conversion of int to str
            num = str(num)      #conversion of str to integer
#create an empty list which stores digits that are correct
            
            right_digits=[]
#4 digits in the number 
#create a for loop that loops 4 times checking each digit
            for i in range(0,4):
                if(intake[i] == num[i]):
                    count +=1
                    right_digits.append(intake[i]) #adds onto the list
                    print("Number of correct digits in correct place: ")
                else:
                    print("Number of correct digits not in correct place: ")
                    continue    #returns to the control to the beginning of the while loop



if __name__ == "__main__":
    run_game()
