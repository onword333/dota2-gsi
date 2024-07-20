import tkinter as tk
import requests
from runes.gold_rune import GoldRune
from runes.wisdom_rune import WisdomRune


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

        self.update_data()

    def update_data(self):
        try:            
            response = requests.get('http://localhost:3000/get_data')
            data = response.json()

            msg = ''
            for rune in self.runes:                
                msg += f'{rune.name}: {rune.time_until_next_appearance(data)}\n'

            self.label.config(text=msg)
        except Exception as e:
            self.label.config(text=f"Error: {e}")

        self.after(1000, self.update_data)
