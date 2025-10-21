from typing import Tuple
import customtkinter as ctk
from datetime import datetime
import threading
import time

"""
this is my sandbox for all of my thoughts, AI will help me sort out and teach me all the necessary
tools I need to be a successful programmer. This will be my first official commit.

first project I will make a personal task timer with notification
"""

class PomdoroTimer(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Window makeup
        
        self.title("focus timer")
        self.geometry("400x300")
        
        # Timer state
        
        self.time_left = 25 * 60
        self.is_running = False
        
        
        # UI Elements
        # Timer display label
        self.timer_label = ctk.CTkLabel(
            self,
            text="25:00",
            font=("Arial", 48, "bold")
        )
        self.timer_label.pack(pady=40)
        
        
        self.start_Button = ctk.CTkButton(
            self,
            text = "Start",
            command = self.Start_timer,
            width=200,
            height=40,
            font=("Arial", 16)
        )
        self.start_Button.pack(pady=10)
        
        self.reset_Button = ctk.CTkButton(
            self,
            text = "Reset",
            command= self.Reset_timer,
            width=200,
            height=40,
            font=("Arial", 16)
        )
        self.reset_Button.pack(pady=10)

    def Start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.start_Button.configure(text="Pause")
            self.countdown()
        else:
            self.is_running = False
            self.start_Button.configure(text = "Start")
    def countdown(self):
        if self.is_running and self.time_left > 0:
            # Calculate minutes and seconds
            minutes, seconds = divmod(self.time_left, 60)
            self.timer_label.configure(text=f"{minutes:02}:{seconds:02}")
            self.time_left -= 1
            self.after(1000, self.countdown)
        elif self.time_left == 0:
            self.timer_label.configure(text="Time's up!")
            self.is_running = False
            self.start_Button.configure(text="Start")
    
    def Reset_timer(self):
        self.time_left = 25 * 60
        self.is_running = False
        self.timer_label.configure(text="25:00")
        self.start_Button.configure(text="Start")
    
    
    
if __name__ == "__main__":
    app = PomdoroTimer()
    app.mainloop() 
