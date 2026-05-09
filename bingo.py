import os              # To talk to folders
import random          # To shuffle the photos
import tkinter as tk   # To make the window 
from tkinter import filedialog, messagebox # For pop-ups
from PIL import Image, ImageDraw, ImageFont # For the photos and text
import textwrap

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        entry_folder.delete(0, tk.END)
        entry_folder.insert(0, folder_selected)

def generate_bingo():

    image_folder = entry_folder.get() #"photos"
    all_images = []
    used_images_master = set()


    if not os.path.exists(image_folder):
        messagebox.showerror("ERROR", f" The folder '{image_folder} does not exist. Please create it.")
        return
    
    for filename in os.listdir(image_folder):
        if filename.lower().endswith((".jpg", ".png", ".jpeg")):
            full_path = os.path.join(image_folder, filename)
           #all_images.append(full_path)
            all_images.append(os.path.join(image_folder, filename))

    messagebox.showinfo("Status", f"I found {len(all_images)} images in the folder.")

    try: 
       #grid_size = int(input("Enter the grid size (e.g.: 3 for 3x3, 5 for 5x5): ") )
       #total_cards = int(input("Enter the number of cards: "))
       grid_size = int(entry_grid.get())
       total_cards = int(entry_cards.get())
    except ValueError:
        messagebox.showerror("ERROR", "Please enter numbers only.")
        return

    photos_per_card = grid_size * grid_size
    output_folder = "my_generated_cards"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created folder: {output_folder}")

    if len(all_images) < photos_per_card:
        messagebox.showerror("ERROR", "Please add more photos")
        return
    else: 
        messagebox.showinfo("Status", "Preparing to build cards.")


    for i in range(total_cards):
        card_canvas = Image.new("RGB", (2000, 2000), "white")
        draw = ImageDraw.Draw(card_canvas) 
    
        current_card_photos = random.sample(all_images, photos_per_card)
        used_images_master.update(current_card_photos) 

        cell_size = 2000 // grid_size
        photo_index = 0



        for row in range(grid_size):
            for col in range(grid_size):
                x = col * cell_size
                y = row * cell_size
        
                img_path = current_card_photos[photo_index]
            


                with Image.open(img_path) as img:
                    padding = 40
                    max_photo_w = cell_size - (padding * 2)
                    max_photo_h = int(cell_size * 0.7)
                
                    img.thumbnail((max_photo_w, max_photo_h))
                
                    img_w, img_h = img.size
                    center_x = x + (cell_size - img_w) // 2
                    center_y = y + (max_photo_h - img_h) // 2 + 20
                
                    card_canvas.paste(img, (center_x, center_y))
            
                label = os.path.splitext(os.path.basename(img_path))[0]
                dynamic_size = max(20, cell_size // 10)
                try:
                    #font = ImageFont.load_default(size=60)
                    font = ImageFont.truetype("arial.ttf", dynamic_size)
                except:
                    font = ImageFont.load_default(size=60) 
                wrapper = textwrap.TextWrapper(width=15)
                wrapped_label = wrapper.fill(text=label)


                text_y = y + int(cell_size * 0.82)
                draw.multiline_text((x + cell_size//2, text_y), wrapped_label, fill="black", font=font, anchor="ms")

                draw.rectangle([x, y, x + cell_size, y + cell_size], outline="black", width=3)

                photo_index += 1

        card_filename = f"{output_folder}/card_{i+1}.png"
        card_canvas.save(card_filename)
        print(f"Saved: {card_filename}")


    


    print("Status", "Creating the Master Call Card...")

    final_call_list = sorted(list(used_images_master))

    import math
    total_pics = len(final_call_list)
    cols = 8 
    rows = math.ceil(total_pics / cols)

    

    master_cell_size = 300 
    master_w = cols * master_cell_size
    master_h = rows * master_cell_size
    master_card = Image.new("RGB", (master_w, master_h), "white")
    master_draw = ImageDraw.Draw(master_card)
    try:
        master_font = ImageFont.truetype("arial.ttf", 60)
    except:
        master_font = ImageFont.load_default(size=40)
    wrapper = textwrap.TextWrapper(width=15)
    wrapped_label = wrapper.fill(text=label)


    text_y = y + int(cell_size * 0.82)
    draw.multiline_text((x + cell_size//2, text_y), wrapped_label, fill="black", font=font, anchor="ms")
    

    for index, img_path in enumerate(final_call_list):


        current_row = index // cols
        current_col = index % cols
    
        x = current_col * master_cell_size
        y = current_row * master_cell_size
    

        master_draw.rectangle([x, y, x + master_cell_size, y + master_cell_size], outline="gray", width=2)
    
        with Image.open(img_path) as img:

            img.thumbnail((master_cell_size - 20, master_cell_size - 60))
            img_w, img_h = img.size
        

            offset_x = x + (master_cell_size - img_w) // 2
            offset_y = y + (master_cell_size - img_h) // 2 - 10
            master_card.paste(img, (offset_x, offset_y))
        

        label = os.path.splitext(os.path.basename(img_path))[0]
        master_draw.text((x + master_cell_size//2, y + master_cell_size - 20), 
                     label, fill="black", anchor="ms")


    master_card.save(f"{output_folder}/_MASTER_CALL_CARD.png")
    print("Status", "🎉 Master Call Card saved as '_MASTER_CALL_CARD.png'")

    messagebox.showinfo("Status", "🎉 All Bingo cards have been generated successfully!")
    messagebox.showinfo("Status", f"Check the '{output_folder}' folder to see your cards.")


root = tk.Tk()
root.title("Bingo!")
root.geometry("400x300")
tk.Label(root, text="Photo Folder:").pack(pady=5) 
entry_folder = tk.Entry(root,width=30)
entry_folder.insert(0, "photos") 
entry_folder.pack()

tk.Button(root, text="Browse", command=browse_folder).pack()
tk.Label(root, text="Grid Size (e.g. 5):").pack(pady=5)
entry_grid = tk.Entry(root)
entry_grid.pack()

tk.Label(root, text="Number of Cards:").pack(pady=5) 
entry_cards = tk.Entry(root)
entry_cards.pack()

btn_generate = tk.Button(root, text= "GENERATE CARDS", command=generate_bingo, bg= "green", fg="white")
btn_generate.pack(pady=20)
root.mainloop()