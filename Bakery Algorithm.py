import threading
import time

THREAD_COUNT = 8

# Shared variables (Bakery Algorithm)
tickets = [0] * THREAD_COUNT
choosing = [0] * THREAD_COUNT

resource = 0
resource_lock = threading.Lock()  # শুধু print consistency এর জন্য

def lock(thread_id):
    global tickets, choosing

    # choosing ticket
    choosing[thread_id] = 1

    max_ticket = 0
    for i in range(THREAD_COUNT):
        if tickets[i] > max_ticket:
            max_ticket = tickets[i]

    tickets[thread_id] = max_ticket + 1
    choosing[thread_id] = 0

    # Entry section
    for other in range(THREAD_COUNT):
        # wait while other is choosing
        while choosing[other]:
            pass

        # bakery condition
        while (tickets[other] != 0 and
               (tickets[other] < tickets[thread_id] or
                (tickets[other] == tickets[thread_id] and other < thread_id))):
            pass


def unlock(thread_id):
    tickets[thread_id] = 0


def use_resource(thread_id):
    global resource

    with resource_lock:
        if resource != 0:
            print(f"Resource was acquired by {thread_id}, but still in use by {resource}")

        resource = thread_id
        print(f"{thread_id} using resource...")

    time.sleep(2)

    with resource_lock:
        resource = 0


def thread_body(thread_id):
    lock(thread_id)
    use_resource(thread_id)
    unlock(thread_id)


def main():
    threads = []

    for i in range(THREAD_COUNT):
        t = threading.Thread(target=thread_body, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


if __name__ == "__main__":
    main()
