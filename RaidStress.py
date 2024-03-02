import subprocess
import os

def test_raid():
    # Define the path to your RAID array
    raid_path = "/data"
    test_file = os.path.join(raid_path, "testfile")

    # Define the size of the file you want to write in bytes
    file_size = 1024 * 1024 * 1024  # 1 GB

    # Write to the RAID
    write_cmd = f"dd if=/dev/zero of={test_file} bs=1M count={file_size} conv=fdatasync"
    write_process = subprocess.Popen(write_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    write_stdout, write_stderr = write_process.communicate()

    # Check if the write command was successful
    if write_process.returncode != 0:
        print(f"Write command failed with error: {write_stderr}")
        return write_stderr, None

    # Read from the RAID
    read_cmd = f"dd if={test_file} of=/dev/null bs=1M count={file_size}"
    read_process = subprocess.Popen(read_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    read_stdout, read_stderr = read_process.communicate()

    # Check if the read command was successful
    if read_process.returncode != 0:
        print(f"Read command failed with error: {read_stderr}")
        return write_stderr, read_stderr

    # Check if the file exists before trying to remove it
    if os.path.exists(test_file):
        # Remove the test file
        try:
            os.remove(test_file)
        except FileNotFoundError:
            print(f"The file {test_file} does not exist.")
    else:
        print(f"The file {test_file} does not exist.")

    return write_stderr, read_stderr

write_speed, read_speed = test_raid()
print(f"Write speed: {write_speed}")
print(f"Read speed: {read_speed}")


