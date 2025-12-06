import input

def split_line(s):
    result = []
    for ch in s:
        if ch.isdigit():
            result.append(int(ch))
        else:
            result.append(None)
    return result

lists = input.input
lists = lists.split("\n")[1:-1]
numbers = [split_line(line) for line in lists[:-1]]
operators = lists[-1].split()

# print(numbers)
# print(operators)

def get_vertical_number(col):
    col_numbers = [numbers[i][col] for i in range(len(numbers))]
    valid_numbers = [n for n in col_numbers if n is not None]
    result = 0
    for n in valid_numbers:
        result = result * 10 + n
    return result

def is_seperator(col):
    return all(numbers[i][col] is None for i in range(len(numbers)))

def calc(nums, operator):
    if operator == '*':
        r = 1
        for n in nums:
            r *= n
    else:
        r = 0
        for n in nums:
            r += n
    return r

result = 0
operator_index = 0
temp_numbers = []

for i in range(len(numbers[0])):
    if is_seperator(i):
        result += calc(temp_numbers, operators[operator_index])
        temp_numbers = []
        operator_index += 1
    else:
        temp_numbers.append(get_vertical_number(i))

result += calc(temp_numbers, operators[operator_index])
print(result)