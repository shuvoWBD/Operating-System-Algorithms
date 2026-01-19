import threading
import time

N = 2
flag = [False] * N
turn = 0

def process(id):
    other = 1 - id
    while True:
        # Entry Section
        flag[id] = True         # Express intent to enter
        global turn
        turn = other            # Give priority to the other process
        while flag[other] and turn == other:
            # Busy wait until it’s safe to enter
            pass

        # Critical Section
        print(f'Process {id} is in critical section')

        # Exit Section
        flag[id] = False

        # Remainder Section
        print(f'Process {id} is in remainder section')

if __name__ == '__main__':
    t1 = threading.Thread(target=process, args=(0,))
    t2 = threading.Thread(target=process, args=(1,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()