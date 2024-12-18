import tkinter as tk
from tkinter import messagebox
import pygame
import random

# Initialize Pygame mixer for sounds
pygame.mixer.init()

# Basic Animal Class (OOP)
class Animal:
    def __init__(self, name, animal_type, sound_file):
        self.name = name
        self.animal_type = animal_type
        self.sound_file = sound_file

    def make_sound(self):
        pygame.mixer.Sound(self.sound_file).play()

# Zoo Manager Class (OOP)
class ZooManager:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def get_animal_list(self):
        return [f"{animal.name} the {animal.animal_type}" for animal in self.animals]

# Create the zoo manager instance
zoo_manager = ZooManager()

# Tkinter GUI Setup
def add_animal():
    name = name_entry.get()
    animal_type = type_entry.get().lower()
    
    # Validate input
    if not name or not animal_type:
        messagebox.showerror("Input Error", "Please enter both name and type!")
        return

    # Assign sound file based on type
    sound_map = {
        "lion": "roar.wav",
        "parrot": "squawk.wav",
        "elephant": "trumpet.wav",
    }

    sound_file = sound_map.get(animal_type)
    if not sound_file:
        messagebox.showerror("Animal Error", "We only support Lion, Parrot, and Elephant!")
        return

    # Add animal to the zoo
    new_animal = Animal(name, animal_type.capitalize(), sound_file)
    zoo_manager.add_animal(new_animal)
    messagebox.showinfo("Success", f"{name} the {animal_type.capitalize()} added!")
    refresh_animal_list()

def refresh_animal_list():
    animal_list.delete(0, tk.END)
    for animal_info in zoo_manager.get_animal_list():
        animal_list.insert(tk.END, animal_info)

def play_sound():
    selected_idx = animal_list.curselection()
    if not selected_idx:
        messagebox.showwarning("Selection Error", "Please select an animal first!")
        return

    animal = zoo_manager.animals[selected_idx[0]]
    animal.make_sound()

# Tkinter GUI
root = tk.Tk()
root.title("Mini Zoo Manager")

# Widgets for Adding Animals
tk.Label(root, text="Animal Name:").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Animal Type (Lion/Parrot/Elephant):").grid(row=1, column=0, padx=10, pady=10)
type_entry = tk.Entry(root)
type_entry.grid(row=1, column=1, padx=10, pady=10)

add_button = tk.Button(root, text="Add Animal", command=add_animal)
add_button.grid(row=2, column=0, columnspan=2, pady=10)

# Animal List Display
tk.Label(root, text="Animal List:").grid(row=3, column=0, padx=10, pady=10)
animal_list = tk.Listbox(root, width=40)
animal_list.grid(row=3, column=1, padx=10, pady=10)

# Play Sound Button
play_sound_button = tk.Button(root, text="Play Sound", command=play_sound)
play_sound_button.grid(row=4, column=0, columnspan=2, pady=10)

# Pygame Animation for Fun
def animal_animation():
    pygame.init()
    screen = pygame.display.set_mode((500, 300))
    pygame.display.set_caption("Animal Animation")

    running = True
    x, y = 0, 150  # Starting position
    clock = pygame.time.Clock()

    # Load a simple image for animation
    animal_image = pygame.image.load("lion.png")  # Replace with your image
    animal_image = pygame.transform.scale(animal_image, (100, 100))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move the animal across the screen
        x += 5
        if x > 500:
            x = -100  # Reset position

        # Drawing
        screen.fill((255, 255, 255))  # White background
        screen.blit(animal_image, (x, y))
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

# Add Animation Button
animation_button = tk.Button(root, text="Start Animation", command=animal_animation)
animation_button.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
