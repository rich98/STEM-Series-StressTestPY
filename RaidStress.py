import subprocess
import os

def test_raid():
    # Define the path to your RAID array
    raid_path = "/path/to/your/raid"
    test_file = os.path.join(raid_path, "testfile")

    # Define the size of the file you want to write in bytes
    file_size = 1024 * 1024 * 1024  # 1 GB

    # Write to the RAID
    write_cmd = f"dd if=/dev/zero of={test_file} bs=1M count={file_size} conv=fdatasync"
    write_process = subprocess.Popen(write_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    write_stdout, write_stderr = write_process.communicate()

    # Read from the RAID
    read_cmd = f"dd if={test_file} of=/dev/null bs=1M count={file_size}"
    read_process = subprocess.Popen(read_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    read_stdout, read_stderr = read_process.communicate()

    # Remove the test file
    os.remove(test_file)

    return write_stderr, read_stderr

write_speed, read_speed = test_raid()
print(f"Write speed: {write_speed}")
print(f"Read speed: {read_speed}")
