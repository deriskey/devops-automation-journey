# placeholder variable to count errors
error_counter = 0

#open log file 
with open("server.log", "r") as file:

    #Loop throught filr line by line
    for line in file:
        #Convert currnet line to all lowercase char
        lowercase_line = line.lower()

        #Check if word [ERROR] exists in current line
        if "error" in lowercase_line:
            print("Alert!!! Found an Error Line:")
            print(line.strip()) #.strip() removes annoying blank spaces

            #Increase our error count by 1
            error_counter = error_counter + 1

#After checking all lines, print the final DevOps Summary report
print("==============================")
print(f"Scan complter. Total erorrs found: {error_counter}")
print("==============================")