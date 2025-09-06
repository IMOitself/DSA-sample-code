
import random

emojis = ["⭐", "❤️", "⚪"]

print(emojis)
while True:
    print("\nenter 1 to push")
    print("just enter to pop")
    choice = input()
    print("\033[H\033[J") # clear screen

    if choice == "1":
        emojis.append(random.choice(["👍", "❤️", "⭐", "🎉", "⚪"]))
    else:
        emojis.pop()
    
    print(emojis)
    print()

