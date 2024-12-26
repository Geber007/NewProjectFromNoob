import pygame
import tkinter as tk
from tkinter import filedialog

class MP3Player:
    def __init__(self, root):
        self.root = root
        self.root.title("MP3 Player")
        self.root.geometry("300x150")

        # Инициализация Pygame
        pygame.mixer.init()

        # Кнопки управления
        self.play_button = tk.Button(root, text="Play", command=self.play)
        self.play_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(pady=10)

        self.load_button = tk.Button(root, text="Load MP3", command=self.load)
        self.load_button.pack(pady=10)

        self.file_path = ""

    def load(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        if self.file_path:
            print(f"Loaded: {self.file_path}")

    def play(self):
        if self.file_path:
            pygame.mixer.music.load(self.file_path)
            pygame.mixer.music.play()
        else:
            print("No file loaded.")

    def stop(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    root = tk.Tk()
    player = MP3Player(root)
    root.mainloop()