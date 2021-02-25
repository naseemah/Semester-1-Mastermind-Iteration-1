import random

def run_game():
#this function generates the code and returns it. 4 different numbers that get chosen at random
    num1 = random.randint(1,8)
    num2 = random.randint(1,8)      
    num3 = random.randint(1,8)
    num4 = random.randint(1,8)
    num_list=[num1, num2, num3, num4]

    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")
    #print(num_list)

    num_list_str = "".join(str(e) for e in num_list) #coversion of the list into a string
    guess = ""
    condition = True
    counter = 12
    
    while counter >= 0:
        if counter == 0:
            print("The code was: "+num_list_str)
            break
        else:
            if counter == 12:
                #condition = True
                while condition:
                    guess = input("Input 4 digit code: ")
                    if len(guess) != 4 or guess.isdigit()!= True: #if the length of guess is not 4 digit, its false 
                        print("Please enter exactly 4 digits.") #for the above statement
                    else:
                        test_range=all(int(i)in range(0,9)for i in str(guess))
                        if test_range == True:
                            condition = False
                        else:
                            print("Please enter exactly 4 digits.")
                            condition = True
            else:
                print("Turns left: "+str(counter))
                condition = True
                while condition:
                    guess = input("Input 4 digit code: ")
                    if len(guess) != 4 or guess.isdigit() != True:
                        print("Please enter exactly 4 digits.")
                    else:
                        test_range=all(int(i)in range(1,9)for i in str(guess))
                        if test_range == True:
                            condition = False
                        else:
                            print("Please enter exactly 4 digits.")
                            condition = True
            i = 0
            counter1 = 0
            counter2 = 0
            while i < 4:
                num_list_index = str(num_list[i])
                guess_index = str(guess[i])
                if guess_index == num_list_index:
                    counter1 = counter1 + 1
                elif guess_index in num_list_str:  
                    counter2 = counter2 + 1
                i = i + 1
            if guess == num_list_str:
                print("Number of correct digits in correct place:     "+str(counter1))
                print("Number of correct digits not in correct place: "+str(counter2))
                print("Congratulations! You are a codebreaker!")
                print("The code was: "+ num_list_str)
                break
            else:
                print("Number of correct digits in correct place:     "+str(counter1))
                print("Number of correct digits not in correct place: "+str(counter2))
                counter = counter - 1

if __name__ == "__main__":
    run_game()