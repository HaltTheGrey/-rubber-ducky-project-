from typing import Tuple
import customtkinter as ctk
from datetime import datetime
import threading
import time
from win10toast import ToastNotifier

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
        self.geometry("400x400")
        
        self.toaster = ToastNotifier()
        
        # Timer state
        self.set_time = 25
        self.time_left = self.set_time * 60
        self.is_running = False
        
        
        # UI Elements
        # Timer display labels
        self.timer_input_label = ctk.CTkLabel(
            self,
            text="Set Timer (minutes):",
            font=("Arial", 14)
        )
        self.timer_input_label.pack(pady=(20, 5))
        self.time_input = ctk.CTkEntry(
            self,
            width=200,
            height=35,
            font=("Arial", 14),
            justify="center"
        )
        self.time_input.pack(pady=5)
        self.time_input.insert(0, "25")
        
        self.set_button = ctk.CTkButton(
            self,
            text="Set Time",
            command=self.update_timer,
            width=200,
            height=35,
            font=("Arial", 14)
        )
        self.set_button.pack(pady=10)
        
        self.timer_label = ctk.CTkLabel(
            self,
            text=f"{self.set_time:02}:00",
            font=("Arial", 48)
        )
        self.timer_label.pack(pady=20)
        
        
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
    def update_timer(self):
        try:
            new_time = int(self.time_input.get())
            if new_time <= 0:
                raise ValueError("Time must be positive.")
            self.set_time = new_time
            self.time_left = self.set_time * 60
            self.timer_label.configure(text=f"{self.set_time:02}:00")
        except ValueError:
            self.time_input.delete(0, ctk.END)
            self.time_input.insert(0, "25")  # Reset to default if invalid input
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
            self.show_notification()  # Add this line
    def show_notification(self):
        """Show a Windows notification when the timer ends."""
        threading.Thread(
            target=self.toaster.show_toast,
            kwargs={
                "title" : "Pomodoro Timer",
                "msg" : "Time's up! Take a break.",
                "duration" : 5, # duration in seconds
                "icon_path" : None
            },
            daemon=True
        ).start()
        
    def Reset_timer(self):
        self.time_left = self.set_time * 60
        self.is_running = False
        self.timer_label.configure(text=f"{self.set_time:02}:00")
        self.start_Button.configure(text="Start")
    
    
    
if __name__ == "__main__":
    app = PomdoroTimer()
    app.mainloop() 
