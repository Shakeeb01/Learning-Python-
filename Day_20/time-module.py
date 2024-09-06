# The time module in Python provides various functions to manipulate and work with time-related tasks such as measuring execution time, pausing execution, or converting time formats.
import time
print(time.ctime())  # Prints current time in a human-readable form


# Converts seconds since the Epoch to a struct_time in local time. If no argument is provided, it uses the current time.
local_time = time.localtime()
print(local_time)


# Formats a struct_time into a string as specified by the format string.
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(formatted_time)


# Returns the value of a high-resolution timer useful for measuring the performance of code.

start = time.perf_counter()
# Some code execution
end = time.perf_counter()
print(f"Execution time: {end - start} seconds")


