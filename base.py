import tkinter as tk
import string

letter_map = {
    "A": [
        " XXX ",
        "X   X",
        "X   X",
        "XXXXX",
        "X   X",
        "X   X",
        "X   X"
    ],
    "B": [
        "XXXX ",
        "X   X",
        "X   X",
        "XXXX ",
        "X   X",
        "X   X",
        "XXXX "
    ],
    "C": [
        " XXX ",
        "X   X",
        "X    ",
        "X    ",
        "X    ",
        "X   X",
        " XXX "
    ],
    "D": [
        "XXXX ",
        "X   X",
        "X   X",
        "X   X",
        "X   X",
        "X   X",
        "XXXX "
    ],
    "E": [
        "XXXXX",
        "X    ",
        "X    ",
        "XXXX ",
        "X    ",
        "X    ",
        "XXXXX"
    ],
    "F": [
        "XXXXX",
        "X    ",
        "X    ",
        "XXXX ",
        "X    ",
        "X    ",
        "X    "
    ],
    "G": [
        " XXX ",
        "X   X",
        "X    ",
        "X XXX",
        "X   X",
        "X   X",
        " XXX "
    ],
    "H": [
        "X   X",
        "X   X",
        "X   X",
        "XXXXX",
        "X   X",
        "X   X",
        "X   X"
    ],
    "I": [
        "XXXXX",
        "  X  ",
        "  X  ",
        "  X  ",
        "  X  ",
        "  X  ",
        "XXXXX"
    ],
    "J": [
        "  XXX",
        "   X ",
        "   X ",
        "   X ",
        "   X ",
        "X  X ",
        " XX  "
    ],
    "K": [
        "X   X",
        "X  X ",
        "X X  ",
        "XX   ",
        "X X  ",
        "X  X ",
        "X   X"
    ],
    "L": [
        "X    ",
        "X    ",
        "X    ",
        "X    ",
        "X    ",
        "X    ",
        "XXXXX"
    ],
    "M": [
        "X   X",
        "XX XX",
        "X X X",
        "X   X",
        "X   X",
        "X   X",
        "X   X"
    ],
    "N": [
        "X   X",
        "X   X",
        "XX  X",
        "X X X",
        "X  XX",
        "X   X",
        "X   X"
    ],
    "O": [
        " XXX ",
        "X   X",
        "X   X",
        "X   X",
        "X   X",
        "X   X",
        " XXX "
    ],
    "P": [
        "XXXX ",
        "X   X",
        "X   X",
        "XXXX ",
        "X    ",
        "X    ",
        "X    "
    ],
    "Q": [
        " XXX ",
        "X   X",
        "X   X",
        "X   X",
        "X X X",
        "X  X ",
        " XX X"
    ],
    "R": [
        "XXXX ",
        "X   X",
        "X   X",
        "XXXX ",
        "X X  ",
        "X  X ",
        "X   X"
    ],
    "S": [
        " XXX ",
        "X   X",
        "X    ",
        " XXX ",
        "    X",
        "X   X",
        " XXX "
    ],
    "T": [
        "XXXXX",
        "  X  ",
        "  X  ",
        "  X  ",
        "  X  ",
        "  X  ",
        "  X  "
    ],
    "U": [
        "X   X",
        "X   X",
        "X   X",
        "X   X",
        "X   X",
        "X   X",
        " XXX "
    ],
    "V": [
        "X   X",
        "X   X",
        "X   X",
        "X   X",
        "X   X",
        " X X ",
        "  X  "
    ],
    "W": [
        "X   X",
        "X   X",
        "X   X",
        "X   X",
        "X X X",
        "XX XX",
        "X   X"
    ],
    "X": [
        "X   X",
        "X   X",
        " X X ",
        "  X  ",
        " X X ",
        "X   X",
        "X   X"
    ],
    "Y": [
        "X   X",
        "X   X",
        " X X ",
        "  X  ",
        "  X  ",
        "  X  ",
        "  X  "
    ],
    "Z": [
        "XXXXX",
        "    X",
        "   X ",
        "  X  ",
        " X   ",
        "X    ",
        "XXXXX"
    ],
    " ": [
        "    ",
        "    ",
        "    ",
        "    ",
        "    ",
        "    ",
        "    "
    ]
}


# Paste your full letter_map here above this line

BOX_SIZE = 16
GAP = 2
COLUMNS = 52
ROWS = 7
CANVAS_WIDTH = COLUMNS * (BOX_SIZE + GAP)
CANVAS_HEIGHT = ROWS * (BOX_SIZE + GAP)

def draw_word(event=None):
    canvas.delete("all")

    word = entry.get().upper()

    # Draw background grid first
    for row in range(ROWS):
        for col in range(COLUMNS):
            draw_block(col, row, color="white", outline="#e0e0e0")

    # Prepare text layout
    char_blocks = []
    for char in word:
        if char in letter_map:
            grid = letter_map[char]
            width = len(grid[0])
            char_blocks.append((char, width))

    if not char_blocks:
        stats_label.config(text="Green blocks: 0 / 364 (0.00%)")
        return

    total_width = sum(w for _, w in char_blocks) + (len(char_blocks) - 1)
    start_col = max((COLUMNS - total_width) // 2, 0)
    current_col = start_col

    green_cells = 0

    for idx, (char, char_width) in enumerate(char_blocks):
        grid = letter_map[char]
        for y in range(min(len(grid), ROWS)):
            for x in range(char_width):
                if current_col + x >= COLUMNS:
                    continue
                if grid[y][x] == "X":
                    green_cells += 1
                    draw_block(current_col + x, y, color="#43a047")  # green
        current_col += char_width
        if idx < len(char_blocks) - 1 and current_col < COLUMNS:
            current_col += 1

    percent = (green_cells / (COLUMNS * ROWS)) * 100
    stats_label.config(text=f"Green blocks: {green_cells} / {COLUMNS * ROWS} ({percent:.2f}%)")

def draw_block(col, row, color="white", outline=None):
    x = col * (BOX_SIZE + GAP)
    y = row * (BOX_SIZE + GAP)
    canvas.create_rectangle(x, y, x + BOX_SIZE, y + BOX_SIZE, fill=color, outline=outline or color, width=1)

# GUI setup
root = tk.Tk()
root.title("Fast Pixel Grid (Canvas)")

entry = tk.Entry(root, width=60, font=("Segoe UI", 12))
entry.pack(pady=(20, 5))
entry.bind("<Return>", draw_word)

btn = tk.Button(root, text="Render", command=draw_word)
btn.pack(pady=(0, 10))

canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="#f7f7f7", highlightthickness=0)
canvas.pack()

stats_label = tk.Label(root, text="", font=("Segoe UI", 10), bg="#f7f7f7")
stats_label.pack(pady=(5, 20))

root.configure(bg="#f7f7f7")
root.mainloop()
