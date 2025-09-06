def get_connections(vertex):
    if vertex in emoji_graph:
        return emoji_graph[vertex]

# create
emojis = ["👍", "❤️", "⭐", "🎉", "⚪"]
emoji_graph = {
    "👍": ["❤️", "🎉"],
    "❤️": ["👍", "🎉"],
    "⭐": ["🎉"],
    "🎉": ["👍", "❤️", "⭐", "⚪"],
    "⚪": ["🎉"]
}

# start
i = 0
while True:
    input("\npress enter :D")
    print("\033[H\033[J") # clear screen

    emoji = emojis[i]

    print("[👍 ❤️ ⭐ 🎉 ⚪]")
    print(emoji, "connected to", get_connections(emoji))

    i += 1