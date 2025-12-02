import input

# lists = input.sample
lists = input.input
lists = lists.split(",")

result = 0
ranges = [a.split("-")  for a in lists] #[[int(id[0]), int(id[1])] for id in [a.split("-")  for a in lists]]

def next_invalid_id_half(id):
    if len(id) % 2 == 0:
        left = int(id[:len(id)//2])
        right = int(id[len(id)//2:])
        if left >= right: return left
        else: return left + 1
    return 10 ** (len(id)//2)

def last_invalid_id_half(id):
    if len(id) % 2 == 0:
        left = int(id[:len(id)//2])
        right = int(id[len(id)//2:])
        if left <= right: return left
        else: return left - 1
    return 10 ** (len(id)//2) - 1

for r in ranges:
    min = next_invalid_id_half(r[0])
    max = last_invalid_id_half(r[1])
    while min <= max:
        result += min * (10 ** len(str(min))) + min
        min += 1

print(result)

