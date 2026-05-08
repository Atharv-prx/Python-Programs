import time

mytime = int(input("Enter a time in seconds"))

for x in range (mytime, 0, -1):
    seconds = x%60
    minutes = int(x/60)%60
    hours = int(x/3600) # Didn't add modulus here cuz we are not counting days
    print(f"{hours}:{minutes}:{seconds:02}")
    time.sleep(1)
print("Time's up")