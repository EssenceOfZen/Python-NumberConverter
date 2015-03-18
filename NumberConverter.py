# =========================================================================
# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  NumberConverter.py by ZenOokami 
#  
#  Copyright 2015 Essence Of Zen
#  www.EssenceOfZen.org
# =========================================================================

# ==Global Variables== #
version = "0.3.5"
dev_team = ["ZenOokami"]
last_updated = "March 15th, 2015"


def mode_menu():
    print("#===========================================#")
    print("#Menu Under Construction for Later Update   #")
    print("#===========================================#")

# -------------------------
def decimalBinaryMenu():
    switch = 1
    while (switch == 1):
        number = int(input("Plase input a decimal number to convert: "))
        decimalToBinaryConvert(number)  # Call our function
        print()
        question = 1
        while (question == 1):
            user_response = input("Convert again? ").lower()
            if (user_response == "yes" or user_response == "y"):
                question = 0  #Turn off 2nd loop
                switch = 1
                #print("yes "+ str(question)) #Testing
            elif (user_response == "no" or user_response == "n"):
                question = 0  #Turn off 2nd loop
                switch = 0
                #print("no "+ str(question) + str(switch)) #Testing
            else:
                print("invalid response")
                question = 1  #Keep 2nd loop on
                switch = 1  #Keep 1st loop on


def decimalToBinaryConvert(number):
    binary_list = []  # We create an empty list ahead of time.
    original_number = number  # For reference
    binary_number = ''
    while (number > .5):  # We setup our loop to finish out an entire conversion.
        if number % 2 != 0:  # If a number/2 = a number and 1/2
            binary_list.append(1)
        else:
            binary_list.append(0)  # If a number is a whole number.
        number /= 2  #  Divide the starting nubmer by 2
        number = int(number)  # Get rid of the .5 if there is one.
        #print(binary_list) # Check to see if it's working

    print("The Binary form for " + str(original_number) + " is: ")
    final_binary = binary_list[::-1]
    #print(binary_list[::-1]) # Print the binary list backwards to show correctly.
    print(final_binary)
    return final_binary
# --------------------------------------

# --------------------------------------
def binaryDecimalMenu():
    switch = 1
    while (switch == 1):
        binary = []

        number = input("Plase input a binary number to convert: ")  #Input a binary number (string)
        #Take said input and add it to a list after turning them into actual numbers
        for item in number:
            binary.append(int(item))
        print("Binary number is " + str(binary))  #Testing
        print()

        #call the function
        decimal = binaryToDecimalConvert(binary)

        print("Decimal number is: " + str(decimal))
        print()

        question = 1
        while (question == 1):
            user_response = input("Convert again? ").lower()
            if (user_response == "yes" or user_response == "y"):
                #print("yep")
                question = 0
                switch = 1
            elif (user_response == "no" or user_response == "n"):
                print("nope")
                question = 0
                switch = 0
            else:
                print("Invalid response, try again")
                question = 1
                switch = 1



def binaryToDecimalConvert(array):  # we feed in an array
    decimal = 0
    power = len(array) - 1
    # print()
    # print(array)
    # print()

    for item in array:
        # print("power is: " + str(power))
        # print(decimal)
        # print("Current item: " + str(item))

        decimal += (2 ** power) * item
        power -= 1

    # print("Decimal number is: " + str(decimal))

    return decimal


# --------------------------------------

# --------------------------------------
def hexBinaryMenu():
    pass

def hexToBinary(hex_number):
    pass
# --------------------------------------

# --------------------------------------
def binaryHexMenu():
    switch = 1
    while (switch == 1):
        binary = []

        number = input("Plase input a binary number to convert: ")  #Input a binary number (string)
        #Take said input and add it to a list after turning them into actual numbers
        for item in number:
            binary.append(int(item))
        print("Binary number is " + str(binary))  #Testing
        print()

        #call the function
        hex_number = binaryToHexConvert(binary)


        print("Hex number is: " + hex_number)
        print()

        question = 1
        while (question == 1):
            user_response = input("Convert again? ").lower()
            if (user_response == "yes" or user_response == "y"):
                #print("yep")
                question = 0
                switch = 1
            elif (user_response == "no" or user_response == "n"):
                print("nope")
                question = 0
                switch = 0
            else:
                print("Invalid response, try again")
                question = 1
                switch = 1


def binaryToHexConvert(array):
    hex_number = ''
    number_holder = [] # will hold 4 bits, and convert them to decimal, then pass that to hex_number
    decimal_set = []

    # Check the length of the array, see if it's a set of 4s, if not add how many 0s needed to balance it out.
    if ((len(array) % 4) == 1): # If modulo = 1, then it's missing 3 items
        for index in range(0,3): # Add 3 items
            array.insert(0,0)
    elif ((len(array) % 4) == 2): # Missing 2 items
        for index in range(0,2): #add 2 items
            array.insert(0,0)
    elif ((len(array) % 4) == 3): # Missing 1 item
        for index in range(0,1): #add 1 item
            array.insert(0,0)

    # Once we've taken care of the length, we have to add a check to see if array is empty,
    while(len(array) != 0): # while not empty
        for index in range (0,4):
            number_holder.append(array.pop(0)) #Grab the 4 far left items from array

        decimal_set.append(binaryToDecimalConvert(number_holder)) # Converts 4 bits into decimal
        number_holder = [] #Make sure holder is empty

    # Once array is empty, convert all portions of decimal set into hex and add it to the hex_number
    for index in decimal_set:
        if (index == 10):
            hex_number += "A"
        elif (index == 11):
            hex_number += "B"
        elif (index == 12):
            hex_number += "C"
        elif (index == 13):
            hex_number += "D"
        elif (index == 14):
            hex_number += "E"
        elif (index == 15):
            hex_number += "F"
        else:
            hex_number += str(index)

    return hex_number
# --------------------------------------







# --------------------------------------

def main():
    print("Welcome to EoZ's number converter!")
    switch = 1
    while (switch == 1):
        print("0.)Quit | 1.) Decimal to Binary | 2.) Binary to Decimal | 3.) Binary to Hex")
        print()
        user_choice = int(input("Please choose option: "))
        if (user_choice == 1):
            decimalBinaryMenu()

        elif (user_choice == 2):
            binaryDecimalMenu()

        elif (user_choice == 3):
            binaryHexMenu()

        elif (user_choice == 0):
            switch = 0
        else:
            print("Invalid input, try again")
            switch = 1

        user_choice = input("Are you finished?: ").lower()
        if (user_choice == "yes" or "y"):
            switch = 0
        elif (user_choice == "no" or "n"):
            switch = 1
        else:
            print("Invalid response, try again")

    print("Thank you for using our program")
    print("version: " + str(version))
    print("Last Update: " + last_updated)


main()
		
