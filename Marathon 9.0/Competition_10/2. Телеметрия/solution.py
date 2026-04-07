import sys


def solve():
    n, m, k = map(int, sys.stdin.readline().split())
    windows = [""] * n
    clipboard = ""
    current_window_index = 0
    for _ in range(m):
        command = sys.stdin.readline().strip()
        if command == "Next":
            current_window_index = (current_window_index + 1) % n
        elif command == "Copy":
            current_text = windows[current_window_index]
            clipboard = current_text[-k:]
        elif command == "Paste":
            windows[current_window_index] += clipboard
        elif command == "Backspace":
            if windows[current_window_index]:
                windows[current_window_index] = windows[current_window_index][
                    :-1
                ]
        else:
            windows[current_window_index] += command
    final_text = windows[current_window_index]
    if not final_text:
        print("Empty")
    else:
        print(final_text[-k:])


if __name__ == "__main__":
    solve()
