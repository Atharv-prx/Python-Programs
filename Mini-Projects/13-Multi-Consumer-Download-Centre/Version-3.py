# Added consumer shutdown using sentinel values

import threading
import queue
import time
import random

q = queue.Queue()

print_lock = threading.Lock()


def producer(num_of_consumers):

    for i in range(10):

        item = f"Task-{i}"

        with print_lock:
            print(f"[Produced] {item}")

        q.put(item)

        time.sleep(0.5)

    # Sentinel values to stop consumers
    for _ in range(num_of_consumers):
        q.put(None)


def consumer(name):

    while True:

        item = q.get()

        # Stop signal
        if item is None:

            with print_lock:
                print(f"[{name}] shutting down...")

            q.task_done()

            break

        with print_lock:
            print(f"[{name}] processing {item}")
            print(f"Queue size: {q.qsize()}")

        time.sleep(random.uniform(1, 3))

        with print_lock:
            print(f"[{name}] finished {item}")

        q.task_done()


def get_int(prompt):

    while True:

        try:

            value = int(input(prompt))

            if value > 0:
                return value

            print("Enter a positive number.")

        except ValueError:
            print("Invalid input.")


def main():

    num_of_consumers = get_int(
        "Enter the number of consumers: "
    )

    consumer_threads = []

    # Start consumers first
    for i in range(num_of_consumers):

        consumer_thread = threading.Thread(
            target=consumer,
            args=(f"Consumer-{i+1}",)
        )

        consumer_thread.start()

        consumer_threads.append(consumer_thread)

    # Start producer
    producer_thread = threading.Thread(
        target=producer,
        args=(num_of_consumers,)
    )

    producer_thread.start()

    producer_thread.join()

    q.join()

    # Wait for all consumers to exit
    for thread in consumer_threads:
        thread.join()

    with print_lock:
        print("\nAll tasks completed successfully.")


if __name__ == "__main__":
    main()