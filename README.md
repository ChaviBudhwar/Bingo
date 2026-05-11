## Bingo Card Maker  
This repository contains my project **Bingo**, a custom Python-based automation tool designed to create Bingo cards with images and text. It transforms a folder of images into a set of customised and randomised Bingo cards.

## 📂 What’s Inside:
  - **bingo.py**: The core logic and GUI.
  - **my_generated_cards**: The output folder where the finished cards are saved.

## 📝 Features:
  - **Customisation**: User gets the freedom to choose the grid size and the number of cards to generate.
  - **Relative Scaling**: Text and image sizes are automatically adjusted based on the selected grid size and long phrases are automatically wrapped to prevent "leaking" into other squares.
  - **Master Call Sheet**: Automatically creates a single sheet containing all the images used in the set.
  - **Privacy**: Works 100% offline.

## 🎨 Languages and Libraries Used:
  - **Python**: The core logic.
  - **Pillow (PIL)**: Used for image processing, resizing and text rendering.
  - **Tkinter**: Used for creating an offline GUI.

## 📝 P.S.:
While building this project, I deepened my knowledge of the Pillow library for image manipulation and Tkinter for the GUI. I found the latter more challenging to grasp initially; when I got stuck, I leveraged AI assistance to help debug and refine the code. The current interface is functional, but I plan to add more features in the future.

I'm a student interning as a TA in an English class. I built this Bingo Card Maker to save myself time and show my students how cool coding can be!

* **For Teachers:** Please feel free to use this for your classes! 
* **Open Source:** I've used the **GPLv3 license** to ensure this tool stays free and open for the education community.
