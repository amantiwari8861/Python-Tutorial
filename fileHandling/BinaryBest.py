# Open the file in 'a+' mode to read and append
with open('file.txt', 'a+') as file:
    # Read the existing contents of the file
    file.seek(0)  # Move the file pointer to the beginning of the file
    contents = file.read()
    print("Existing Contents:", contents)

    # Append new data to the file
    file.write("\nNew data to append")
    print("New data appended successfully.")

    # Move the file pointer to the beginning of the file again
    file.seek(0)
    # Read the updated contents of the file
    updated_contents = file.read()
    print("Updated Contents:", updated_contents)
