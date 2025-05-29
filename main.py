import tkinter as tk
from PIL import Image, ImageTk  # Pillow library for better image format support

root = tk.Tk()
root.geometry("600x400") 

# Frames
main_text = tk.Frame(root)
main_text.place(x=0, y=0)

navigation_text = tk.Frame(root)
navigation_text.place(x=0, y=20)

score_board = tk.Frame(root)
score_board.place(x=0, y=40)

# Load image with PIL and convert to PhotoImage
image = Image.open("images/img1.jpg")  # Your image file path here
image = image.resize((100,100))  # Resize to fit window if needed
bg_image = ImageTk.PhotoImage(image)

#event function
def on_click(event):
    selected_fruit.config(text= "Pineapple")
    # rules.config(text= "Make it 4 straight pineapple to get 1 point")
    print("Clicked")
    

counter = 0
start_count = 0
score_count = 0

def attempt_function (event):   
    global counter 
    counter += 1

    if (counter <= 4):
        attempt.config(text=f"Attempt: {counter}")
        return
    # Reset to 0
    elif (counter >= 4):
        counter = 0
        counter += 1
        attempt.config(text= f"Attempt: {counter}")
        return
            
def scores_function (event):
    global counter
    global score_count
    if(counter >= 4 and counter == 4):
        score_count += 1
        scores.config(text = f"Scores: {score_count}")

def combined_function (event):
    on_click(event)
    attempt_function(event)
    scores_function(event)
    

# Create a label with the image
background_label = tk.Label(root, image=bg_image)
background_label.pack()
background_label.bind("<Button-1>", combined_function)


# Main Text
req_fruits = tk.Label(main_text, text="Select Fruits: ")
req_fruits.pack(side="left")

selected_fruit = tk.Label(main_text, text= "None")
selected_fruit.pack()

attempt = tk.Label(navigation_text, text=f"Attempt: {counter}")
attempt.pack(side='left')

scores = tk.Label(score_board, text = f"Scores: {score_count}")
scores.pack(side='left')

root.mainloop()