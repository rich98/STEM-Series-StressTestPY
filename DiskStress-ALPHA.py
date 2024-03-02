def disk_write_read_test(path, data):
    # Write data to the file
    with open(path, 'wb') as f:
        f.write(data)

    # Read data from the file
    with open(path, 'rb') as f:
        read_data = f.read()

    # Verify if the written data is the same as the read data
    if data == read_data:
        print('Disk write-read test passed.')
    else:
        print('Disk write-read test failed.')

def create_large_file(path, size_in_gb):
    # Convert size to bytes
    size_in_bytes = size_in_gb * (1024 ** 3)

    # Create a file of the specified size
    with open(path, 'wb') as f:
        f.write(b'\0' * size_in_bytes)

    # Call the disk_write_read_test function to verify the file
    disk_write_read_test(path, b'\0' * size_in_bytes)

# Specify the path where the file will be created
path = '/data/large_file.txt'  # Replace with your actual path

# Call the function
create_large_file(path, 2)
