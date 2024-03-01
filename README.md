## STEM Series: Stress testing

This script is like a fitness test for# CPU and Memory Stress Test

This script is a simple stress test for your computer. It's like a fitness test to see how well your computer performs under heavy tasks.

## How it works

1. **Importing necessary modules**: The script starts by importing necessary Python modules. These are like the tools the script needs to do its job.

2. **Setting the duration**: The `DURATION = 180` line sets how long the 'fitness test' should last, in seconds. So, 180 seconds means the test will last for 3 minutes.

3. **`get_usage()` function**: This function checks how hard the computer's brain (the CPU) and its memory are working at any given moment.

4. **`run_stress_test()` function**: This function is where the 'fitness test' happens. It makes the computer do some hard work, and uses our `get_usage` function to check the CPU and memory usage every second.

5. **`generate_report(usage_data)` function**: After the test, this function writes down all the measurements into a report (a .csv file), so you can look at them later.

6. **Running the test and generating the report**: The last two lines of the script actually start the test and then generate the report.

This script is a way to make your computer do some hard work for a set amount of time, and then write down how hard its CPU and memory were working during that time. It's a good way to see how well your computer can handle heavy tasks!
