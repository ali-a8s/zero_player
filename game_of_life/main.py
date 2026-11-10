import time 
import random
import os 
import sys


def clear_consol():
    if sys.platform.startswith('win'):
        os.system('cls')
    elif sys.platform.startswith('linux'):
        os.system('clear')
    elif sys.platform.startswith('darwin'):
        os.system('clear')
    else:
        print("unable to clear terminal.")


def draw(world, w, h, round_count, percentage, alive_cells, speed):
    clear_consol()

    print("*** GAME OF LIFE ***\n")

    print(f"initial live cell {percentage * 100} % | speed {speed} seconds")
    print(f"round {round_count} | alive cells {alive_cells}\n")

    print("+" + "-" * w + "+")

    for y in range(h):
        print("|", end="")

        for x in range(w):
            print("+" if world[y][x] else " ", end="")
        
        print("|") 

    print("+" + "-" * w + "+")


def evolution(world, w, h):
    new_world = [[0] * w for _ in range(h)]

    for x in range(w):
        for y in range(h):
            lives = 0 
            for xd in range(x - 1, x + 2):
                for yd in range(y - 1, y + 2):
                    if (world[(yd + h) % h][(xd + w) % w]):
                        lives += 1

            if (world[y][x]):
                lives -= 1

            if (lives == 3):
                new_world[y][x] = 1
            elif (lives == 2) and (world[y][x] == 1):
                new_world[y][x] = 1
            else:
                new_world[y][x] = 0

    for y in range(h):
        for x in range(w):
            world[y][x] = new_world[y][x]


def count_alive_cells(world, w, h):
    total = 0

    for y in range(h):
        for x in range(w):
            if (world[y][x]):
                total += 1

    return total


def main():
    w, h = 50, 20
    w = int(input("Width: "))
    h = int(input("Height: "))
    percentage = float(input("initial live cell density (0.0 - 1.0): "))
    speed = float(input("speed of evolution (in second): "))

    world = [[0] * w for _ in range(h)]
    round_count = 1

    for y in range(h):
        for x in range(w):
            world[y][x] = 1 if random.random() < percentage else 0

    while True:
        alive_cells = count_alive_cells(world, w, h)
        draw(world, w, h, round_count, percentage, alive_cells, speed)
        evolution(world, w, h)
        time.sleep(speed)
        round_count += 1

if __name__ == "__main__":
    main()