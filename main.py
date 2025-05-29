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

# Load all images from the folder and resize, and save with fruit names
IMAGE_FOLDER = "images/fruits"
image_files = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

images_with_names = []
for filename in image_files:
    img_path = os.path.join(IMAGE_FOLDER, filename)
    img = Image.open(img_path).resize((100, 100))  # resize all images to 100x100
    photo_img = ImageTk.PhotoImage(img)
    fruit_name = os.path.splitext(filename)[0].lower()  # get fruit name from filename
    images_with_names.append((photo_img, fruit_name))

if len(images_with_names) == 0:
    raise Exception("No images found in the images folder!")

counter = 0
score_count = 0

def on_click(event):
    clicked_btn = event.widget
    fruit = getattr(clicked_btn, 'fruit_name', 'Unknown')
    selected_fruit.config(text=fruit.capitalize())
    print(f"Clicked fruit: {fruit}")

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
        img, fruit = random.choice(images_with_names)
        button_images.append(img)  # keep reference
        
        btn = tk.Button(grid_frame, image=img)
        btn.fruit_name = fruit  # store fruit name on the button
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
