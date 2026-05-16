# Upgrade of Producer-Consumer program from Multithreading/03-Producer-Consumer.py

import threading
import queue
import time
import random

q = queue.Queue()

def producer():

    for i in range(10):

        item = f"Task-{i}"

        print(f"[Produced] {item}")

        q.put(item)

        time.sleep(0.5)

def consumer(name):

    while True:

        item = q.get()

        print(f"[{name}] processing {item}")

        time.sleep(random.uniform(1, 3))
        
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
    
    num_of_consumers = get_int("Enter the number of consumers: ")
    
    consumer_threads = []

    for i in range(num_of_consumers):

        consumer_thread = threading.Thread(target=consumer,
                                           args=(f"Consumer-{i+1}",),
                                           daemon=True)
        
        consumer_thread.start()
        consumer_threads.append(consumer_thread)

    producer_thread = threading.Thread(
        target=producer,)

    producer_thread.start()
    producer_thread.join()

    q.join()

    print("\nAll tasks completed")

if __name__ == "__main__":
    main()