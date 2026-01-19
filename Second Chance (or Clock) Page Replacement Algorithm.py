def find_and_update(x, arr, second_chance, frames):
    for i in range(frames):
        if arr[i] == x:
            second_chance[i] = True
            return True
    return False

def replace_and_update(x, arr, second_chance, frames, pointer):
    while True:
        if not second_chance[pointer]:
            arr[pointer] = x
            return (pointer + 1) % frames
        second_chance[pointer] = False
        pointer = (pointer + 1) % frames

def print_hits_and_faults(reference_string, frames):
    pointer = 0
    pf = 0
    arr = [-1] * frames
    second_chance = [False] * frames
    str_list = reference_string.split()
    l = len(str_list)
    for i in range(l):
        x = int(str_list[i])
        if not find_and_update(x, arr, second_chance, frames):
            pointer = replace_and_update(x, arr, second_chance, frames, pointer)
            pf += 1
    print(f'Total page faults were {pf}')

# Driver code
reference_string = '0 4 1 4 2 4 3 4 2 4 0 4 1 4 2 4 3 4'
frames = 3
print_hits_and_faults(reference_string, frames)

reference_string = '2 5 10 1 2 2 6 9 1 2 10 2 6 1 2 1 6 9 5 1'
frames = 4
print_hits_and_faults(reference_string, frames)