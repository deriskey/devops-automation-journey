# placeholder variable to count errors
error_counter = 0

#open log file 
with open("server.log", "r") as file:

    #Loop throught filr line by line
    for line in file:

        #Check if word [ERROR] exists in current line
        if "[ERROR]" in line:
            print("Alert!!! Found an Error Line:")
            print(line.strip()) #.strip() removes annoying blank spaces

            #Increase our error count by 1
            error_counter = error_counter + 1

#After checking all lines, print the final DevOps Summary report
print("==============================")
print(f"Scan complter. Total erorrs found: {error_counter}")
print("==============================")