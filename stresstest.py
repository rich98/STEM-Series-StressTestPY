import os
import time
import psutil
import subprocess

# Define the stress test duration in seconds
DURATION = 180

# Get the current CPU and memory usage
def get_usage():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    return cpu_usage, memory_usage

# Run the stress test
def run_stress_test():
    # Start the stress test
    stress = subprocess.Popen(['stress', '--cpu', '75', '--vm', '2', '--vm-bytes', '1024M', '--timeout', f'{DURATION}s'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Monitor the CPU and memory usage
    start_time = time.time()
    usage_data = []
    while time.time() - start_time < DURATION:
        cpu_usage, memory_usage = get_usage()
        usage_data.append((time.time(), cpu_usage, memory_usage))
        time.sleep(1)

    # Wait for the stress test to finish
    stress.communicate()

    return usage_data

# Generate a report of the stress test
def generate_report(usage_data):
    report = 'Time,CPU Usage,Memory Usage\n'
    for timestamp, cpu_usage, memory_usage in usage_data:
        report += f'{timestamp},{cpu_usage},{memory_usage}\n'
    with open('report.csv', 'w') as f:
        f.write(report)

# Run the stress test and generate a report
usage_data = run_stress_test()
generate_report(usage_data)

