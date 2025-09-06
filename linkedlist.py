class Node:
    def __init__(self, data):
        self.data = data  # the emoji
        self.next = None  # the pointer to the next emoji

# create
star = Node("⭐")
heart = Node("❤️")
circle = Node("⚪")

star.next = heart  # ⭐ -> ❤️
heart.next = circle  # ❤️ -> ⚪
circle.next = star  # ⚪ -> ⭐

# start
current_node = star
while True:
    input("\npress enter :D")
    print("\033[H\033[J") # clear screen

    print("[⭐ ❤️ ⚪]")
    print("Current:", current_node.data)
    print("Next:", current_node.next.data)

    current_node = current_node.next