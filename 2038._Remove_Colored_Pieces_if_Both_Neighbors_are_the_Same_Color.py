class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        player = "Alice"
        l_colors = list(colors)
        running = True
        while running:
            found_move = False
            for i in range(1, len(l_colors) - 1):
                if player[0] == l_colors[i] and l_colors[i - 1] == l_colors[i + 1] and l_colors[i] == l_colors[i + 1]:
                    l_colors.pop(i)
                    found_move = True
                    break

            if not found_move:
                running = False
                if player == "Alice":
                    return False
                else:
                    return True

            player = "Alice" if player == "Bob" else "Bob"

        return False
