import os
import random
import time
import msvcrt  # for keyboard inputs on windows

# dimensions of the board
WIDTH = 30
HEIGHT = 15

def clear_screen():
    #clears the terminal screen 
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(snake, food, score):
    #draws the game board in the terminal

    for y in range(HEIGHT):
        for x in range(WIDTH):
            if y == 0 or y == HEIGHT -1 or x == 0 or x == WIDTH -1:
                print('#', end='')
            elif (y, x) == food:
                print('*', end='')
            elif (y, x) == snake[0]:
                print('@', end='')
            elif (y, x) in snake[1:]:
                print('O', end='')
            else:
                print(' ', end='')
        print()
    print(f"Score: {score}")

def get_key():
    """
    checks if a key is pressed 
    returns key code or nothing if no key is pressed 
    handles arrow keys 
    """
    if msvcrt.kbhit():
        key = msvcrt.getch()
        if key == b'\xe0':
            key2 = msvcrt.getch()
            return key2
        else:
            return key
    return None

def main():
    snake = [(7, 15), (7, 14), (7, 13)]
    direction = b'M'  # right arrow key 
    opposite = {b'M': b'K', b'K': b'M', b'H': b'P', b'P': b'H'}

    food = (random.randint(1, HEIGHT - 2), random.randint(1, WIDTH - 2))
    score = 0

    while True:
        clear_screen()
        print_board(snake, food, score)

        start_time = time.time()
        while time.time() - start_time < 0.1:  
            key = get_key()
            if key == b'\x1b':  # esc to quit
                print("Game Over!")
                print(f"Final Score: {score}")
                return
            if key in opposite and opposite[direction] != key:
                direction = key

        y, x = snake[0]
        if direction == b'H':  # up
            y -= 1
        elif direction == b'P':  # down
            y += 1
        elif direction == b'K':  # left
            x -= 1
        elif direction == b'M':  # right
            x += 1

        # wraps around the borders
        if y == 0:
            y = HEIGHT - 2
        elif y == HEIGHT -1:
            y = 1
        if x == 0:
            x = WIDTH - 2
        elif x == WIDTH -1:
            x = 1

        new_head = (y, x)
        if new_head in snake:
            clear_screen()
            print_board(snake, food, score)
            print("Game Over! You died.")
            print(f"Final Score: {score}")
            return

        snake.insert(0, new_head)

        if new_head == food:
            score += 1
            while True:
                food = (random.randint(1, HEIGHT - 2), random.randint(1, WIDTH - 2))
                if food not in snake:
                    break
        else:
            snake.pop()

if __name__ == "__main__":
    main()
