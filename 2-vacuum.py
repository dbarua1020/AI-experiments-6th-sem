import numpy as np

def generate_random_array(m, n):
    return np.random.randint(2, size=(m, n))

def clean_dirt(array, pos):
    if array[pos] == 1:
        print("Cleaning dirt at position:", pos)
        array[pos] = 0
    else:
        print("No dirt at position:", pos)

def is_valid_move(array, pos, direction):
    m, n = array.shape
    if direction == 0:  # left
        return pos[1] > 0
    elif direction == 1:  # right
        return pos[1] < n - 1
    elif direction == 2:  # up
        return pos[0] > 0
    elif direction == 3:  # down
        return pos[0] < m - 1

def move(pos, direction):
    if direction == 0:  # left
        return (pos[0], pos[1] - 1)
    elif direction == 1:  # right
        return (pos[0], pos[1] + 1)
    elif direction == 2:  # up
        return (pos[0] - 1, pos[1])
    elif direction == 3:  # down
        return (pos[0] + 1, pos[1])

def display_array(array):
    print(array)

def clean_array(array):
    m, n = array.shape
    total_dirt = np.sum(array)
    cleaned_dirt = 0
    pos = (np.random.randint(m), np.random.randint(n))

    print("Initial array:")
    display_array(array)

    while cleaned_dirt < total_dirt:
        clean_dirt(array, pos)
        cleaned_dirt += array[pos[0], pos[1]]
        array[pos[0], pos[1]] = 0
        display_array(array)

        direction = np.random.randint(4)
        while not is_valid_move(array, pos, direction):
            direction = np.random.randint(4)

        pos = move(pos, direction)

m = int(input("Enter the number of rows (m): "))
n = int(input("Enter the number of columns (n): "))

array = generate_random_array(m, n)
clean_array(array)
