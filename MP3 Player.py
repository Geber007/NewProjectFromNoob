import pygame
import tkinter as tk
from tkinter import filedialog, messagebox

class MP3Player:
    def __init__(self, root):
        self.root = root
        self.root.title("MP3 Плеер")
        self.root.geometry("400x300")
        self.root.configure(bg="#2E2E2E")

        pygame.mixer.init()

        self.tracks = []
        self.current_track_index = -1

        self.load_button = tk.Button(root, text="Загрузить MP3", command=self.load, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        self.load_button.pack(pady=10)

        self.play_button = tk.Button(root, text="Играть", command=self.play, bg="#2196F3", fg="white", font=("Helvetica", 12))
        self.play_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="Остановить", command=self.stop, bg="#F44336", fg="white", font=("Helvetica", 12))
        self.stop_button.pack(pady=5)

        self.track_label = tk.Label(root, text="Нет загруженного трека", bg="#2E2E2E", fg="white", font=("Helvetica", 14))
        self.track_label.pack(pady=10)

        self.frame = tk.Frame(root, bg="#2E2E2E")
        self.frame.pack(pady=10)

        self.prev_button = tk.Button(self.frame, text="Предыдущий", command=self.previous_track, bg="#FFC107", fg="white", font=("Helvetica", 12))
        self.prev_button.pack(side=tk.LEFT, padx=10)

        self.next_button = tk.Button(self.frame, text="Следующий", command=self.next_track, bg="#FFC107", fg="white", font=("Helvetica", 12))
        self.next_button.pack(side=tk.RIGHT, padx=10)

    def load(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("MP3 Файлы", "*.mp3")])
        if file_paths:
            self.tracks.extend(file_paths)
            self.current_track_index = len(self.tracks) - 1
            self.update_track_label()

    def update_track_label(self):
        if self.current_track_index >= 0:
            track_name = self.tracks[self.current_track_index].split('/')[-1]
            self.track_label.config(text=track_name)
        else:
            self.track_label.config(text="Нет загруженного трека")

    def play(self):
        if self.current_track_index >= 0:
            pygame.mixer.music.load(self.tracks[self.current_track_index])
            pygame.mixer.music.play()
        else:
            messagebox.showwarning("Предупреждение", "Нет загруженного трека!")

    def stop(self):
        pygame.mixer.music.stop()

    def next_track(self):
        if self.tracks:
            self.current_track_index = (self.current_track_index + 1) % len(self.tracks)
            self.play()
            self.update_track_label()

    def previous_track(self):
        if self.tracks:
            self.current_track_index = (self.current_track_index - 1) % len(self.tracks)
            self.play()
            self.update_track_label()

if __name__ == "__main__":
    root = tk.Tk()
    player = MP3Player(root)
    root.mainloop()
