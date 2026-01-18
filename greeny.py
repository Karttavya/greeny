
import tkinter as tk
from tkinter import scrolledtext
import datetime
from collections import defaultdict

# --- LETTER MAP (Shortened for brevity) ---
# --- COMPLETE LETTER MAP (A-Z, 0-9, Symbols, Artifacts) ---
letter_map = {
    # --- ALPHABET (A-Z) ---
    "A": [" XXX ", "X   X", "X   X", "XXXXX", "X   X", "X   X", "X   X"],
    "B": ["XXXX ", "X   X", "X   X", "XXXX ", "X   X", "X   X", "XXXX "],
    "C": [" XXX ", "X   X", "X    ", "X    ", "X    ", "X   X", " XXX "],
    "D": ["XXXX ", "X   X", "X   X", "X   X", "X   X", "X   X", "XXXX "],
    "E": ["XXXXX", "X    ", "X    ", "XXXX ", "X    ", "X    ", "XXXXX"],
    "F": ["XXXXX", "X    ", "X    ", "XXXX ", "X    ", "X    ", "X    "],
    "G": [" XXX ", "X   X", "X    ", "X XXX", "X   X", "X   X", " XXX "],
    "H": ["X   X", "X   X", "X   X", "XXXXX", "X   X", "X   X", "X   X"],
    #"I": ["XXX", " X ", " X ", " X ", " X ", " X ", "XXX"],
    "I": ["XXXXX", "  X  ", "  X  ", "  X  ", "  X  ", "  X  ", "XXXXX"],
    "J": ["  XXX", "   X ", "   X ", "   X ", "   X ", "X  X ", " XX  "],
    "K": ["X   X", "X  X ", "X X  ", "XX   ", "X X  ", "X  X ", "X   X"],
    "L": ["X    ", "X    ", "X    ", "X    ", "X    ", "X    ", "XXXXX"],
    "M": ["X   X", "XX XX", "X X X", "X   X", "X   X", "X   X", "X   X"],
    "N": ["X   X", "X   X", "XX  X", "X X X", "X  XX", "X   X", "X   X"],
    "O": [" XXX ", "X   X", "X   X", "X   X", "X   X", "X   X", " XXX "],
    "P": ["XXXX ", "X   X", "X   X", "XXXX ", "X    ", "X    ", "X    "],
    "Q": [" XXX ", "X   X", "X   X", "X   X", "X X X", "X  X ", " XX X"],
    "R": ["XXXX ", "X   X", "X   X", "XXXX ", "X X  ", "X  X ", "X   X"],
    "S": [" XXX ", "X   X", "X    ", " XXX ", "    X", "X   X", " XXX "],
    "T": ["XXXXX", "  X  ", "  X  ", "  X  ", "  X  ", "  X  ", "  X  "],
    "U": ["X   X", "X   X", "X   X", "X   X", "X   X", "X   X", " XXX "],
    "V": ["X   X", "X   X", "X   X", "X   X", "X   X", " X X ", "  X  "],
    "W": ["X   X", "X   X", "X   X", "X   X", "X X X", "XX XX", "X   X"],
    "X": ["X   X", "X   X", " X X ", "  X  ", " X X ", "X   X", "X   X"],
    "Y": ["X   X", "X   X", " X X ", "  X  ", "  X  ", "  X  ", "  X  "],
    "Z": ["XXXXX", "    X", "   X ", "  X  ", " X   ", "X    ", "XXXXX"],
    
    # --- NUMBERS (0-9) ---
    "0": [" XXX ", "X   X", "X   X", "X   X", "X   X", "X   X", " XXX "],
    "1": ["  X  ", " XX  ", "  X  ", "  X  ", "  X  ", "  X  ", "XXXXX"],
    "2": [" XXX ", "X   X", "    X", "   X ", "  X  ", " X   ", "XXXXX"],
    "3": ["XXXXX", "    X", "   X ", " XXX ", "    X", "X   X", " XXX "],
    "4": ["X   X", "X   X", "X   X", "XXXXX", "    X", "    X", "    X"],
    "5": ["XXXXX", "X    ", "XXXX ", "    X", "    X", "X   X", " XXX "],
    "6": [" XXX ", "X    ", "X    ", "XXXX ", "X   X", "X   X", " XXX "],
    "7": ["XXXXX", "    X", "   X ", "  X  ", " X   ", "X    ", "X    "],
    "8": [" XXX ", "X   X", "X   X", " XXX ", "X   X", "X   X", " XXX "],
    "9": [" XXX ", "X   X", "X   X", " XXXX", "    X", "   X ", " XX  "],

    # --- SYMBOLS ---
    " ": ["  ", "  ", "  ", "  ", "  ", "  ", "  "], # Space
    "₹": ["XXXX", "  X ", "XXXX", "  X ", "   X", "   X", "   X"], # Rupee (Indian)
    "$": ["  X  ", " XXXX", "X X  ", " XXX ", "  X X", "XXXX ", "  X  "], # Dollar
    "!": ["  X  ", "  X  ", "  X  ", "  X  ", "  X  ", "     ", "  X  "], # Exclamation
    "?": [" XXX ", "X   X", "    X", "   X ", "  X  ", "     ", "  X  "], # Question
    ".": ["   ", "   ", "   ", "   ", "   ", "XX ", "XX "], # Period
    ",": ["     ", "     ", "     ", "     ", "  XX ", "  XX ", " X   "], # Comma
    "+": ["     ", "  X  ", "  X  ", "XXXXX", "  X  ", "  X  ", "     "], # Plus
    "-": ["     ", "     ", "     ", "XXXXX", "     ", "     ", "     "], # Minus
    "=": ["     ", "XXXXX", "     ", "XXXXX", "     ", "     ", "     "], # Equals
    "/": ["    X", "   X ", "   X ", "  X  ", " X   ", " X   ", "X    "], # Slash
    ":": ["     ", " XX  ", " XX  ", "     ", " XX  ", " XX  ", "     "], # Colon
    "@": [" XXX ", "X   X", "X XXX", "X X X", "X XXX", "X    ", " XXX "], # At
    "#": [" X X ", " X X ", "XXXXX", " X X ", "XXXXX", " X X ", " X X "], # Hash

    # --- ARTIFACTS (Mapped to symbols) ---
    # Type '^' for Heart
    "^": [ 
        "     ",
        " X X ",
        "XXXXX",
        "XXXXX",
        "XXXXX",
        " XXX ",
        "  X  "
    ],
    "%": [ 
        "     ",
        "     ",
        "     ",
        "     ",
        "     ",
        "     ",
        "X X X"
    ],
    # Type '*' for Star 
    "*": [
        "  X  ",
        "X X X",
        " X X ",
        "XXXXX",
        " X X ",
        "X   X",
        "X   X"
    ],
    # Type '~' for Smiley Face
    "~": [
        "     ",
        " X X ",
        "     ",
        "     ",
        "X   X",
        "X   X",
        " XXX "
    ],
    "`": [
        "     ",
        "XX XX",
        "XX XX",
        "     ",
        "X   X",
        "X   X",
        " XXX "
    ],
    # Type '>' for Arrow
    ">": [
        "    ",
        "X   ",
        "XX  ",
        "XXX ",
        "XX  ",
        "X   ",
        "    "
    ],
    "<": [
        "    ",
        "   X",
        "  XX",
        " XXX",
        "  XX",
        "   X",
        "    "
    ],
    # Type '[' for Pacman
    "[": [
        " XXX ",
        "XXXXX",
        "XXXX ",
        "XXX  ",
        "XXXX ",
        "XXXXX",
        " XXX "
    ],
    # Type ']' for Ghost
    "]": [
        " XXX ",
        "XXXXX",
        "X X X",
        "XXXXX",
        "XXXXX",
        "XXXXX",
        "X X X"
    ],
    "{": [
        " XX ",
        "XXXX",
        " XX ",
        "  X ",
        " XX ",
        "  X ",
        "  X "
    ],
"}": [
        " XXX ",
        "XXXXX",
        " XXX ",
        "  X  ",
        " XXX ",
        "  X  ",
        "  X  "
    ],
")": [
        " XXXX ",
        "XXXXXX",
        " XXXX ",
        "   X  ",
        "  XXX ",
        "   X  ",
        "   X  "
    ],
"(": [
        "  XXX  ",
        " XXXXX ",
        "XXXXXXX",
        " XXXXX ",
        "   X   ",
        "  XXX  ",
        "   X   "
    ],
"?": [
        " X X ",
        "XXXXX",
        " X X ",
        "  X  ",
        "  X  ",
        " X X ",
        "  X  "
    ],
"'": [
        " X   X ",
        " XXXXX ",
        "XXXXXXX",
        " XXXXX ",
        "   X   ",
        "   X   ",
        "   X   "
    ]
}

# --- CONFIGURATION ---
BOX_SIZE = 14
GAP = 3
COLUMNS = 53
ROWS = 7
CANVAS_WIDTH = COLUMNS * (BOX_SIZE + GAP) + 20
CANVAS_HEIGHT = ROWS * (BOX_SIZE + GAP) + 20

# 2026 Configuration
YEAR = 2026
START_DATE = datetime.date(YEAR, 1, 1)
GRID_START_DATE = START_DATE - datetime.timedelta(days=4)

def get_date_from_grid(col, row):
    """Calculates the date for a specific grid block."""
    days_to_add = (col * 7) + row
    return GRID_START_DATE + datetime.timedelta(days=days_to_add)

def draw_word(event=None):
    canvas.delete("all")
    word = entry.get().upper()
    
    # 1. Prepare text layout
    char_blocks = []
    for char in word:
        if char in letter_map:
            grid = letter_map[char]
            width = len(grid[0])
            char_blocks.append((char, width))

    target_pixels = set()
    
    if char_blocks:
        total_width = sum(w for _, w in char_blocks) + (len(char_blocks) - 1)
        start_col = max((COLUMNS - total_width) // 2, 0)
        current_col = start_col

        for idx, (char, char_width) in enumerate(char_blocks):
            grid = letter_map[char]
            for y in range(min(len(grid), ROWS)):
                for x in range(char_width):
                    if current_col + x < COLUMNS:
                        if grid[y][x] == "X":
                            target_pixels.add((current_col + x, y))
            current_col += char_width + 1

    # 2. Draw the Calendar Grid
    active_dates = []
    
    for col in range(COLUMNS):
        for row in range(ROWS):
            current_date = get_date_from_grid(col, row)
            
            x = 10 + col * (BOX_SIZE + GAP)
            y = 10 + row * (BOX_SIZE + GAP)
            
            if current_date.year == YEAR:
                fill_color = "#ebedf0"
                outline_color = "#e1e4e8"
                
                if (col, row) in target_pixels:
                    fill_color = "#39d353"
                    outline_color = "#2ea043"
                    active_dates.append(current_date)
                
                canvas.create_rectangle(x, y, x + BOX_SIZE, y + BOX_SIZE, 
                                     fill=fill_color, outline=outline_color)
            else:
                pass

    # 3. Generate Output List in the GUI
    display_schedule(active_dates)

def display_schedule(dates):
    """Organizes dates by Month ONLY and displays in the GUI text box."""
    result_text.config(state=tk.NORMAL)  # Enable editing to clear old text
    result_text.delete(1.0, tk.END)      # Clear previous text
    
    if not dates:
        stats_label.config(text="No dates selected.")
        result_text.insert(tk.END, "Enter a word above to generate dates.")
        result_text.config(state=tk.DISABLED)
        return

    dates.sort()
    
    # --- LOGIC CHANGE: Group only by Month ---
    schedule = defaultdict(list)
    for d in dates:
        month_name = d.strftime("%B")
        schedule[month_name].append(d)

    total_days = len(dates)
    stats_label.config(text=f"Total Contribution Days: {total_days}")

    # Header for text box
    result_text.insert(tk.END, f"SCHEDULE FOR '{entry.get().upper()}' ({YEAR})\n")
    result_text.insert(tk.END, "="*40 + "\n")

    # Ensure months are printed in order
    month_order = list(dict.fromkeys([d.strftime("%B") for d in dates]))
    
    for month in month_order:
        days_in_month = schedule[month]
        
        # Format: "12, 13, 15, 20"
        date_strs = [d.strftime("%d") for d in days_in_month]
        date_list_str = ", ".join(date_strs)
        
        # Display: Month Name | Count | Days
        result_text.insert(tk.END, f"\n{month} ({len(days_in_month)} days)")
        result_text.insert(tk.END, f": {date_list_str}\n")
    
    result_text.config(state=tk.DISABLED) # Make read-only again

# --- GUI SETUP ---
root = tk.Tk()
root.title("2026 GitHub Contribution Planner")
# Set a reasonable default size
root.geometry(f"{CANVAS_WIDTH + 60}x600")

frame_top = tk.Frame(root, bg="#f7f7f7")
frame_top.pack(pady=20)

entry = tk.Entry(frame_top, width=30, font=("Segoe UI", 12))
entry.pack(side=tk.LEFT, padx=10)
entry.bind("<Return>", draw_word)

btn = tk.Button(frame_top, text="Generate Plan", command=draw_word, bg="#000000", fg="white", font=("Segoe UI", 10, "bold"))
btn.pack(side=tk.LEFT)

# Add labels for rows (S M T W T F S)
frame_grid = tk.Frame(root, bg="#f7f7f7")
frame_grid.pack(padx=20)

days = ["S", "M", "T", "W", "T", "F", "S"]
for i, d in enumerate(days):
    lbl = tk.Label(frame_grid, text=d, font=("Segoe UI", 8), bg="#f7f7f7", fg="#767676")
    lbl.place(x=0, y=10 + i*(BOX_SIZE+GAP) + 2)

canvas = tk.Canvas(frame_grid, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="#f7f7f7", highlightthickness=0)
canvas.pack(side=tk.LEFT, padx=(20, 0))

stats_label = tk.Label(root, text="Enter text to see dates", font=("Segoe UI", 10, "bold"), bg="#f7f7f7")
stats_label.pack(pady=(10, 5))

# --- NEW: Scrollable Text Box for Results ---
# This is placed below the graph to show the list of dates
result_frame = tk.Frame(root, bg="#f7f7f7")
result_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))

result_text = scrolledtext.ScrolledText(result_frame, height=10, font=("Consolas", 13))
result_text.pack(fill=tk.BOTH, expand=True)

root.configure(bg="#f7f7f7")
root.mainloop()