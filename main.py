import tkinter as tk
from PIL import Image, ImageTk
import os
import random

root = tk.Tk()
root.geometry("600x600")

# Frames (keep as is)
main_text = tk.Frame(root)
main_text.place(x=0, y=0)

navigation_text = tk.Frame(root)
navigation_text.place(x=0, y=20)

score_board = tk.Frame(root)
score_board.place(x=0, y=40)

# Load all images from the folder and resize
IMAGE_FOLDER = "images/fruits"
image_files = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

loaded_images = []
for img_file in image_files:
    img_path = os.path.join(IMAGE_FOLDER, img_file)
    img = Image.open(img_path).resize((100, 100))  # resize all images to 100x100
    loaded_images.append(ImageTk.PhotoImage(img))

# If less than 16 images, images will repeat randomly
if len(loaded_images) == 0:
    raise Exception("No images found in the images folder!")

# Event function
def on_click(event):
    selected_fruit.config(text="Pineapple")
    print("Clicked")

counter = 0
score_count = 0

def attempt_function(event):
    global counter
    counter += 1
    if counter <= 4:
        attempt.config(text=f"Attempt: {counter}")
    else:
        counter = 1
        attempt.config(text=f"Attempt: {counter}")

def scores_function(event):
    global counter, score_count
    if counter == 4:
        score_count += 1
        scores.config(text=f"Scores: {score_count}")

def combined_function(event):
    on_click(event)
    attempt_function(event)
    scores_function(event)

# Create a Frame to hold the grid so we don't mix pack and grid in root
grid_frame = tk.Frame(root)
grid_frame.pack(expand=True)

# Keep references to image objects to prevent garbage collection
button_images = []

for row in range(4):
    for col in range(4):
        # Pick a random image from loaded_images
        img = random.choice(loaded_images)
        button_images.append(img)  # keep reference
        
        btn = tk.Button(grid_frame, image=img)
        btn.grid(row=row, column=col, padx=5, pady=5)
        btn.bind("<Button-1>", combined_function)

# Configure grid weights for resizing (optional)
for i in range(4):
    grid_frame.grid_rowconfigure(i, weight=1)
    grid_frame.grid_columnconfigure(i, weight=1)

# Main Text Labels (existing UI)
req_fruits = tk.Label(main_text, text="Select Fruits: ")
req_fruits.pack(side="left")

selected_fruit = tk.Label(main_text, text="None")
selected_fruit.pack()

attempt = tk.Label(navigation_text, text=f"Attempt: {counter}")
attempt.pack(side='left')

scores = tk.Label(score_board, text=f"Scores: {score_count}")
scores.pack(side='left')

root.mainloop()
