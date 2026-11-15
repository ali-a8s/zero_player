import time
import random
import os
import msvcrt


def draw(world, w, h, round_count, percentage, alive_cells, speed):
    """display the current state and information of the game."""

    print("*** GAME OF LIFE ***\n")

    print(f"density {percentage * 100} % | speed {speed} seconds")
    print(f"generation {round_count} | alive {alive_cells}\n")

    print("+" + "-" * w + "+")

    for y in range(h):
        print("|", end="")

        for x in range(w):
            print("+" if world[y][x] else " ", end="")

        print("|")

    print("+" + "-" * w + "+")

    print("\n[r] restart [Space] pause/resume [Esc] quit ")


def evolution(world, w, h):
    """calculate the next generation of cells."""

    # a new empty world for the next generation
    new_world = [[0] * w for _ in range(h)]

    for x in range(w):
        for y in range(h):
            lives = 0

            # count the live neighbors around the current cell
            for xd in range(x - 1, x + 2):
                for yd in range(y - 1, y + 2):
                    # wrap around the edges of the world
                    if world[(yd + h) % h][(xd + w) % w]:
                        lives += 1

            # exclude the current cell
            if world[y][x]:
                lives -= 1

            # apply rules
            if lives == 3:
                new_world[y][x] = 1
            elif lives == 2 and world[y][x] == 1:
                new_world[y][x] = 1
            else:
                new_world[y][x] = 0

    return new_world


def count_alive_cells(world, w, h):
    """count the number of living cells."""

    total = 0

    for y in range(h):
        for x in range(w):
            if world[y][x]:
                total += 1

    return total


def create_world(w, h, percentage):
    """generate the initial world"""
    return [[1 if random.random() < percentage else 0
            for _ in range(w)] for _ in range(h)]
    

def main():
    # get game settings
    w = int(input("Width: "))
    h = int(input("Height: "))
    percentage = float(input("initial live cell density (0.0 - 1.0): "))
    speed = float(input("speed of evolution (in second): "))

    world = create_world(w, h, percentage)
    round_count = 1
    paused = False

    while True:
        # keyboard input
        if msvcrt.kbhit():
            key_stroke = msvcrt.getch()

            if key_stroke == b'\x1b':  # Esc
                break
            elif key_stroke == b' ':  # Space
                paused = not paused
            elif key_stroke.lower() == b'r': # for restart
                world = create_world(w, h, percentage)
                round_count = 1
                paused = False

        os.system('cls')

        alive_cells = count_alive_cells(world, w, h)
        draw(world, w, h, round_count, percentage, alive_cells, speed, paused)

        # pausing game
        if paused:
            print("\n*** PAUSED ***")
            time.sleep(0.5)
            continue

        # next generation
        world = evolution(world, w, h)
        round_count += 1

        time.sleep(speed)


if __name__ == "__main__":
    main()