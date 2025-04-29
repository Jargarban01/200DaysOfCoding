#!/usr/bin/env python
# coding: utf-8

# timestamp,meter_id,energy_kwh,status
# 2025-04-29 08:00:00,M001,5.2,OK
# 2025-04-29 08:15:00,M001,5.8,OK
# 2025-04-29 08:00:00,M002,3.9,ERROR

# In[1]:


import os

# File name for smart meter data
filename = "smart_meter_data.txt"

# 1. Create initial smart meter data file (write mode)
def create_meter_data():
    with open(filename, 'w') as file:  # open: Create or overwrite file in write mode
        # write: Write header and sample data
        file.write("timestamp,meter_id,energy_kwh,status\n")
        file.write("2025-04-29 08:00:00,M001,5.2,OK\n")
        file.write("2025-04-29 08:15:00,M001,5.8,OK\n")
        file.write("2025-04-29 08:00:00,M002,3.9,ERROR\n")
        file.flush()  # flush: Ensure data is written to disk
    print(f"Created {filename}")

# 2. Read entire file content (read mode)
def read_full_file():
    with open(filename, 'r') as file:  # open: Open file in read mode
        content = file.read()  # read: Read entire file as a string
        print("\nFull file content:")
        print(content)
        return content

# 3. Read file line by line (readline)
def read_line_by_line():
    with open(filename, 'r') as file:
        print("\nReading line by line:")
        while True:
            line = file.readline()  # readline: Read one line at a time
            if not line:  # Break at end of file
                break
            print(line.strip())
        return file.tell()  # tell: Get current file position

# 4. Read all lines into a list (readlines)
def read_all_lines():
    with open(filename, 'r') as file:
        lines = file.readlines()  # readlines: Read all lines into a list
        print("\nAll lines as list:")
        for line in lines:
            print(line.strip())
        return lines

# 5. Append new meter reading (append mode)
def append_new_reading():
    new_reading = "2025-04-29 08:30:00,M001,6.1,OK\n"
    with open(filename, 'a') as file:  # open: Open in append mode
        file.write(new_reading)  # write: Append new data
        file.flush()  # flush: Ensure appended data is written
    print(f"\nAppended new reading: {new_reading.strip()}")

# 6. Update a specific line using seek (read/write mode)
def update_reading():
    with open(filename, 'r+') as file:  # open: Open in read/write mode
        lines = file.readlines()
        for i, line in enumerate(lines):
            if "M002,3.9,ERROR" in line:
                file.seek(0)  # seek: Move cursor to start
                lines[i] = line.replace("3.9,ERROR", "4.0,OK")  # Update line
                file.writelines(lines)  # writelines: Write updated lines
                file.truncate()  # truncate: Remove any remaining content
                print(f"\nUpdated M002 reading to 4.0,OK")
                break

# 7. Demonstrate file position and manual close
def demonstrate_position_and_close():
    file = open(filename, 'r')  # open: Manual open
    print(f"\nInitial file position: {file.tell()}")
    first_line = file.readline()
    print(f"Position after reading first line: {file.tell()}")
    file.seek(0)  # seek: Move back to start
    print(f"Position after seek(0): {file.tell()}")
    file.close()  # close: Manually close file
    print("File closed")

# Main execution
if __name__ == "__main__":
    # Create initial file
    create_meter_data()
    
    # Read full file
    read_full_file()
    
    # Read line by line and show position
    final_position = read_line_by_line()
    print(f"Final file position: {final_position}")
    
    # Read all lines
    read_all_lines()
    
    # Append new reading
    append_new_reading()
    
    # Update a reading
    update_reading()
    
    # Demonstrate position and manual close
    demonstrate_position_and_close()
    
    # Verify final file content
    print("\nFinal file content:")
    with open(filename, 'r') as file:
        print(file.read())


# In[ ]:




