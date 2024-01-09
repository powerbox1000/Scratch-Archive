# This is the greeting.
print \
"""
Emerald 0.1
By Magnie
"""

commands = ["print","run","end","ask"] # Commands that you can type
encode = [] # for print and ask commands
encode2 = [] # for Variables
onOrOff = "off" # I switch I never really knew what to call it.
line = 0 # Just shows what line the Programming Language is accessing on the program
i = 0 # Another switch
program = [] # Where all the commands will be put.

# Start
while i != 1:
    while onOrOff == "off": # Add commands here
        command = raw_input("Type in a command: ")
        command.lower()
        if command != "run":
            if command == commands[0]: # Checks to see if it is print.
                recode = raw_input("What should your program print? ") # Allows you type type what you want for it to print.
                encode.append(recode)
                program.append(command)
                encode2.append(None)
            if command == commands[2]: # Checks to see if it's end.
                onOrOff = None # Makes it so you can't add a command and makes it so you can't run the program allowing it to close.
                i = 1 # Disables the whole script
            if command == commands[3]: # Checks to see if the command is Ask.
                recode = raw_input("What should you ask them? ") # Allows you to type what the 'question' is.
                encode.append(recode)
                program.append(command)
                encode2.append(None)
        else: # If it is run.
            onOrOff = "on" # Makes the program run.
            print "\n\n"
    while line != len(program): # As long as 'line' is less than the length of the program it will run the program.
        if program[line] == commands[0]: # If it is 'print'
            print encode[line] # Print what was typed in.
            line += 1
        elif program[line] == commands[3]: # If it is 'ask'
            raw_input(encode[line]) # Ask so and so then allows the user to type.
            line += 1
        else:
            print "There seems to be something wrong with either your programming or my programming"
    onOrOff = "off" # Go back to adding commands mode.
    print "\n\n"
    line = 0
