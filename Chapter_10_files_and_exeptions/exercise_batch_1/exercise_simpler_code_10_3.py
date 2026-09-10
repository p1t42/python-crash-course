# 10-3. Simpler Code: The program file_reader.py in this section uses a temporary variable, lines, to show how splitlines() 
# works. You can skip the temporary variable and loop directly over the list that splitlines() returns:

# for line in contents.splitlines():

# Remove the temporary variable from each of the programs in this section, to make them more concise.

from pathlib import Path

path = Path("/Users/peterfedotovskii/Documents/python_crash_course/Chapter_10_files_and_exeptions/txt_files/pi_million_digits.txt")
contents = path.read_text()

pi_string = ''
for line in contents.splitlines():
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))