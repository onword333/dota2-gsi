import tkinter as tk
import requests
from runes.gold_rune import GoldRune
from runes.wisdom_rune import WisdomRune
import random


class OverlayApp(tk.Tk):

    def __init__(self):
        super().__init__()        
        self.runes = [GoldRune(), WisdomRune()]
        self.title("Осталось до появления рун")

        # ширина x высота x отступ_слева x отступ_сверху
        # если нужно расположить в нужном месте, то меняем здесь
        self.geometry("180x100+210+668")

        self.attributes('-topmost', True)
        self.attributes('-alpha', 0.7)
        self.configure(bg='black')

        self.overrideredirect(True)

        self.label = tk.Label(self, text="Waiting for data...", fg="white", bg="black")
        self.label.pack(pady=20)

        self.shaking = False
        self.flash_state = False
        self.after(100, self.initialize_position)        

    def shake(self):
        end_time = self.after(1000, self.stop_shake)
        self.perform_shake(end_time)

    def perform_shake(self, end_time):
        if not self.shaking:
            return

        x_offset = random.randint(-5, 5)
        y_offset = random.randint(-5, 5)
        self.geometry(f"+{self.original_x + x_offset}+{self.original_y + y_offset}")
        self.after(50, self.perform_shake, end_time)

    def stop_shake(self):
        self.shaking = False
        self.geometry(f"+{self.original_x}+{self.original_y}")

    def initialize_position(self):
        self.update_idletasks()
        self.original_x = self.winfo_x()
        self.original_y = self.winfo_y()

        self.update_data()

    def flash_red(self):
        if not self.flashing:
            return

        # Переключаем цвет фона
        self.flash_state = not self.flash_state
        if self.flash_state:
            self.configure(bg='red')
            self.label.configure(bg='red')
        else:
            self.configure(bg='black')
            self.label.configure(bg='black')

        # Планируем следующее переключение
        self.after(200, self.flash_red)

    def start_flashing(self):
        if not self.flashing:
            self.flashing = True
            self.flash_red()

    def stop_flashing(self):
        self.flashing = False
        self.configure(bg='black')
        self.label.configure(bg='black')

    def update_data(self):
        try:
            response = requests.get('http://localhost:3000/get_data')
            data = response.json()

            rune_coming_soon = False

            msg = ''
            for rune in self.runes:
                time_until_next_appearance = rune.time_until_next_appearance(data)
                msg += f'{rune.name}: {time_until_next_appearance}\n'

                if time_until_next_appearance <= 10 and time_until_next_appearance != 0:
                    rune_coming_soon = True

            if rune_coming_soon:
                self.start_flashing()
            else:
                self.stop_flashing()

            self.label.config(text=msg)
        except Exception as e:
            self.label.config(text=f"Error: {e}")

        self.after(1000, self.update_data)
