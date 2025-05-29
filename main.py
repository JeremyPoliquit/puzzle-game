import tkinter as tk
from PIL import Image, ImageTk
import os
import random
import tkinter.messagebox as messagebox

root = tk.Tk()
root.geometry("600x600")
root.title("Puzzle Game")

# Frames
main_text = tk.Frame(root)
main_text.place(x=0, y=0)

navigation_text = tk.Frame(root)
navigation_text.place(x=0, y=20)

score_board = tk.Frame(root)
score_board.place(x=0, y=40)

# Load question mark image
QUESTION_IMAGE_PATH = "images/question.jpg"
question_image_raw = Image.open(QUESTION_IMAGE_PATH).resize((100, 100))
question_image = ImageTk.PhotoImage(question_image_raw)

# Load all fruit images from the folder and resize
IMAGE_FOLDER = "images/fruits"
image_files = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

images_with_names = []
for filename in image_files:
    img_path = os.path.join(IMAGE_FOLDER, filename)
    fruit_name = os.path.splitext(filename)[0].lower()
    img = Image.open(img_path).resize((100, 100))
    photo_img = ImageTk.PhotoImage(img)
    images_with_names.append((photo_img, fruit_name))

if len(images_with_names) == 0:
    raise Exception("No fruit images found in the fruits folder!")

# Game state
counter = 0
score_count = 0
selected_fruit_name = None

# Function to reset the game state
def reset_game():
    global selected_fruit_name, counter, score_count
    selected_fruit_name = None
    counter = 0
    selected_fruit.config(text="None")
    attempt.config(text=f"Attempt: {counter}")
    # Don't reset score here (optional: keep score)
    for btn in all_buttons:
        btn.config(image=question_image)
        btn.revealed = False

# Handle button click
def on_click(event):
    global selected_fruit_name

    clicked_btn = event.widget

    if clicked_btn.revealed:
        return False  # do nothing if already revealed

    fruit = clicked_btn.fruit_name
    clicked_btn.config(image=clicked_btn.real_image)
    clicked_btn.revealed = True

    if selected_fruit_name is None:
        selected_fruit_name = fruit
        selected_fruit.config(text=fruit.capitalize())
        return True
    else:
        if fruit != selected_fruit_name:
            messagebox.showerror("Game Over", f"You already selected {selected_fruit_name.capitalize()}. Selecting {fruit.capitalize()} is not allowed!")
            reset_game()
            return False
        else:
            selected_fruit.config(text=fruit.capitalize())
            return True

# Track attempts
def attempt_function():
    global counter
    counter += 1
    if counter <= 4:
        attempt.config(text=f"Attempt: {counter}")
    else:
        counter = 1
        attempt.config(text=f"Attempt: {counter}")

# Track score
def scores_function():
    global counter, score_count
    if counter == 4:
        score_count += 1
        scores.config(text=f"Scores: {score_count}")

# Master click handler
def combined_function(event):
    success = on_click(event)
    if success:
        attempt_function()
        scores_function()

# Grid frame for buttons
grid_frame = tk.Frame(root)
grid_frame.pack(expand=True)

button_images = []
all_buttons = []

# Generate 4x4 grid with hidden images
for row in range(4):
    for col in range(4):
        fruit_img, fruit_name = random.choice(images_with_names)
        button_images.append(fruit_img)

        btn = tk.Button(grid_frame, image=question_image)
        btn.fruit_name = fruit_name
        btn.real_image = fruit_img
        btn.revealed = False

        btn.grid(row=row, column=col, padx=5, pady=5)
        btn.bind("<Button-1>", combined_function)

        all_buttons.append(btn)

# Make grid stretch with window
for i in range(4):
    grid_frame.grid_rowconfigure(i, weight=1)
    grid_frame.grid_columnconfigure(i, weight=1)

# Top labels
req_fruits = tk.Label(main_text, text="Select Fruits: ")
req_fruits.pack(side="left")

selected_fruit = tk.Label(main_text, text="None")
selected_fruit.pack()

attempt = tk.Label(navigation_text, text=f"Attempt: {counter}")
attempt.pack(side='left')

scores = tk.Label(score_board, text=f"Scores: {score_count}")
scores.pack(side='left')

root.mainloop()
