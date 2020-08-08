#import all the functions necessary
import gamefunct
import random

#data validation loop to ensure there is a positive number of problems
while True:
    #ask for input
    num_problems=int(input("How many problems would you like to attempt? "))
    #condition 1
    if num_problems >= 1:
        break
    #if condition 1 isn't fulfilled
    else:
        print("Invalid number, try again\n")
        
#data validation loop to ensure the width of digits is in the range we want
while True:
    #ask for input
    width=int(input("How wide do you want your digits to be? 5-10: "))
    #condition 1
    if width >= 5 and width <= 10:
        break
    #if condition 1 isn't fulfilled
    else:
        print("Invalid width, try again\n")

#data validation loop to make sure string is one character long
while True:
    #ask for user input
    character=input("What character would you like to use? ")
    #condition 1
    if len(character) == 1:
        break
    #condition 2
    elif len(character) > 1:
        print("String too long, try again\n")
    #if none of the other conditions are meant
    else:
        print("String too short, try again\n")

#data validation loop to make sure valid inputs are entered for drill mode
while True:
    #lower the string just in case they have it mixed case
    drill_mode=str.lower(input("Would you like to activate 'drill' mode? yes or no: "))
    #condition 1: drill mode on, do not count number correct
    if drill_mode == "yes":
        print("\nHere we go!\n")
        addition=0
        subtraction=0
        multiplication=0
        division=0
        extra_add=0
        extra_sub=0
        extra_mult=0
        extra_div=0
        #for loop to cycle through the number of problems requested
        for n in range(1, num_problems+1):
            #randomly generate a problem
            number_1=random.randint(0, 9)
            number_2=random.randint(0, 9)
            operator_rand=random.randint(1, 4)
            #determine operator
            if operator_rand == 1:
                operator = "+"
                addition+=1
            elif operator_rand==2:
                operator = "-"
                subtraction+=1
            elif operator_rand==3:
                operator="*"
                multiplication+=1
            else:
                operator="/"
                division+=1
                while True:
                    if  number_2 == 0:
                        number_2=random.randint(0, 9)
                    else:
                        break
                while True:
                    if number_1<number_2:
                        number_1=random.randint(0, 9)
                    else:
                        break
                answer=number_1/number_2
                while True:
                    if answer % 1!= 0:
                        number_1=random.randint(0, 9)
                    else:
                        break
                    
            print("What is .....")
            print()
            #print the digital number
            gamefunct.print_number(number_1, width, character)
            #print the sign
            if operator_rand == 1:
                print(gamefunct.plus(width, character))
            elif operator_rand == 2:
                print(gamefunct.minus(width, character))
            elif operator_rand==3:
                print(gamefunct.multiply(width, character))
            else:
                print(gamefunct.divide(width, character))


                
            #print the second digital number
            gamefunct.print_number(number_2, width, character)
            #ensure that answer is correct, if it's not repeat until it is
            while True:
                input_answer=int(input("= "))
                #check the answer to see if it's correct
                if gamefunct.check_answer(number_1, number_2, input_answer, operator) == True:

                    print("Correct!\n")
                    break
                else:
                    print("Sorry, that's not correct.")
                    if operator=="+":
                        extra_add+=1
                    elif operator=="-":                    
                        extra_sub+=1
                    elif operator=="*":
                        extra_mult+=1
                    else:    
                        extra_div+=1
        if addition >0:
            print("Total addition problems presented:", addition)
            print("# of extra attempts needed:", extra_add)
        else:
            print("No addition problems presented")
        if subtraction >0:
            print("Total subtraction problems presented:", subtraction)
            print("# of extra attempts needed:", extra_sub)
        else:
            print("No subtraction problems presented")
            
        if multiplication>0:
            print("Total multiplication problems presented:", multiplication)
            print("# of extra attempts needed:", extra_mult)
        else:
            print("No multiplication problems presented")
        if division>0:
            print("Total division problems presented:", division)
            print("# of extra attempts needed:", extra_div)
        else:
            print("No division problems presented")
        print("\nThanks for playing!")
        break
    #if it is not drill mode--determine number correct                    
    elif drill_mode == "no":
        print("\nHere we go!\n")
        #accumulator variable to know how many are correct
        correct=0
        addition=0
        subtraction=0
        multiplication=0
        division=0
        add_cor=0   
        sub_cor=0
        mult_cor=0
        div_cor=0
        #for loop to cycle through number of problems requested
        for n in range(1, num_problems+1):
            #randomly generate a problem
            number_1=random.randint(0, 9)
            number_2=random.randint(0, 9)
            operator_rand=random.randint(1, 4)
            #determine operator
            if operator_rand == 1:
                operator = "+"
                addition+=1
            elif operator_rand==2:
                operator = "-"
                subtraction+=1
            elif operator_rand==3:
                operator="*"
                multiplication+=1
            else:
                operator="/"
                division+=1
                while True:
                    if  number_2 == 0:
                        number_2=random.randint(0, 9)
                    else:
                        break
                while True:
                    if number_1<number_2:
                        number_1=random.randint(0, 9)
                    else:
                        break
                answer=number_1/number_2
                while True:
                    if answer % 1!= 0:
                        number_1=random.randint(0, 9)
                    else:
                        break
                    
            print("What is .....")
            print()
            #print the digital number
            gamefunct.print_number(number_1, width, character)
            #print the sign
            if operator_rand == 1:
                print(gamefunct.plus(width, character))
            elif operator_rand == 2:
                print(gamefunct.minus(width, character))
            elif operator_rand==3:
                print(gamefunct.multiply(width, character))
            else:
                print(gamefunct.divide(width, character))
            gamefunct.print_number(number_2, width, character)
            input_answer=int(input("= "))
            #check answer
            if gamefunct.check_answer(number_1, number_2, input_answer, operator) == True:
                print("Correct!\n")
                #if one is correct, then add to the accumulator variable
                correct += 1
                if operator=="+":
                    add_cor+=1
                elif operator=="-":
                    sub_cor+=1
                elif operator=="*":
                    mult_cor+=1
                else:
                    div_cor+=1
                    
            else:
                print("Sorry, that's not correct.")
                
        #print accumulator variable
        print("\nYou got", correct, "out of", num_problems, "correct!")
        if addition >0:
            print("Total addition problems presented:", addition)
            print("Correct addition problems:", add_cor, "(", ((add_cor/addition)*100),"% )")
        else:
            print("No addition problems presented")
        print()
        if subtraction>0:
            print("Total subtraction problems presented:", subtraction)
            print("Correct subtraction problems:", sub_cor, "(", ((sub_cor/subtraction)*100),"% )")
        else:
            print("No subtraction problems presented")
        print()
        if multiplication>0:
            print("Total multiplication problems presented:", multiplication)
            print("Correct addition problems:", mult_cor, "(", ((mult_cor/multiplication)*100),"% )")
        else:
            print("No multiplication problems presented")
        print()

        if division>0:
            print("Total division problems presented:", division)
            print("Correct division problems:", div_cor, "(", ((div_cor/division)*100),"% )")
        else:
            print("No division problems presented")
        break
    #if they enter the wrong input, the loop will continue until they do
    else:
        print("Invalid input, try again")
            


            


                
