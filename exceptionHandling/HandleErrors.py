def calculate_expenditure(list_of_expenditure):
    total = 0
    try:
        for expenditure in list_of_expenditure:
            total += expenditure
        print("Total:", total)
        avg = total/num_values
        print("Average:", avg)
    except ZeroDivisionError:
        print("Divide by Zero error")
    except TypeError:
        print("Wrong data type")
    except:
        print("Some error occured")

    print("Thank-you visit again!!")

# list_of_values = [100, 200, 300, "400", 500]
list_of_values = [100, 200, 300, 400, 500]
# num_values = 0
num_values = 2
calculate_expenditure(list_of_values)


# Note: 
# Default except block is the one without any type mentioned.

# If an error occurs and the matching except block is found, then that is executed.

# If an error occurs and the matching except block is not found, it executes the default except block.

# If an error occurs and the matching except block is not found and if the default except block is also not found, the code crashes.

# The default except block, if present should be the last except block, otherwise it will result in a runtime error.