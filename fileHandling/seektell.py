# Open a file in read mode
with open('example.txt', 'r') as file:
    # Read the first 10 characters
    data = file.read(10)
    print("Read:", data)

    # Get the current position
    position = file.tell()
    print("Current Position:", position)

    # Move the file pointer to the beginning
    file.seek(0)

    # Read the next 5 characters
    data = file.read(5)
    print("Read:", data)

    # Get the current position
    position = file.tell()
    print("Current Position:", position)
