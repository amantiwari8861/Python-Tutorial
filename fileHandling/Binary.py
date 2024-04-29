# Reading Binary File
with open('binary_file.bin', 'rb') as file:
    binary_data = file.read()
    # Process the binary data
    print("Binary Data Read:", binary_data)

# Writing Binary File
binary_data_to_write = b'\x48\x65\x6C\x6C\x6F\x20\x57\x6F\x72\x6C\x64'  # Example binary data
with open('binary_file.bin', 'wb') as file:
    file.write(binary_data_to_write)
    print("Binary Data Written Successfully.")

# Appending Binary File
binary_data_to_append = b'\x57\x6F\x72\x6C\x64'  # Example binary data to append
with open('binary_file.bin', 'ab') as file:
    file.write(binary_data_to_append)
    print("Binary Data Appended Successfully.")
