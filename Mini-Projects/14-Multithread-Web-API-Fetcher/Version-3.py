# Added execution time measurement and error handling for network issues and invalid pokemon names.

import requests
import threading
import time

base_url = "https://pokeapi.co/api/v2/"
print_lock = threading.Lock()

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"

    try:
        response = requests.get(url, timeout = 5) # This method is gonna return a response object,   
                                                  # Timeout = 5 --> Wait at most 5 seconds for the server response.
        if response.status_code == 200:           # Our response object does have a attribute of status_code
            return response.json()
        else:
            with print_lock:
                print(f"Pokemon '{name}' not found!")
                print("-" * 20)

    except requests.exceptions.Timeout:
        with print_lock:
            print("The reqest took too long!")

    except requests.exceptions.RequestException as e:
        with print_lock:
            print(f"Error: {e}")

def display_pokemon_info(name):

    info = get_pokemon_info(name)
    
    if info:
        with print_lock:

            print(f"Name: {info['name']}")
            print(f"Height: {info['height']}")
            print(f"Weight: {info['weight']}")
            print(f"Type: {[t['type']['name'] for t in info['types']]}")
            print("-" * 20)

def main():
   
    pokemon_names = input("Enter pokemon names (comma separated): ").lower().split(",")
    
    start_time = time.perf_counter()
    
    threads = []

    for name in pokemon_names:
        thread = threading.Thread(target=display_pokemon_info, args=(name.strip(),))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    end_time = time.perf_counter()
    print(f"Time taken: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()