# function:   horizontal_line
# input:      a width value (integer) and a single character (string)
# processing: generates a single horizontal line of the desired size
# output:     returns the generated pattern (string)
def horizontal_line(width,char):
    return width*char + "\n"

# function:   vertical_line
# input:      a shift value and a height value (both integers)  and a single character (string)
# processing: generates a single vertical line of the desired height.  the line is
#             offset from the left side of the screen using the shift value
# output:     returns the generated pattern (string)
def vertical_line(shift,height,char):
    pattern = ""
    for i in range(height):
        pattern += shift*" " + char + "\n"
    return pattern

# function:   two_vertical_lines
# input:      a width value and a height value (both integers)  and a single character (string)
# processing: generates two vertical lines.  the first line is along the left side of
#             the screen. the second line is offset using the "width" value supplied
# output:     returns the generated pattern (string)
def two_vertical_lines(width,height,char):
    pattern = ""
    for i in range(height):
        pattern += char + " "*(width-2) + char + "\n"
    return pattern

# function:   number_1
# input:      a width value (integer) and a single character (string)
# processing: generates the number 1 as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)
def number_1(width, character):
	pattern = vertical_line(width-1, 5, character)
	return pattern


# function:   number_2
# input:      a width value (integer) and a single character (string)
# processing: generates the number 1 as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)
def number_2(width, character):
	pattern = horizontal_line(width, character)+vertical_line(width-1, 1, character)+horizontal_line(width, character)+vertical_line(0, 1, character)+horizontal_line(width, character)
	return pattern


# function:   number_3
# input:      a width value (integer) and a single character (string)
# processing: generates the number 1 as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)
def number_3(width, character):
	pattern = horizontal_line(width, character)+vertical_line(width-1, 1, character)+horizontal_line(width, character)+vertical_line(width-1, 1, character)+horizontal_line(width, character)
	return pattern


# function:   number_4
# input:      a width value (integer) and a single character (string)
# processing: generates the number 1 as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)
def number_4(width, character):
	pattern = two_vertical_lines(width, 2, character)+horizontal_line(width, character)+vertical_line(width-1, 2, character)
	return pattern


# function:   number_5
# input:      a width value (integer) and a single character (string)
# processing: generates the number 1 as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)
def number_5(width, character):
	pattern = horizontal_line(width, character)+vertical_line(0, 1, character)+horizontal_line(width, character)+vertical_line(width-1, 1, character)+horizontal_line(width, character)
	return pattern



# function:   number_6
# input:      a width value (integer) and a single character (string)
# processing: generates the number 1 as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)
def number_6(width, character):
	pattern = horizontal_line(width, character)+vertical_line(0, 1, character)+horizontal_line(width, character)+two_vertical_lines(width, 1, character)+horizontal_line(width, character)
	return pattern



# function:   number_7
# input:      a width value (integer) and a single character (string)
# processing: generates the number 1 as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)
def number_7(width, character):
	pattern = horizontal_line(width, character)+vertical_line(width-1, 4, character)
	return pattern


# function:   number_8
# input:      a width value (integer) and a single character (string)
# processing: generates the number 1 as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)
def number_8(width, character):
	pattern = horizontal_line(width, character)+two_vertical_lines(width, 1, character)+horizontal_line(width, character)+two_vertical_lines(width, 1, character)+horizontal_line(width, character)
	return pattern


# function:   number_9
# input:      a width value (integer) and a single character (string)
# processing: generates the number 1 as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)
def number_9(width, character):
	pattern = horizontal_line(width, character)+two_vertical_lines(width, 1, character)+horizontal_line(width, character)+vertical_line(width-1, 2, character)
	return pattern


# function:   number_0
# input:      a width value (integer) and a single character (string)
# processing: generates the number 1 as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)
def number_0(width, character):
	pattern = horizontal_line(width, character) + two_vertical_lines(width, 3, character) + horizontal_line(width, character)
	return pattern


# function:   print_number
# input:      a number to print (integer), a width value (integer) and a single character (string)
# processing: prints the desired number to the screen using the supplied width value
# output:     does not return anything
def print_number(integer, width, character):
    if integer == 0:
        print(number_0(width, character))
    elif integer == 1:
        print(number_1(width, character))        
    elif integer == 2:
        print(number_2(width, character))        
    elif integer == 3:
        print(number_3(width, character))        
    elif integer == 4:
        print(number_4(width, character))        
    elif integer == 5:
        print(number_5(width, character))
    elif integer == 6:
        print(number_6(width, character))        
    elif integer == 7:
        print(number_7(width, character))        
    elif integer == 8:
        print(number_8(width, character))        
    elif integer == 9:
        print(number_9(width, character))

# function:   two_vertical_lines_no_space
# input:      a width value and a height value (both integers)  and a single character (string)
# processing: generates two vertical lines which will return in the center of the width value provided
# output:     returns the generated pattern (string)
def two_vertical_lines_no_space(width,height,char):
    pattern = ""
    for i in range(height):
        pattern += " " * ((width-1)//2) + char * 2 + "\n"
    return pattern

# function:   plus
# input:      width value (integer) and a single character (string)
# processing: generates the addition sign as a pattern, given the width (it will change depending on if the width is an even or odd value)
# output:     returns the generated pattern (string)
def plus(width, character):
    if width % 2 == 0:
        far_line = width//2
        pattern = two_vertical_lines_no_space(width, 2, character) + horizontal_line(width, character) + two_vertical_lines_no_space(width, 2, character)
        return pattern
    else:
        pattern = vertical_line(width//2, 2, character) + horizontal_line(width, character) + vertical_line(width//2, 2, character)
        return pattern


# function:   minus
# input:      width value (integer) and a single character (string)
# processing: generates the minus sign given the width and character
# output:     returns the generated pattern (string)
def minus(width, character):
    pattern = vertical_line(0, 2, " ") + horizontal_line(width, character) + vertical_line(0, 2, " ")
    return pattern

# function:   divide
# input:      width value (integer) and a single character (string)
# processing: generates the division sign given the width and character
# output:     returns the generated pattern (string)
def divide(width, character):
    if width % 2 == 0:
        far_line = width//2
        pattern = two_vertical_lines_no_space(width, 1, character) + horizontal_line(width, character) + two_vertical_lines_no_space(width, 1, character)
        return pattern
    else:
        pattern = vertical_line(width//2, 1, character) + horizontal_line(width, character) + vertical_line(width//2, 1, character)
        return pattern


# function:   multiply
# input:      width value (integer) and a single character (string)
# processing: generates the multiplication sign given the width and character
# output:     returns the generated pattern (string)
def multiply(width, character):
    if width % 2 == 0:
        far_line = width//2
        pattern = two_vertical_lines(width, 2, character)+"  "+horizontal_line(width//2, character)+ two_vertical_lines(width, 2, character)
        return pattern
    else:
        pattern = two_vertical_lines(width, 2, character)+" "+horizontal_line(width//2, character)+ two_vertical_lines(width, 2, character)
        return pattern



# function:   check_answer
# input:      two numbers (number1 & number2, both integers); an answer (an integer)
#             and an operator (+ or -, expressed as a String)
# processing: determines if the supplied expression is correct.  for example, if the operator
#             is "+", number1 = 1, number2 = 2 and answer = 3 then the expression is correct
#             (1 + 2 = 3).
# output:     returns True if the expression is correct, False if it is not correct
def check_answer(number_1, number_2, answer, operator):
    if operator == "+":
        if number_1 + number_2 == answer:
            return True
        else:
            return False
    if operator == "-":
        if number_1 - number_2 == answer:
            return True
        else:
            return False
    if operator=="*":
        if number_1 * number_2 == answer:
            return True
        else:
            return False
    if operator == "/":
        if number_2 == 0:
            if answer == "undefined":
                return True
            else:
                return False
        elif number_1//number_2==answer:
            return True
        else:
            return False
        
