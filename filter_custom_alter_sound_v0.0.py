import re


with open('old.filter', 'rt') as f:
    all_lines = f.readlines()

new_lines = []
pattern1 = r"\sPlayAlertSound\s\d\s\d{3}"
pattern2 = r"\sPlayAlertSound\s\d{2}\s\d{3}"

for line in all_lines:
    if re.match(pattern1, line):
        ## sound number start from 16th letter.
        ## Notice the number is not integer.
        if line[16] == "1":
            new_line = line.replace(
                line, "\tCustomAlertSound \"AlertSound_01.wav\"\n")
            new_lines.append(new_line)
        elif line[16] == "2":
            new_line = line.replace(
                line, "\tCustomAlertSound \"AlertSound_02.wav\"\n")
            new_lines.append(new_line)
        elif line[16] == "3":
            new_line = line.replace(
                line, "\tCustomAlertSound \"AlertSound_03.wav\"\n")
        elif line[16] == "4":
            new_lines.append(new_line)
            new_line = line.replace(
                line, "\tCustomAlertSound \"AlertSound_04.wav\"\n")
            new_lines.append(new_line)
        elif line[16] == "5":
            new_line = line.replace(
                line, "\tCustomAlertSound \"AlertSound_05.wav\"\n")
            new_lines.append(new_line)
        elif line[16] == "6":
            new_line = line.replace(
                line, "\tCustomAlertSound \"AlertSound_06.wav\"\n")
            new_lines.append(new_line)
    elif re.match(pattern2, line):
        # j += 1
        if line[16:17] == "12":
            new_line = line.replace(
                line, "\tCustomAlertSound \"AlertSound_12.wav\"\n")
            new_lines.append(new_line)
    else:
        new_lines.append(line)

with open("new.filter", "wt") as new_filter:
    new_filter.writelines(new_lines)

print("New filter has been generated.")
