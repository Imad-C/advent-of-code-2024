import re

def calculate_muls(text):
    # matches for "mul(XXX,XXX)" where X is 0-9
    pattern = re.compile(r'mul\([0-9]{1,3},[0-9]{1,3}\)') 
    matches = pattern.findall(text)

    result = 0
    for match in matches:
        numbers = match.split('(')[1][:-1]
        x = int(numbers.split(',')[0])
        y = int(numbers.split(',')[1])
        result += x*y

    return result


with open("day_3/input.txt", "r") as f:
    file_contents = f.read()

## Task 1
print(f'Task 1: {calculate_muls(file_contents)}') # 165225049

## Task 2
# matches for "do()" or "don't()"
pattern = re.compile(r'(do\(\)|don\'t\(\))') 
matches = pattern.finditer(file_contents)

do_string = ''
last_do_idx = 0
currently_do = True

# generate a new string to process, containing only "do()" text
for match in matches:
    match_string = match.group(0)

    if match_string == "don't()":
        if currently_do:
            do_string += file_contents[last_do_idx:match.start()]
            currently_do = False
        else:
            continue

    else: # match_string == "do()"
        if currently_do:
            continue
        else:
            last_do_idx = match.end() 
            currently_do = True

# capture last do (which is missed in case of ending in "do()")
if currently_do:
    do_string += file_contents[last_do_idx:]

print(f'Task 2: {calculate_muls(do_string)}') # 108830766